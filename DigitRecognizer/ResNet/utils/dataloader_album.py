import os
import numpy as np
import pandas as pd

import cv2
import albumentations as albu
from albumentations.pytorch import ToTensor

import torch
import torch.nn as nn

from torchvision import transforms

from sklearn.model_selection import train_test_split

class MNIST(torch.utils.data.Dataset):
    
    def __init__(self, images, labels, trans):
        super().__init__()
        
        self.trans = trans
        
        self.images = images
        self.labels = labels
        
    def __len__(self):
        return len(self.images)
    
    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        
        image = self.trans(image=image)['image']
        
        return image, label