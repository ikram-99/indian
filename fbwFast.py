#Coded by  Mr Rana
#YOUTUBE   Mr Nadeem
#FB        www.facebook.com/ikramali007

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))
