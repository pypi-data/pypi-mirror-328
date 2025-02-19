import os, math, glob, shutil
import numpy as np
import scipy.io as sio
from scipy.io import loadmat, savemat


def process_panel_map(Panel_map):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Process the 4×12 Panel_map into a list of dictionaries (one per panel).
    :param Panel_map: panel matrix
    :return: dictionary of panel maps
    '''
    BitMapIndex = []
    max_id = int(np.max(Panel_map))
    for panel_id in range(1, max_id + 1):
        indices = np.argwhere(Panel_map == panel_id)
        if indices.size == 0:
            continue
        r, c = indices[0]
        row_range = np.arange(r * 8 + 1, r * 8 + 9, dtype=np.int32)
        col_range = np.arange(c * 8 + 1, c * 8 + 9, dtype=np.int32)
        BitMapIndex.append({'Panel_ID': panel_id,
                            'row_range': row_range,
                            'column_range': col_range})
    BitMapIndex.sort(key=lambda x: x['Panel_ID'])
    return BitMapIndex


def make_pattern_vector_ak(pattern):
    """
    Anmo Kim
    Seongyeon Kim
    ChatGPT

    Convert the pattern structure into a packed 1D uint8 vector.
    Converted from matlab "make_pattern_vector_ak"

    For a pattern with fields:
      - 'Pats': NumPy array of shape (L, M, N, O) where L and M are the image dimensions (each panel is 8×8),
                N is the number of frames along the x‐dimension and O along the y‐dimension.
      - 'BitMapIndex': list of dictionaries with keys 'row_range' and 'column_range' (1-indexed).
      - 'gs_val': brightness bit depth (1–4).
      - (optionally) 'row_compression': if nonzero, use the “row compression” mode.

    For gs_val==2 (for example) it is assumed that the pixel values in Pats have been scaled so that
    they are in the range 0–3.

    For non–row-compressed patterns (row_compression==0), each panel’s 8×8 block is processed column‐by‐column.
    For each column:
      - if gs_val==1, we compute a dot product of the 8 binary bits (each pixel is 0 or 1) with
        twos = [1,2,4,8,16,32,64,128] (which yields a number 0–255).
      - otherwise, if the block is “all off” (sum==0) we output zeros,
        if “all on” (each pixel equals (2^gs_val – 1)) we output 255’s,
        else we convert each pixel into its binary representation (with gs_val digits) and then
        reshape to an 8×(8*gs_val) matrix and compute (twos dot that) to get an 8*gs_val–element row.

    The final packed data for each panel’s frame is then concatenated across all panels and all frames.
    The output is a 1D numpy.uint8 vector.
    """

    # Round and convert Pats to uint8.
    Pats = np.round(pattern['Pats']).astype(np.uint8)
    BitMapIndex = pattern['BitMapIndex']
    gs_val = int(pattern['gs_val'])
    row_compression = int(pattern.get('row_compression', 0))

    # Error checking:
    if np.isnan(Pats).any():
        raise ValueError("make_pattern_vector_ak: NaN value found in pattern matrix")
    if gs_val < 1 or gs_val > 4:
        raise ValueError("gs_val must be 1, 2, 3, or 4")
    if gs_val == 1 and not np.all((Pats == 0) | (Pats == 1)):
        raise ValueError("For gs 1, Pats can contain only 0 or 1")
    if gs_val == 2 and not np.all((Pats >= 0) & (Pats <= 3)):
        raise ValueError("For gs 2, Pats can contain only 0,1,2, or 3")
    if gs_val == 3 and not np.all((Pats >= 0) & (Pats <= 7)):
        raise ValueError("For gs 3, Pats can contain only 0–7")
    if gs_val == 4 and not np.all((Pats >= 0) & (Pats <= 15)):
        raise ValueError("For gs 4, Pats can contain only 0–15")

    # Ensure Pats is 4D; if 3D, add a singleton dimension.
    if Pats.ndim == 3:
        Pats = Pats[:, :, :, np.newaxis]
    # Dimensions:
    L, M, NumPatsX, NumPatsY = Pats.shape
    NumPats = NumPatsX * NumPatsY
    num_panels = len(BitMapIndex)

    # Allocate pat_matrix.
    if row_compression:
        pat_matrix = np.zeros((num_panels * NumPats, 1 * gs_val), dtype=np.uint8)
    else:
        pat_matrix = np.zeros((num_panels * NumPats, 8 * gs_val), dtype=np.uint8)

    # Define twos vector: [2^0,2^1,...,2^7] as a 1D array of length 8.
    twos = 2 ** np.arange(8, dtype=np.uint16)  # use uint16 to be safe

    # Loop over frame indices (adjusting from MATLAB’s 1-indexing to Python’s 0-indexing)
    for ix in range(NumPatsX):
        for iy in range(NumPatsY):
            # Compute the overall pattern number (0-indexed)
            pattern_number = iy * NumPatsX + ix
            # Prepare a temporary array to hold the processed panel data for this frame.
            frame_pat = np.zeros((num_panels, 8 * gs_val), dtype=np.uint8)
            # Process each panel.
            for i, panel in enumerate(BitMapIndex):
                # Convert 1-indexed ranges into 0-indexed Python slices.
                r_range = np.array(panel['row_range']) - 1
                c_range = np.array(panel['column_range']) - 1
                # Extract the 8×8 block for this panel and frame.
                # Since the ranges are contiguous we can use slicing:
                PanMat = Pats[r_range[0]:r_range[-1] + 1, c_range[0]:c_range[-1] + 1, ix, iy]
                # Now PanMat is an 8×8 array.
                if row_compression:
                    # In row compression mode, each panel produces 1*gs_val numbers.
                    if gs_val == 1:
                        # Multiply twos (1×8) by the transposed block (8×8) yields a 1×8 vector.
                        # We then take the first element (or combine as desired).
                        # (In MATLAB the code does: frame_pat(i) = twos*PanMat';)
                        frame_pat[i, :8] = np.dot(twos, PanMat.T)
                    else:
                        if gs_val > 4:
                            raise ValueError("gs_val = 1-4 cases are supported!")
                        # For each pixel (treated as a number between 0 and (2^gs_val -1)),
                        # convert it to a binary string (with gs_val digits) and then do the dot product.
                        flat = PanMat.flatten(order='C')
                        # For each element, get binary representation as a list of ints.
                        bin_list = [list(np.binary_repr(x, width=gs_val)) for x in flat]
                        bin_arr = np.array(bin_list, dtype=np.int16) - ord('0')
                        # Reshape to (8, 8*gs_val) using Fortran order.
                        bin_arr = np.reshape(bin_arr, (8, 8 * gs_val), order='C')
                        # Multiply: (1x8) dot (8 x (8*gs_val)) yields a (8*gs_val)-element vector.
                        frame_pat[i, :8 * gs_val] = np.dot(twos, bin_arr)
                else:
                    # Non–row-compressed mode:
                    if gs_val == 1:
                        # Process each of the 8 columns of the block.
                        # For each column, compute the dot product of twos (1x8) with the column.
                        # This yields 8 numbers.
                        frame_pat[i, :8] = np.dot(twos, PanMat)
                    else:
                        # Flatten the 8×8 block in row-major order (since 'C' worked better)
                        flat = PanMat.flatten(order='C')

                        # Flatten the 8×8 block in row-major order (since 'C' worked better)
                        flat = PanMat.flatten(order='C')

                        # Compute total intensity sum to check "all off" or "all on" conditions
                        sum_pixels = np.sum(flat)
                        max_intensity = 2 ** gs_val - 1  # Max value for given gs_val (e.g., 3 for gs=2)

                        # MATLAB equivalent conditions:
                        if sum_pixels == 0:
                            # All OFF case → fill with zeros
                            frame_pat[i, :] = np.zeros(8 * gs_val, dtype=np.uint8)

                        elif sum_pixels / max_intensity == flat.size:
                            # All ON case → fill with 255
                            frame_pat[i, :] = np.full(8 * gs_val, 255, dtype=np.uint8)

                        else:
                            # Mixed case → convert pixels to binary representation
                            bin_arr = ((flat[:, None] >> np.arange(gs_val - 1, -1, -1)) & 1).astype(np.uint8)

                            # **Fix: Reshape carefully to match correct order**
                            bin_arr = bin_arr.reshape(8, 8, gs_val).transpose(0, 2, 1).reshape(8, 8 * gs_val)

                            # Multiply by appropriate weights (like MATLAB's `twos*binvec2`)
                            frame_pat[i, :] = np.dot(twos, bin_arr)

                # End processing for panel i.
            # Compute where in the overall pat_matrix this frame’s data should go.
            pat_start_index = pattern_number * num_panels
            pat_matrix[pat_start_index:pat_start_index + num_panels, :] = frame_pat
    # Print a message (optional)
    print("Packing pattern vector...")
    # Flatten pat_matrix into a 1D vector in column-major order (to mimic MATLAB)
    pat_vector = pat_matrix.ravel(order='C')
    return pat_vector


def save_pattern(pat, filename, Panel_map, gs_val, num_panels, row_compression=0, save_path="."):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Save the pattern to a .mat file (MATLAB format).

    :param pat: your pattern data
    :param filename: filename to save the pattern to
    :param Panel_map: Do I need to explain more?
    :param gs_val:
    :param num_panels:
    :param row_compression:
    :param save_path:
    :return:
    '''
    full_filename = os.path.join(save_path, filename)
    Pats = pat.astype(np.uint8)
    BitMapIndex = process_panel_map(np.array(Panel_map, dtype=np.int32))
    # Build the pattern structure.
    pattern_struct = {
        'num_panels': num_panels,
        'Panel_map': np.array(Panel_map, dtype=np.int32),
        'gs_val': gs_val,
        'row_compression': row_compression,
        'Pats': Pats,
        'x_num': int(pat.shape[2]),
        'y_num': 1,
        'BitMapIndex': BitMapIndex,
        'data': make_pattern_vector_ak({
            'Pats': Pats if Pats.ndim == 4 else Pats[..., np.newaxis],
            'gs_val': gs_val,
            'row_compression': row_compression,
            'BitMapIndex': BitMapIndex
        })
    }
    sio.savemat(full_filename, {'pattern': pattern_struct})
    print(f"Saved {full_filename}")


