---
author: Vasken Dermardiros
title: Foam How-To
categories: note
tags:
- reference
links:
- https://github.com/foambubble/foam-template/tree/master/docs
---

+ `ctrl + shift + p`: then Foam: Create New Note or New Note From Template
+ `alt + h`: open daily note
+ `alt + d`: create daily note
+ `alt + shift + f`: format document, will also format tables
+ `ctrl + alt + v`: paste image
+ Run Janitor to fix links
+ Copy paste onto a word should convert to a wiki link but it doesn't...
+ `![[]]` to embed a note in another note, use this for long projects?
+ Publish as a website: follow [this github](https://github.com/mathieudutour/gatsby-digital-garden) to publish like I had it with Hugo. Each link opening on the right.


add this to link markdown on save:
``` json
  "editor.codeActionsOnSave": {
    "source.fixAll.markdownlint": true
  },
```
