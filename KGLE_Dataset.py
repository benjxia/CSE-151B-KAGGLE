import torch
import pandas as pd
from torch.utils.data import DataLoader, Dataset


class KGLE_Dataset(Dataset):
    """
    Kaggle Dataset Pytorch class (Training set only)
    """
    def __init__(self, path: str):
        """
        Create a dataset object
        :param path: Path to PROCESSED training csv file
        """
        self.df: pd.DataFrame = pd.read_csv(path)

    def __len__(self):
        """
        :return: Size of dataset
        """
        return len(self.df)

    def __getitem__(self, item):
        """
        :param item: Index of item
        :return: (item, label) at index in dataset, item is predictor, label is prediction target
        """
        row = self.df.iloc[item]
        return torch.tensor(row[:-1]).double(), torch.tensor(row[-1]).double()
