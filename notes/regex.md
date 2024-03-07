---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Regex
---

# Regex (Regular Expression)

https://regexr.com/: regex checker and learning

`grep <pattern> file`

+ Use `''` or `""` to protect expression from shell interpretation
+ `.` :: matches any single character
+ `\.` :: literal period
+ `.*` :: matches any character zero or more times
+ `.+` :: matches any character 1 or more times
+ `^` :: matches beginning of the line
+ `$` :: matches end of the line
+ `[a-z]` :: match character a through z
+ `[a-zA-Z0-9]` :: matches any alphanumeric character in ASCII
+ `[^0-9]` :: don't match numbers

Use `^2\.4\.150.1$` to match `2.4.150.1` since search is fuzzy and will capture
substrings too

https://www.youtube.com/watch?v=vcRPNhLbhoc

`grep 'Watson' sherlock.txt`
search for the word "Watson" in sherlock.txt

`grep '[Ss]ome' sherlock.txt`
search for some or Some

`grep '\<wind' sherlock.txt`
match if wind is at the beginning of a word

`grep '\<wind\>' sherlock.txt`
match if wind is at the beginning and end of a word

`grep '^The' sherlock.txt`
match The at the beginning of a line

`grep '[ [:digit:] ]{4\}' sherlock`
match 4 digits
(delete the spaces between square brackets)
`:alpha:` for letters
`\{16,17\}`: 16 or 17 letters long
`:alnum:` for alphanumeric
`:lower:` `:upper:`
`:punct:`
`[ [:digit:] [:alpha:] ]` digit followed by a letter

`grep 'fl..d' sherlock.txt`
match fl(blank)(blank)d

`grep 'die\?d' sherlock.txt`
`\?` means the letter 'e' is optional

`grep 'June\|July' sherlock.txt`
match June or July

# Cheatsheet
![Regex cheastsheet](../attachments/regex_cheat_sheet.png)