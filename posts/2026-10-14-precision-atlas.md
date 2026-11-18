---
title: A whole-brain interface from 70 patients: the Precision Neuroscience atlas
description: Precision recorded 70 patients with 1024-electrode surface grids and built an atlas of cortex, brainstem and spinal cord. What they found, and what I would train on this data.
tag: review
---

Precision Neuroscience posted a big preprint: they recorded 70 patients with their flexible 1024-electrode grids (micro-ECoG) and built an atlas from it. Cortex, brainstem, and even the spinal cord.

The idea is interesting. A whole-brain interface is usually imagined as one huge device in one head. They come at it from the other side: record many people piece by piece, bring everything into shared anatomical coordinates, and get something functionally similar.

## How they recorded
The grid lies on the brain surface and doesn't penetrate anything. The pitch is 400 µm, exactly like the Utah array we work with, but there are 10 times more electrodes, and you see LFP and high-gamma, not spikes. That's 600 times denser than clinical ECoG (~1 cm pitch). Our FingerFlex paper used clinical grids; with Precision's density, quality could in theory improve a lot.

Recordings were made during neurosurgery, so most are short: in 58 of 70 cases the grid was placed during surgery, median 22 minutes. 12 people kept it for several days and account for 85% of the ~180 hours.

## What they saw
The SSEP polarity reversal at the central sulcus fits within two grid steps (0.8 mm) at best, fingers in S1 are mostly ordered as in the homunculus, and the auditory cortex shows tonotopy. They also recorded the brainstem and spinal cord, though only evoked responses under anesthesia: on the thoracic cord, left and right leg stimulation lands on opposite sides of the grid.

There is decoding too, but always within one patient and on small tasks. Joystick in 4 directions: 83% at 25% chance. Three words plus silence: 92% with 18 training examples. 8 facial expressions: up to 67% on the best classes. Decoding is possible!

## What I'd try on this data
The data isn't released yet (access will be decided after peer review), but here's what I'd test. The interesting question is whether one model generalizes to a new patient: hand gestures were recorded in 21 patients, so train on 20 and test on the 21st. In speech BCI, Fogg et al. 2026 did something similar: a shared model with a separate input layer per person cut offline WER by 51% on average versus single-person models. I'd pretrain that shared model as an MAE on all 180 hours (87k electrodes; the authors mention foundation models themselves), then fine-tune on the small tasks (18 to 200 examples). For electrode position I'd add a relative embedding from functional connectivity, not only the template-brain coordinate, which has up to 2 mm error.

Paper: Ho, Barth, Dister et al. [Toward a whole-brain interface enabled by high-resolution surface electrophysiology](https://doi.org/10.64898/2026.09.24.754261). bioRxiv, 2026.
