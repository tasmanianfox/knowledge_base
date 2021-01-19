# ls

List contents directory. Current direcotry by default.

### List files with no detailed info

```
$ ls

binutils  common  languages  LICENSE  README.md
```

### List files with no detailed info, one file or directory per line

_No need to format the output for Unix pipes. Useful for Bash scripts_


```bash
$ ls -1

common
languages
LICENSE
README.md
unix
unix_binutils
```

### List files with detailed info

```
$ ls -l

total 24
-rw-rw-r-- 1 myuser mygroup 7048 Jul  4 21:50 LICENSE
-rw-rw-r-- 1 myuser mygroup  384 Jul  8 21:35 README.md
drwxrwxr-x 2 myuser mygroup 4096 Jul 10 21:20 binutils
drwxrwxr-x 3 myuser mygroup 4096 Jul  4 22:27 common
drwxrwxr-x 3 myuser mygroup 4096 Jul  4 22:16 languages
```

### List files with detailed info + show hidden (prefixed with dot) files

```
$ ls -la

total 36
drwxrwxr-x  6 myuser mygroup 4096 Jul 10 21:19 .
drwxr-xr-x 14 myuser mygroup 4096 Jul  4 21:42 ..
drwxrwxr-x  8 myuser mygroup 4096 Jul 10 21:20 .git
-rw-rw-r--  1 myuser mygroup 7048 Jul  4 21:50 LICENSE
-rw-rw-r--  1 myuser mygroup  384 Jul  8 21:35 README.md
drwxrwxr-x  2 myuser mygroup 4096 Jul 10 21:20 binutils
drwxrwxr-x  3 myuser mygroup 4096 Jul  4 22:27 common
drwxrwxr-x  3 myuser mygroup 4096 Jul  4 22:16 languages
```

### List files with detailed info + show hidden (prefixed with dot) files + human readable file size

```
$ ls -lah

total 36K
drwxrwxr-x  6 myuser mygroup 4.0K Jul 10 21:19 .
drwxr-xr-x 14 myuser mygroup 4.0K Jul  4 21:42 ..
drwxrwxr-x  8 myuser mygroup 4.0K Jul 10 21:20 .git
-rw-rw-r--  1 myuser mygroup 6.9K Jul  4 21:50 LICENSE
-rw-rw-r--  1 myuser mygroup  384 Jul  8 21:35 README.md
drwxrwxr-x  2 myuser mygroup 4.0K Jul 10 21:20 binutils
drwxrwxr-x  3 myuser mygroup 4.0K Jul  4 22:27 common
drwxrwxr-x  3 myuser mygroup 4.0K Jul  4 22:16 languages
```

### Show contents of a specified directory
Add a directory name to the end. It could be either relative or absolute path.

```
$ ls -lah languages 

total 16K
drwxrwxr-x 3 myuser mygroup 4.0K Jul  4 22:16 .
drwxrwxr-x 6 myuser mygroup 4.0K Jul 10 21:19 ..
-rw-rw-r-- 1 myuser mygroup   41 Jul 10 21:19 README.md
drwxrwxr-x 2 myuser mygroup 4.0K Jul  8 21:32 python
```

