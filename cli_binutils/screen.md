# GNU Screen

### Start a new terminal session

```bash
screen -S session_name
```

### Detach from current session

`<CTRL>` + `A`, then `<CTRL>` + `D`

### List running sessions

```bash
screen -list
```

### Attach to running session

```bash
screen -rS session_name
```