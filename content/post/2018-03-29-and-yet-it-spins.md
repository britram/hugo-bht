---
title: And yet, it spins
date: 2018-03-29T09:00:00
draft: false
tags:
  - Geekery
math: false
---

I'm writing today from Berlin, after an excellent [Passive and Active
Measurement](https://pam2018.inet.berlin) conference and a very long but
fruitful week in London for [IETF
101](https://www.ietf.org/how/meetings/past/101/), which, for me, came to be
dominated by the [The Spin
Bit](https://datatracker.ietf.org/doc/draft-trammell-quic-spin).

The spin bit is an explicit signal for passive measurability of round-trip
time, currently [possible](/publication/qof-tma-2014/) in TCP but not in QUIC
due to lack of acknowlegment and timestamp information in the clear. It's an
example of a facility designed to fulfill the principles for measurement as a
first class function of the network stack we laid out in [an
article](/publication/ipim-ccr-2017/) published last year. I won't go into the
details of how it works or why it matters here; read the draft or [watch the
presentation](https://www.youtube.com/watch?v=TQq6Z4_HBaY&feature=youtu.be&t=1276)
for that. 

![the spin bit](/img/spinbit.png)

It's taken about a year of discussion and research to refine the proposal to
add this facility to the
[QUIC](https://datatracker.ietf.org/doc/draft-ietf-quic-transport) protocol,
and we're still not done: agreed in London was the reservation of three bits
for experimentation with passive RTT measurement, with the result of this
experimentation to inform an eventual working group decision to include the
bit in the "shipping" version 1 of the protocol, scheduled to be complete by
November 2018. 

On this point, Geoff Huston [writes](http://www.potaroo.net/ispcol/2018-03/onebit.html):

> A cynical view would see the IETF as being incapable of holding the line that the end-to-end control state should be completely withheld from the network, and this spin bit is just one more step along an inexorable path of compromise that once more ends up gratuitously exposing user’s actions to the network. There is probably a less cynical view as well, but I just can't think what it may be!

This article attempts to present one such less cynical view.

## Wire Images of Network Protocols

Those of us who work with Internet infrastructure have had decades to get used
to the idea that what you see in a protocol's headers, on the wire, is what
you get. IP and TCP, as Geoff points out, expose all the
information required by their operation to any observer along the path, which
can leak sensitive, user-linked metadata. TCP options and timestamp rate
drift, for example, can be used as part of relatively unique device
fingerprints.

The creation of transport protocols like QUIC, which encrypts its headers,
splits the *wire image* of the protocol -- what it looks like on the wire --
and the information used by the protocol in its own operation. This is new,
and provides us as protocol engineers an opportunity to design the protocol's
wire image to expose exactly what we want the wire to see. See [the
Internet-Draft](https://datatracker.ietf.org/doc/draft-trammell-wire-image)
for more on wire images.

## Explicit signaling for better efficiency and privacy

The spin bit, as designed, leverages an engineered wire image to get a large
win -- passive latency measurement on a per-flow basis at one sample per RTT,
which can be used to drive a large variety of measurement tasks on an Internet
connected network without the overhead or uncertainty of active measurement
methods -- for minimal overhead -- three bits per packet that would be wasted
anyway, and a trivial amount of additional code in each QUIC endpoint that
doesn't even need access to internal, encrypted protocol state to operate. As
to the safety of round-trip time information, well, that's why I'm in Berlin,
to present [our paper on the
subject](/publication/rttpriv-pam-2018/) at PAM
2018. The summary findings: Internet RTT is not useful for locating endpoints
that have known IP addresses or inferring endpoint activity, as the
per-hop variance and error compounds very quickly.

In summary, it's a low-risk, high-utility way to continue to support passive
RTT measurement in a world in which TCP is displaced by QUIC -- the world
we'll be in in a few years, if QUIC is as successful as we hope.

## A spinning slope?

Is it "one more step along an inexorable path of compromise"? Normally I share Geoff's cynicism on most things networking, but that sounds a
little nihilistic, even to me<sup>(1)</sup>.

The truly useful, transport-independent signals that one can place in an
engineered wire image are quite limited. RTT is one of them, since it is
a property largely determined by the network, and the spin bit is a very good
signal for RTT measurement. 

We might want to revisit a "clear path state" signal, replacing TCP FIN/ACK,
as we discuss in the [paper](/publication/plus-cnsm-2017/) that sums up our
findings from our work on the PLUS proposal. This seems especially useful for
long-lived connections where either side, not just the initiator, may want to
resume sending after a delay -- 0RTT resumption will perform well when it's
always the client resuming, but does nothing for two-way application
protocols.

Beyond that, though, we may well be done. Arrival information as we proposed
in the [principles](/publication/ipim-ccr-2017/) paper would be nice to have
for end-to-end loss measurement, but we're still working to find mechanisms
that have acceptable overhead/utility tradeoffs for arrival information and
loss/reordering metrics. In any case, the spin bit itself can be used for loss
measurement between two vantage points. Measurement techniques that get deeper
into the operation of the transport protocol, replacing retransmission
detection as in TCP, are very brittle, and don't give actionable data, and I
don't really see the point.

So I can't share the cynical view here: if it's an inexorable path of
compromise, it's a very, very short one. 

- - - 

<sup>(1)</sup> Indeed, I've been [accused of
nihilism](https://youtu.be/TQq6Z4_HBaY?t=5833) -- live, on video, on this very
subject, last week.