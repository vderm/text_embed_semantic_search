---
author: Stoyan Nikolov
categories: website
tags:
- programming
- improve
title: OOP Is Dead, Long Live Data Oriented Design
links:
- https://www.youtube.com/watch?v=yy8jQgmhbAU
---


Title: CppCon 2018: Stoyan Nikolov “OOP Is Dead, Long Live Data-oriented Design”
Watch video: https://www.youtube.com/watch?v=yy8jQgmhbAU

OOP hides stuff in classes and forces interactions that don't need to happen.
It's an unhappy marriage!

Go with a data-oriented approach instead.

Data feeds into functions and out goes other functions. (Really looks like
functional programming.)

Study chromium: it's an amazing piece of software, **a lot to learn!**

(He goes through the animation stack in chromium, holy shit, a class
inherits another 6 classes, updates shit here and there, makes virtual
references / abstract classes and smart pointers, etc etc etc!!!)

![Animation Controller](../attachments/2021-07-04-18-22-00.png)

![Go flat!](../attachments/2021-07-04-18-22-32.png)

![Key points](../attachments/2021-07-04-18-33-06.png)

Table-based output -> input to next thing down the pipeline -> data flows

![Testability analysis](../attachments/2021-07-04-18-36-00.png)

OOP: too many edge cases to cover and needs to mock certain interactions.
DoD: know what outputs will occur -> straight line, no links between classes

![Modifiability analysis](../attachments/2021-07-04-18-37-06.png)

OOP: Changes are unlikely to happen -> huge refactors

Downsides of DoD: easy to explain, hard to master; need some domain knowledge to help.

OOP and DoD are both tools at the end.