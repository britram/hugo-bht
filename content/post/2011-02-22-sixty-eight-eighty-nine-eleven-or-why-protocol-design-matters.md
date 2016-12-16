---
title: 'Sixty-eight, eighty-nine, eleven, or: Why Protocol Design Matters'
author: brian
layout: post
date: 2011-02-22T17:49:50+00:00
url: /2011/02/sixty-eight-eighty-nine-eleven-or-why-protocol-design-matters/
categories:
  - News

---
It is not yet completely clear the extent to which the Revolutions of 2011 were run on Facebook and Twitter, but to say they have not been instrumental would, I think, be disingenuous. Like Matthew Brady&#8217;s Civil War photographs, the body counts in Vietnam, or CNN in Kuwait, from the American standpoint the social networking protocols have removed one more layer of separation between the reality of these revolutions, and those watching them. The key here is that they are also used as a primary communications medium for those taking part.

Now is perhaps not the time to point out that they&#8217;re doing it wrong.

<!--more-->One of the key differences between &#8220;Web 1.0&#8221; and &#8220;Web 2.0&#8221; has been monetization. It is basically impossible to monetize a commodity based upon an open standard, and as soon as the world figured this out in late 1999 or early 2000, the first web bubble exploded. In making sure not to make the same mistake again, a key feature of 2.0 businesses was closing these protocols off, and charging in some way for access to them. For the most part, what they charge you for access is ownership of the things you contribute to them.

The core of both the Twitter and Facebook &#8220;protocols&#8221; is a giant proprietary database (running on presumably bog-standard relational database software). In the case of Twitter, if the incidence of the Fail Whale is any indication, it is not even a particularly well-designed or -provisioned one. Sure, each of them has an &#8220;API&#8221; that allows third-party developers some small degree of freedom of interfacing to this database, but you can&#8217;t send a Twitter message (tweet) or Facebook message (post/like) without sticking a row in that database.

This non-protocolness of the protocols is a single point of epic failure. It has the following consequence for revolutionaries: they cannot be used for any activity which is not at least implicitly approved and accepted as legal by the powers in control of the jurisdictions in which those databases operate. For Facebook and Twitter, this is the United States. From this, we can at least infer that the United States is in support of the revolutions against Arab dictatorships, even against those it has supported in the past.

But before we go congratulating ourselves for inventing a machine that makes freedom, let us acknowledge its limitations, so that we are not surprised when we reach for it in the future and it&#8217;s not there, because its many masters don&#8217;t approve of the particular type of freedom we happen to be trying to make: ask [Birgitta Jonsdottir][1] how it&#8217;s working out for her. Open protocols may not be monetizable, but you pretty much have to resort to disconnecting the internet to bring them down.

 [1]: http://twitter.com/#!/birgittaj