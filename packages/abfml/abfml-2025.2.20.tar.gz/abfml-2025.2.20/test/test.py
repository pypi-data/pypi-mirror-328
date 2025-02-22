import torch
import torch.nn as nn
import torch.optim as optim
from typing import Optional

# 定义简单神经网络
class SimpleNN():
    def __init__(self, input_size:Optional[int]=None, hidden_size:Optional[int]=None, output_size:Optional[int]=None):

        self.fc1 = 3 # 第一层
        self.relu = 1
        self.fc2 = 2
        self.input_size=input_size# 输出层

    def forward(self, x):
        x = self.fc1

        mapped_value = torch.arange(0, 10)
        a: int = int(torch.max(mapped_value).item())
        mapped_table = torch.full(size=( 1+ 1,2), fill_value=-1)
        if self.input_size is not None:
            x=x+1
        return x

torch.jit.script(SimpleNN(2, 3, 4))
print('aa')
