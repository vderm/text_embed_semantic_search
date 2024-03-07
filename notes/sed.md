---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Sed
---

# Stream Editor (sed)

`sed 's/Nick/John/g' report.txt`
Replace every occurrence of Nick with John in report.txt

`sed 's/Nick|nick/John/g' report.txt`
Replace every occurrence of Nick or nick with John.

`sed 's/^/ /' file.txt > file_new.txt`
Add 8 spaces to the left of a text for pretty printing.

`sed -n '/Of course/,/attention you \ pay/p' myfile`
Display only one paragraph, starting with "Of course" and ending in "attention you pay"

`sed -n 12,18p file.txt`
Show only lines 12-18 of file.txt

`sed 12,18d file.txt`
Show all of file.txt except for lines from 12 to 18

`sed G file.txt`
Double-space file.txt

`sed -f script.sed file.txt`
Write all commands in script.sed and execute them

`sed '5!s/ham/cheese/' file.txt`
Replace ham with cheese in file.txt except in the 5th line

`sed '$d' file.txt`
Delete the last line

`sed '/[0-9]\{3\}/p' file.txt`
Print only lines with three consecutive digits

`sed '/boom/!s/aaa/bb/' file.txt`
Unless boom is found replace aaa with bb

`sed '17,/disk/d' file.txt`
Delete all lines from line 17 to 'disk'

`echo ONE TWO | sed "s/one/unos/I"`
Replaces one with unos in a case-insensitive manner, so it will print "unos TWO"

`sed 'G;G' file.txt`
Triple-space a file

`sed 's/.$//' file.txt`
A way to replace dos2unix :)

`sed 's/^[ ^t]*//' file.txt`
Delete all spaces in front of every line of file.txt

`sed 's/[ ^t]*$//' file.txt`
Delete all spaces at the end of every line of file.txt

`sed 's/^[ ^t]*//;s/[ ^]*$//' file.txt`
Delete all spaces in front and at the end of every line of file.txt

`sed 's/foo/bar/' file.txt`
Replace foo with bar only for the first instance in a line.

`sed 's/foo/bar/4' file.txt`
Replace foo with bar only for the 4th instance in a line.

`sed 's/foo/bar/g' file.txt`
Replace foo with bar for all instances in a line.

`sed '/baz/s/foo/bar/g' file.txt`
Only if line contains baz, substitute foo with bar

`sed '/./,/^$/!d' file.txt`
Delete all consecutive blank lines except for EOF

`sed '/^$/N;/\n$/D' file.txt`
Delete all consecutive blank lines, but allows only top blank line

`sed '/./,$!d' file.txt`
Delete all leading blank lines

`sed -e :a -e '/^\n*$/{$d;N;};/\n$/ba' \ file.txt`
Delete all trailing blank lines

`sed -e :a -e '/\\$/N; s/\\\n//; ta' \ file.txt`
If a file ends in a backslash, join it with the next (useful for shell scripts)

`sed '/regex/,+5/expr/'`
Match regex plus the next 5 lines

`sed '1~3d' file.txt`
Delete every third line, starting with the first

`sed -n '2~5p' file.txt`
Print every 5th line starting with the second

`sed 's/[Nn]ick/John/g' report.txt`
Another way to write some example above. Can you guess which one?

`sed -n '/RE/{p;q;}' file.txt`
Print only the first match of RE (regular expression)

`sed '0,/RE/{//d;}' file.txt`
Delete only the first match

`sed '0,/RE/s//to_that/' file.txt`
Change only the first match

`sed 's/^[^,]*,/9999,/' file.csv`
Change first field to 9999 in a CSV file

```
s/^ *\(.*[^ ]\) *$/|\1|/;
s/" *, */"|/g;
: loop
s/| *\([^",|][^,|]*\) *, */|\1|/g;
s/| *, */|\1|/g;
t loop
s/ *|/|/g;
s/| */|/g;
s/^|\(.*\)|$/\1/;
```
sed script to convert CSV file to bar-separated (works only on some types of CSV, with embedded "s and commas)

`sed ':a;s/\(^\|[^0-9.]\)\([0-9]\+\)\\ ([0-9]\{3\}\)/\1\2,\3/g;ta' file.txt`
Change numbers from file.txt from 1234.56 form to 1.234.56

`sed -r "s/\<(reg|exp)[a-z]+/\U&/g"`
Convert any word starting with reg or exp to uppercase

`sed '1,20 s/Johnson/White/g' file.txt`
Do replacement of Johnson with White only on lines between 1 and 20

`sed '1,20 !s/Johnson/White/g' file.txt`
The above reversed (match all except lines 1-20)

`sed '/from/,/until/ { s/\<red\>/magenta/g; \ s/\<blue\>/cyan/g; }' file.txt`
Replace only between "from" and "until"

`sed '/ENDNOTES:/,$ { s/Schaff/Herzog/g; \ s/Kraft/Ebbing/g; }' file.txt`
Replace only from the word "ENDNOTES:" until EOF

`sed '/./{H;$!d;};x;/regex/!d' file.txt`
Print paragraphs only if they contain regex

`sed -e '/./{H;$!d;}' -e 'x;/RE1/!d;\ /RE2/!d;/RE3/!d' file.txt`
Print paragraphs only if they contain RE1, RE2 and RE3

`sed ':a; /\\$/N; s/\\\n//; ta' file.txt`
Join two lines in the file