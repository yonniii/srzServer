import os


# path_dir = "C:Users/rkdtj/PycharmProjects/unititled/files"
import string

class getFiles:
    def __init__(self):
        self.path_dir = '/home/yonnii/srz/srzServer/files'

    def exe(self):
        fileList = os.listdir(self.path_dir)
        metalist = []
        if os.path.exists(self.path_dir):
            for i in fileList:
                path = self.path_dir+"/"+i
                fileinfo = os.stat(path)
                # time = datetime.datetime.fromtimestamp(fileinfo.st_mtime)
                time = fileinfo.st_mtime
                # md5 = hash.getHash('%s,%s'%(path,time))
                # md5 = hash.getHash(path)
                metalist.append("%s,%s,%s" %(time,
                                         i,
                                         path))
                # list.append("filename :%s size :%d modified :%s" %(i,fileinfo.st_size,datetime.datetime.fromtimestamp(fileinfo.st_mtime)))
        return metalist

g=getFiles()
print(g.exe())