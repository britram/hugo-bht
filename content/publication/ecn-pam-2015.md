+++
title = "Enabling Internet-Wide Deployment of Explicit Congestion Notification"
authors = ["B. Trammell", "M. Kühlewind", "D. Boppart", "I. Learmonth", "G. Fairhurst", "R. Scheffenegger"]
publication = "In *Passive and Active Measurement* 2015, Springer LNCS 8995."
publication_short = "In *PAM* 2015"
date = "2015-03-19"
image = ""
image_preview = ""
math = false
selected = true

abstract = "Explicit Congestion Notification (ECN) is an TCP/IP extension to signal network congestion without packet loss, which has barely seen deployment though it was standardized and implemented more than a decade ago. On-going activities in research and standardization aim to make the usage of ECN more beneficial. This measurement study provides an update on deployment status and newly assesses the marginal risk of enabling ECN negotiation by default on client end-systems. Additionally, we dig deeper into causes of connectivity and negotiation issues linked to ECN. We find that about five websites per thousand suffer additional connection setup latency when fallback per RFC 3168 is correctly implemented; we provide a patch for Linux to properly perform this fallback. Moreover, we detect and explore a number of cases in which ECN brokenness is clearly path-dependent, i.e. on middleboxes beyond the access or content provider network. Further analysis of these cases can guide their elimination, further reducing the risk of enabling ECN by default."

# url_code = "#"
# url_dataset = "#"
url_pdf = "http://ecn.ethz.ch/ecn-pam15.pdf"
# url_slides = "#"
# url_video = "#"


+++

ednote: Link to followup. Link to WWDC talk about the followup. Link to Pathspider. 
