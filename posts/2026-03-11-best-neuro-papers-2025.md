---
title: The most tasty neuro papers of 2025
description: My personal, completely subjective list of the best neural decoding papers of 2025: invasive and noninvasive foundation models, neuro tools, and one paper from our lab.
tag: digest
telegram: https://t.me/neural_cell/333
---

My personal, completely subjective list of the best neural decoding papers of 2025. Trend of the year: throw in more data and pray it gets better. But the main question is still how to combine data across animals, brain areas and electrode types in one model.

I split 10 papers into 4 sections: invasive signals, noninvasive signals, neuro software, and at the end a paper from our lab (I'm not a co-author, the work started before me).

## 01. Invasive signals

**Foundation model of neural activity predicts response to new stimulus types**
Foundation model trained on mouse V1 generalizes to completely new stimulus types (motion, noise, Gabor) and predicts cell types from MICrONS.
[Nature 2025](https://www.nature.com/articles/s41586-025-08829-y)

**Neural Encoding and Decoding at Scale (NEDS)**
One model does both encoding and decoding across 83 mice on Neuropixels/IBL data. Multi-task masking, SOTA on both directions, predict brain activity and behavior.
[ICML 2025](https://arxiv.org/pdf/2504.08201v1)

**A cross-species neural foundation model for end-to-end speech decoding (BIT)**
End-to-end brain-to-text: transformer pretrained on 367 hours of Utah array data (human + monkey), paired with audio-LLM. WER drops from 24.69% to 10.22%, transfers to imagined speech.
[ICLR 2026](https://arxiv.org/abs/2511.21740)

**A Generalist Intracortical Motor Decoder (NDT3)**
Autoregressive transformer pretrained on 2000 hours of intracortical spiking from 30+ subjects. Beats from-scratch models when you have less than 1.5 hours of task data.
[NeurIPS 2025](https://github.com/joel99/ndt3)

**OMiSO: Adaptive optimization of state-dependent brain stimulation**
Closed-loop stimulation that uses pre-stim brain state to pick which electrodes to zap on a Utah array in monkey PFC. Adapts online, outperforms state-blind methods.
[NeurIPS 2025](https://arxiv.org/abs/2507.07858v1)

## 02. Noninvasive signals

**REVE: A Foundation Model for EEG**
MAE on 60,000 hours of EEG from 25,000 subjects across 92 datasets. 4D positional encoding handles any electrode config. SOTA on 10 downstream tasks.
[NeurIPS 2025](https://brain-bzh.github.io/reve/)

**LSM-2: Learning from incomplete wearable sensor data**
Foundation model for wearables pretrained on 40M hours of day-long sensor data. Learns directly from incomplete recordings via learnable mask tokens, no imputation.
[arXiv 2025](https://arxiv.org/abs/2506.05321)

## 03. NeuroTools

**Kilosort4**
Graph-based clustering with merging trees for spike sorting. Best across all conditions, handles low-amplitude neurons under high drift.
[Nature Methods 2024](https://www.nature.com/articles/s41592-024-02232-7)

**Jaxley: differentiable simulation of biophysical neural models**
JAX framework for biophysical neuron models with autodiff and GPU acceleration. Fit compartmental models orders of magnitude faster, trained a 100k-param morphological network on vision.
[Nature Methods 2025](https://www.nature.com/articles/s41592-025-02895-w)

## 04. Our lab

**Neural correlates of phosphene perception in blind individuals: A step toward a bidirectional cortical visual prosthesis**
[Science Advances 2025](https://www.science.org/doi/10.1126/sciadv.adv8846)

p.s. Write which papers I missed and should have added to this top.
