---
title: Principles for Measurability in Protocol Design
authors:
  - M. Allman
  - R. Beverly
  - B. Trammell
publication: In *ArXiV*, preprint 1612.02902 
publication_short: In *ArXiV* 
date: 2016-12-09
abstract: Measurement has become fundamental to the operation of networks and at-scale services, whether for management, security, diagnostics, optimization, or simply enhancing our collective understanding of the Internet as a complex system. Further, measurements are useful across points of view, from end hosts to enterprise networks and data centers to the wide area Internet. We observe that many measurements are decoupled from the protocols and applications they are designed to illuminate. Worse, current measurement practice often involves the exploitation of side-effects and unintended features of the network; or, in other words, the artful piling of hacks atop one another. This state of affairs is a direct result of the relative paucity of diagnostic and measurement capabilities built into today's network stack.  Given our modern dependence on ubiquitous measurement, we propose measurability as an explicit low-level goal of current protocol design, and argue that measurements should be available to all network protocols throughout the stack. We seek to generalize the idea of measurement within protocols, e.g., the way in which TCP relies on measurement to drive its end-to-end behavior. Rhetorically, we pose the question "what if the stack had been built with measurability and diagnostic support in mind?". We start from a set of principles for explicit measurability, and define primitives that, were they supported by the stack, would not only provide a solid foundation for protocol design going forward, but also reduce the cost and increase the accuracy of measuring the network.
abstract_short: We seek to generalize the idea of measurement within protocols, e.g., the way in which TCP relies on measurement to drive its end-to-end behavior. Rhetorically, we pose the question "what if the stack had been built with measurability and diagnostic support in mind?". We start from a set of principles for explicit measurability, and define primitives that, were they supported by the stack, would not only provide a solid foundation for protocol design going forward, but also reduce the cost and increase the accuracy of measuring the network.
math: false
selected: true
image: 
image_preview:
url_pdf: https://arxiv.org/pdf/1612.02902v1
---