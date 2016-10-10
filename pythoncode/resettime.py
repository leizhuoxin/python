import exifread
import os

p=r'D:\z_test\sample'

LOG=r'D:\z_test\sample\log.txt'
ALLOWFORMAT=('.JPG','.PNG','.jpg','.png')

def listdir(path):
    dirs=os.listdir(path)
    for d in dirs:
        temp='{0}\{1}'.format(path,d)
        if os.path.isfile(temp) and ismatch(temp):
            dealfile(temp)
        elif os.path.isdir(temp):
            listdir(temp)    

def ismatch(filename):
    return os.path.splitext(filename)[1] in ALLOWFORMAT

def dealfile(path):
    t=gettime(path)
    if t:
        rename(path,t)
    else:
        writelog(path)
def gettime(path):
    val=None   
    try:       
        f=open(path,'rb')
    except:       
        writelog(path)
        pass
        #raise ReadFailException
    data=exifread.process_file(f)
    if data:
        try:
            val=str(data['EXIF DateTimeOriginal']).replace(':','-')            
        except:  
            writelog(path)         
            pass
    return val

def writelog(path):
    mode='wt'
    if os.path.exists(LOG):
        mode='at'
    with open(LOG,mode) as f:
        f.write('{info}{line}'.format(info=path,line=os.linesep))

def rename(path,date):
    oldname=os.path.basename(path)
    newname='{0}_{1}'.format(date,oldname)
    newpath='{0}\{1}'.format(os.path.dirname(path),newname)

    os.rename(path,newpath)


listdir(p)
#dealfile(p)
