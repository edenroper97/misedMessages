print("Question 1 answer:")

import shutil

src="Practice1.txt"
dst="Practice2.txt"

shutil.copy(src,dst)

print("<-------------------------------------------------------->")


import os

os.rename("Practice2.txt","Practice3.txt")


print("-------------------------------------")





