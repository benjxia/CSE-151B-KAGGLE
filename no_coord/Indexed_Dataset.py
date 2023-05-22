import torch
import pandas as pd
from torch.utils.data import DataLoader, Dataset
import numpy as np


class Indexed_Dataset(Dataset):
    """
    Kaggle Dataset Pytorch class (Training set only)
    """

    def __init__(self, path: str = None, npy: bool = False, arr=None):
        """
        Create a dataset object
        :param path: Path to PROCESSED training csv file
        :param npy: Put true if path is from .npy file, leave false if .csv
        :param arr: Existing array, will override all parameters
        """
        if arr is not None:
            self.arr = arr
        elif not npy:
            self.arr = np.loadtxt(path, delimiter=",", skiprows=1, dtype=np.float32)
        else:
            self.arr = np.load(path)

    def __len__(self):
        """
        :return: Size of dataset
        """
        return self.arr.shape[0]

    def __getitem__(self, item):
        """
        :param item: Index of item
        :return: (item, label) at index in dataset, item is predictor, label is prediction target
        """
        # The main difference from normal dataset: it skips the first column for indexing
        return torch.from_numpy(self.arr[item, 1: -1]), torch.from_numpy(self.arr[item, -1:])
