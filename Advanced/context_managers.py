

class FileOpen:
    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.fd = open(self.filename, self.mode)
        return self.fd

    def __exit__(self, *args):
        self.fd.close()
        print('fd closed')

with FileOpen('temp1.txt', 'w') as wd:
    wd.write('this is for testing new')        
    
from contextlib import contextmanager

@contextmanager
def fileopen(filename, mode):
    fd = open(filename, mode)
    yield fd
    fd.close()

with fileopen('temp.txt', 'w') as wd:
    wd.write('this is for testing')