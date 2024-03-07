---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Parallel
links:
- https://opensource.com/article/18/5/gnu-parallel
- https://www.youtube.com/watch?v=OpaiGYxkSuQ&list=PL284C9FF2488BC6D1
---

Easy to write a script that runs one command and then use parallel to run it in parallel.

Given the example `find . -name "*jpeg" | parallel -I% --max-args 1 convert % %.png`

+ `find . -name "*jpeg"` finds all files in the current directory that end in `jpeg`.
+ `parallel` invokes GNU Parallel.
+ `-I%` creates a placeholder, called `%`, to stand in for whatever `find` hands over to Parallel. You use this because otherwise you'd have to manually write a new command for each result of `find`, and that's exactly what you're trying to avoid.
+ `--max-args 1` limits the rate at which Parallel requests a new object from the queue. Since the command Parallel is running requires only one file, you limit the rate to 1. Were you doing a more complex command that required two files (such as `cat 001.txt 002.txt > new.txt`), you would limit the rate to 2.
+ `convert % %.png` is the command you want to run in Parallel.

Each line returned by `find` is treated as 1 argument. To pass more arguments, set the `max-args` to something higher.

`ls -1 | parallel echo`

`ls -1 | parallel --max-args=2 ffmpeg -i {1} -i {2} -vcodec copy -acodec copy {1}.mkv`


To run a list of things, you can create a file and put functions

``` bash
cat jobs2run
bzip2 oldstuff.tar
oggenc music.flac
opusenc ambiance.wav
convert bigfile.tiff small.jpeg
ffmepg -i foo.avi -v:b 12000k foo.mp4
xsltproc --output build/tmp.fo style/dm.xsl src/tmp.xml
bzip2 archive.tar
```

Then hand it to parallel: `parallel --jobs 6 > jobs2run`.

**It can also send jobs across multiple computers!**