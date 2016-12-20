---
title: Peeling Away Timing Error in NetFlow Data
authors:
  - B. Trammell
  - B. Tellenbach
  - D. Schatzmann
  - M. Burkhart

publication: In proceedings of the 2011 *Passive and Active Measurement* Conference, Atlanta, March 2011.
publication_short: In *PAM* 2011
date: 2011-03-19
image: 
image_preview: 
math: false
selected: false
abstract: In this paper, we characterize, quantify, and correct timing errors introduced into network flow data by collection and export via Cisco NetFlow version 9. We find that while some of these sources of error (clock skew, export delay) are generally implementation-dependent and known in the literature, there is an additional cyclic error of up to one second that is inherent to the design of the export protocol. We present a method for correcting this cyclic error in the presence of clock skew and export delay. In an evaluation using traffic with known timing collected from a national-scale network, we show that this method can successfully correct the cyclic error. However, there can also be other implementation-specific errors for which insufficient information remains for correction. On the routers we have deployed in our network, this limits the accuracy to about 70ms, reinforcing the point that implementation matters when conducting research on network measurement data.
abstract_short: In this paper, we characterize, quantify, and correct timing errors introduced into network flow data by collection and export via Cisco NetFlow version 9. We find that while some of these sources of error (clock skew, export delay) are generally implementation-dependent and known in the literature, there is an additional cyclic error of up to one second that is inherent to the design of the export protocol. We present a method for correcting this cyclic error in the presence of clock skew and export delay.
url_pdf: http://pam2011.gatech.edu/papers/pam2011--Trammell.pdf
url_slides: /pdf/pam-2011-trammell.pdf

---