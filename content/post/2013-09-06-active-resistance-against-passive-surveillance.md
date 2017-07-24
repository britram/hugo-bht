---
title: Active Resistance against Passive Surveillance
author: brian

date: 2013-09-06T12:24:44+00:00
url: /2013/09/active-resistance-against-passive-surveillance/
tags:
  - Geekery
  - News
  - Nonfiction

---
So I [complain][1] about a lull in the news about the more-or-less [complete compromise of the Internet][2] by the National Security Agency _et al_, and then [this][3] goes and happens.

One of my old standard interview questions for people applying for jobs with some responsibility for information security was &#8220;are you paranoid&#8221;? When the lighting was good, and my eyes bugged out just right, this could be a little scary. It&#8217;s time to retire this question, I think, because the answer would seem to be &#8220;no, I am clearly not paranoid enough&#8221;, unless the applicant shows up to the interview in a [tin-foil hat][4].

<!--more-->Okay, I wouldn&#8217;t be 

_too_ alarmist about it: the theoretical underpinnings of public-key cryptography are probably secure, so some implementations of some protocols using some ciphers are probably still trustworthy. And there is nothing new to the revelation that the NSA spends ridiculous amounts of money every year trying to break cryptosystems both in theory and in practice: this is, after all, exactly what the NSA was chartered to do. But there is now a great deal of public uncertainty about which communications channels are safe. Add to this the fact that the NSA has an asymmetric ability to compromise physical infrastructure on American soil and/or owned by entities subject to American jurisdiction, and the United States just became a _much_ less attractive place to do any kind of business which involves (1) any communications network and (2) any sort of secrecy whatsoever (i.e., most kinds of business). This effect will not be immediate. But I fear it will be prove to be devastating.

As for Schneier&#8217;s [call][2] to make the upcoming IETF meeting in Vancouver about engineering resistance to pervasive surveillance into the Internet, well, [I&#8217;m doing my part][5]. The outcome of this work will probably be an exploration of exactly what information radiates off IETF protocols, leading to recommendations to protocol designers to:

  1. **Use transport-layer security everywhere**. We&#8217;ve been [moving in this direction][6] for quite some time. There are [serious problems][7] with the certificate authority system — stemming in large part from the decision to include support for the CA business model in the design requirements – which current work in [DANE][8] is attempting to address.
  2. **Use end-to-end security** for protocols which use multiple hops at the application layer. SMTP is the big one here, and here we have a problem:  S/MIME and PGP are concerned with protecting message payload, leaving headers (addresses, subjects, etc.) unprotected. Addresses need to be left in plaintext to route messages to their destination, so for electronic mail, anyway, there are design changes that need to be made.
  3. **Resist protocol fingerprinting** by adding randomness to metadata everywhere we can: to interpacket times (as in the [SSH timing hack][9]), packet and flow sizes (as used, e.g., by the [snack][10] Skype detector). There&#8217;s lots of work to do here.
  4. Add **indirection** to the network where possible to make it difficult to associate network addresses with physical locations, organizations, or individuals. [Tor][11] does this, but has the problem of directing all anonymized traffic through a set of exit nodes, which represent [tempting targets][12] for state security services. So there&#8217;s probably lots of work to do here, too.
  5. Design for **end-to-end [So I [complain][1] about a lull in the news about the more-or-less [complete compromise of the Internet][2] by the National Security Agency _et al_, and then [this][3] goes and happens.

One of my old standard interview questions for people applying for jobs with some responsibility for information security was &#8220;are you paranoid&#8221;? When the lighting was good, and my eyes bugged out just right, this could be a little scary. It&#8217;s time to retire this question, I think, because the answer would seem to be &#8220;no, I am clearly not paranoid enough&#8221;, unless the applicant shows up to the interview in a [tin-foil hat][4].

<!--more-->Okay, I wouldn&#8217;t be 

_too_ alarmist about it: the theoretical underpinnings of public-key cryptography are probably secure, so some implementations of some protocols using some ciphers are probably still trustworthy. And there is nothing new to the revelation that the NSA spends ridiculous amounts of money every year trying to break cryptosystems both in theory and in practice: this is, after all, exactly what the NSA was chartered to do. But there is now a great deal of public uncertainty about which communications channels are safe. Add to this the fact that the NSA has an asymmetric ability to compromise physical infrastructure on American soil and/or owned by entities subject to American jurisdiction, and the United States just became a _much_ less attractive place to do any kind of business which involves (1) any communications network and (2) any sort of secrecy whatsoever (i.e., most kinds of business). This effect will not be immediate. But I fear it will be prove to be devastating.

As for Schneier&#8217;s [call][2] to make the upcoming IETF meeting in Vancouver about engineering resistance to pervasive surveillance into the Internet, well, [I&#8217;m doing my part][5]. The outcome of this work will probably be an exploration of exactly what information radiates off IETF protocols, leading to recommendations to protocol designers to:

  1. **Use transport-layer security everywhere**. We&#8217;ve been [moving in this direction][6] for quite some time. There are [serious problems][7] with the certificate authority system — stemming in large part from the decision to include support for the CA business model in the design requirements – which current work in [DANE][8] is attempting to address.
  2. **Use end-to-end security** for protocols which use multiple hops at the application layer. SMTP is the big one here, and here we have a problem:  S/MIME and PGP are concerned with protecting message payload, leaving headers (addresses, subjects, etc.) unprotected. Addresses need to be left in plaintext to route messages to their destination, so for electronic mail, anyway, there are design changes that need to be made.
  3. **Resist protocol fingerprinting** by adding randomness to metadata everywhere we can: to interpacket times (as in the [SSH timing hack][9]), packet and flow sizes (as used, e.g., by the [snack][10] Skype detector). There&#8217;s lots of work to do here.
  4. Add **indirection** to the network where possible to make it difficult to associate network addresses with physical locations, organizations, or individuals. [Tor][11] does this, but has the problem of directing all anonymized traffic through a set of exit nodes, which represent [tempting targets][12] for state security services. So there&#8217;s probably lots of work to do here, too.
  5. Design for **end-to-end][13]** as opposed to [closed services][14]. The IETF does this reflexively anyway, but I think we have an opportunity here to advocate publicly for an end-to-end Internet, as an effort such as [PRISM][15] would be rather pointless if most communications among people, by volume, hadn&#8217;t already moved to single points of failure.

