# Importing Files📁 from different Folder🗃️
## Folder structure
> [`GitHub Repo`](https://github.com/Ayon-SSP/Importing-Files) Practical project

```js
Folders
├── Folder1
│   ├── subFolder1
│   │    └── File2.py 
│   ├── File1.py  
│   └── MainFile.py 
└── Folder2
    └── subFolder3
         └── File3.py
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

![image](https://user-images.githubusercontent.com/80549753/222135458-87f76004-cda6-4b9f-895a-90c793116c2f.png)

```python
import sys
sys.path.append('../../ChatGPT-Twitter-Bot/')
from credentials import *
```
