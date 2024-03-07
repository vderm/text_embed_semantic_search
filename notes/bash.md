---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Bash
---


# For-Loop
`for f in test{2..4}.txt ; do cp file.txt $f ; done`

This script: (1) tries to create a folder, does nothing if it exists, (2) copies
the contents of "measures_template" into "measures_XYZ".

``` bash
for f in 2 3 4 6 8
do
    mkdir -p measures_$f
    cp -a measures_template/. measures_$f/
done
```

# Chaining Bash Commands
#+AUTHOR: Luke Smith
https://www.youtube.com/watch?v=p0KKBmfiVl0

+ `cmd0 && cmd1`: run cmd0 then run cmd1 if cmd0 was successful
+ `cmd0 || cmd1`: run cmd0 then run cmd1 if cmd0 was NOT successful
+ `cmd0 ; cmd1`: run cmd0 then cmd1, wait for cmd0 to finish successful or not
+ `cmd0 & cmd1`: run cmd0 and cmd1 concurrently

#  Merging a bunch of files together using `paste`
https://stackoverflow.com/questions/43339859/merge-two-csv-files-in-bash

+ `paste -d, f1.csv f2.csv > out.csv`
+ `paste {file1,file2}.csv > out.csv`
* find a recent file modified and copy somewhere else
+ see: https://www.cyberciti.biz/faq/linux-unix-osxfind-files-by-date/
+ see: https://ostechnix.com/find-copy-certain-type-files-one-directory-another-linux/

`find /tmp/*.json -type f -newermt 2020-08-18 -exec cp {} $HOME \;`

Explanation: find in a certain location (here: /tmp/ and only considering json files) files that were modified at time (mt stand for modified/time) 2020-08-18, once you find these, copy them to $HOME

# Find words inside all python files within subdirectories
`find . -type f -name "*.py" | xargs grep -iRn "request"`