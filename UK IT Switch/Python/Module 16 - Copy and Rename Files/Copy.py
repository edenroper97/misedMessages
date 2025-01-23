import shutil

src="demo.txt"
dst="EdenDemo.txt"
shutil.copy(src,dst)

print("-------------------------------------")

print("Rename files os") 

import os

os.rename("EdenDemo.txt","EdenDemoRename.txt")


print("-------------------------------------")

print("Delete File")

import os
os.remove("EdenDemo.txt")




