# Importing Filesπ from different FolderποΈ
## Folder structure
> [`GitHub Repo`](https://github.com/Ayon-SSP/Importing-Files) Practical project

```js
Folders
βββ Folder1
β   βββ subFolder1
β   β    βββ File2.py 
β   βββ File1.py  
β   βββ MainFile.py 
βββ Folder2
    βββ subFolder3
         βββ File3.py
```

> Main Folder is `Folders`
> `Folders` -> contains 2 subFolder Name `Folder1` & `Folder2`
> `Folder1` -> `subFolder1` & `MainFile.py`
> `Folder2` -> `subFolder3` -> `File3.py`
> `subFolder1` -> `File1.py` & `File2.py`

## **To import File from different Folders**
### 1. File in the same directory
`MainFile.py`
```python
import File1
```
### 2. File in the sub directory
`MainFile.py`
```python
from subFolder1 import File2
```
### 3. File in the parent directory
`MainFile.py`
```python
# You Can use this to import file from any directory
import sys
sys.path.insert(1,'C://Repo//temptodel//Folders//Folder2//subFolder3')

import File3
print(File3.f33)
```