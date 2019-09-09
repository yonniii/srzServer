import os
import datetime
from md5hash import md5hash

# path_dir = "C:Users/rkdtj/PycharmProjects/unititled/files"
import string

class getFiles:
    def __init__(self):
        self.path_dir = 'C:\\Users\\yonnii\\Desktop\\3-2\\srzServer\\srzProject\\files'

    def exe(self):
        fileList = os.listdir(self.path_dir)
        metalist = []
        hash = md5hash()
        if os.path.exists(self.path_dir):
            for i in fileList:
                path = self.path_dir+"\\"+i
                fileinfo = os.stat(path)
                # time = datetime.datetime.fromtimestamp(fileinfo.st_mtime)
                time = fileinfo.st_mtime
                md5 = hash.getHash('%s,%s'%(path,time))
                # md5 = hash.getHash(path)
                metalist.append("%s,%s,%s,%s" %(time,
                                         i,
                                         path,
                                         md5))
                # list.append("filename :%s size :%d modified :%s" %(i,fileinfo.st_size,datetime.datetime.fromtimestamp(fileinfo.st_mtime)))
        return metalist

g=getFiles()
g.exe()