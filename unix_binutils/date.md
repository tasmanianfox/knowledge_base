# date

## Local date

Display a current date:

```bash
date
# Wed Jul 29 21:07:10 EEST 2020
```

The output format is dependent on system locale:

```bash
LC_ALL=et_EE.utf-8 date # Passed the Estonian locale using environment variable
# K 29 juuli 2020 21:11:07 EEST
```

## UTC date

```bash
date --utc
# Wed 29 Jul 2020 06:23:47 PM UTC
```

## Date formats

_yyyy-mm-dd:_

```bash
date +%F
# 2020-07-29

date --rfc-3339=date
# 2020-07-29
```

_mm/dd/yy:_

```bash
date +%D
# 07/29/20
```

_yyyy-mm-dd h:m(inutes):s

```bash
date +"%Y-%m-%d %H:%M:%S"
# 2020-07-29 21:18:30
```

__More format options__ - see https://man7.org/linux/man-pages/man1/date.1.html