import marshal
import base64
import gzip
import zlib
import pickle

def pickle_enc(code):
    return pickle.dumps(code)
def marshal_enc(code):
    return marshal.dumps(code)
def base64_enc(code):
    return base64.b64encode(code)
def zlib_enc(code):
    return zlib.compress(code)
def gzip_enc(code):
    return gzip.compress(code)


def pickle_dec(code):
    return pickle.loads(code)
def marshal_dec(code):
    return marshal.loads(code)
def base64_dec(code):
    return base64.b64decode(code)
def zlib_dec(code):
    return zlib.decompress(code)
def gzip_dec(code):
    return gzip.decompress(code)

def Cencrypt(code):
    try:
        n = pickle_enc(code)
        a=marshal_enc(n)
        b=base64_enc(a)
        c=zlib_enc(b)
        d=gzip_enc(c)
        return d
    except Exception as e:
        return f"Error {e}"


def Cdecrypt(code):
    try:
        a=gzip_dec(code)
        b=zlib_dec(a)
        c=base64_dec(b)
        d=marshal_dec(c)
        e = pickle_dec(d)
        return e
    except Exception as e:
        return f"Error {e}"