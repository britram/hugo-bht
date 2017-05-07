---
title: What does it mean to trust the Internet?
date: 2017-05-08T08:00:00
draft: true
tags:
  - Geekery
math: false
---

Tomorrow, I'll take part in
[a panel discussion](https://www.gess.ethz.ch/news-und-veranstaltungen/sip-talk/sip-talk-1.html)
at ETH Zürich, entitled "Internet and Trust". From the flyer for the discussion:
"The Internet relies on so many layers of trust that one is sometimes surprised
that [it] actually works". This is true, but I suppose that's a property of any
system of sufficient complexity, when viewed by someone who understands it well
enough to know how much bubble gum and duct tape is used to hold it together.

<!-- more -->

Looking back on it, working to make the Internet more trustworthy has been a
theme of my career, and I suspect, the careers of many who've worked on it.
Internet measurement is largely concerned with bringing transparency to the
opaque inner workings of a massively distributed, administratively disjoint
system. And the Internet, after all, was born of a paradox of trust: in its
earliest days, it was an academic project run by people who knew mostly each
other and mostly liked each other and shared more or less the same
values<sup>1</sup>. Everyone running a node connected to the Internet could be
trusted to know what the right thing was, and to do it, in any particular
situation. This level of trust was what made it possible to scale the Internet
out in its early years - anyone could learn to play by the rules, and anyone who
could play by the rules was welcomed to.

This trust was reflected in the protocols that drove the early Internet, and to
a large extent drive them today. This is where the problems start.
Authentication and confidentiality were added up and down the stack
later<sup>2</sup>, when at all, and made optional. So many of the most basic
problems we have with trust in the Internet, from routing operations and BGP
hijacking to email and spam, derive precisely from this presumed trust among
participants in the early experiment that became the predominant global
communications network.

A fair amount of effort has gone recently into the judicious application of
cryptography between the Internet's transport and application layers, largely
centered around increased deployment (and revision) of the
[TLS](https://tlswg.github.io/tls13-spec/) protocol. This effort has accelerated
after Edward Snowden's revelations made it clear how
[pervasive](https://tools.ietf.org/html/7624) surveillance was on the Internet.
This provides some assurance that you're connected to the server you think
you're connected to, and that nobody can see or change the content of your
communications with it<sup>3</sup>, which is exactly what you need when your
threat model is an indiscriminately snooping nation-state. 

It does nothing, though, about whether you can trust that server, or the
infrastructure or the people behind it. Indeed, this cryptography can get too
tightly locked down, for example allowing an app to communicate with its
publisher without its user being able to see the contents of that exchange. In
this case the user is left with to choice but to trust the app, or not to use it
at all. This is where the question of "what does it mean to trust the Internet?"
gets interesting, and is indeed where much of the current discussion about trust
in the Internet leads, to what we in the protocol engineering community refer to
as the Political and Economic layers of the stack.

Here there are no easy answers at all. 

Confidentiality is the opposite of transparency. Confidentiality is necessary to
protect Internet communications against unauthorized third parties. On the other
hand, transparency is necessary to build trust between a first and a second
party whose interests are not necessarily aligned, which is the case of most of
the business models driving Internet content today. The questions need to be
more nuanced here: transparency of what? Confidentiality from whom? Our
protocols probably need knobs that are finer-grained than those we have in order
to find the right balance.

All of which we may or may not get into during Tuesday's talk. In any case, if
you're in Zürich, and this is at least a little interesting to you, please do
drop by at 17:30 Tuesday 9 May, ETH Main Building, room HG G60.

- - - 
1: See Richard Stallman's 
[writing](https://www.gnu.org/gnu/thegnuproject.en.html) on the birth of GNU at
the MIT AI Lab, and early ARPANET node, for a counterpoint to this utopian
oversimplification.

2: To some extent, this was born of technical inadequacy as much as it was of
wide-eyed trust. Until the end of the 20th century, the simplest asymmetric
cryptosystem remained patented, and ran slowly on computers of the time, which
limited the deployment of cryptographic protocols. In addition, even uselessly
rudimentary cryptographic technology was
[export-restricted](https://en.wikipedia.org/wiki/Export_of_cryptography_from_the_United_States#PC_era)
by the United States until about this time.

3: It does this if you trust the Web PKI, which is another question entirely. Fortunately there's a lot of work going on to make this work better as well, e.g [Certificate Transparency](https://tools.ietf.org/html/rfc6962). And it helps if you trust the routing infrastructure, too, which I won't talk about here because it's an incredible mess, held together only through the heroic efforts of the people who make it work.