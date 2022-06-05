import os
import pandas as pd
import numpy as np

def csv2mart(path):
    data_read = pd.read_csv(path)
    list = data_read.keys().tolist()
    list_new = list[0].split()
    return list_new

if __name__ == '__main__':
    path = 'G:\\dice'
    output_path = 'G:\\test.xlsx'
    mask1num = []
    for _,_,files in os.walk(path):
        for file in files:
            #if file[10:12] == '50':
            print(file)
            data = csv2mart(os.path.join(path, file))
            mask1num.append(data)
    da = np.array(mask1num)
    da1 = np.resize(da, (38, 10))
    print(da1.shape)
    pd.DataFrame(da1).to_excel(os.path.join(output_path), sheet_name='Sheet1')
