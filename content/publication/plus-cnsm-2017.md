---
title: A Path Layer for the Internet - Enabling Network Operations on Encrypted Protocols
authors:
  - M. Kühlewind
  - T. Bühler
  - B. Trammell
  - R. Müntener
  - S. Neuhaus
  - G. Fairhurst
publication: In proceedings of the 2017 IEEE *Conference on Network and Service Management* Conference, Tokyo.
publication_short: In *CNSM* 2017
date: 2017-11-28
image: 
image_preview: 
math: false
selected: true
abstract_short: We propose an architectural solution to the blindness of network functions driven by increasing deployment of encryption, by introducing a new "path layer" for transport-independent, in-band signaling between Internet endpoints and network elements on the paths between them, and using this layer to reinforce the boundary between the hop-by-hop network layer and the end-to-end transport layer. We define a path layer header on top of UDP to provide a common wire image for new, encrypted transports. This path layer header provides information to a transport-independent on-path state machine that replaces stateful handling currently based on exposed header flags and fields in TCP; it enables explicit measurability of transport layer performance; and offers extensibility by sender-to-path and path-to-receiver communications for diagnostics and management.
abstract: The deployment of encrypted transport protocols imposes new challenges for network operations. Key in-network functions such as those implemented by firewalls and passive measurement devices currently rely on information exposed by the transport layer. Encryption, in addition to improving privacy, helps to address ossification of network protocols caused by middleboxes that assume certain information to be present in the clear. However, "encrypting it all" risks diminishing the utility of these middleboxes for the traffic management tasks for which they were designed. A middlebox cannot use what it cannot see. We propose an architectural solution to this issue, by introducing a new "path layer" for transport-independent, in-band signaling between Internet endpoints and network elements on the paths between them, and using this layer to reinforce the boundary between the hop-by-hop network layer and the end-to-end transport layer. We define a path layer header on top of UDP to provide a common wire image for new, encrypted transports. This path layer header provides information to a transport-independent on-path state machine that replaces stateful handling currently based on exposed header flags and fields in TCP; it enables explicit measurability of transport layer performance; and offers extensibility by sender-to-path and path-to-receiver communications for diagnostics and management. This provides not only a replacement for signals that are not available with encrypted traffic, but also allows integrity-protected, enhanced signaling under endpoint control. We present an implementation of this wire image integrated with the QUIC protocol, as well as a basic stateful middlebox built on Vector Packet Processing (VPP) provided by FD.io.

url_pdf: https://nsg.ee.ethz.ch/fileadmin/user_upload/CNSM_2017.pdf
url_slides: /pdf/cnsm17-path-layer.pdf
---
