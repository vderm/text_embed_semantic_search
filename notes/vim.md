---
author: Vasken Dermardiros
categories: note
tags:
- programming
- reference
title: Vim
---

# Vim Main Shortcuts
h: left
j: down
k: up
l: right

H: jump to top of the screen
M: middle
L: bottom

0: goto beginning of line
$: goto end of line
w: forward word
b: backward word

ctrl+f: forward page
ctrl+b: backward page
ctrl+d: half page down
ctrl+u: half page up

gg: goto first line
G: goto last line
`#G`: goto line "#"

:w: write file
:q: quit file
:q!: quit file, ignore changes
:wq: write then quit file

i: insert at cursor
a: insert after cursor (append)
I: insert at beginning of line
A: insert at end of line

o: insert line after line
O: insert line at line (push down)

x: delete
X: backspace
`#x`: number of deletes
dw: delete word

.: redo last command

d0: from cursor, delete all previous text
d$: from cursor, delete all following text

ctrl+z: go back to terminal
fg: from terminal, go back to vim

v: in Normal mode, select characters
V: in Normal mode, select lines
d: cut
y: copy
p: paste after cursor
P: paste before cursor
ddkP: delete current line and place in register; k moves up, P pastes above line

ci): clear inside ) type of parenthesis
ca): clear inside ) and ()s

:sp : split window horizontally
:sp10 : split window horizontally, 10 lines
:vsp : split window vertically

:e filename : edit filename
:split filename :split window and load another
:vsplit filename :vertical split
:sview filename: same as split, but read only
:hide close current window
:only keep only this window open
ctrl-w ctrl-w : move cursor to another window
:ls show current buffers
:b 2 open buffer #2 in this window
:bd n : buffer delete (current) or buffer `#n`

:tabs : list all tabs
gt | :tabn : goto next tab
gT | :tabp : goto previous tab

\ww :start vimwiki

/... : search text for "..."
n: goto next result
N: goto previous result
:noh :clear results

qk : record macro in register "k"; q again to stop recording
@k : execute recorded macro "k"
@@ : repeat last one
5@@: repeat 5 times
"kp: print macro "k"

:g/pattern/command
:v... : match all lines except
:g... : match all lines
:v/^\w/d : match lines that start (^) with a word (\w) and delete it (d)
:v/^\w\|<img/d : match lines that start with a word and contains "<img" and delete
:%s/foo/bar/g : find each occurance of "food" and replace by "bar"
:s/foo/bar/g : ditto except for current line only

zm: fold code, from deepest level
zr: unfold code, from shallowest level
zM: fold all code
zR: unfold all code
za: toggle open/close at indent
zo: open up when in block of code
zc: close up when in block of code

%: skip to closing parenthesis or code block

gq: reflow line.

C-w = : makes windows equal sized
C-w +/- : makes bottom larger/smaller
C-w _ : take full vertical
C-w | : take full horizontal
C-w r : rotate

# Delete all lines containing a pattern
For example, to delete all lines containing "profile" (remove the /d to show the
lines that the command will delete):

`:g/profile/d`

More complex patterns can be used, such as deleting all lines that are empty or
that contain only whitespace:

`:g/^\s*$/d`

To delete all lines that do not contain a pattern, use g!, like this command to
delete all lines that are not comment lines in a Vim script:

`:g!/^\s*"/d`

Note that g! is equivalent to v, so you could also do the above with:

`:v/^\s*"/d`

The next example shows use of `\|` ("or") to delete all lines except those that contain "error" or "warn" or "fail" (:help pattern):

`:v/error\|warn\|fail/d`

# vimdiff
`vimdiff file1 file2`

`]c`               - advance to the next block with differences
`[c`               - reverse search for the previous block with differences
`do` (diff obtain) - bring changes from the other file to the current file
`dp` (diff put)    - send changes from the current file to the other file
`zo`               - unfold/unhide text
`zc`               - refold/rehide text
`zr`               - unfold both files completely
`zm`               - fold both files completely