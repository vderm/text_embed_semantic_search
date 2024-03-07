---
author:
- Vasken Dermardiros
categories: note
date: 2020-08-20 00:00:00-04:00
draft: false
lastmod: 2021-01-03 22:49:03-05:00
slug: deep_fake
tags:
- research
- reading-week
- GAN
- visualization
title: Deep Fake
---

## <span class="section-num">1</span> A Deep Fake {#a-deep-fake}

### <span class="section-num">1.1</span> What is a \`deep fake\`? {#what-is-a-deep-fake}

{{< figure src="<https://en.wikipedia.org/wiki/File:Deepfake%5Fexample.gif>]]

Take one person's face and put it on another's, fine-tune to match the lip
movement, synthesize the voices, and voila!

### <span class="section-num">1.2</span> Obama {#obama}

<https://www.youtube.com/watch?v=C8FO0P2a3dA>

### <span class="section-num">1.3</span> Super cool! {#super-cool}

{{< figure src="~/Downloads/conair-618x360.jpg]]

Time to replace every character in every movie by Nicolas Cage!

### <span class="section-num">1.4</span> Not so fast! {#not-so-fast}

It'll take a few days to process a small scene and then some hours to manually
fix it to make it more realistic in After Effects.

Still though, 99% of people don't know what Deep Fakes are.

It's in the domain of **style transfer**.

## <span class="section-num">2</span> Style Transfer {#style-transfer}

### <span class="section-num">2.1</span> GAN {#gan}

At the center of it all lies a GAN.

In a nutshell, a GAN consists of:

The Generator
: has to generate an image, sequence, etc that seems realistic
    to try to _fool_ the discriminator.

The Discriminator
: has to judge whether the image, sequence, etc it's
    looking is real and from the dataset or whether it's generated/fake.

(Optional) The Critic
: soft discriminator, says how fake the image is
    instead of a discrete real/fake.

### <span class="section-num">2.2</span> Problem with GANs: Manifold Collapse {#problem-with-gans-manifold-collapse}

If the Discriminator likes zebras, the Generator can end up always giving it the
exact same image of a zebra. No novelty.

### <span class="section-num">2.3</span> CycleGAN {#cyclegan}

- Link: <https://arxiv.org/pdf/1703.10593.pdf>

<sup id="7c1ad6f6a99d34484f8052f357917740"><a href="#Zhu_UnpairedImagetoImageTranslation_2018" title="">Zhu_UnpairedImagetoImageTranslation_2018</a></sup>
Zhu, J., Park, T., Isola, P., & Efros, A. A., Unpaired Image-to-Image
Translation using Cycle-Consistent Adversarial Networks, arXiv:1703.10593 [cs],
(),  (2018).

Novelty in this paper is to covert to a new domain then be able to convert it
back.

Relies on a cascade of Generators:

- 1<sup>st</sup> Generator transforms the zebra to a horse
- 2<sup>nd</sup> Generator transforms it back

### <span class="section-num">2.4</span> Zebras and Horsies {#zebras-and-horsies}

![[2020-08-20_16-00-15_screenshot.png]]

### <span class="section-num">2.5</span> Cost Function {#cost-function}

![[2020-08-20_16-00-42_screenshot.png]]

### <span class="section-num">2.6</span> RecycleGAN {#recyclegan}

- Link: <https://www.cs.cmu.edu/~aayushb/Recycle-GAN/>
- Link: <https://www.cs.cmu.edu/~aayushb/Recycle-GAN/recycle%5Fgan.pdf>

<sup id="37b04b66e78e1d38e28548429b261a77"><a href="#Bansal_RecycleGANUnsupervisedVideo_2018" title="@incollection{Bansal_RecycleGANUnsupervisedVideo_2018,
  title = {Recycle-{{GAN}}: {{Unsupervised Video Retargeting}}},
  shorttitle = {Recycle-{{GAN}}},
  booktitle = {Computer {{Vision}} \textendash{} {{ECCV}} 2018},
  author = {Bansal, Aayush and Ma, Shugao and Ramanan, Deva and Sheikh, Yaser},
  editor = {Ferrari, Vittorio and Hebert, Martial and Sminchisescu, Cristian and Weiss, Yair},
  year = {2018},
  volume = {11209},
  pages = {122--138},
  publisher = {{Springer International Publishing}},
  address = {{Cham}},
  doi = {10.1007/978-3-030-01228-1_8},
  abstract = {We introduce a data-driven approach for unsupervised video retargeting that translates content from one domain to another while preserving the style native to a domain, i.e., if contents of John Oliver's speech were to be transferred to Stephen Colbert, then the generated content/speech should be in Stephen Colbert's style. Our approach combines both spatial and temporal information along with adversarial losses for content translation and style preservation. In this work, we first study the advantages of using spatiotemporal constraints over spatial constraints for effective retargeting. We then demonstrate the proposed approach for the problems where information in both space and time matters such as face-to-face translation, flower-to-flower, wind and cloud synthesis, sunrise and sunset.},
  file = {/Users/vasken/Documents/Notes/org/papers/Bansal_RecycleGANUnsupervisedVideo_2018.pdf},
  isbn = {978-3-030-01227-4 978-3-030-01228-1},
  language = {en},
  note = {\url{http://link.springer.com/10.1007/978-3-030-01228-1_8}}
}">Bansal_RecycleGANUnsupervisedVideo_2018</a></sup>

Considers time domain!

![[2020-08-20_16-05-43_screenshot.png]]

## <span class="section-num">3</span> Pipeline {#pipeline}

### <span class="section-num">3.1</span> Instruction to make your own {#instruction-to-make-your-own}

<https://www.youtube.com/watch?v=t59gRbpYMiY>

### <span class="section-num">3.2</span> What else can we add? {#what-else-can-we-add}

- Lips synchronization
- Voice synthesis
  - Speech-to-speech language-to-language: <https://ai.googleblog.com/2019/05/introducing-translatotron-end-to-end.html>

### <span class="section-num">3.3</span> Painting transfer {#painting-transfer}

<https://www.youtube.com/watch?v=dyzn3Fmtw-E>

[//begin]: # "Autogenerated link references for markdown compatibility"
[[2020-08-20_16-00-15_screenshot.png]: ../attachments/Style_Transfer/2020-08-20_16-00-15_screenshot.png "2020-08-20_16-00-15_screenshot.png"
[[2020-08-20_16-00-42_screenshot.png]: ../attachments/Style_Transfer/2020-08-20_16-00-42_screenshot.png "2020-08-20_16-00-42_screenshot.png"
[[2020-08-20_16-05-43_screenshot.png]: ../attachments/Style_Transfer/2020-08-20_16-05-43_screenshot.png "2020-08-20_16-05-43_screenshot.png"
[//end]: # "Autogenerated link references"