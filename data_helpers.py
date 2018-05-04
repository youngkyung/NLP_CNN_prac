import numpy as np
import re
import itertools
from collections import Counter

def load_data_and_labels(true_data_file, false_data_file):
    """
    Loads MR polarity data from files, splits the data into words and generates labels.
    Returns split sentences and labels.
    """
    # Load data from files
    true_examples = list(open(true_data_file, "rt", encoding='UTF8').readlines())
    true_examples = [s.strip() for s in true_examples]
    false_examples = list(open(false_data_file, "rt", encoding='UTF8').readlines())
    false_examples = [s.strip() for s in false_examples]
    # Split by words
    x_text = true_examples + false_examples
    # Generate labels
    true_labels = [[0, 1] for _ in true_examples]
    false_labels = [[1, 0] for _ in false_examples]
    y = np.concatenate([true_labels, false_labels], 0)


    # print([x_text, y])
    # print(np.array(y).tolist())
    return [x_text, y]


def batch_iter(data, batch_size, num_epochs, shuffle=True):
    """
    Generates a batch iterator for a dataset.
    """
    data = np.array(data)
    data_size = len(data)
    num_batches_per_epoch = int((len(data)-1)/batch_size) + 1
    for epoch in range(num_epochs):
        # Shuffle the data at each epoch
        if shuffle:
            shuffle_indices = np.random.permutation(np.arange(data_size))
            shuffled_data = data[shuffle_indices]
        else:
            shuffled_data = data
        for batch_num in range(num_batches_per_epoch):
            start_index = batch_num * batch_size
            end_index = min((batch_num + 1) * batch_size, data_size)
            yield shuffled_data[start_index:end_index]