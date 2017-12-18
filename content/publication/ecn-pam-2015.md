---
title: Enabling Internet-Wide Deployment of Explicit Congestion Notification
authors:
  - B. Trammell
  - M. Kühlewind
  - D. Boppart
  - I. Learmonth
  - G. Fairhurst
  - R. Scheffenegger
publication: In proceedings of the 2015 *Passive and Active Measurement* Conference, Brooklyn, Springer LNCS 8995.
publication_short: In *PAM* 2015
date: 2015-03-19
image: 
image_preview: 
math: false
selected: true
abstract_short: This measurement study provides an update on deployment status and newly assesses the marginal risk of enabling ECN negotiation by default on client end-systems. Additionally, we dig deeper into causes of connectivity and negotiation issues linked to ECN. We find that about five websites per thousand suffer additional connection setup latency when fallback per RFC 3168 is correctly implemented; we provide a patch for Linux to properly perform this fallback. 
abstract: Explicit Congestion Notification (ECN) is an TCP/IP extension to signal network congestion without packet loss, which has barely seen deployment though it was standardized and implemented more than a decade ago. On-going activities in research and standardization aim to make the usage of ECN more beneficial.This measurement study provides an update on deployment status and newly assesses the marginal risk of enabling ECN negotiation by default on client end-systems. Additionally, we dig deeper into causes of connectivity and negotiation issues linked to ECN. We find that about five websites per thousand suffer additional connection setup latency when fallback per RFC 3168 is correctly implemented; we provide a patch for Linux to properly perform this fallback. Moreover, we detect and explore a number of cases in which ECN brokenness is clearly path-dependent, i.e. on middleboxes beyond the access or content provider network. Further analysis of these cases can guide their elimination, further reducing the risk of enabling ECN by default.

url_pdf: http://ecn.ethz.ch/ecn-pam15.pdf
url_code: https://github.com/mami-project/ecn-conspiracy/tree/master/2014
---

This is the most recent academic paper describing an ongoing project. The
measurement tool developed by Damiano Boppart for this work became
[PathSpider](https://pathspider.net). The MAMI project published a 
[follow-up study](https://mami-project.eu/index.php/2016/06/13/70-of-popular-web-sites-support-ecn/) 
in June 2016, showing continued linear adoption of ECN. This paper, and the
follow-up study, were cited in Apple's WWDC announcements of client-side
default support for ECN in macOS and iOS. Measurements continue with PathSpider.
