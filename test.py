import torch
import numpy as np


tensor = torch.ones(4, 4)
print(tensor)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
tensor = tensor.to(device)
print(tensor.is_cuda)
print(f"device: ", tensor.device)
print(torch.cuda.device_count())