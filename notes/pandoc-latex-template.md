---
abstract: As our team is growing, we are finding it more and more difficult to communicate
  and coordinate the various needs of the team. I've decided to break.
author:
- Vasken Dermardiros
- Matt Daemon
bibliography: articles/library.bib
categories: note
date: \today
figPre:
- Fig.
- Figs.
fontfamily: lmodern
geometry: margin=1in
keywords:
- Markdown
- Example
numbersections: true
secPrefix:
- Section
- Sections
tags:
- template
title: The Document Title
titlepage: true
titlepage-rule-color: da3737
titlepage-rule-height: 2
titlepage-text-color: da3737
urlcolor: pink
---

<!-- titlepage-color: "D8DE2C" -->
<!-- titlepage-rule-color: "322cde" -->
<!-- toc-own-page: true -->
<!-- toc: true -->
<!-- mainfont: Font-Regular.otf //works? -->

<!--
If wanting to use other fonts, use XeLaTeX engine:
`--pdf-engine=xelatex`
monofont: FiraCode-Regular.ttf
-->



# Pandoc Latex Template

Folling this template: https://github.com/Wandmalfarbe/pandoc-latex-template

Custom Template Variables: https://github.com/Wandmalfarbe/pandoc-latex-template#custom-template-variables

Something said by [@ASHRAE_AddendumANSIASHRAE_2003] and his friend [@Azam_OccupancyEstimationUsing_2019]

My own shit @Dermardiros_SimplifiedBuildingControls_2019

``` python
import numpy as np

pew = np.random.rand(10)
y += pew * 10
print(f"This isn't != bad")
```

`pandoc pandoc-latex-template.md -o example.pdf --from markdown --template eisvogel --listings`

make a command: `md2pdf {input_file.md}`

that runs: `pandoc {input_file}.md -o {input_file}.pdf --from markdown --template eisvogel --listings`

<!-- drop extension -->
``` bash
name=$(echo "$1" | cut -f 1 -d '.')
echo "Base name is $name"
```

# Introduction
 Lorem ipsum dolor sit amett, ametti consectetur adipiscing elit. Mauris ut sem elit. Donec consectetur vehicula ligula, sit amet semper diam sollicitudin sed. Nulla non elementum magna. Donec interdum sem ac velit blandit rutrum. Donec sit amet lobortis turpis. Cras volutpat egestas diam, in finibus felis tincidunt ac. Quisque id eros orci. Pellentesque ullamcorper eu odio id tempor. Suspendisse ac aliquam sem. Pellentesque fermentum venenatis ipsum in mattis. Fusce erat velit, ultrices quis nisi nec, aliquet eleifend erat. Integer porta semper massa, nec faucibus purus.

Integer eu tempus velit, in mollis nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet ultrices ex. Pellentesque sed mauris dignissim, tristique urna eu, sollicitudin mi. Proin mattis tortor nec lorem ullamcorper, eu vehicula purus rutrum. Phasellus tincidunt nibh vitae nisl sollicitudin condimentum. Maecenas consectetur risus vitae risus varius, sed rhoncus libero vehicula. Aliquam tortor dui, elementum a convallis vel, sollicitudin sed nunc. Aliquam tincidunt ultricies lorem vel luctus. Cras malesuada sit amet nisl sit amet ornare. Pellentesque molestie elit vitae ornare pretium. Praesent justo leo, ultrices pharetra lobortis eget, consequat a ligula. Nulla dapibus tortor et lectus feugiat, sit amet laoreet nibh tempor.

## Section Pew
Nulla ut lorem condimentum, imperdiet est eu, cursus eros. Pellentesque id justo et mauris sagittis iaculis. Etiam ac sem at metus commodo dapibus non eu ipsum. Donec vel ante mauris. Proin in ornare risus. Cras vulputate et lorem id iaculis. Nullam lacinia quam non nulla accumsan euismod. Donec odio tortor, vestibulum id urna posuere, aliquet convallis velit.

