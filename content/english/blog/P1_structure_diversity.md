---
title: "When Structure Becomes the Villain: Structural Diversity and Long-Term Stability in Natural Tropical Forests"
meta_title: ""
description: "this is meta description"
date: 2025-12-20T05:00:00Z
image: "/images/Structurediversity.png"
categories: ["Macroecology", "Data","Ecology","Structure diversity"]
author: "Yuyue Deng"
tags: ["Macroecology", "Ecology"]
draft: false
---
## 人们对多样性-temporal stability 的传统认知

Most forest ecologists grew up with a comforting idea: **more biodiversity stabilizes ecosystem functioning**. 但这一印象一直都是源于草地生态系统，北方森林，亦或是在一些幼苗中国，这些生态系统有一个共有的特征，那就是-**low species richness，一般来说，每公顷不超过20（你改一下）个物种** .  这种现象是否是general的，例如 in *natural* tropical or subtropical forests—where species richness is already extreme—this relationship 是否还是  behave the way we assume？ 这值得让人思考.

---

## Why tropical or subtropical matured forest 的另一个重要特征 - Complex Structure

1. 热带森林拥有超大的树木和更丰富的林下层，这导致了结构多样性的存在，简而言之，结构多样性就是 quantifies variation in the size and form of plant organs, for example, tree stem and canopy, among individuals (Atkins et al., 2023; LaRue et al., 2023)
2. 热带森林可能再局部更加拥挤，而在另一局部更加的开阔。这一种horizontal水平structure 特征，更拥挤意味着更弱的竞争，而更开阔意味着更强的竞争。因此，这种空间分配模式，将可能强烈影响群落的long term stabilit.

<div style="margin: 2rem 0;">
  <div style="display: flex; gap: 1.5rem; align-items: flex-start; flex-wrap: wrap;">
    <!-- Tropical forest -->
    <div style="flex: 1; min-width: 300px; text-align: center;">
      <img src="/images/forest/Tropical2.png" alt="Tropical forest with large canopy trees and dense understory" style="width: 100%; height: 400px; object-fit: cover; border-radius: 6px; display: block;" loading="lazy" />
      <p style="font-size: 0.9rem; margin-top: 0.5rem; color: inherit;">
        <strong>Tropical forest</strong><br/>
        Large emergent trees, wide size spectrum, dense understory regeneration
      </p>
    </div>
    <!-- Boreal / temperate forest -->
    <div style="flex: 1; min-width: 300px; text-align: center;">
      <img src="/images/forest/Wisconsin_forest.jpg" alt="Wisconsin forest with simpler vertical structure" style="width: 100%; height: 400px; object-fit: cover; border-radius: 6px; display: block;" loading="lazy" />
      <p style="font-size: 0.9rem; margin-top: 0.5rem; color: inherit;">
        <strong>Boreal / temperate forest (Wisconsin)</strong><br/>
        Simpler vertical structure, fewer understory saplings
      </p>
    </div>
  </div>
  <p style="text-align: center; font-size: 0.85rem; margin-top: 0.75rem; color: #555;">
    <strong>Figure.1</strong> Visual contrast in forest structural diversity.
    Tropical forests exhibit extreme tree size variation, with very large canopy trees
    coexisting with abundant understory individuals, whereas boreal and temperate forests
    tend to show simpler vertical structure and narrower size distributions.
  </p>
</div>

This page introduces an ongoing research direction we are building with long-term Forest Dynamics Plot (FDP) data:
**structural diversity may be a more reliable predictor of long-term stability than species richness—and it may even act as a “bad guy.”**

{{< callout type="info" title="Quick take" >}}
We are inviting collaborators from ForestGEO and other FDP networks to test whether
*structural diversity* (size and spatial heterogeneity) can **reduce long-term stability**
in mature, species-rich tropical forests, and to map when and where that happens.
{{< /callout >}}

{{< stab_show height="800px" width="100%" >}}

---



## 我们专注的问题，The core question

We focus on **long-term temporal stability** of forest productivity, commonly quantified as:

- **Stability (S)** = mean productivity / temporal standard deviation (μ / σ)

In words: *a forest is “stable” when it maintains high function with low inter-census variability.*

### Two candidate predictors

- **Species richness (SR)** Captures how many species are present; often linked to stability via **species asynchrony** (insurance effects).
- **Structural diversity (SD)**
  Captures variation in size and form among individuals (e.g., stem size inequality, canopy layering); a more proximate representation of **realized niche occupancy**.

---

## Why structural diversity could be the “bad guy” in natural tropical forests

尽管structure diversity 可能提供更多的垂直ecological niche, 但是:


In mature tropical forests, **structure is not just heterogeneity—it is competition embodied**.

