---
title: Tracking transport-layer evolution with PATHspider
authors:
  - B. Trammell
  - M. Kühlewind
  - P. De Vaere
  - I. Learmonth
  - G. Fairhurst
publication: In proceedings of the second ACM/IRTF *Applied Networking Research Workshop*, Prague, July 2016.
publication_short: In *ANRW* 2017
date: 2017-07-15
image: 
image_preview: 
math: false
selected: false

short_abstract: This paper details PATHspider's design, and applies it to trace the evolution of deployment of two extensions to TCP, ECN and the newer TFO; as well as the degree of interference with the DSCP carried in the IP header. Interestingly, we observe a correlation between ECN-linked connectivity failure in the core of the network with the presence of large-scale, heterogeneous Internet censorship infrastructure.


abstract:  The ossification of the Internet protocol stack, due in large part to mangling of packets by middleboxes, has led to a relatively slow rate of change in today's Internet. We have developed the PATHspider active Internet measurement tool which performs one-sided measurements of a variety of transport-layer features and extensions, to investigate these impairments to protocol evolution along an Internet path. Data collected with PATHspider can be used both to determine the degree of support for these features, as well as to detect connectivity issues caused by attempting to use them. The wider aim of this effort is to provide quantifiable input to protocol design and deployment choices that can be based on the level of impairment present in the Internet. This paper details PATHspider's design, and applies it to trace the evolution of deployment of two extensions to TCP, ECN and the newer TFO; as well as the degree of interference with the DSCP carried in the IP header. Our ECN results, in particular, expand on a long-term study beginning in 2012, and show continued linear adoption of ECN. Automating PATHspider measurements has allowed us to collect far more data than in previous campaigns, allowing us to better distinguish ECN-linked connectivity failures from transient effects. Interestingly, we observe a correlation between ECN-linked connectivity failure in the core of the network with the presence of large-scale, heterogeneous Internet censorship infrastructure.


url_pdf: https://irtf.org/anrw/2017/anrw17-final16.pdf
---