Donec elementum magna eget semper ultrices. Sed feugiat, elit vel facilisis dictum, erat mi porttitor lectus, non consectetur erat sem sed dui. Mauris pharetra mi eu convallis fermentum. Sed facilisis leo eget lacus placerat tempus. Cras porta tristique tristique. Duis vel diam at erat molestie vehicula. Nunc turpis nunc, gravida vitae ante non, laoreet luctus lectus. Mauris lacinia metus tincidunt dui ullamcorper, eu iaculis velit facilisis. Etiam ultrices ipsum a tincidunt ultrices. Nullam convallis eget massa sit amet aliquam.

### Section Pew
Aliquam facilisis blandit porttitor. Nunc dui massa, sodales ac elementum nec, consequat sit amet turpis. Duis dapibus nec justo et placerat. Aliquam et sapien viverra, elementum lacus sed, ultrices mi. Maecenas at erat nisl. Duis feugiat malesuada facilisis. Nullam nec est in leo mollis porttitor.


# Section 3
 Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ut sem elit. Donec consectetur vehicula ligula, sit amet semper diam sollicitudin sed. Nulla non elementum magna. Donec interdum sem ac velit blandit rutrum. Donec sit amet lobortis turpis. Cras volutpat egestas diam, in finibus felis tincidunt ac. Quisque id eros orci. Pellentesque ullamcorper eu odio id tempor. Suspendisse ac aliquam sem. Pellentesque fermentum venenatis ipsum in mattis. Fusce erat velit, ultrices quis nisi nec, aliquet eleifend erat. Integer porta semper massa, nec faucibus purus.

Integer eu tempus velit, in mollis nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Quisque sit amet ultrices ex. Pellentesque sed mauris dignissim, tristique urna eu, sollicitudin mi. Proin mattis tortor nec lorem ullamcorper, eu vehicula purus rutrum. Phasellus tincidunt nibh vitae nisl sollicitudin condimentum. Maecenas consectetur risus vitae risus varius, sed rhoncus libero vehicula. Aliquam tortor dui, elementum a convallis vel, sollicitudin sed nunc. Aliquam tincidunt ultricies lorem vel luctus. Cras malesuada sit amet nisl sit amet ornare. Pellentesque molestie elit vitae ornare pretium. Praesent justo leo, ultrices pharetra lobortis eget, consequat a ligula. Nulla dapibus tortor et lectus feugiat, sit amet laoreet nibh tempor.

Nulla ut lorem condimentum, imperdiet est eu, cursus eros. Pellentesque id justo et mauris sagittis iaculis. Etiam ac sem at metus commodo dapibus non eu ipsum. Donec vel ante mauris. Proin in ornare risus. Cras vulputate et lorem id iaculis. Nullam lacinia quam non nulla accumsan euismod. Donec odio tortor, vestibulum id urna posuere, aliquet convallis velit.

Donec elementum magna eget semper ultrices. Sed feugiat, elit vel facilisis dictum, erat mi porttitor lectus, non consectetur erat sem sed dui. Mauris pharetra mi eu convallis fermentum. Sed facilisis leo eget lacus placerat tempus. Cras porta tristique tristique. Duis vel diam at erat molestie vehicula. Nunc turpis nunc, gravida vitae ante non, laoreet luctus lectus. Mauris lacinia metus tincidunt dui ullamcorper, eu iaculis velit facilisis. Etiam ultrices ipsum a tincidunt ultrices. Nullam convallis eget massa sit amet aliquam.

Aliquam facilisis blandit porttitor. Nunc dui massa, sodales ac elementum nec, consequat sit amet turpis. Duis dapibus nec justo et placerat. Aliquam et sapien viverra, elementum lacus sed, ultrices mi. Maecenas at erat nisl. Duis feugiat malesuada facilisis. Nullam nec est in leo mollis porttitor.


# References
