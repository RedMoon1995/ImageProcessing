"""
@Author : Nanrong Zeng
@Date   : 2022/5/25 21:26 
@Desc   : 
"""
import pandas as pd
from torch.utils.tensorboard import SummaryWriter

train_loss = pd.read_csv('../log/train_loss.csv')
valid_loss = pd.read_csv('../log/valid_loss.csv')
writer = SummaryWriter(log_dir='../log/train_valid_loss')

for i in range(len(train_loss)):
    writer.add_scalars('Loss', {'Train Loss': float(train_loss['Value'][i]), 'Valid Loss': float(valid_loss['Value'][i])},
                       train_loss['Step'][i])
print("finish")
writer.close()
