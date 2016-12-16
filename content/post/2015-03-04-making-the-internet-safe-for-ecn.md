---
title: Making the Internet Safe for ECN
author: brian
layout: post
date: 2015-03-04T20:21:03+00:00
url: /2015/03/making-the-internet-safe-for-ecn/
tags:
  - Uncategorized

---
I&#8217;m off to New York in a couple of weeks to present a [paper][1] at PAM (which I mentioned [here][2], though sadly the flashy automated demo I was hoping to build was a bit optimistic). The question: &#8220;is it safe to turn on [ECN][3] on client machines by default, completing the end to end deployment of a simple fifteen year old protocol to give us a better way to signal network congestion than simply dropping packets on the floor?&#8221; The answer is: &#8220;define safe.&#8221; Our key findings:<!--more-->

  1. More than half of the Alexa top million web servers (600k accounting for duplicate IPs) will happily negotiate and mark ECT0 if you ask nicely (at least as of September 2014). This mainly reflects people upgrading Linux servers to kernels where tcp_ecn=2 is the default, and strongly validates changing default configurations as a method for increasing ECN deployment.
  2. 0.42% of these webservers will fail to connect if you try to negotiate ECN, but simple ECN fallback as in RFC 3168 (retransmitted SYN ECE CWR sent as SYN) commutes this to a risk of slightly increased handshake latency.
  3. A vanishingly small number (15 / ~600k) of these have _different_ ECN connectivity dependency depending on where you connect from, indicating that the box breaking ECN is not directly adjacent to the server. A third of these (6) are GoDaddy parking sites.
  4. There is more mangling of the ECN IP header bits than connectivity dependency, and successful negotiation does not always mean successful marking. About 2% of IPv4 servers and 15% (!!!) of IPv6 servers signal in other than expected ways, indicating that negotiated ECN might not be useful.
  5. We appear to have seen two (count &#8217;em, two!) CE markings in the wild, both from the same webserver (www.grandlyon.com) when probing 600k IP addresses 3 times from 3 different locations (i.e., 2 out of 5.6 million flows). This is neither encouraging nor surprising.

Bottom line, the risk to connectivity of turning ECN on by default in clients is vanishingly low, though not yet in the one in ten million range, when simple fallback as in RFC3168 is implemented. Modern Windows and Mac OS X do this; Linux doesn&#8217;t yet, though we have a three line patch (which, anecdotally, I&#8217;ve been running without incident on my desktop at the office for the past half year).

Given the signaling anomalies, especially on IPv6, defining simple methods to detect and dynamically ignore anomalous signaling at the endpoints is probably the next area of work to getting ECN deployable.

So now I know what I&#8217;m doing with the _rest_ of my copious free time&#8230;

&nbsp;

 [1]: http://ecn.ethz.ch/ecn-pam15.pdf
 [2]: /2015/01/on-repeatable-internet-measurement-interlude
 [3]: http://en.wikipedia.org/wiki/Explicit_Congestion_Notification