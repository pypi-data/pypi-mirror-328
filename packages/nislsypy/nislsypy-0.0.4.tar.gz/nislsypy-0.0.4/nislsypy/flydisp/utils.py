import numpy as np
from scipy.signal import find_peaks
from sklearn.cluster import KMeans
from scipy.ndimage import median_filter


def clear_nonflying(lwba, rwba, patid, voltage_threshold):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Change the value under threshold as nan

    :param lwba: lwba in your data (returned value from import_edr)
    :param rwba: do I need to explain more?
    :param patid:
    :param voltage_threshold:
    :return:
    '''
    if lwba.shape != rwba.shape:
        raise ValueError("Error: lwba and rwba must have the same shape")

    lwba = np.where(lwba < voltage_threshold, np.nan, lwba)
    rwba = np.where(rwba < voltage_threshold, np.nan, rwba)

    new_lwba = lwba
    new_rwba = rwba
    new_patid = patid

    return new_lwba, new_rwba, new_patid


def group_pattern_ids(x, patID_to_be_tested, threshold=-5, trim_frac=0.0):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Convert analogue pattern signal to real pattern ID
    I used several grouping methods

    :param x: patid column
    :param patID_to_be_tested: your pattern ID information like this "np.arange(1, 33)  # MATLAB 1:32 -> Python range 1 to 32"
    :param threshold: analogue value filter
    :param trim_frac: you can cut edge value
    :return: pretty pattern ids
    '''
    result = np.zeros_like(x, dtype=int)

    pos_mask = x > threshold
    if not np.any(pos_mask):
        return result

    pos_vals = x[pos_mask]

    sort_idx = np.argsort(pos_vals)
    sorted_vals_full = pos_vals[sort_idx]
    n = len(sorted_vals_full)

    lower_cut = int(np.floor(trim_frac * n))

    mapped_sorted = np.empty(n, dtype=int)

    mapped_sorted[:lower_cut] = 0
    sorted_vals = sorted_vals_full[lower_cut:]

    reshaped_data = sorted_vals.reshape(-1, 1)  # Reshape for clustering

    sorted_vals = median_filter(sorted_vals, size=3)

    # You can change the bins, estimated variables.
    # Depend on the variables, the pattern number can be shifted. Be careful
    # The below is recommended one
    hist, bin_edges = np.histogram(sorted_vals, bins=1000)
    estimated_prominence = np.max(hist) * 0.01
    estimated_distance = 5
    peaks, _ = find_peaks(hist, prominence=estimated_prominence, distance=estimated_distance)  # Detect histogram peaks
    k = len(peaks)

    kmeans = KMeans(n_clusters=k, n_init="auto", random_state=0)
    raw_labels = kmeans.fit_predict(reshaped_data)

    cluster_means = {label: np.mean(sorted_vals[raw_labels == label]) for label in np.unique(raw_labels)}
    sorted_labels = sorted(cluster_means, key=cluster_means.get)
    sorted_means = [cluster_means[label] for label in sorted_labels]

    step_sizes = np.diff(sorted_means)
    median_step_size = np.median(step_sizes)

    labels = np.zeros_like(raw_labels, dtype=int)
    current_label = 1
    prev_mean = sorted_means[0]

    for label, mean_value in zip(sorted_labels, sorted_means):
        step_size = mean_value - prev_mean  # Compute step difference

        # Dynamically adjust the label increment based on all step sizes
        step_jump = round(step_size / median_step_size)  # Normalize by median step size
        current_label += max(1, step_jump)

        labels[raw_labels == label] = current_label
        prev_mean = mean_value  # Update previous mean

    labels = labels - max(labels)
    labels = labels + max(patID_to_be_tested)
    mapped_sorted[lower_cut:] = labels

    final_labels = np.empty_like(pos_vals, dtype=int)
    final_labels[sort_idx] = mapped_sorted

    result[pos_mask] = final_labels
    return result


def filter_onset_indices(onset_indices, min_gap=3000):
    '''
    Tue 18 Feb 2025
    v0.0.1
    Seongyeon Kim

    Sometimes there are some noise and one trial is detected as two.
    To prevent that kind of thing...

    :param onset_indices: trial onset indices in your code
    :param min_gap: ms
    :return: the small gap onset indices is removed
    '''
    onset_indices = np.asarray(onset_indices)
    if onset_indices.size == 0:
        return onset_indices
    filtered = [onset_indices[0]]
    for idx in onset_indices[1:]:
        if idx - filtered[-1] >= min_gap:
            filtered.append(idx)
    return np.array(filtered)
