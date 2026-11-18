---
title: FingerFlex: inferring finger trajectories from ECoG signals
description: Our preprint FingerFlex: a simple U-Net-like encoder-decoder on wavelet features of ECoG predicts finger movements, correlation up to 0.74 on BCI Competition IV.
tag: my work
affiliation: ALVI Labs
image: /img/fingerflex/demo-thumb.jpg
---

We are happy to share our preprint FingerFlex. We propose a new state-of-the-art model for predicting finger movements from brain activity (ECoG).

[paper](https://arxiv.org/abs/2211.01960) · [code](https://github.com/Irautak/FingerFlex)

Authors: Vlad Lomtev, Aleksandr Kovalev, Alex Timchenko.

<video src="/img/fingerflex/demo.mp4" poster="/img/fingerflex/demo-thumb.jpg" controls muted playsinline loop></video>

**Architecture.** We use a convolutional encoder-decoder architecture adapted for finger movement regression on electrocorticographic (ECoG) brain data. We show great performance with a simple U-Net-inspired architecture. As ECoG features we used the wavelet transform.

**Data.** We use open-source motor-brain datasets: BCI Competition IV and the Stanford dataset. These datasets have brain activity and finger movements recorded at the same time.

**Results.** We beat all competitors on BCI Competition IV with a correlation coefficient between true and predicted trajectories of up to 0.74.

The video above is a demonstration of our model on validation data.
