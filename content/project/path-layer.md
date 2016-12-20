---
date: 2016-07-20
title: The Path Layer
summary: Making the Internet architecture's implicit path layer explicit.

image_preview: path-layer.png

image: path-layer.png

tags:
  - architecture

math: false
---

For the current state of this work, read the following Internet-drafts:

- [draft-hardie-path-signals](https://tools.ietf.org/html/draft-hardie-path-signals)
- [draft-trammell-plus-statefulness](https://tools.ietf.org/html/draft-trammell-plus-statefulness)
- [draft-trammell-plus-abstract-mech](https://tools.ietf.org/html/draft-trammell-plus-abstract-mech)

Starting with a simple question about [evolving the transport stack](/publication/udp35-ieee-2014/), 
leading to half of the scope of the 
[Measurement and Architecture for a Middleboxed Internet](https://mami-project.eu/) Horizon 2020 research project,
we have come to realize that the simplified four-layer Internet stack model is
missing an implicit layer. The network layer was designed for stateless, hop-
by-hop functions between hosts, and the transport layer for stateful, end-to-
end functions between processes. The rise of NAT and various other network
functions based on packet inspection and manipulation have blurred the line
between them. One can argue that NAT alone has moved port numbers into the
network layer header, for instance.

The accelerated deployment of encryption in the wake of the Snowden
revelations, and the creation of fully-encrypted transport protocols
encapsulated within UDP
([QUIC](https://tools.ietf.org/html/draft-ietf-quic-protocol) being the most
significant current example) gives us an opportunity to make this path layer
explicit. In this vision, the network layer returns to its original intent,
the end-to-end nature of the transport layer is enforced by end-to-end
encryption, and the transport layer explicitly exposes a *wire image* (through
a UDP encapsulation, necessary for NAT traversal) for use by devices on path
(e.g. for signaling sender intent and traffic characteristics, exposing
diagnostic information lost in encrypted transports, etc.). Each transport may
expose different information in its wire image, according to its requirements,
but defining a small set of common transport-independent wire images would
significantly ease deployment of future transport protocols.

Current work on the path layer is focused on 
[defining these wire images](https://github.com/mami-project/draft-kt-plus-protocol), 
and experimental implementations thereof.
