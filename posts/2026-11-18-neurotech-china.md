---
title: Brain-computer interfaces in China: 12 companies, money and data
description: China approved the first implantable BCI as a product, lets hospitals start implant studies themselves, and raised over $1B for BCI in the first half of 2026 alone. I went through 12 companies.
tag: review
image: /fig/china/map-preview.png
---

<img class="svg wide" src="/fig/china/map.svg" alt="Map of China with the twelve companies and how much each raised">

Recently Bashar Badran from the Chinese startup Gestala visited us. He used to work at Neuralink, and now he runs clinical and science there. He told us how strong neurotech in China is right now. At AAAI I also talked a lot with a colleague from a BCI lab in Beijing. Then I got sick, stayed at home and finally decided to figure out what is really going on there.

First thing I found: on March 13, 2026 China approved NEO by Neuracle, the world's first implantable brain-computer interface as a product. 9 days later it got an insurance billing code, 11 days later it was on public procurement lists ([MIT Tech Review](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/)).

Then I found out that in China a hospital can start a human study of an implant by itself. Lab tests, materials and large-animal studies are still required ([example](https://ccj.pku.edu.cn/Article/DownLoad?id=797921449017413&type=ArticleFile)), but the hospital reviews them, and since May 2026 the National Health Commission only gets a notification and can stop the study later ([NHC](https://www.nhc.gov.cn/qjjys/c100015/202604/1c2cca29daef42509e8ffd9ddf9c64fd.shtml)). In the US, the FDA reviews all of this before the start.

And money. By the Chinese database IT桔子, Chinese BCI raised ~$357M in all of 2025 and ~$1.08B in just the first half of 2026, 3x more ([36Kr](https://news.pedaily.cn/202610/570325.shtml)). The tracker New Market Pitch counts only rounds with a disclosed amount and sees less: at least $922M for China by mid-November 2026, against $932M for the US ([New Market Pitch](https://newmarketpitch.com/blogs/news/brain-computer-interface-funding-trends)). So even by the lower count China is level with the US, and by the Chinese count it is probably already ahead.

Now the companies.

<img class="svg wide" src="/fig/china/section.svg" alt="Cross-section of the head with each device at its depth">
<p class="meta">How deep each device goes. The vision implants are in their own section below.</p>

## Invasive

### [Neuracle](https://www.neuracle.cn)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-neo.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">博睿康</dd><dt>Where</dt><dd>Shanghai</dd><dt>Founded</dt><dd>2011</dd><dt>Raised</dt><dd>not public (valuation ~$595M)</dd><dt>Last round</dt><dd>$45M (11.2025), preparing an IPO</dd><dt>Data</dt><dd><span class="ev pre">preprint, one patient</span></dd></dl></div>

**what:** the first approved implant, NEO. For people with tetraplegia after a neck injury: close and open the hand.
- Basically 8 contacts on top of the dura, nothing goes into the cortex. No battery, it works while a coil sits on the head. An external computer decodes and inflates a glove on the hand
- One patient: F1 0.91 over 9 months at home ([medRxiv](https://www.medrxiv.org/content/10.1101/2024.09.05.24313041)). My first thought was that EEG has done the same for years. I found a similar patient: ~70% accuracy after a year of training ([Rohm 2013](https://doi.org/10.1016/j.artmed.2013.07.004)). Different metrics, but the gap is clear
- A kit costs $71k, 13 sold since July. No paper yet on the 32 patients from the trial

### [StairMed](https://www.stairmed.com/en)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-threads.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">阶梯医疗</dd><dt>Where</dt><dd>Shanghai</dd><dt>Founded</dt><dd>2021</dd><dt>Raised</dt><dd>$387M</dd><dt>Last round</dt><dd>~$208M (H2 2026), preparing an IPO</dd><dt>Data</dt><dd><span class="ev paper">paper on recording, not decoding</span></dd></dl></div>

**what:** the closest to Neuralink: flexible electrodes that actually go into the cortex, 256 channels.
- 42 implants, by their count already more than Neuralink
- cursor 6.5 bits/s, but this is the company's number
- there is a paper, but about single-neuron recording, not decoding ([Nat Comms](https://www.nature.com/articles/s41467-026-71443-7)). Waiting for a decoding paper

### [NeuroXess](https://www.neuroxess.com)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-grid.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">脑虎科技</dd><dt>Where</dt><dd>Shanghai</dd><dt>Founded</dt><dd>2021</dd><dt>Raised</dt><dd>~$168M</dd><dt>Last round</dt><dd>$104M (10.2026)</dd><dt>Data</dt><dd><span class="ev paper">peer-reviewed decoding paper</span></dd></dl></div>

**what:** basically a Chinese Precision. A flexible micro-ECoG grid sits on the cortex and does not penetrate it. 256 channels vs 1024 at Precision, but they have a fully implanted version with a battery.
- 65 clinical cases, now a registration trial in 16 hospitals
- Mandarin speech: 394 syllables, median 71.2% ([Science Advances](https://doi.org/10.1126/sciadv.adz9968)). By the way, Li Yuanning is a co-author there, he shows up again below

### NeuCyber / Beinao

<div class="cocard"><img class="svg dev" src="/fig/china/dev-pad.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">北京芯智达 · 北脑</dd><dt>Where</dt><dd>Beijing</dd><dt>Founded</dt><dd>2023</dd><dt>Raised</dt><dd>~$30M from the Beijing government</dd><dt>Last round</dt><dd>no private rounds</dd><dt>Data</dt><dd><span class="ev claim">numbers from the institute only</span></dd></dl></div>

**what:** a state project of the Beijing brain institute [CIBR](https://www.cibr.ac.cn).
- Beinao-1 sits above the dura, 128 channels, decodes ~100 Chinese words. 40+ patients, but the numbers differ between sources
- Beinao-2 is intracortical, 512 channels, promised in humans by the end of 2026

**New wave of intracortical startups.** Lots of money, no clinical data at all:

<div class="cocards">
<div class="cocard"><img class="svg dev" src="/fig/china/dev-threads.svg" alt=""><h4><a href="https://www.aitbci.com">AIT</a></h4><dl><dt>In Chinese</dt><dd lang="zh">主动科技</dd><dt>Where</dt><dd>Shanghai</dd><dt>Founded</dt><dd>2026</dd><dt>Raised</dt><dd>~$118M</dd><dt>Last round</dt><dd>$69M (11.2026)</dd><dt>Data</dt><dd><span class="ev none">no human data</span></dd></dl><p class="note">Active Intelligence Technologies. A record for an angel round. Ultra-flexible electrodes, 1024 channels</p></div>
<div class="cocard"><img class="svg dev" src="/fig/china/dev-threads.svg" alt=""><h4><a href="https://www.bciflex.com">Zhiran / BCIFlex</a></h4><dl><dt>In Chinese</dt><dd lang="zh">智冉医疗</dd><dt>Where</dt><dd>Beijing</dd><dt>Founded</dt><dd>2022</dd><dt>Raised</dt><dd>$93M</dd><dt>Last round</dt><dd>$45M (02.2026)</dd><dt>Data</dt><dd><span class="ev none">no human data</span></dd></dl><p class="note">Ultra-thin flexible electrodes</p></div>
<div class="cocard"><img class="svg dev" src="/fig/china/dev-unknown.svg" alt=""><h4>Zhonghua</h4><dl><dt>In Chinese</dt><dd lang="zh">衷华脑机</dd><dt>Where</dt><dd>Wuhan</dd><dt>Founded</dt><dd>2021</dd><dt>Raised</dt><dd>no rounds</dd><dt>Last round</dt><dd>funded personally by the chairman of Guide Infrared</dd><dt>Data</dt><dd><span class="ev none">no paper</span></dd></dl><p class="note">Claims 65,536 channels, “20x more than Neuralink”</p></div>
</div>

## Vision

This is the most interesting part for me: we work with a Utah array in V1 of a blind participant ourselves.

### Mindtrix

<div class="cocard"><img class="svg dev" src="/fig/china/dev-tiles.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">明视脑机</dd><dt>Where</dt><dd>Suzhou (one source)</dd><dt>Founded</dt><dd>2024</dd><dt>Raised</dt><dd>&gt;$74M in 2026</dd><dt>Last round</dt><dd>pre-A+ (11.2026)</dd><dt>Data</dt><dd><span class="ev claim">company claims, one sighted patient</span></dd></dl></div>

**what:** visual cortex stimulation, 1024 channels.
- Data so far from one sighted patient with epilepsy, an acute experiment. He saw "shapes and colors", phosphene positions matched in 95% of cases, according to the company
- No paper, no video. The first blind patient is promised in 2027

### Xinsheng Shijie

<div class="cocard"><img class="svg dev" src="/fig/china/dev-tiles.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">芯生视界</dd><dt>Where</dt><dd>Beijing</dd><dt>Founded</dt><dd>2026</dd><dt>Raised</dt><dd>~$15M</dd><dt>Last round</dt><dd>seed (06.2026)</dd><dt>Data</dt><dd><span class="ev none">preclinical</span></dd></dl></div>

**what:** also a cortical visual prosthesis, still preclinical. Their co-founder is the same [Li Yuanning](https://yuanningli.github.io) from the NeuroXess paper, a former postdoc of Edward Chang.

### [NanoChap](https://www.nanochap.com)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-eye.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">暖芯迦</dd><dt>Where</dt><dd>Hangzhou</dd><dt>Founded</dt><dd>2014</dd><dt>Raised</dt><dd>~$149M</dd><dt>Last round</dt><dd>$74M (11.2026)</dd><dt>Data</dt><dd><span class="ev claim">clinical trial, no paper yet</span></dd></dl></div>

**what:** a retinal implant, 320 channels, already in a clinical trial.
- a woman who had not seen for ~20 years recognizes some letters and writes the word "China" in Chinese characters
- a 1280-channel cortical version is still in development

Europe for comparison:

- **[ReVision Implant](https://www.revision-implant.com/) · Leuven · 2020 · last round $4.5M (05.2026)**. Cortical prosthesis. They plan the first clinical study in humans in our lab at the end of 2027
- **[Phosphoenix](https://www.phosphoenix.nl) · Amsterdam · last round $1.5M (09.2026)**. They stimulate the LGN, not the cortex

## Non-invasive

### [BrainCo](https://www.brainco.tech)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-band.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">强脑科技</dd><dt>Where</dt><dd>Hangzhou and Boston</dd><dt>Founded</dt><dd>2015</dd><dt>Raised</dt><dd>~$370M</dd><dt>Last round</dt><dd>$286M (01.2026)</dd><dt>Data</dt><dd><span class="ev claim">products on sale</span></dd></dl></div>

**what:** EEG headbands, a bionic hand on sEMG and hands for humanoids. The Hong Kong IPO was postponed.

### [Gestala](https://www.gestala.com)

<div class="cocard"><img class="svg dev" src="/fig/china/dev-waves.svg" alt=""><dl><dt>In Chinese</dt><dd lang="zh">格式塔科技</dd><dt>Where</dt><dd>Chengdu and Shanghai</dd><dt>Founded</dt><dd>2026</dd><dt>Raised</dt><dd>$85M in six months</dd><dt>Last round</dt><dd>~$63M (07.2026)</dd><dt>Data</dt><dd><span class="ev claim">company numbers, 30+ cases</span></dd></dl></div>

**what:** ultrasound without an implant plus a brain foundation model.
- first indication: chronic pain, 30+ cases
- the same Bashar joined them from Neuralink in April 2026, where he led clinical partnerships ([Gestala](https://www.gestala.com/news/15))

## My thoughts

Time to move to China 😅

OK, seriously: China invests a lot in neurotech. There is both private and state money. The regulator makes it easier to test new technologies in humans, so you can work with a hospital directly. It may look like there are not many papers and details, but we can say the same about American companies. In my view, this is fine. It is hard to demand papers in top journals from startups.

On vision: Mindtrix alone raised more than 10x what ReVision and Phosphoenix raised together in 2026. And the Europeans have no human data at all, while Mindtrix has at least one test (on a sighted patient, during a different procedure).

China is quickly becoming the second neurotech center in the world, right after the US. My prediction: in 5–10 years China can take first place by the number of implanted neural devices.

## References

**Regulation and money**
- MIT Technology Review, [China has approved the world's first invasive brain-computer chip](https://www.technologyreview.com/2026/06/01/1138133/china-world-first-brain-chip/), 2026-06-01
- BioSpectrum Asia, [Approved, coded, listed: China's neurotech speed run](https://www.biospectrumasia.com/analysis/29/28439/approved-coded-listed-chinas-neurotech-speed-run.html), 2026-10-01
- National Health Commission, [notice on hospital-initiated clinical research](https://www.nhc.gov.cn/qjjys/c100015/202604/1c2cca29daef42509e8ffd9ddf9c64fd.shtml), 2026-04
- Peking University, [example of the preclinical package for an implant study](https://ccj.pku.edu.cn/Article/DownLoad?id=797921449017413&type=ArticleFile)
- Chen L. et al., [Clinical translation of BCI in China: IITs, registered trials, regulatory approval](https://arxiv.org/abs/2607.07185), arXiv, 2026-07
- 36Kr / PEdaily, [IT桔子 data: 64 deals and ¥7.25B in H1 2026, ¥2.40B in all of 2025](https://news.pedaily.cn/202610/570325.shtml), 2026-10-15
- New Market Pitch, [BCI funding trends](https://newmarketpitch.com/blogs/news/brain-computer-interface-funding-trends) (disclosed rounds only, January 1 – November 13), updated 2026-11-17

**Neuracle**
- Preprint on the home-use patient, [medRxiv](https://www.medrxiv.org/content/10.1101/2024.09.05.24313041)
- EEG comparison: Rohm et al., [Artificial Intelligence in Medicine, 2013](https://doi.org/10.1016/j.artmed.2013.07.004)
- Price and sales of NEO, [CLS](https://www.cls.cn/detail/2496641), 2026-09-30
- First commercial implant at Huashan, [InsideBCI](https://insidebci.com/news/2026-07-16-neuracle-neo-shanghai-huashan-first-commercial-invasive-bci-motor-restoration/), 2026-07-16
- Round E and valuation, [36Kr](https://www.36kr.com/p/3914507815048580)

**StairMed**
- Single-neuron recording paper, [Nature Communications](https://www.nature.com/articles/s41467-026-71443-7)
- 42 long-term implants, [Sina Finance](https://finance.sina.com.cn/tjhz/2026-10-28/doc-iniwttrx3881920.shtml), 2026-10-28
- IPO preparation and total raised, [The Paper](https://www.thepaper.cn/newsDetail_forward_34393222), 2026-11-03

**NeuroXess**
- Mandarin speech decoding, [Science Advances](https://doi.org/10.1126/sciadv.adz9968)
- Series B and 65 cases, [TechNode](https://technode.com/2026/10/28/brain-computer-interface-startup-neuroxess-raises-rmb-700-million-in-series-b-funding/), 2026-10-28
- Registration trial in 16 hospitals, [10jqka](https://news.10jqka.com.cn/20260707/c678002947.shtml), 2026-07-07

**NeuCyber / Beinao**
- Beinao-1 registration trial, [China Daily](https://global.chinadaily.com.cn/a/202606/15/WS6a2fc5cba310986e2b460147.html), 2026-06-15
- "3 years behind Neuralink", [Reuters via Yahoo Finance](https://finance.yahoo.com/sectors/technology/articles/beijing-backed-brain-chip-firm-091954964.html), 2026-03-20
- 40+ implants, [CLS](https://www.cls.cn/detail/2452538), 2026-08

**AIT, Zhiran / BCIFlex, Zhonghua**
- AIT angel+ round, [PEdaily](https://news.pedaily.cn/202611/571311.shtml), 2026-11
- Zhiran A+ round, [36Kr](https://eu.36kr.com/zh/p/3677251288654473)
- Zhonghua: 65,536 channels and first clinical test, [Yicai](https://www.yicai.com/news/102020432.html), 2024-11; funding by the chairman of Guide Infrared, [NBD](https://www.mrjjxw.com/articles/2024-03-10/3274015.html), 2024-03

**Vision**
- Mindtrix pre-A and pre-A+ rounds, [ChinaVenture](https://m.chinaventure.com.cn/news/111-20261111-393997.html), 2026-11-11; MXIRV1024, [VCBeat](https://www.vcbeathealth.com/article/30930), 2026-06-07
- Xinsheng Shijie seed round, [Sina Finance](https://finance.sina.cn/2026-06-18/detail-inicvfcv5537233.d.html), 2026-06-18
- NanoChap round C+ and total raised, [STAR Market Daily](https://www.chinastarmarket.cn/detail/2523248); retinal implant, [36Kr](https://eu.36kr.com/zh/p/4053371952288905)
- ReVision Implant, [Tech.eu](https://tech.eu/2026/05/26/revision-implant-secures-eur4m-to-advance-vision-restoration-technology/), 2026-05-26

**Non-invasive**
- BrainCo round, [Hangzhou government](https://www.ehangzhou.gov.cn/2026-01/08/c_296701.htm), 2026-01-08; Hong Kong IPO filing, [Sohu](https://www.sohu.com/a/975181101_115831)
- Gestala rounds and two headquarters, [Yicai](https://www.yicai.com/news/103259858.html), 2026-07; Bashar Badran joins, [Gestala](https://www.gestala.com/news/15)

Amounts in yuan are converted at 6.72 ¥/$ (November 2026).
