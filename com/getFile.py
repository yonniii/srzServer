import os
import datetime

# path_dir = "C:Users/rkdtj/PycharmProjects/unititled/files"
import string

class getFiles:
    def __init__(self):
        self.path_dir = 'C:\\Users\\rkdtj\\PycharmProjects\\srzProject\\files'

    def exe(self):
        fileList = os.listdir(self.path_dir)
        list = []
        if os.path.exists(self.path_dir):
            for i in fileList:
                path = self.path_dir+"\\"+i
                fileinfo = os.stat(path)
                # print("filename :%s size :%d modified :%s" %(i,fileinfo.st_size,datetime.datetime.fromtimestamp(fileinfo.st_mtime)))
                list.append("filename :%s size :%d modified :%s" %(i,fileinfo.st_size,datetime.datetime.fromtimestamp(fileinfo.st_mtime)))
        return list

g=getFiles()
g.exe()