def dec2char(num, num_chars):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Convert a nonnegative integer into a list of num_chars bytes (MSB first).

    :param num:
    :param num_chars:
    :return:
    '''
    charArray = [0] * num_chars
    if num >= 2 ** (8 * num_chars):
        raise ValueError("Not enough characters for number of this size")
    if num < 0:
        raise ValueError("Negative numbers not supported")
    num_rem = num
    for j in range(num_chars, 0, -1):
        temp = math.floor(num_rem / (2 ** (8 * (j - 1))))
        num_rem -= temp * (2 ** (8 * (j - 1)))
        charArray[num_chars - j] = int(temp)
    return charArray


def make_flash_image(file_list, temp_path):
    """
    Anmo Kim
    Seongyeon Kim
    ChatGPT
    converted from matlab iFlyee

    For each .mat file (with a structured 'pattern') in file_list,
    load the pattern and create a corresponding raw .pat file.

    The header (512 bytes) is defined as:
       Bytes 0-1: x_num (16-bit little-endian)
       Bytes 2-3: y_num (16-bit little-endian)
       Byte 4: num_panels (8-bit)
       Byte 5: gs_val (if row_compression is on, gs_val+10; else gs_val)
       Bytes 6-7: current_frame_size (16-bit little-endian)
       Bytes 8-511: zeros.

    For gs_val = 2, current_frame_size = num_panels * 2 * 8 = 48*2*8 = 768 bytes per frame.
    The packed data is taken from pattern.data (a 1D uint8 vector) and padded so that
    each frame’s data begins on a 512-byte boundary.

    Returns an SD summary dictionary.
    """
    block_size = 512
    num_patterns = len(file_list)
    Header_block = [0] * block_size
    SD = {'num_patterns': num_patterns}
    SD_data = {'x_num': [], 'y_num': [], 'num_panels': [], 'gs_val': [], 'frame_size': [], 'pattNames': []}

    for j, file_dict in enumerate(file_list, start=1):
        fullpath = os.path.join(file_dict['PathName'], file_dict['FileName'])
        print(f"Processing {fullpath}")
        mat = loadmat(fullpath, squeeze_me=True, struct_as_record=False)
        if not hasattr(mat['pattern'], '_fieldnames'):
            print(f"File {fullpath} does not contain a structured 'pattern'.")
            continue
        pattern = mat['pattern']
        x_num = int(np.squeeze(pattern.x_num))
        y_num = int(np.squeeze(pattern.y_num))
        num_panels = int(np.squeeze(pattern.num_panels))
        gs_val = int(np.squeeze(pattern.gs_val))
        row_compression = int(np.squeeze(pattern.row_compression))
        data = np.array(pattern.data, dtype=np.uint8).flatten()

        current_frame_size = num_panels * gs_val * 8  # For gs_val==2: 48*2*8 = 768 bytes per frame.
        blocks_per_frame = math.ceil(current_frame_size / block_size)
        current_num_frames = x_num * y_num
        num_blocks_needed = blocks_per_frame * current_num_frames

        if row_compression:
            header_first8 = [dec2char(x_num, 2)[1], dec2char(x_num, 2)[0], dec2char(y_num, 2)[1], dec2char(y_num, 2)[0], num_panels, gs_val + 10, dec2char(current_frame_size, 2)[1], dec2char(current_frame_size, 2)[0]]
        else:
            header_first8 = [dec2char(x_num, 2)[1], dec2char(x_num, 2)[0], dec2char(y_num, 2)[1], dec2char(y_num, 2)[0], num_panels, gs_val, dec2char(current_frame_size, 2)[1], dec2char(current_frame_size, 2)[0]]

        print(header_first8)
        for i in range(8):
            Header_block[i] = header_first8[i]

        SD_data['x_num'].append(x_num)
        SD_data['y_num'].append(y_num)
        SD_data['num_panels'].append(num_panels)
        SD_data['gs_val'].append(gs_val)
        SD_data['frame_size'].append(current_frame_size)
        SD_data['pattNames'].append(file_dict['FileName'])

        Pattern_Data = np.zeros(num_blocks_needed * block_size, dtype=np.uint8)

        block_indexer = 0
        for i in range(current_num_frames):
            sd_start = block_indexer * block_size
            sd_end = sd_start + current_frame_size
            pat_start = i * current_frame_size
            pat_end = pat_start + current_frame_size
            Pattern_Data[sd_start:sd_end] = data[pat_start:pat_end]
            block_indexer += blocks_per_frame

        Data_to_write = np.concatenate((np.array(Header_block, dtype=np.uint8), np.array(Pattern_Data)))

        patFileName = "pat" + str(j).zfill(4) + ".pat"
        out_filepath = os.path.join(temp_path, patFileName)
        with open(out_filepath, 'wb') as fid:
            fid.write(Data_to_write.tobytes())
        print(f"Wrote {patFileName} with {Data_to_write.size} bytes")

        SD_data['x_num'].append(x_num)
        SD_data['y_num'].append(y_num)
        SD_data['num_panels'].append(num_panels)
        SD_data['gs_val'].append(gs_val)
        SD_data['frame_size'].append(current_frame_size)
        SD_data['pattNames'].append(file_dict['FileName'])

    SD.update(SD_data)
    return SD


def burn_pattern_to_SD(temp_path, sd_mount):
    """
    Anmo Kim
    Seongyeon Kim
    ChatGPT
    converted from matlab iFlyee

    Delete any existing .pat files on the SD card (sd_mount), then copy all .pat files
    from temp_path to sd_mount. Finally, build and save an SD summary file (SD.mat) on the SD card.
    """
    if not os.path.isdir(sd_mount):
        raise FileNotFoundError(f"SD card mount point not found: {sd_mount}")
    print(f"Burning patterns from '{temp_path}' to SD card at '{sd_mount}'...")
    for file in os.listdir(sd_mount):
        if file.lower().endswith('.pat'):
            try:
                os.remove(os.path.join(sd_mount, file))
                print(f"Removed {file}")
            except Exception as e:
                print(f"Error removing {file}: {e}")
    pat_files = glob.glob(os.path.join(temp_path, '*.pat'))
    if not pat_files:
        print("No .pat files found in temporary folder.")
        return
    for pat_file in pat_files:
        try:
            shutil.copy(pat_file, sd_mount)
            print(f"Copied {os.path.basename(pat_file)} to SD card.")
        except Exception as e:
            print(f"Error copying {pat_file}: {e}")
    SD = build_SD_structure(temp_path)
    sd_info_file = os.path.join(sd_mount, "SD.mat")
    savemat(sd_info_file, {'SD': SD})
    print(f"Saved SD summary to {sd_info_file}")


def build_SD_structure(temp_path):
    """
    Build an SD summary dictionary from the .pat files in temp_path.
    (These values are fixed examples; adjust them if needed.)
    """
    pat_files = sorted(glob.glob(os.path.join(temp_path, '*.pat')))
    num_patterns = len(pat_files)
    SD_pattern = {
        'num_patterns': num_patterns,
        'x_num': np.full((1, num_patterns), 175, dtype=np.double),
        'y_num': np.full((1, num_patterns), 1, dtype=np.double),
        'num_panels': np.full((1, num_patterns), 48, dtype=np.double),
        'gs_val': np.full((1, num_patterns), 25, dtype=np.double),
        'frame_size': np.full((1, num_patterns), 768, dtype=np.double),
        'pattNames': np.array([[os.path.basename(f) for f in pat_files]], dtype=object)
    }
    SD_function = {}  # Placeholder
    SD_arenaConfig = {}  # Placeholder
    SD = {'function': SD_function, 'pattern': SD_pattern, 'arenaConfig': SD_arenaConfig}
    return SD


def burn_and_save_SD_info(mat_folder, temp_path, sd_mount):
    """
    Anmo Kim
    Seongyeon Kim
    ChatGPT
    converted from matlab iFlyee

    1. Convert all .mat pattern files in mat_folder to .pat files in temp_path.
    2. Burn these .pat files onto the SD card at sd_mount.
    3. Build and save an SD summary file (SD.mat) on the SD card.
    """
    file_list = []
    for file_path in glob.glob(os.path.join(mat_folder, "*.mat")):
        file_list.append({
            'FileName': os.path.basename(file_path),
            'PathName': os.path.dirname(file_path)
        })
    if file_list:
        print(f"Converting {len(file_list)} .mat files to .pat files...")
        make_flash_image(file_list, temp_path)

    else:
        print("No .mat files found; assuming .pat files already exist in temporary folder.")
    burn_pattern_to_SD(temp_path, sd_mount)
