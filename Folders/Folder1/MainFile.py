import File1
print(File1.f1)


from subFolder1 import File2
print(File2.f2)

import sys
sys.path.insert(1,'C://Repo//temptodel//Folders//Folder2//subFolder3')

import File3
print(File3.f33)
