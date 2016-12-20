+++
title = "Evolving Transport in the Internet"
authors = ["B. Trammell", "J. Hildebrand"]
publication = "In *IEEE Internet Computing*, vol. 18 no. 5, September 2014"
publication_short = "In *IEEE Internet Computing*, Sep. 2014"
date = "2014-09-01"
image = ""
image_preview = ""
math = false
selected = true

# url_code = "#"
# url_dataset = "#"
url_pdf = "http://dx.doi.org/10.1109/MIC.2014.91"
# url_project = "#"
# url_slides = "#"
# url_video = "#"

abstract = "The Internet's transport layer - the SOCK_STREAM service from TCP and the SOCK_DGRAM service from UDP - has seen little evolution over the past three decades, despite wildly changing requirements. Indeed, the movement of the waist of the protocol stack hourglass from IP up the stack toward HTTP (over TLS) over TCP has combined with a proliferation of middleboxes that make stringent assumptions about the structure of the traffic they will pass to reduce protocol diversity over time. This ossification has reduced our ability to evolve transport protocols to meet these new application requirements. In this work, the authors describe aspects of this problem and propose a solution space and agenda for improving the situation."

# [[url_custom]]
# name = "Custom Link"
# url = "http://www.example.org"

+++

This paper led to the [Substrate Protocol for User Datagrams](https://tools.ietf.org/html/draft-trammell-spud-req) and [Path Layer UDP Substrate](https://tools.ietf.org/html/draft-trammell-plus-abstract-mech) BoFs at IETF meetings in Dallas and Berlin, respectively, and the [path layer](/project/path-layer) effort in general. The initial focus on the non-evolvability of the APIs in this paper inspired work on [Post Sockets](project/post-sockets) as well.