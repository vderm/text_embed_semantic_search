---
author:
- Vasken Dermardiros
- Matt Daemon
bibliography: articles/library.bib
categories: note
date: \today
geometry: margin=1in
numbersections: true
tags:
- template
title: Test Output Pandoc LaTeX
titlepage: true
titlepage-rule-color: da3737
titlepage-text-color: da3737
urlcolor: pink
---

<!-- csl: ieee.csl -->
<!-- figPrefix:
  - "Fig."
  - "Figs."
secPrefix:
  - "Section"
  - "Sections" -->

# Pandoc Latex Template

Something said by [@ASHRAE_AddendumANSIASHRAE_2003] and his friend [@Azam_OccupancyEstimationUsing_2019, ch. 5]

<!-- Taking notes would maybe look like this: [[@ASHRAE_AddendumANSIASHRAE_2003]] -->

My own shit @Dermardiros_SimplifiedBuildingControls_2019 and someone elses @Hu_DatadrivenFeedforwardDecision_2015.

I sometimes go on tangents[^1].

``` python
import numpy as np

pew = np.random.rand(10)
y += pew * 10
print(f"This isn't != bad")
```

Start reading from Chapter \ref{sec:intro} also see \ref{introduction}. Also see Equation \ref{eq:slope}

# Introduction
\label{sec:intro}

 Lorem ipsum dolor sit amett, ametti consectetur adipiscing elit. Mauris ut sem elit. Donec consectetur vehicula ligula, sit amet semper diam sollicitudin sed. Nulla non elementum magna. Donec interdum sem ac velit blandit rutrum. Donec sit amet lobortis turpis. Cras volutpat egestas diam, in finibus felis tincidunt ac. Quisque id eros orci. Pellentesque ullamcorper eu odio id tempor. Suspendisse ac aliquam sem. Pellentesque fermentum venenatis ipsum in mattis. Fusce erat velit, ultrices quis nisi nec, aliquet eleifend erat. Integer porta semper massa, nec faucibus purus. Table \ref{tab:table} and Figure \ref{fig:gradient}

Table: Awesome Statistics \label{tab:table}

| Date       | Version | Changes                          |
| ---------- | ------- | -------------------------------- |
| 18/06/2021 | 1       | First finalized version          |
| 18/06/2021 | 2       | Reference to release note added  |
| 21/06/2021 | 3       | Fahimeh in AI-Dev                |
| 01/07/2021 | 4       | Note about Release branch, typos |

At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr.

## Image with Caption

![Nam liber.]() \label{fig:gradient}


$$ y = a*x + b $$

\label{eq:slope}



\begin{equation}\label{eq:neighbor-propability}
    p_{ij}(t) = \frac{\ell_j(t) - \ell_i(t)}{\sum_{k \in N_i(t)}^{} \ell_k(t) - \ell_i(t)}
\end{equation}


Integer eu tempus velit, in mollis nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet ultrices ex. Pellentesque sed mauris dignissim, tristique urna eu, sollicitudin mi. Proin mattis tortor nec lorem ullamcorper, eu vehicula purus rutrum. Phasellus tincidunt nibh vitae nisl sollicitudin condimentum. Maecenas consectetur risus vitae risus varius, sed rhoncus libero vehicula. Aliquam tortor dui, elementum a convallis vel, sollicitudin sed nunc. Aliquam tincidunt ultricies lorem vel luctus. Cras malesuada sit amet nisl sit amet ornare. Pellentesque molestie elit vitae ornare pretium. Praesent justo leo, ultrices pharetra lobortis eget, consequat a ligula. Nulla dapibus tortor et lectus feugiat, sit amet laoreet nibh tempor.

## Section Pew
Nulla ut lorem condimentum, imperdiet est eu, cursus eros. Pellentesque id justo et mauris sagittis iaculis. Etiam ac sem at metus commodo dapibus non eu ipsum. Donec vel ante mauris. Proin in ornare risus. Cras vulputate et lorem id iaculis. Nullam lacinia quam non nulla accumsan euismod. Donec odio tortor, vestibulum id urna posuere, aliquet convallis velit.

Donec elementum magna eget semper ultrices. Sed feugiat, elit vel facilisis dictum, erat mi porttitor lectus, non consectetur erat sem sed dui. Mauris pharetra mi eu convallis fermentum. Sed facilisis leo eget lacus placerat tempus. Cras porta tristique tristique. Duis vel diam at erat molestie vehicula. Nunc turpis nunc, gravida vitae ante non, laoreet luctus lectus. Mauris lacinia metus tincidunt dui ullamcorper, eu iaculis velit facilisis. Etiam ultrices ipsum a tincidunt ultrices. Nullam convallis eget massa sit amet aliquam.

# References

[^1]: Like basically all the time.