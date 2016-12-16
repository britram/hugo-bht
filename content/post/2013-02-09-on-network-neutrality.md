---
title: On Network Neutrality
author: brian
layout: post
date: 2013-02-09T14:11:13+00:00
url: /2013/02/on-network-neutrality/
tags:
  - Geekery
  - Nonfiction
  - Switzerland

---
The National Council of Switzerland<sup>1</sup> is considering the addition of a guarantee of network neutrality into a forthcoming revision of Swiss telecommunications law. This is generally a Good Thing. We all like the Internet. This being Switzerland, we all like neutrality. So network neutrality must be great.

More seriously, the Internet has largely replaced the public switched telephone network and the postal system as the basic communications infrastructure of our society; just as with these systems, the &#8220;last mile&#8221; is a natural monopoly, so guaranteeing equal access to it is important. However, the results that legislation of network neutrality will lead to may vary widely based on how, precisely, it is defined.<!--more-->

At its most basic, &#8220;network neutrality&#8221; means the network infrastructure treats all traffic equally, and is essentially an aspect of the [end-to-end principle][1], which moves more complex and application-specific functionality to the network edge, and is one of the keys to the success of the Internet architecture both as a communications network and a platform for innovation.

Here&#8217;s where it gets complicated, though: what do we mean by &#8220;traffic&#8221;, and what do we mean by &#8220;equal&#8221;?

At the lowest level<sup>2</sup>, traffic consists of packets. One definition of network neutrality would focus on this lowest level, and demand equal treatment for all packets. Aside from small absurdities — of course the network has to treat packets differently by sending each packet to its appropriate (i.e. different) destination, otherwise the Internet would be analogous to a post office that was good for nothing but letters to Santa, and that would clearly be ridiculous — this seems to make sense until you get into the fine print.

The problem here is that traffic looks different at the packet level depending on the service it&#8217;s providing. Most video applications, for instance, send lots of packets at a more or less constant rate; packets that arrive more than a few fractions of a second late are useless,  as they represent parts of video frames or audio signal that should already have been played. On the other hand, file sharing applications don&#8217;t really care when the packets arrive, as long as they arrive eventually. Interactive traffic like web browsing falls somewhere between these extremes: users don&#8217;t notice short delays on the order of milliseconds, but will perceive longer ones on the order of seconds.

So demanding that video packets get treated the same as file sharing packets is the worst of both worlds: file sharing gets meaningless guarantees about delay, while video traffic gets capacity it can&#8217;t use. A network that can fairly allocate appropriate service to each application would be desirable. This subtlety should be appreciated by any legal definition of network neutrality.

Indeed, there is current work in network optimization, such as the IETF&#8217;s Congestion Exposure working group, which promises to increase network efficiency, performance, and fairness, that would be made impracticable by such low-level definitions of neutrality.

When providing different network service to different applications, the question becomes: what do we mean by &#8220;application&#8221;, and here is where equal access becomes important. From a technical standpoint, there is very little difference between video from provider A and video from provider B. This is not true from a business standpoint. Running a network — the business of delivering bits from point A to point B — is a very low-margin business, and network operators have an incentive to bundle higher-margin services. This is the origin of the &#8220;triple play&#8221; offers ubiquitous throughout the developed world.

Obviously, the operators also have an incentive to make sure their high-margin services — video, telephony, etc. — run better than those from other service providers. There are two ways to do this, broadly: invest in service improvement, or reduce the performance of the services of their competitors by treating the packets delivering those services differently on their network.

This is the key of the open access argument, and why network neutrality is important. If incumbent operators use the tools and techniques of network management to stifle competition, the quality of service across the entire industry suffers, new applications don&#8217;t have room to emerge, and the Internet loses its power as an engine of innovation.

In legislating network neutrality, however, there are potential pitfalls to avoid:

  * The tools and techniques used to deny fair and open access by providing different levels of service are key to the day-to-day management of networks — the difference lies in whether an application is getting priority to increase overall network performance, or whether it is purely at the expense of a competing application. Legislation that restricts the usage of these tools and techniques can increase the cost of running the network while decreasing overall performance. This would be bad.
  * Different classes of service at different price points can give an important signal to operators about which traffic is more important to its users. Consider the difference between personal videoconferencing traffic and videoconferencing for e.g. telesurgery<sup>3</sup>: it is much more important for the second to work, the cost of ensuring it works is higher, and that cost can certainly be passed on to the customer. So approaches that prohibit tiered service agreements at different price points are also likely to have undesirable side effects for future innovation.
  * The speed of innovation even in a relatively unexciting field like network management is much higher than the speed of legislation, so legislation that names _specific_ tools or technologies is not likely to be effective, as new techniques would simply be developed to work around the law.

It will be interesting to see how the debate here develops.

* * *

<small>1: for American readers, the National Council is the rough equivalent of the House of Representatives, but elected by a party-plurality list system, and without any of the built-in misfeatures that lead to it being a wretched hive of extremism, corruption, and idiocy.</small>

<small>2: the lowest level I&#8217;ll deal with in this article, anyway; my only experience on layer 1 is ripping fiber out of a convention center.</small>

<small>3: there are of course other barriers to life-critical services such as telesurgery over the open Internet, but network neutrality legislation enacted today will probably be in effect for at least half a century; I am optimistic that these barriers can be surmounted over such timescales.</small>

 [1]: http://web.mit.edu/saltzer/www/publications/endtoend/endtoend.pdf