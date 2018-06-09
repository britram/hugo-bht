---
title: On blind reviewing
date: 2018-06-06T08:00:00
draft: false
tags:
  - Geekery
math: false
---

Two high-profile network communications conferences -- the ACM Internet
Measurement Conference (IMC)<sup>(1)</sup> and ACM CoNEXT -- recently
announced that they are moving from single-blind reviewing (with an anonymous
TPC reviewing papers by known authors) to double-blind reviewing (where both
reviewers and authors are anonymous) relatively late in the submission cycle.
Indeed, IMC reversed its decision, presumably because the switch just days
before the submission deadline was too disruptive to papers in progress, but I expect IMC to be double-blind in 2019.

These decisions have generally been met with positive feedback, at least in
public. Indeed, double-blind reviewing is preferable to single-blind
reviewing, as the fundamental problem with single-blind reviewing is the
imbalance of power that comes from the reviewer having asymmetric information.
Double-blind reviewing restores this balance, removing the identity of the
author from the set of things a reviewer can base a decision on, consciously
or not<sup>(2)</sup>. But this balance comes at a price.

One particularly nasty piece of collateral damage done by a move to
double-blind reviewing is that of supporting artifacts. Though I might be in
the minority here, I expect any good paper on Internet science to provide
links to source code and preprocessed or raw data, or at least an apology and
decent explanation as to why these are not given. We pointed out in a
paper<sup>(3)</sup> last year that self-hosted artifacts and code can be used
to de-anonymize reviewers (through access logs on URLs published only in a
submission, for example), but they are even more effective in de-anonymizing
authors. Moving IMC and CoNext to a double-blind model without also providing
some system for non-self-hosted code and other artifacts disadvantages those
authors who go to the extra effort to make their work reusable and
reproducible, which seems to me to be unambiguously bad for science.

Double-blinding as a technique to remove bias also presumes that removing the
authors' names and any identifying information about the subject of the paper
can effectively anonymize those authors, and that is easier to do in fields
that are less crowded or more specialized than computer network communications
and Internet measurement. Especially in the latter, a specialist researcher up
to date on the current themes of the few dozen groups currently active in core
infrastructure measurement will find it hard not to draw conclusions about the
authorship of even well-anonymized work.

There's another way to fix the imbalance, of course: move to open reviewing,
that is, signed reviews published along with the paper. The main argument
behind single-blind reviews is that reviewers will be less likely to provide
honest criticism if their names are known, particularly if the reviewer is
junior and fears reprisal in future publication or job search efforts. Humans
will be humans, of course, but using anonymity as a way to avoid feuds better
suited to kindergarten playgrounds seems to me to ask *extremely* little
of ourselves as a profession. 

Anonymous reviews, whether single- or double-blind, have the effect of not
disincentivizing laziness. When the only people who will see your review are
the authors, who need your approval to publish, and some subset of the program
committee, there is little reputational danger to being less than thorough.
Couple this with minimal rewards for thorough and thoughtful reviews, and the
quality of reviews from all but the highest tier of venues in computer science
is self-explanatory.

- - - 

<sup>(1)</sup>: full disclosure: I am an IMC program committee member in 2018.

<sup>(2)</sup>: There's research (e.g., in [CACM this month](https://cacm.acm.org/magazines/2018/6/228027-effectiveness-of-anonymization-in-double-blind-review/fulltext)) showing that anonymization of authors can be effective in reducing bias.

<sup>(3)</sip>: *cite Bajpai et al here*