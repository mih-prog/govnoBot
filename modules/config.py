import json, io, os


class configs():
    def __init__(self, confDir):
        self.DbDerectoryName = confDir

    def get(self, path):
        if not os.path.isdir(self.DbDerectoryName + '/' + path):
            return None
        else:
            if not os.path.isfile(self.DbDerectoryName + '/' + path + '/data'):
                return None
            else:
                file = io.FileIO(self.DbDerectoryName+'/'+path+'/data')
                file.seek(0)
                try:data = json.loads(file.read().decode())
                except:file.seek(0); file.write(b'{}'); data = {}
                file.close()
                return data

    def set(self, path, data):
        if not os.path.isdir(self.DbDerectoryName + '/' + path):
            os.makedirs(self.DbDerectoryName + '/' + path)
            file = io.FileIO(self.DbDerectoryName+'/'+path+'/data', 'w+')
            file.write(json.dumps(data).encode())
            file.close()
        else:
            if not os.path.isfile(self.DbDerectoryName + '/' + path + '/data'):
                file = io.FileIO(self.DbDerectoryName + '/' + path + '/data', 'w+')
                file.write(json.dumps(data).encode())
                file.close()
            else:
                file = io.FileIO(self.DbDerectoryName + '/' + path + '/data', 'w+')
                file.seek(0)
                file.write(json.dumps(data).encode())
                file.close()
