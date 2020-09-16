# awk

Use cases: transformation of stdout.

### Print the specified column

```bash
$ cat ./awk_sample.txt | awk '{print $0}' # prints the entire line

John,Smith  23
Jane,Doe    22

$ cat ./awk_sample.txt | awk '{print $1}' # prints the first column

John,Smith
Jane,Doe

$ cat ./awk_sample.txt | awk '{print $2}' # prints the second column

23
22

$ cat ./awk_sample.txt | awk -F, '{print $2}' # use comma as a separator. The default separators are spaces and tabs

Smith  23
Doe    22
```

### Replace string

The example below replaces `J` with `K` in each line

```bash
$ cat ./awk_sample.txt | awk '{gsub("J", "K", $0);print}'

Kohn,Smith  23
Kane,Doe    22
```

Replace `h` with `!` in all columns __NB! Comma is used as a column separator__

```bash
$ cat ./awk_sample.txt | awk -F, '{gsub("h", "!", $0);print}'

Jo!n,Smit!  23
Jane,Doe    22
```

Replace `h` with `!` in the second column only __NB! Comma is used as a column separator__

```bash
cat ./awk_sample.txt | awk -F, '{gsub("h", "!", $2);print}'

John Smit!  23
Jane,Doe    22
```