# xz

### Create a *.xz arhive from a directory

```bash
$ tar -cf - my_directory/ | xz -9 -c - > my_archive.tar.xz 
```