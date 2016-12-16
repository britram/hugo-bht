---
title: 'On Repeatable Internet Measurement: Interlude'
author: brian
layout: post
date: 2015-01-02T15:44:04+00:00
url: /2015/01/on-repeatable-internet-measurement-interlude/
categories:
  - Geekery
  - Science

---
[Part one][1] of this post painted a somewhat bleak picture of the state of Internet measurement as a science. The dreariness will continue later this month in [part two][2]. And yet there seems to be quite a lot of measuring the Internet going on. It can&#8217;t all be _that_ bad, can it?

<!--more-->

Well, no.

[CAIDA][3] has been beating this drum _far_ longer than I have, makes a great deal of raw data available, and has set up a [clearinghouse][4] for others to report metadata about data everyone can use, thereby solving the problem of not knowing what&#8217;s available or where, but not doing much for the underlying problems of incentives.

And there are a few measurement infrastructures out there based on software that works and data everyone can use. The &#8220;everyone can use&#8221; part is much easier to achieve if one limits oneself to a relatively restricted set of active measurements. [RIPE Atlas][5], run by the RIPE NCC, is a shining example of how to do this right: a network of lightweight hardware probes, on a common software base, centrally managed, [globally distributed][6] free of charge, running on a diverse-if-Eurocentric set of network connections donated by probe hosts. The measurements these probes can perform are selected in part to be those whose results are freely publishable, because they expose nothing personally identifiable or privacy sensitive. This does limit the types of measurements that can be done, but the risk-utility tradeoff has a wider sweet spot in active measurement.

The most recent [paper][7] we&#8217;ve published, &#8220;Enabling Internet-Wide Deployment of Explicit Congestion Notification&#8221;, is also based on active measurements, and we&#8217;ve tried our best to walk the walk. The analysis uses the open-source QoF flow meter and the ECN-Spider tool,  both developed with a focus on usability and stability. Data collected during the study is available in raw CSV files, along with the [IPython][8] [notebooks][9] used to run the analysis: anyone can check our work on our data. By the time we present the paper at the Passive and Active Measurement Conference<sup>1</sup> next March, we hope to have enough tooling that we can rerun the measurement and analysis with a single invocation of a script hosted on a virtual machine somewhere.

This may be a way forward, in fact: for many types of active measurement research, it is probably more appropriate to publish the measurement as running code than as an academic paper. This brings with it the obligation to keep the code running for as long as the measurement is relevant, which is indeed a lot more work, but with the reward that the results are accessible, verifiable, and easier to build on.

Watch this space.

* * *

[1]: We note happily that PAM does its part for data availability by only giving the best paper award to those papers which make their data available.

 [1]: https://trammell.ch/2014/12/on-repeatable-internet-measurement-part-one/
 [2]: https://trammell.ch/2015/01/on-repeatable-internet-measurement-part-two
 [3]: http://www.caida.org
 [4]: http://imdc.datcat.org/
 [5]: http://atlas.ripe.net
 [6]: https://labs.ripe.net/Members/emileaben/distribution-of-ripe-atlas-probes
 [7]: http://ecn.ethz.ch/ecn-pam15.pdf
 [8]: http://www.ipython.org
 [9]: http://nbviewer.ipython.org/url/ecn.ethz.ch/data/pam15-csv-analysis.ipynb