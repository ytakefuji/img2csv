from PIL import Image
import sys,os

flag=0
l=len(sys.argv)
st=str(sys.argv[1:])

if "sdir" in st:
 if "ddir" in st:
  if "size" in st:
   if "type" in st:
    flag=1
   else:print("no type")
  else:print("no size")
 else:print("no ddir")
else: print("no sdir")
if flag==0:sys.exit()
st=sys.argv[1:]

for i in st:
 if "sdir" in i:sdir=i.split("sdir=",2)[1]
 if "ddir" in i:ddir=i.split("ddir=",2)[1]
 if "type" in i:type=i.split("type=",2)[1]
 if "size" in i:size=i.split("size=",2)[1]
sdir=str(sdir)+"/"
ddir=str(ddir)+"/"
size=(int(size),int(size))
type=str(type)
list=os.listdir(sdir)

for i in list:
 try:
  img=Image.open(sdir+i).convert(type)
  img.resize(size,Image.ANTIALIAS).save(ddir+i)
 except:
  print("something wrong in ",i)
  sys.exit()
print("resizing completed")