Working to change the Internet to actively resist an adversary intent on widespread, pervasive surveillance will be hard work. It will involve tradeoffs for latency and bandwidth. It will make life easier for those who wish to stay hidden from authority, and will make the job of those authorities – even those with a legitimate interest in protecting the security of their citizens – more difficult. But if the Internet is to continue to form the basis of a trustworthy global communications network, it is necessary.

 [1]: http://www.trammell.ch/2013/08/the-freedom-panopticon/
 [2]: http://www.theguardian.com/commentisfree/2013/sep/05/government-betrayed-internet-nsa-spying
 [3]: http://www.nytimes.com/2013/09/06/us/nsa-foils-much-internet-encryption.html?hp
 [4]: http://en.wikipedia.org/wiki/Tin_foil_hat
 [5]: http://tools.ietf.org/html/draft-trammell-perpass-ppa
 [6]: https://www.eff.org/https-everywhere
 [7]: http://en.wikipedia.org/wiki/DigiNotar#Issuance_of_fraudulent_certificates
 [8]: http://en.wikipedia.org/wiki/DNS-based_Authentication_of_Named_Entities
 [9]: http://www.cs.jhu.edu/~rubin/courses/fall03/papers/timing.ssh.pdf
 [10]: http://link.springer.com/chapter/10.1007%2F978-3-642-20305-3_7
 [11]: https://www.torproject.org
 [12]: http://raided4tor.cryto.net
 [13]: http://www.trammell.ch/2012/10/talk-the-open-internet-under-threat/#more-482
 [14]: http://www.trammell.ch/2011/02/sixty-eight-eighty-nine-eleven-or-why-protocol-design-matters/
 [15]: http://en.wikipedia.org/wiki/PRISM_(surveillance_program)