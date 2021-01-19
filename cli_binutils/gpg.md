# GNU Privacy Guard

### List public keys

```bash
gpg --list-keys
```

### List secret keys

```bash
gpg --list-secret-keys
```

### Encrypt data from stdin and save to file

```bash
echo "Hello, World\!" | gpg --output output_filetxt.gpg --encrypt --recipient john.doe@example.com
```

### Encrypt data from file and save to file

```bash
gpg --output output_file.txt.gpg --encrypt --recipient john.doe@example.com input_file.txt
```

### Decrypt a file to stdout

```bash
gpg --decrypt myfile.txt.gpg > /dev/stdout 2>/dev/null
```
`2>/dev/null` is added to get rid of status message "gpg: encrypted with ....-bit RSA key ... ..."