import cv2
import numpy as np
from torch.utils.data import Dataset

class ContourDataset(Dataset):
    def __init__(self, image_paths):
        self.image_paths = image_paths

    def __getitem__(self, idx):
        img = cv2.imread(self.image_paths[idx], cv2.IMREAD_GRAYSCALE)
        # Canny算法参数说明：
        # - 100: 低阈值，低于此值的边缘被忽略
        # - 200: 高阈值，高于此值的边缘被保留
        edges = cv2.Canny(img, 100, 200)
        edges = edges / 255.0  # 归一化到[0,1]
        return torch.FloatTensor(edges).unsqueeze(0)  # 增加通道维度 (1, H, W)