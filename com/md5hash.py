import hashlib

class md5hash:
    def getHash(self,path,blocksize=65536):
        # afile = open(path, 'rb')
        hasher = hashlib.md5()
        buf = path.encode()
        hasher.update(buf)
        # buf = afile.read(blocksize)
        # while len(buf) > 0:
        #     hasher.update(buf)
        #     buf = afile.read(blocksize)
        # afile.close()
        return hasher.hexdigest()