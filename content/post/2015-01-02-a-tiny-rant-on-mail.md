---
title: A Tiny Rant on Mail
author: brian
layout: post
date: 2015-01-02T14:49:49+00:00
url: /2015/01/a-tiny-rant-on-mail/
tags:
  - Geekery
format: aside

---
Mail is broken.

This is nothing new. [RFC 822][1], after all, wasn&#8217;t the beginning of Internet e-mail, merely an attempt to fix it, which admittedly worked reasonably well for a while. But even with all the brokenness of mail, I wasn&#8217;t expecting to dig into my Postfix logs today to find that [USENIX][2] couldn&#8217;t send me mail because the [firm they&#8217;ve outsourced to][3] was too lazy to create [IN PTR][4] records for their nodes in the cloud.

More annoying than the fact that the IN PTR records aren&#8217;t there, though, is that best practice (i.e., fighting spam) dictates that they should be. Considering adding &#8220;think about fixing messaging&#8221; to the list of Futile Things To Do in 2015.

 [1]: https://www.ietf.org/rfc/rfc0822.txt
 [2]: http://www.usenix.org
 [3]: https://www.getpantheon.com/
 [4]: http://en.wikipedia.org/wiki/Reverse_DNS_lookup