- 从垂直结构来讲，这加剧了 asymmetric competition for light, water,etc，
- 从水平结构来讲当过度聚集时或过度分散时，能量的分配存在大量的倾斜，例如
- 不仅如此，群落的生产力增加绝大部分是由于tree growth所贡献，而recruitment对生产力的影响较小。更大的树木的存在，意味着如果遭遇恶劣环境，例如typhoon，雷暴，大树将会死亡，大部分的growth停摆，当然，大树的死亡会由大量的recuitment productivity 所替代，但是这无济于事
- 
- Demographic stochasticity and neighborhood crowding
- Potential niche overlap despite extremely high species richness

These processes can generate a counterintuitive outcome:

<details open>
<summary><strong>The core hypothesis</strong></summary>

{{< callout type="tip" title="Hypothesis" >}}
In species-rich natural tropical forests, higher structural diversity—especially
adult-tree size inequality—may **destabilize** long-term function by amplifying
competitive asymmetry and increasing inter-census volatility.
{{< /callout >}}

</details>




---

## What is missing in the literature

Evidence for biodiversity–stability (and structural diversity–stability) relationships in forests is often derived from:

- temperate forests with relatively low species richness
- sapling layers, where size variation is narrow
- experimental plantations with only a few species

What we still lack are tests that are simultaneously:

1. **Species-rich** (natural tropical or subtropical forests)
2. **Adult-tree dominated** (where size inequality is pronounced)
3. **Long-term** (multiple censuses, not short snapshots)
4. **Cross-site comparable** (replication across plots)

{{< callout type="note" title="Why FDP plots matter" >}}
Long-term FDP censuses are one of the few data infrastructures that can directly
test these questions with the necessary temporal depth and demographic detail.
{{< /callout >}}

---

## What we are building

Science 2024, this project aims to develop a **cross-site, census-based analytical framework** to evaluate:

- whether structural diversity outperforms species richness in predicting long-term stability
- whether structural diversity effects are **directionally negative** in mature tropical forests
- whether these effects operate via:
  - species asynchrony
  - population-level stability
  - or direct structural mechanisms

### What counts as “structural diversity” here?

Depending on what a site can provide, structural diversity may include (examples):

- size inequality metrics (e.g., Gini coefficients of DBH or basal area contribution)
- distributional shape metrics (e.g., Lorenz-based asymmetry)
- vertical and horizontal structure proxies, when available

<details>
<summary><strong>What I typically need from a plot (minimal data request)</strong></summary>

- Standard FDP tree census table(s), including:

  - tree ID
  - species code
  - DBH (with census year or measurement date)
  - status (alive/dead) and recruitment information, if available
  - spatial coordinates (optional but strongly preferred for spatial analyses)
- At least **three censuses** preferred (more is better)
- Site metadata: plot area, census years, and basic climate descriptors if available

</details>

---

## What collaborators get

I aim to keep this a **low-friction, high-credit** collaboration model.

- Co-authorship opportunities (default for meaningful data contributions)
- Site PI involvement welcomed in framing and interpretation
- Transparent, reproducible pipelines with documented outputs
- Option to include site-specific questions (e.g., drought events, disturbance history)

{{< callout type="success" title="Collaboration modes" >}}

1. **Data contribution + co-authorship**
2. **Joint analysis with your team**
3. **Methods transfer** – I help you run the pipeline locally if data governance requires
   {{< /callout >}}

---

## Data governance & credit

I fully respect plot-level data governance.

- No redistribution of raw plot data
- Analyses are reproducible and shareable
- Site PI approval and authorship policies will be followed
- Outputs can be returned in formats useful for site reporting

<details>
<summary><strong>Authorship statement (draft)</strong></summary>

Authorship will follow standard ecological norms and site governance policies.
Plots providing data that are central to cross-site inference will be offered co-authorship.
Site PIs are encouraged to co-develop interpretations and contribute contextual knowledge
(e.g., disturbance history, measurement protocols, site-specific mechanisms).

</details>

---

## Current status

- Conceptual framework: ready
- Pipeline: under active development and harmonization across censuses
- Target outputs:
  - a cross-site synthesis paper
  - a methods note or open workflow (where permitted)
  - optional plot-specific vignettes

---

## Interested in joining?

If you manage or work with a Forest Dynamics Plot and are interested in testing how
**structural diversity shapes long-term stability**, I would be very happy to connect.

- Contact: **Yuyue Deng**
- Suggested email subject line: *“FDP collaboration: structural diversity & long-term stability”*

{{< callout type="warning" title="One-sentence pitch (copy & paste)" >}}
I am building a cross-site FDP analysis to test whether structural diversity is a
stronger—and potentially negative—predictor of long-term stability than species
richness in mature, species-rich tropical forests.
{{< /callout >}}
