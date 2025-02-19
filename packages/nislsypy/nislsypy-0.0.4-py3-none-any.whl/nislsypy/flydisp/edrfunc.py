import os
import numpy as np
import neo


def search_edr(directory):
    '''
        Tue 18 Feb 2025
        v0.0.1
        Seongyeon Kim

        :param directory: your folder path which .edr files are located
        :return: each edr file
    '''
    return [os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".EDR")]


def import_edr(file_path):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    import edr and return as ideal dataform (like matlab)

    :param file_path: edr file path (search_edr will do)
    :return: Stacked 1D arrays (like column) (n, m) shape
    '''
    reader = neo.WinEdrIO(file_path)
    block = reader.read_block()
    analog_signals = block.segments[0].analogsignals

    dt = analog_signals[0].sampling_period.rescale("s").magnitude
    signals = [np.squeeze(sig.magnitude) for sig in analog_signals]

    for idx, s in enumerate(signals):
        print(f"Channel {idx} shape: {s.shape}")

    data = np.column_stack(signals)

    return data, {"DT": dt}
