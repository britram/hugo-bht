---
title: Inline Data Integrity Signals for Passive Measurement
authors:
  - B. Trammell
  - D. Gugelmann
  - N. Brownlee
publication: In Sixth International Workshop on *Traffic Measurement and Analysis*, London, April 2014, Springer LNCS 8406
publication_short: In *TMA* 2014

date: 2014-04-01
url_pdf: /pdf/qof-tma14.pdf
url_slides: /pdf/tma14-trammell-talk.pdf
url_code: https://github.com/britram/qof

abstract: In passive network measurement, the quality of an observed traffic stream is obviously crucial to the quality of the results. Some sources of error (e.g., packet loss at a capture device) are well understood, others less so. In this work, we describe the inline data integrity measurement provided by the QoF TCP-aware flow meter. By instrumenting the data structures QoF uses for detecting lost and retransmitted TCP segments, we can provide an in-band, per-flow estimate of observation loss -- segments which were received by the recipient but not observed by the flow meter. We evaluate this mechanism against controlled, induced error, and apply it to two data sets used in previous work
abstract_short: In this work, we describe the inline data integrity measurement provided by the QoF TCP-aware flow meter. By instrumenting the data structures QoF uses for detecting lost and retransmitted TCP segments, we can provide an in-band, per-flow estimate of observation loss -- segments which were received by the recipient but not observed by the flow meter. 

math: false
selected: false

---

