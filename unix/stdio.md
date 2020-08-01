# Standard input and output

### Writing stdout to a file

This will create a new file if it doesn't exist or __overwrite__ an existing one otherwise:

```bash
command > file.txt
```

This will create a new file if it doesn't exist or __append__ the output to existing file otherwise:

```bash
command >> file.txt
```

__Example:__

```bash
$ echo "Hello, world!" > 1.txt
$ echo "Hello, world!" > 1.txt
# File "1.txt" has a single line "Hello, World!"

$ echo "Hello, world!" >> 2.txt
$ echo "Hello, world!" >> 2.txt
# File "2.txt" has two "Hello, World!" lines
```

In this case errors (`stderr`) are still passed to terminal instead of file:

```bash
$ date % > 1.txt # "date %" is an invalid commmand which generates an error message
date: invalid date ‘%’

$ cat 1.txt

# The 1.txt file is empty
```

### Writing stdout and stderr to the same file

```bash
$ date % > 1.txt 2>&1

$ cat 1.txt
date: invalid date ‘%’
```

### Writing stdout and stderr to different files

Let's try a command `bash -c 'echo test && date %'` which will print "test" to `stdout` and then throw an error on attempt to execute the `date %` command

``` bash
$ bash -c 'echo test && date %' > my_stdout.txt 2> my_stderr.txt

$ cat my_stdout.txt 
test

$ cat my_stderr.txt 
date: invalid date ‘%’
```

### Passing contents of file to stdin

```bash
$ myprogram < /path/to/file.txt
```

__Example for this repo: calculation of lines number in a file__

```bash
$ wc -l < ./README.md
13
```

### Passing stdout of one command to another command

```bash
$ command1 | command2 | command3 | ... | commandn
```

__Example for this repo: calculation of lines number in a file__

```bash
$ cat ./README.md | wc -l
13
```

__Example for this repo: finding files and dirs in root directory which name contains "unix"__

```bash
$ ls -lah | grep unix
drwxrwxr-x  2 myuser mygroup 4.0K Jul 29 22:29 unix
drwxrwxr-x  3 myuser mygroup 4.0K Jul 29 21:06 unix_binutils
```