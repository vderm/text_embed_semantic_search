---
author: Vasken Dermardiros
categories: note
date: February 2, 2023
tags:
- research
- template
- reference
title: Markdown Cheatsheet
links: https://raw.githubusercontent.com/gabrieldim/Markdown-Crash-Course/main/README.md
---

Following is all the types of formatting available. If you are using VSCode, install the following extensions: "Markdown All in One", "Markdown Math", "Spell Right". With those extensions, you can use `Ctrl+b` for bold, `Ctrl+i` for italics. You can copy a link onto a selected text. You can use `Ctrl+Shift+v` to open the preview mode.

You might start realizing that the Python docstrings we've been writting is actually markdown!

<!-- This is how you comment. -->

<!--  All the available headings. In LaTeX, these get converted to \section, \subsection, \subsubsection, \paragraph, and so on. -->
# Heading 1  '# '
## Heading 2 '## '
### Heading 3 '### '
#### Heading 4 '#### '
##### Heading 5 '##### '
###### Heading 6 '###### '

<!-- Italics -->
*This text is italic*
_This text is italic_

<!-- Strong -->
**This text is bold**
__This text is bold__

<!-- Strikethrough -->
~~This text~~ is strikethrough

<!-- Horizontal Role -->
---
___

<!-- Escape char -->
\ before the actual rule.

<!-- Blackquote -->
> This is a quote

<!-- Links -->
[Gabriel Dimitrievski - GitHub](https://github.com/gabrieldim)

<!-- Links cover text-->
[Gabriel Dimitrievski - GitHub](https://github.com/gabrieldim "Follow me :)")

<!-- Unordered List -->
* Text 1
* Text 2
* Text 3
    * Nested text 1
    * Nested text 2
        * Nested text 1
        * Nested text 2

<!-- Unordered List, alternatives using `+` and `-` -->
+ Text 1
+ Text 2
+ Text 3
  - Nested text 1
  - Nested text 2

<!-- Ordered List -->
1. Text 1
2. Text 2
    1. Nested text 1
5. Text 3 // it gives the appropriate order

<!-- InLine Code Block -->
`<p>This is paragraph</p>`

<!-- Images -->
![Markdown Logo](https://markdown-here.com/img/icon256.png "Markdown Logo")

<!-- Code Blocks -->
``` java
//in the previous line we are saying the language that we are using.
BufferedReader br = new BufferedReader(New InputStreamReader(System.in));

String s = br.readLine();
```

``` javascript
function add(num1, num2){
    return num1 + num2;
}
```

``` python
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(100)
y = np.sin(x)

plt.plot(x,y)
plt.show()
```

<!-- Tables -->

| Name   | Email           |
| -----  | --------------- |
| Test   | Test@gmail.com  |
| Test2  | Test2@gmail.com |

<!-- Tables are symbolic, you can define it like this and the second line handles the alignment via `:` -->
1st Header|2nd Header|3rd Header
---|:---:|---:
col 1 is|left-aligned|1
col 2 is|center-aligned|2
col 3 is|right-aligned|3

<!-- Task Lists -->
* [x] Task 1
* [x] Task 2
* [ ] Task 3
* [ ]

<!-- LaTeX Snippet, encapsulated by $ is inline (don't leave any spaces next to the delimiters) -->
The function $y = ax + b$ is linear, where $a$ and $b$ are learned parameters.

<!-- LaTeX Snippet, encapsulated by $$ creates an equation -->
The following equation
$$
    y = \frac{x+10}{3}
$$
is a fraction. And to get something more complex, no problem, check out this matrix:
$$
\begin{matrix}
    1 & 2 & 3 \\
    4 & 5 & 6 \\
    7 & 8 & 9
\end{matrix}
$$

<!-- References -->
I get 10 times more traffic from [Google][1] than from
[Yahoo][2] or [MSN][3].

[1]: http://google.com/        "Google"
[2]: http://search.yahoo.com/  "Yahoo Search"
[3]: http://search.msn.com/    "MSN Search"

<!-- Quoted text block -->
    When you need to include a larger snippet.
