# Tar

## Flags

### Compress / extract / view
```
-c - create an archive
-t - list contents of archive
-v - show progress
-x - extract an archive
```

### Compression
```
-z - gzip
-j - bzip2
-J - xz
```

## Examples

### Create a *.tar.gz archive

```bash
tar -czf archive.tar.gz directory_to_process
```

### Create a *.tar.xz archive

```bash
tar -cJf archive.tar.xz directory_to_process
```

### Look up contents of *.xz archive

```bash
$ tar -tvf archive.tar.xz
```

## Example for this repo

```bash
$ cp -R languages languages2 # Just for test

$ tar -cJf test.tar.xz languages2 # Create an archive test.tar.xz which contains files from lanugages2 dir

$ tar -tf test.tar.xz # View contents - simplified
languages2/
languages2/README.md
languages2/python/
languages2/python/conditions.md
languages2/python/classes.md
languages2/python/blocks.md
languages2/python/README.md
languages2/python/examples/
languages2/python/examples/classes/
languages2/python/examples/classes/super_method.py

$ tar -tvf test.tar.xz # View contents - more detailed
drwxrwxr-x myuser/mygroup     0 2020-08-05 16:37 languages2/
-rw-rw-r-- myuser/mygroup    41 2020-08-05 16:37 languages2/README.md
drwxrwxr-x myuser/mygroup     0 2020-08-05 16:37 languages2/python/
-rw-rw-r-- myuser/mygroup   278 2020-08-05 16:37 languages2/python/conditions.md
-rw-rw-r-- myuser/mygroup  1512 2020-08-05 16:37 languages2/python/classes.md
-rw-rw-r-- myuser/mygroup   513 2020-08-05 16:37 languages2/python/blocks.md
-rw-rw-r-- myuser/mygroup   113 2020-08-05 16:37 languages2/python/README.md
drwxrwxr-x myuser/mygroup     0 2020-08-05 16:37 languages2/python/examples/
drwxrwxr-x myuser/mygroup     0 2020-08-05 16:37 languages2/python/examples/classes/
-rw-rw-r-- myuser/mygroup   373 2020-08-05 16:37 languages2/python/examples/classes/super_method.py

$ rm -rf languages2 # we will extract the archive here
$ tar -xf test.tar.xz # extract
$ ls languages2 # directory is here again
python  README.md

$ rm -rf languages2 #cleanup
$ rm test.tar.xz
```