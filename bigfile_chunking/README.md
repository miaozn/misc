# big file chunking
This script can help you chunk a big file into several small pieces. For example, let say we have a big file whose size is 10000 bytes.
```bash
$ ls -l
total 16
-rw-r--r-- 1 ubuntu ubuntu 10000 Jul  9 04:31 bigfile
-rwx------ 1 ubuntu ubuntu   545 Jul  9 04:28 chunking.py*
```
## run
To run the script, please specify the file name and chunk size.
```bash
$ ./chunking.py bigfile 1024
```  
## result
```bash
$ ls -l
total 56
-rw-r--r-- 1 ubuntu ubuntu 10000 Jul  9 04:31 bigfile
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_1
-rw-r--r-- 1 ubuntu ubuntu   784 Jul  9 04:32 bigfile_10
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_2
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_3
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_4
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_5
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_6
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_7
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_8
-rw-r--r-- 1 ubuntu ubuntu  1024 Jul  9 04:32 bigfile_9
-rwx------ 1 ubuntu ubuntu   545 Jul  9 04:28 chunking.py*
```

