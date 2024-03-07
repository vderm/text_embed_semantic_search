---
author: Richard Feynman
categories: website
tags:
- lecture
- research
title: Principle Of Least Action
links:
- https://www.feynmanlectures.caltech.edu/II_19.html
---

Richard Feynman lecture

<https://www.feynmanlectures.caltech.edu/II_19.html>

![Path along a gravitational field](../attachments/f19-01b_mg.jpeg)

The path along a gravitational field is of least energy if potential energy and kinetic match -> path of motion emerges from this minimization of the path energy.

![Action equation](../attachments/2021-07-13-22-21-52.png)

For each different possible path you get a different number for this action. Our mathematical problem is to find out for what curve that number is the least.

Finding the path is part of [calculus of variations](https://en.wikipedia.org/wiki/Calculus_of_variations)

![Find the true path](../attachments/2021-07-13-22-25-05.png)

To find the true path, we need to find the path that has minimal action $S$. Like in minimization of variables where the minimum of $x$ is attain where near it is rather flat and further out $x$ tends to increase, the minimal path does the same but we're *wiggling* the path.

(There's a whole derivation for the minimal path in the lecture.)

> The method of solving all problems in the calculus of variations always uses the same general principle. You make the shift in the thing you want to vary (as we did by adding η); you look at the first-order terms; then you always arrange things in such a form that you get an integral of the form ‘some kind of stuff times the shift (η),’ but with no other derivatives (no dη/dt). It must be rearranged so it is always ‘something’ times η.

> Now comes something which always happens—the integrated part disappears. (In fact, if the integrated part does not disappear, you restate the principle, adding conditions to make sure it does!)

If the path between t1 and t2 is minimal, take any two close points on the path, a and b, and the path between them is also minimal. Otherwise, this path can be wiggled and would make the action smaller between t1 and t2.

> Now if we take a short enough section of path—between two points a and b very close together—how the potential varies from one place to another far away is not the important thing, because you are staying almost in the same place over the whole little piece of the path. The only thing that you have to discuss is the first-order change in the potential. The answer can only depend on the derivative of the potential and not on the potential everywhere. So the statement about the gross property of the whole path becomes a statement of what happens for a short section of the path—a differential statement. And this differential statement only involves the derivatives of the potential, that is, the force at a point. That’s the qualitative explanation of the relation between the gross law and the differential law.

Continues on on solving quantum problems of electrons in electromagnetic fields.
