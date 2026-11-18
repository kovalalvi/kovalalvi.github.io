---
title: Cross-subject speech BCI: what is inside the architecture
description: Boccato, Olak and Ferrante (J Neural Eng 2026) jointly train a phoneme decoder on two Utah speech datasets and adapt to new people with almost one linear layer. The three components, the results, and what I would take for NeuroMAE.
tag: review
---

A paper in J Neural Eng (Boccato, Olak, Ferrante, 2026): jointly train a phoneme decoder on two Utah array speech datasets (Willett T12 + Card T15) and adapt to new people with almost a single linear layer.

**The problem.** Almost all brain-to-text systems are trained from scratch on one participant. A new patient means hours of calibration. Cross-subject has barely been touched, although day-to-day drift within a person is of the same order as the difference between people.

## Three components

1. **A day/subject affine layer before everything.** For each `(subject, day)`: `x̃ = W_{d,s} x + b`. Channels are padded to a common 512-d (spike counts + spike-band power, 20 ms bins). This is not a per-channel gain but a linear realignment into a shared space. In the analysis the diag_ratio is ~0.7–0.9 (mostly "own" channels), but there is off-diagonal mixing. Swapping days: the own transform is better, a foreign one still doesn't kill PER, so the manifold is stable up to an affine map.

2. **Hierarchical GRU + feedback, not a transformer.** Three blocks: early = 2× biGRU → phoneme logits → projected back → **added** to the hidden state; middle the same; final = 1× GRU. Hidden size **2048** (the baselines use 512/1024). Loss: `CTC_final + λ (CTC_early + CTC_middle)`, λ = 0.3. The point: plain CTC treats frames as independent; early phoneme hypotheses are fed back into the next GRUs to partly bring back a sequential bias without an autoregressive transformer (in the Brain2Text challenge a small GRU+CTC still beat transformers and SSMs).

3. **WFST + LM outside.** Phoneme → lexicon → 5-gram → rescoring with OPT-125M. Most of the WER errors are here, not in neural → phoneme.

## Where they tested
Joint training on Willett + Card. Hierarchical: Willett PER **16.1%** vs baseline **19.7%**; Card **9.1%** vs **10.2%**. Plain CTC is already almost there; the hierarchy gives a mild gain, significant over 5 seeds. On Kunz (inner speech, T12–T17): freeze the backbone, train only `W, b` on 100–1000 trials → PER drops from chance; full fine-tuning gives another −20–40% relative. From scratch on a tiny vocabulary (7 words) is sometimes better, and they say so honestly. Joint training on 6 subjects is stronger than adapting after the fact.

## What could be improved, and what I'd take for NeuroMAE

1. **An "affine only" ablation.** The main result mixes joint data + H = 2048 + hierarchy. For us the first piece matters. We need a table: plain GRU + day affine vs + hierarchy vs + bigger H. If the affine layer carries 80% of the effect, we copy only that.

2. **Affine vs a proper alignment.** They use a linear `W`. For V1/Utah I would right away compare it with Procrustes / CCA / a soft day embedding (MoE over day id) under the same frozen-backbone protocol. Hypothesis: session drift in MUA is more often an almost orthogonal rotation + scale, not a full `W ∈ R^{512×512}`.

3. **The same adaptation protocol on NeuroMAE.** Pretrain the MAE on subject A (or a pool), on subject B fit only `W_B` / the positional encoding, probe the frozen latents. Null: permute the day labels of `W_{d,s}`; if the metric survives, the alignment overfits. This is exactly their bet "cross-subject = a linear re-centering", just without CTC and a speech LM.

It's not V1 and not imagery: it's speech motor cortex + phoneme CTC. I would steal the align + freeze recipe; a hierarchical GRU is not needed for resting MUA.

Paper: Boccato, Olak, Ferrante. [Cross-subject decoding of human neural data for speech brain computer interfaces](https://doi.org/10.1088/1741-2552/ae8576). J Neural Eng 23, 046018 (2026).
