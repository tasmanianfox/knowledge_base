# Git: a cheatsheet

## Configuration

### Set user's email and name

```bash
git config user.name "John Doe"
git config user.email "john.doe@example.com"
```

These command apply changes only for current git repository. To assign default credentials, use the `--global` flag:

```bash
git config --global user.name "John Doe"
git config --global user.email "john.doe@example.com"
```

### Ignore file permissions in Unix systems:

```bash
git config core.fileMode false
```

## Branches

### Set current branch

```bash
git checkout branch_name
```

### Create a branch and set it as current

```bash
git checkout -b new_branch_name
```

### Rename a current branch

```bash
git branch -m new_branch_name
```

### Delete a local branch (if it is merged)

```bash
git branch -d branch_name
```

### Delete a local branch (forcefully, NO prompt)

```bash
git branch -D branch_name
```

### Delete all branches except master

```bash
git branch | grep -v master | xargs git branch -D 
```

### Merge another branch into current branch

```bash
git merge another_branch_name
```

### Push to a remote branch with the same name forcefully

```bash
git push --force origin brach_name:branch_name
```

### Delete a remote branch

```bash
git push --force origin :branch_name
```

### Get a new remote branch

```bash
git fetch origin branch_name:branch_name
```

### Rollback Git history to specified state (=git commit hash) with NO rollback of files

```bash
git reset hash_here
```

An example for this repo:

```bash
git reset 614a89e0aa9921fdfbdcea684a34481f44ffa057
```

### Rollback Git history to specified state (=git commit hash) with NO rollback of files

```bash
git reset --hard hash_here
```

### Reset to the last commit, undo all non-committed changes

_If you need to delete all new files as well, you need to stage them for commit in the first. Otherwise new files will remain in the filesystem:_
```bash
git add .
```

Reset command:
```bash
git reset --hard HEAD
```

## Git commits

### The concept

```
A new file (not staged for commit)
  -> git add
File is staged for commit
  -> git commit
File is committed locally, but not synced with remote Git repo
  -> git push
File is committed locally and remotelly
```

### Stage all new files (which don't match .gitignore rules) for commit

```bash
git add .
```

### Stage a file for commit

```bash
git add some/file.example.txt
```

### Commit all files staged for commit

```bash
git commit -m "Commit message here"
```

### Push local commits to remote Git

If current branch is pushed for the frist time:

```bash
git push --set-upstream origin branch_name
```

Otherwise:

```bash
git push
```

### Pull changes from remote server to current branch

If changes are pulled for the first time, assign a remote branch to pull from:

```bash
git branch --set-upstream-to=origin/branch_name branch_name
```

The pull command itself:

```bash
git pull
```

### Ignore changes in file:

_This will NOT work for new files_

```bash
git update-index --assume-unchanged path/to/file.txt
```

To undo:

```
git update-index --no-assume-unchanged path/to/file.txt
```

## Viewing files

### Show file contents at particular revision (=by git commit hash)

```bash
git show git_commit_hash:filename
```

An example for this repo:

```bash
git show 6d716315378cc7dcb74fcb1429122c7cbe3863f6:README.md
```

### Display who and when changed each line in file:

```bash
git blame filename.txt
```

## Working with changes between commits

### View changes between two commits

```bash
git diff hash1 hash2
```

An example for this repo:

```bash
git diff 6d716315378cc7dcb74fcb1429122c7cbe3863f6 05ccf2c0e15d85f4fbd496e5786932cfa13c8b96
```