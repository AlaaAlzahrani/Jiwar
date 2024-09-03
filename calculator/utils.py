def split_list(input_list, n_splits):
    """Splits a list into n nearly equal parts."""
    avg_len = len(input_list) / float(n_splits)
    splits = []
    last = 0.0

    while last < len(input_list):
        splits.append(input_list[int(last):int(last + avg_len)])
        last += avg_len

    return splits
