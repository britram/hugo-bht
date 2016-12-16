---
title: The End of the Free Pool
author: brian
layout: post
date: 2011-02-02T08:17:50+00:00
url: /2011/02/the-end-of-the-free-pool/
categories:
  - Geekery

---
ICANN will hold a [press conference][1] in Miami on Thursday, presumably announcing the exhaustion of the IANA IPv4 [address pool][2]. This is when 102/8, 103/8, 104/8, 179/8, and 185/8 — each a block of 16 million addresses — will be handed out to the regional registries (RIRs), thereby ending the allocation of IPv4 address space at the first level of delegation.

I&#8217;m going to go ahead and predict right now that almost every journalist covering this event will get something subtle but essential wrong, and that the result will be fifteen minutes of panic followed by business as usual for everyone except those who understand the minutia of IP address allocation policy until we start seeing pressure at the lower levels of delegation.

As a disclaimer, I&#8217;m not actually one of those people who understands the minutia of IP address allocation policy, but you&#8217;re reading this on the Internet, so you&#8217;ve already proven yourself willing to believe things you read from random people who have no credibility whatsoever, and you certainly can&#8217;t do any worse with me than with the thirty-second blurb you might hear about this on your favorite cable news noisebox. So with that in mind, here&#8217;s what this actually means:

<!--more-->IP addresses are used to identify computers on a network, and are needed to route packets from one machine to another through the Internet. IP address space is allocated from the Internet Assigned Numbers Authority (IANA) to Regional Internet Registries (RIRs) in blocks. For IPv4, these are /8s, which correspond to the first number in an IPv4 address and cover about 16 million addresses. (We say, for example, that 82.1.2.3 is in 82/8.) There are five RIRs organized (roughly) on continental boundaries. ARIN covers North America, RIPE covers Europe and the Middle East, APNIC the Asia-Pacific region and Australia, LACNIC Latin America, and AfriNIC Africa. This allocation is the first level of delegation, and is the level at which we&#8217;ll run out of IPv4 addresses this week.

Each of these RIRs maintains a pool of unassigned space within the /8s it has been allocated, and assigns smaller blocks out of this space on valid request from one of its members. These are generally either large ISPs or national-level registries. This assignment is the second level of delegation.

If you get your Internet access (and therefore, your IPv4 address) from a giant ISP (say, Comcast in the US, Swisscom here) with a direct assignment, you are at the third level of delegation: your ISP either hands you a static address, which is registered (long-term) to your account, or a address out of an active pool of dynamically allocatable addresses. The latter are usually cheaper, because they allow the ISP to serve more customers with fewer addresses — you don&#8217;t need an address when your connection isn&#8217;t up.

If you get your Internet access from a smaller ISP, you are at the fourth or fifth level of delegation. Your ISP gets its addresses from a bigger ISP, which might in turn get it from a national registry, and then gives one of them to you. In any case, the exhaustion of the free pool will almost certainly not mean your ISP will take your current address away.

Until Thursday, the way things have worked is when an RIR had a sufficiently small portion of its current free /8 available for assignment, it would go to IANA to get a new one. The process was driven, bottom up, by the demand from the members, which was in turn driven by demand from their customers.

**Why isn&#8217;t the sky falling?**

The internet is not &#8220;out of space&#8221; because after the assignment Thursday, each of the RIRs will still have a fair amount of space to hand out, as will, presumably, their customers. Only the first level of delegation is completed. APNIC, for example, foresees business as usual for another six months. The RIRs will continue to make assignments out of their free pools until these get close to exhaustion, while in one way or another preferring IPv6 for new assignments.

**How do we fix the problem?**

[Move to IPv6][3], which was specified more than a decade ago to address precisely the situation we&#8217;re in today. Chances are good your computer supports IPv6. You may even be running IPv6 _right now_ without even knowing it (many of the things that &#8220;just work&#8221; on local networks of Macs over Rendezvous use IPv6, for example).

Unfortunately, the transition increases provider costs, while only serious geeks to date have been interested in paying for IPv6 connectivity, so rollout at the network level has fallen way behind. There are lots of _little_ IPv6 networks out there, but relatively few of them are connected to the IPv6 Internet. There are also still genuine open questions as to the best method for transitioning all the various applications that make up what most non-engineers think of as The Internet (that is, the bit with the cat videos and pornography) from an all IPv4-world to an IPv6 world with a long period of coexistence. This is the part I know nothing about, so I&#8217;ll stay quiet on this point. Y&#8217;all know where Wikipedia is.

More unfortunately, unless you&#8217;re a network operator or a big customer, you&#8217;re pretty much just along for the ride. Astute readers will note that, in the link above, there&#8217;s basically no advice for J. Random Cablecom Customer.

Furthermore, it should be noted that IPv4 address exhaustion affects _new_ providers of address space disproportionately. Holders of existing address assignments can continue implementing various tricks (NAT, dynamic addressing, virtualization and consolidation of applications, and so on) to stretch their existing assignments, while receivers of new addresses will get relatively few IPv4 addresses, or even only IPv6 addresses, and will have to put up with transition technologies to reach sites on the Internet that are only IPv4-reachable. This sets up an perverse incentive for large existing operators to delay IPv6 rollout, as their existing IPv4 allocations will increasingly represent a competitive advantage over new entrants.

It would be really nice if Thursday&#8217;s press conference was an announcement of something we don&#8217;t already know, say, that a bunch of legacy space holders (take a look toward the top of the list [here][2]; these are mainly big companies and military networks who got Internet addresses before anyone outside the American academic-military-industrial complex knew what the Internet was) had decided to hand back piles of IPv4 space to help address scarcity during the IPv6 transition, or, more realistically, that IANA had found some sort of magical IPv6-transition unicorn in while it was on a walk in the forest. Failing that, it&#8217;s interesting times for network operations geeks. But, as yet, the internet is not &#8220;full&#8221;.

 [1]: http://www.apnic.net/publications/news/2011/leading-global-internet-groups-make-significant-announcement-about-the-status-of-the-ipv4-address-pool
 [2]: http://www.iana.org/assignments/ipv4-address-space/ipv4-address-space.xml
 [3]: http://www.ipv6actnow.org/