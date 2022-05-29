import glob
import pandas as pd

paths=glob.glob(r'G:\\dice\\*.xlsx')  #获取test文件下所有的excel文件路径

data1=pd.DataFrame(columns=[]) #先构建一个空的数据框

for path in paths:   #遍历下
    data=pd.read_excel(path)
    data1=pd.concat([data1,data])

print(data1)  #打印出来就大功告成啦，最后可以再输出
data1.to_excel(r'G:\\dice.xls')  #输出


# import xlrd, xlwt
#
# target_file = "G:\\dice\\dice.xls"
#
#
# # Press Shift+F10 to execute it or replace it with your code.
# # Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# def IsSubString(SubStrList, Str):
#     '''''
#     #判断字符串Str是否包含序列SubStrList中的每一个子字符串
#     #>>>SubStrList=['F','EMS','txt']
#     #>>>Str='F06925EMS91.txt'
#     #>>>IsSubString(SubStrList,Str)#return True (or False)
#     '''
#     flag = True
#     for substr in SubStrList:
#         if not (substr in Str):
#             flag = False
#     return flag
#
#
# def fn_get_filelist(FindPath, FlagStr=[]):
#     '''''
#     #获取目录中指定的文件名
#     #>>>FlagStr=['F','EMS','txt'] #要求文件名称中包含这些字符
#     #>>>FileList=GetFileList(FindPath,FlagStr) #
#     '''
#     import os
#     FileList = []
#     FileNames = os.listdir(FindPath)
#     if len(FileNames) > 0:
#         for fn in FileNames:
#             if len(FlagStr) > 0:
#                 # 返回指定类型的文件名
#                 if IsSubString(FlagStr, fn):
#                     fullfilename = os.path.join(FindPath, fn)
#                     FileList.append(fullfilename)
#             else:
#                 # 默认直接返回所有文件名
#                 fullfilename = os.path.join(FindPath, fn)
#                 FileList.append(fullfilename)
#                 # 对文件名排序
#     if (len(FileList) > 0):
#         FileList.sort()
#     for i in range(len(FileList)):
#         print(FileList[i])
#
#     return FileList
#
#
# def gather_excel(fn):
#     workbook = xlwt.Workbook(encoding='utf-8')
#     ws = workbook.add_sheet("流量来源详情")
#
#     title_data = ["来源名称", "访客数", "浏览量", "支付金额", "浏览量占比", "店内跳转人数", "跳出本店人数", "收藏人数", "加购人数", "下单买家数", "下单转换率", "支付件数",
#                   "支付买家数", "支付转换率", "直接支付买家", "收藏商品-支付买家数", "粉丝支付买家数", "加购商品-支付买家数"]
#     target_list = [title_data]
#
#     for n in range(len(title_data)):
#         ws.write(0, n, target_list[0][n])
#
#     index = 1
#
#     for i in range(len(fn)):
#
#         data_list = read_excel(fn[i])
#         length_data_list = len(data_list)
#
#         for j in range(length_data_list):
#             list_line = data_list[j]
#
#             target_list.append(list_line)
#             for n in range(len(list_line)):
#                 ws.write(index, n, target_list[index][n])
#             list_line.clear()
#             index = index + 1
#     save_result(workbook)
#
#
# def save_result(wb):
#     wb.save(target_file)
#     print("存储成功！！！")
#
#
# def read_excel(file_name):
#     work = xlrd.open_workbook(file_name)
#     sheet = work.sheet_by_index(0)
#     rows = sheet.nrows
#
#     rows_list = []
#     for i in range(1, rows):
#         rows_list.append(sheet.row_values(i))
#     return rows_list
#
#
# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# def process():
#     fs = fn_get_filelist("G:\\dice", ['xlsx'])
#
#     gather_excel(fs)
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     process()
