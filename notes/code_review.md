---
author: Vasken Dermardiros
categories: note
tags:
- programming
title: Code Review
---


Make sure to be kind and that code explains itself!

How to make good code reviews better:
https://stackoverflow.blog/2019/09/30/how-to-make-good-code-reviews-better/

How to do a code review (eng-practices @ Google):
https://google.github.io/eng-practices/review/reviewer/

*Good code reviews* are the bar that all of us should strive for. They cover common and easy to follow best practices that any team can get started with, while ensuring high-quality and helpful reviews for the long term.

*Better code reviews* are where engineers keep improving how they do code reviews. These code reviews look at the code change in the context of the codebase, of who is requesting it and in what situation. These reviews adjust their approach based on the context and situation. The goal not only being a high-quality review, but also to help the developers and teams requesting the review to be more productive.

Code reviews offer a way to communicate a problem/issue and should be done in a positive attitude. If there are too many back and fourths, it might be worthwhile to communicate in person.

For /nitpicks/, prefix the word /nit/ in front to make it obvious that it's not very important. Too many nitpicks though are a sign of lack of standards. Perhaps some of these can even be automated.

Code review should be at the same level for all. Just have to make the experience less hostile and more empathetic.

How to write code review comments
https://google.github.io/eng-practices/review/reviewer/comments.html

+ Be kind.
+ Explain your reasoning.
+ Balance giving explicit directions with just pointing out problems and letting the developer decide.
+ Encourage developers to simplify code or add code comments instead of just explaining the complexity to you.

# BrainBox AI Standard
#+AUTHOR: Elnaz Taqizadeh
https://git.brainboxai.net/Elnaz/Documents

Quality Assurance
+ Coding Style Guide
+ Git Tutorial
+ Pull Request Template
+ Code Review
+ How to report a bug?
+ Documentation Guideline
+ System Design Document

+ Design
  - Do the interactions of various pieces of code in the make sense?
  - Does it integrate well with the rest of the system?
  - Is now a good time to add this functionality?
+ Functionality
  - Does this code do what the developer intended?
+ Complexity
  - Are individual lines too complex? Are functions too complex? Are classes too complex?
  - Too complex? “Can’t be understood quickly by code readers.”
  - “Developers are likely to introduce bugs when they try to call or modify this code.”
+ Tests
  - Is the code testable? The code should be structured so that it doesn’t add too many or hide dependencies, is unable to initialize objects, test frameworks can use methods etc.
  - Do tests exist, and are they comprehensive?
  - Do unit tests actually test that the code is performing the intended functionality?
+ Style
  - Does it conform to BrainBox AI Coding Style Guideline?(available on the Gitea, Documents repo)
+ Documentation
  - Do comments exist and describe the intent of the code?
  - Are most of the functions commented?
  - Is any unusual behavior or edge-case handling described?
  - Is the use and function of third-party libraries documented?
  - Is there any incomplete code? If so, should it be removed or flagged with a suitable marker like ‘TODO’?
+ Non Functional requirements
  - Extensibility – Is it easy to add enhancements with minimal changes to the existing code?
  - Security – Is it following the security standards of the BrainBox AI?Authentication, authorization, input data validation, encrypting the sensitive data
  - Performance - Are there any apparent optimizations that will improve performance? Can any of the code be replaced with a library of built-in functions? Can any logging or debugging code be removed?
  - Scalability – Does it support a significant load of data?