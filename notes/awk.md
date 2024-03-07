---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: awk
---

Text parsing

By default, breaks into columns based on any type of whitespace

`awk -flag '{<command>}' files`

`awk '/path/ && $2 > 15000 {print $1, $2/1024"K"}'`

`awk -f awkfile.awk file`

```
func round(n) {
    n = n + 0.5
    n = int(n)
    return(n)
}

/^w/ %% $2>25000 {print, $1, round($2/1024)"K"}
```

`zcat file.log.gz | awk -F\\t '{print $3}' | sort | uniq -c | sort -rn`
tab delimited file