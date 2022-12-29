import torch
import torch.nn as nn
from utils import itersection_over_union

class Yololoss(nn.Module):
    def __init__(self, S=7, B=2, C=20):
        super(Yololoss, self).__init__()
        self.mse = nn.MSELoss(reduction="sum")
        