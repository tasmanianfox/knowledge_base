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