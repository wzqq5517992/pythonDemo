#coding=utf-8
def _write(_fileName, mode, text , charset):
    res = open( _fileName, mode , encoding=charset)
    res.write( text)
    res.close()
    return True
def _read(_fileName, mode, charset):
    res2 = open(_fileName , mode , encoding=charset)
    return res2.read()