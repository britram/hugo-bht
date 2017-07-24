---
title: copycat - Testing Differential Treatment of New Transport Protocols in the Wild
authors:
  - K. Edeline
  - M. Kühlewind
  - B. Trammell
  - B. Donnet
publication: In proceedings of the second ACM/IRTF *Applied Networking Research Workshop*, Prague, July 2016.
publication_short: In *ANRW* 2017
date: 2016-07-15
image: 
image_preview: 
math: false
selected: false

short_abstract: This paper introduces copycat, a generic transport protocol testing tool that highlights differential treatment by the path in terms of connectivity and QoS between TCP and a non-TCP transport protocol. copycat generates TCP-shaped traffic with custom headers, and compares its performance in terms of loss and delay with TCP.


abstract:  Recent years have seen the development of multiple transport solutions to address the ossification of TCP in the Internet, and to ease transport-layer extensibility and deployability. Recent approaches, such as PLUS and Google’s QUIC, introduce an upper transport layer atop UDP; their deployment therefore relies on UDP not being disadvantaged with respect to TCP by the Internet. This paper introduces copycat, a generic transport protocol testing tool that highlights differential treatment by the path in terms of connectivity and QoS between TCP and a non-TCP transport protocol. copycat generates TCP-shaped traffic with custom headers, and compares its performance in terms of loss and delay with TCP. We present a proof-of-concept case study (UDP vs. TCP) in order to answer questions about the deployability of current transport evolution approaches, and demonstrate the extent of copycat’s capabilities and possible applications. While the vast majority of UDP impairments are found to be access-network linked, and subtle impairment is rare, middleboxes might adapt to new protocols that would then perform differently in the wild compared to early deployments or controlled environment testing.


url_pdf: https://irtf.org/anrw/2017/anrw17-final16.pdf
---

