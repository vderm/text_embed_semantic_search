---
author: Vasken Dermardiros
categories: note
date: September 12, 2022
tags:
- research
- reference
title: Metrics
---

# F1 Score
+ https://towardsdatascience.com/essential-things-you-need-to-know-about-f1-score-dbd973bf1a3#4c6c

It elegantly sums up the predictive performance of a model by combining two otherwise competing metrics — precision and recall.

The F1-score combines the precision and recall of a classifier into a single metric by taking their harmonic mean.

![F1-score](../attachments/2022-09-12-16-45-22.png)

![F$\beta$-score](../attachments/2022-09-12-16-46-03.png)

![Errors](../attachments/2022-09-12-16-47-03.png)

+ Precision: Of all positive predictions, how many are really positive?
+ Recall (or sensitivity): Of all real positive cases, how many are predicted positive?
  + Cancer case: worst if we don't diagnose people who have cancer (FN are bad) -> put more weight on recall

Precision measures the extent of error caused by False Positives (FPs) whereas recall measures the extent of error caused by False Negatives (FNs)

![Precision vs Recall](../attachments/2022-09-12-16-50-35.png)

If we want both FP and FN to be reduced, then we care about both precision and recall and want to maximize both.

![Means](../attachments/2022-09-12-16-58-43.png)

Harmonic mean assures that very different values are penalized, like, a precision of 1 with recall 0 -> F1-score of 0; whereas an arithmetic mean would yield 0.5 which isn't the effect we want.