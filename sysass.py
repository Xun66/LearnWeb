## -*- coding:gbk -*-
# Sep 13, 2017
import os

try:
    import _winreg, sys, os
except ImportError:
    print '* This Script only runs on windows platform, for linux/unix/macOS, please download unix version.'
    os._exit(-1)

def get_desktop():
    key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER,
                          r'Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders')
    return _winreg.QueryValueEx(key, "Desktop")[0]

def mkdir(path):
    #global detailed_output
    path = path.strip()
    path = path.rstrip("\\")
    isExists = os.path.exists(path)
    if not isExists:
        os.makedirs(path)
        print '�ɹ�����Ŀ¼', path
        return True
    #else:
        #if detailed_output:
            #print '��ȡ�Ѵ���Ŀ¼', path
    return False
