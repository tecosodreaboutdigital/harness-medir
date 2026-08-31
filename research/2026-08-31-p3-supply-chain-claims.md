# Research: five supply-chain-security claims in harness-p3.html

Gathered 31 August 2026, against the method in `.claude/skills/research`. Scope: the
five specific, checkable claims in part 3's "A third-party skill is third-party code"
section (`harness-p3.html`, `#en-supply-chain` and equivalents), all currently
uncited (no `<a class="src">` link, no `harness-sources.html` entry). Exact source
paragraph, English version:

> "The most instructive case, widely reported in the industry, is postmark-mcp, the
> first malicious MCP server caught in real use. Its author published fifteen clean,
> functioning versions first, building a genuine track record of legitimacy, before
> quietly adding a single line of exfiltration code in a later release. [...] It was
> not an isolated case, per industry reports not all independently confirmed: Antiy
> CERT catalogued a campaign of 1,184 malicious skills in February 2026, under the
> name ClawHavoc; Snyk's scan the same month found more than 280 skills leaking API
> keys and personal data; an independent audit of over 7,000 MCP servers found 36.7
> percent potentially vulnerable to server-side request forgery, with a proof of
> concept that recovered live cloud access keys; and a February 2026 count found more
> than 135,000 publicly exposed instances running insecure default configuration."

**Headline finding, before the five items below.** All five claims are real, not
fabricated, and the numbers are close to accurate. But the "not an isolated case"
framing implies four independent proofs from different corners of the ecosystem.
It is not that. Three of the four follow-on items — ClawHavoc, the Snyk scan, and the
135,000 count — are three different vendors reporting on facets of **the same event**:
a two-week security crisis in early February 2026 around one specific product,
**OpenClaw** (an open-source, self-hosted AI-agent framework, formerly named Clawdbot
then Moltbot) and its skill marketplace **ClawHub**. Only the fourth item (BlueRock's
MCP server audit) is a genuinely separate data point, and only postmark-mcp (item 1)
is unrelated to OpenClaw entirely. The current text never names OpenClaw or ClawHub,
which lets a reader infer these are four scattered incidents across the general
agent-skill/MCP ecosystem rather than one dominant news event plus two others.

---

## 1. postmark-mcp — first malicious MCP server caught in real use

**Claim.** postmark-mcp was the first malicious MCP server caught in real use; its
author published fifteen clean versions before quietly adding one line of
exfiltration code in a later release.

**Search process.** WebSearch for "postmark-mcp malicious npm package exfiltration"
and "'postmark-mcp' backdoor first malicious MCP server"; WebFetch on the original
discoverer's writeup and Postmark's own statement.

**What I found.** Confirmed in detail and from the vendor itself. Postmark's own blog
states the "postmark-mcp" npm package was not developed or authorized by Postmark —
"We didn't develop, authorize, or have any involvement with the 'postmark-mcp' npm
package" — and that a malicious actor impersonated the brand to steal email data.
Koi Security, whose risk engine caught the change, published the technical writeup:
versions 1.0.0 through 1.0.15 (fifteen versions) behaved identically to the
legitimate connector; version 1.0.16, released quietly, added roughly one line of
code (line 231) that BCC'd every email sent through the server to
`phan@giftshop[.]club`. Koi's own words: "For 15 versions — FIFTEEN — the tool worked
flawlessly," then "One single line. And boom." The Hacker News, CSO Online, Qualys
ThreatPROTECT, Dark Reading, BleepingComputer and Snyk all independently ran the
story under headlines calling it the first malicious MCP server found in the wild.
Discovered/published late September 2025 (Koi Security: 25 Sept 2025), not
"February 2026" — this incident predates the other four by months and is otherwise
unrelated to them.

**Verdict: FOUND. High confidence.** Every specific number in the harness sentence
(fifteen clean versions, one line of code, "first malicious MCP server") matches the
primary/near-primary record closely.

**Best URLs:**
- Postmark's own statement (vendor confirmation the package was fraudulent): https://postmarkapp.com/blog/information-regarding-malicious-postmark-mcp-package
- Koi Security (discoverer, technical detail on the 15-versions/1-line pattern): https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft
- The Hacker News (widely-cited "first malicious MCP server" framing): https://thehackernews.com/2025/09/first-malicious-mcp-server-found.html
- Snyk's own writeup: https://snyk.io/blog/malicious-mcp-server-on-npm-postmark-mcp-harvests-emails/
- CSO Online: https://www.csoonline.com/article/4064009/trust-in-mcp-takes-first-in-the-wild-hit-via-squatted-postmark-connector.html

**Recommendation.** Add as a real `harness-sources.html` entry (cite Koi Security as
discoverer, Postmark's own post as the "not us" confirmation). No number needs
softening.

---

## 2. Antiy CERT / "ClawHavoc," 1,184 malicious skills, February 2026

**Claim.** Antiy CERT catalogued a campaign of 1,184 malicious skills in February
2026, under the name ClawHavoc.

**Search process.** WebSearch "Antiy CERT ClawHavoc malicious AI agent skills";
WebFetch on Antiy's own report page and cybersecuritynews.com's coverage; cross-check
against the OWASP Agentic Skills Top 10 project page (AST01), which the brief asked
me to check directly.

**What I found.** Real campaign, real count, real Antiy report — but the attribution
in the harness sentence is not quite right. Antiy Labs did publish a report titled
"ClawHavoc: Analysis of Large-Scale Poisoning Campaign Targeting the OpenClaw Skill
Market for AI Agents," and it does classify the malware family (TrojanOpenClaw
PolySkill) and count at least 1,184 malicious skill packages. But Antiy's own report,
and the independent secondary coverage, both say the campaign was **discovered and
named "ClawHavoc" by Koi Security** on 1 February 2026 — Antiy CERT's role was a
follow-on technical analysis under the name Koi Security had already coined, not the
original discovery or naming. Quote from cybersecuritynews.com: "The campaign was
initially disclosed by Koi Security on February 1, 2026, which 'named it
"ClawHavoc."' Antiy CERT provided subsequent analysis... but did not discover the
campaign itself." The OWASP AST01 page also cites this incident (1,184 malicious
skills, 12 publisher accounts, shared C2 IP), sourced to Antiy CERT, but dates it
"Jan 2026" rather than February — a minor date discrepancy against the Feb 1
discovery date most other sources give (plausibly campaign activity started in
January, disclosure in February). The one publisher-account detail is solid: one
account alone (`hightower6eu`) uploaded 677 of the 1,184 packages.

Separately, and importantly: this campaign specifically poisoned **ClawHub**, the
official skill marketplace for **OpenClaw**, a specific open-source AI-agent
framework — not "AI agent skills" as a category in general. The harness sentence
never names the product, which lets the claim read as broader than it is.

**Verdict: PARTIALLY FOUND. Medium-high confidence on the number, low confidence on
the attribution as written.** 1,184 and "February 2026" hold up; "Antiy CERT... under
the name ClawHavoc" implies Antiy coined the name, and it did not — Koi Security did.

**Best URLs:**
- Antiy Labs report (the "Antiy CERT" primary source itself): https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/
- cybersecuritynews.com (clearest statement of the Koi-Security-discovered-and-named / Antiy-analyzed split): https://cybersecuritynews.com/clawhavoc-poisoned-openclaws-clawhub/
- OWASP Agentic Skills Top 10, AST01 (cites Antiy CERT, dates it Jan 2026): https://owasp.org/www-project-agentic-skills-top-10/ast01

**Recommendation.** Fix the attribution before citing: either credit Koi Security as
discoverer/namer with Antiy CERT as independent technical analysis, or drop "under
the name ClawHavoc" and just say "a campaign Antiy CERT catalogued at 1,184 malicious
skills." Consider naming OpenClaw/ClawHub explicitly (it is a real, well-known,
already-public product — this is not a confidentiality problem) so the claim's actual
scope is honest.

---

## 3. Snyk scan, 280+ skills leaking API keys and personal data, same month

**Claim.** Snyk's scan the same month (February 2026) found more than 280 skills
leaking API keys and personal data.

**Search process.** WebSearch "Snyk AI agent skills API key leak scan 2026"; WebFetch
on Snyk's own post.

**What I found.** Confirmed closely at the primary source. Snyk's blog post "280+
Leaky Skills: How OpenClaw & ClawHub Are Exposing API Keys and PII," published 5
February 2026 (announced 3 Feb), states Snyk scanned the full ClawHub registry
(3,984 skills at the time) and found 283 skills — about 7.1% of the registry —
instructing agents to mishandle secrets, forcing API keys, passwords, and even credit
card numbers through the model's context window and output logs in plaintext. The
post explicitly covers PII (its `buy-anything` example skill collects name, address,
city, state, zip, email, phone, and credit-card details), so "personal data" in the
harness sentence is accurate, not an embellishment. Note this is a different Snyk
report from the "ToxicSkills" study the OWASP AST01 page cites (which reports a
different, larger vulnerability-rate figure, 36.82%/1,467 skills, for a different
security-flaw category, prompt injection) — the two are easy to conflate but the
280+/API-keys claim maps cleanly onto this specific post.

Same scope caveat as item 2: this is Snyk scanning the ClawHub/OpenClaw ecosystem
specifically, not agent skills in general.

**Verdict: FOUND. High confidence.** 283 (">280") skills, API keys plus personal
data, published February 2026 — all confirmed at Snyk's own blog.

**Best URL:**
- Snyk, "280+ Leaky Skills: How OpenClaw & ClawHub Are Exposing API Keys and PII" (5 Feb 2026): https://snyk.io/blog/openclaw-skills-credential-leaks-research/

**Recommendation.** Add as a real, linked `harness-sources.html` entry. No number
needs softening. Optionally name OpenClaw/ClawHub for accuracy, same as item 2.

---

## 4. Independent audit of 7,000+ MCP servers, 36.7% potentially vulnerable to SSRF, PoC recovered live cloud access keys

**Claim.** An independent audit of over 7,000 MCP servers found 36.7 percent
potentially vulnerable to server-side request forgery, with a proof of concept that
recovered live cloud access keys.

**Search process.** WebSearch "BlueRock audit 7000 MCP servers SSRF vulnerable" (per
the project's own `sources/inventory.md`, which already names BlueRock for this
claim); WebFetch on BlueRock's own post and on `mcp-trust.com`, BlueRock's public MCP
security registry.

**What I found.** The exact figure is real and traceable to BlueRock's own blog post,
"MCP fURI: SSRF Vulnerability in Microsoft Markitdown MCP." Verbatim quote: "Based on
our analysis of over 7,000 MCP servers, over 36.7% have potential exposed SSRF
vulnerabilities." That post's proof of concept is real and specific, not
hypothetical narration: BlueRock researcher David Onwukwe demonstrated an SSRF
against Microsoft's MarkItDown MCP server (an unrelated, real, popular MCP server,
85k GitHub stars) that fed it the AWS EC2 instance-metadata address
(`http://169.254.169.254/latest/meta-data/iam/security-credentials`) and, in two
requests, recovered a working AWS access key, secret key, and session token from the
instance role. This matches "proof of concept that recovered live cloud access keys"
well — it is a live, working credential recovered from a real EC2 instance in a
controlled disclosure test, the standard form such a PoC takes (not an attack on a
third party's production environment). Microsoft and AWS were notified and responded
that mitigations exist. Discovery: November 2025; public disclosure via Dark Reading
in January 2026.

Two things temper confidence rather than break it. First, "independent audit" is
generous: BlueRock is a security vendor that sells an "MCP Trust Registry" and a
"Secure MCP Server" product, so this is vendor-published research with a commercial
angle, not audit by a disinterested third party — common and legitimate in security
research, but not "independent" in the strict sense. Second, BlueRock's own public
registry site (`mcp-trust.com`) currently states a *different* figure for the same
underlying research question — "12,000+ MCP servers scanned," "33% vulnerable to
SSRF" — with no dated report linked. The 7,000/36.7% figure in the harness text
matches one specific, dated BlueRock blog post exactly; it just is not the number
BlueRock is currently surfacing on its own front page, suggesting this is a moving,
self-reported target that has already been superseded once.

This is the one item of the four that is genuinely unrelated to OpenClaw/ClawHub —
it concerns MCP servers broadly, including Microsoft's MarkItDown connector.

**Verdict: FOUND, with a caveat on "independent."** The number and the PoC both check
out against a real, dated, primary vendor post. Confidence: medium-high on the
figures, lower on the word "independent."

**Best URLs:**
- BlueRock, "MCP fURI: SSRF Vulnerability in Microsoft Markitdown MCP" (source of the exact 7,000/36.7% figure and the AWS-key PoC): https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities
- BlueRock's MCP Trust Registry (shows a different, current 12,000+/33% figure — cite only for the discrepancy note, not as confirmation): https://www.mcp-trust.com/

**Recommendation.** Cite the BlueRock post directly rather than calling it an
"independent audit" — say "a security vendor's audit" or name BlueRock outright.
Keep the 7,000/36.7% number (it is accurately quoted) but consider a footnote that
BlueRock's own current public figure differs, so the number is a snapshot, not a
settled fact.

---

## 5. February 2026 count, 135,000+ publicly exposed instances, insecure default configuration

**Claim.** A February 2026 count found more than 135,000 publicly exposed instances
running insecure default configuration.

**Search process.** WebSearch per the project's `sources/inventory.md`, which already
names SecurityScorecard for this claim ("SecurityScorecard MCP servers exposed
February 2026," "135,000 exposed instances SecurityScorecard"); WebFetch on
SecurityScorecard's own blog posts, Bitdefender's coverage, and The Register.

**What I found.** Real, well-corroborated, and precisely dated, but about a specific
product, not generic "MCP" instances. SecurityScorecard's STRIKE threat-intelligence
team ran an internet scan in early February 2026 and found that OpenClaw (the same
product behind item 2's ClawHavoc campaign) binds by default to `0.0.0.0:18789` —
listening on all network interfaces instead of localhost — exposing its control panel
to the open internet. The count climbed fast over the scan's first days: 40,214
instances in SecurityScorecard's first post (9 Feb 2026, "Beyond the Hype"), 42,900
unique IPs across 82 countries with 15,200 vulnerable to RCE in its second post (11
Feb 2026). The 135,000 figure is not in either of those two SecurityScorecard posts
directly, but is independently confirmed by top-tier outlets covering the same
disclosure that week: The Register's 9 Feb 2026 headline is "More than 135,000
OpenClaw instances exposed to internet in latest vibe-coded disaster," attributing
the number to SecurityScorecard STRIKE, and Bitdefender's HotForSecurity blog (12 Feb
2026) reports the same "more than 135,000" figure with the same root cause (default
bind to all interfaces) and the same SecurityScorecard STRIKE attribution.
SecurityScorecard's own press page for February 2026 confirms and links The
Register's 135,000-instance coverage. Secondary aggregator sites report inconsistent
higher numbers for later dates (140,000; 220,000) as the scan's methodology and
window expanded — 135,000 reads as a real snapshot count from the 9-12 February 2026
window, not an invented number, but it was a rapidly moving count during an active
disclosure, not a single fixed audit result.

As with items 2 and 3, "instances" here means specifically OpenClaw agent
deployments, not MCP protocol servers in general — placed right after the sentence
about "7,000 MCP servers," a reader would reasonably assume this continues talking
about MCP servers, when the real subject is a different, if related, product.

**Verdict: FOUND. High confidence on the number and date; the "instances" label
should be made specific.** 135,000+, February 2026, insecure default configuration
(binds to all interfaces) — all confirmed by SecurityScorecard's own reporting plus
independent, reputable secondary coverage (The Register, Bitdefender) from the same
week.

**Best URLs:**
- The Register, "More than 135,000 OpenClaw instances exposed to internet in latest vibe-coded disaster" (9 Feb 2026, attributes number to SecurityScorecard STRIKE): https://www.theregister.com/2026/02/09/openclaw_instances_exposed_vibe_code/
- Bitdefender HotForSecurity, "135K OpenClaw AI Agents Exposed to Internet" (12 Feb 2026, same figure, same root cause, same attribution): https://www.bitdefender.com/en-us/blog/hotforsecurity/135k-openclaw-ai-agents-exposed-online
- SecurityScorecard, "How Exposed OpenClaw Deployments Turn Agentic AI Into an Attack Surface" (primary source, 11 Feb 2026, shows the count still climbing at 40,000+ at time of writing): https://securityscorecard.com/blog/how-exposed-openclaw-deployments-turn-agentic-ai-into-an-attack-surface/
- SecurityScorecard's own February 2026 press roundup (confirms and links The Register's 135,000 figure): https://securityscorecard.com/company/press/securityscorecard-in-the-news-february-2026/

**Recommendation.** Cite The Register and/or Bitdefender rather than SecurityScorecard's
own posts directly, since neither SecurityScorecard post I could reach states 135,000
verbatim (it may appear in a later SecurityScorecard update not indexed here). Name
OpenClaw explicitly instead of "instances," both for accuracy and to avoid implying
this continues the "MCP servers" sentence just before it.

---

## Overall recommendation

1. All five numbers can stay — none needs to be softened or removed for being
   fabricated. Do add real citations; right now this whole paragraph is the one
   uncited passage in an otherwise well-sourced section.
2. Fix one real error: do not credit Antiy CERT with coining "ClawHavoc" — Koi
   Security discovered and named it; Antiy CERT (correctly cited for the 1,184
   count) did the follow-on technical analysis.
3. Consider naming OpenClaw and ClawHub explicitly. Three of the four "not isolated"
   examples (ClawHavoc, Snyk's scan, the 135,000 count) are three vendors reporting
   on the same February 2026 event around one specific, real, already-public
   product. Leaving the product unnamed makes four data points look like four
   independent corners of the industry when it is closer to two: one event
   (OpenClaw/ClawHub, seen from three angles) plus one unrelated MCP-server-wide
   study (BlueRock) plus one unrelated earlier npm incident (postmark-mcp).
4. For the BlueRock line, drop or soften "independent" — it is vendor research from
   a company that sells MCP security products, and BlueRock's own public site now
   shows a different figure (12,000+ servers / 33%) for what looks like the same
   ongoing measurement.

## Suggested `harness-sources.html` entries

```html
<li id="en-src-postmark-mcp">Koi Security. <em>First Malicious MCP in the Wild: The Postmark Backdoor That's Stealing Your Emails.</em> 25 Sep 2025. <a href="https://www.koi.ai/blog/postmark-mcp-npm-malicious-backdoor-email-theft">koi.ai</a></li>
<li id="en-src-clawhavoc">Antiy Labs. <em>ClawHavoc: Analysis of a Large-Scale Poisoning Campaign Targeting the OpenClaw Skill Market for AI Agents.</em> Campaign discovered and named by Koi Security, 1 Feb 2026. <a href="https://www.antiy.net/p/clawhavoc-analysis-of-large-scale-poisoning-campaign-targeting-the-openclaw-skill-market-for-ai-agents/">antiy.net</a></li>
<li id="en-src-snyk-leaky-skills">Snyk. <em>280+ Leaky Skills: How OpenClaw &amp; ClawHub Are Exposing API Keys and PII.</em> 5 Feb 2026. <a href="https://snyk.io/blog/openclaw-skills-credential-leaks-research/">snyk.io</a></li>
<li id="en-src-bluerock-ssrf">BlueRock. <em>MCP fURI: SSRF Vulnerability in Microsoft Markitdown MCP.</em> Disclosed Jan 2026; states the 7,000-server/36.7%-SSRF figure and the AWS-key proof of concept. <a href="https://www.bluerock.io/post/mcp-furi-microsoft-markitdown-vulnerabilities">bluerock.io</a></li>
<li id="en-src-openclaw-exposed">The Register. <em>More than 135,000 OpenClaw instances exposed to internet in latest vibe-coded disaster.</em> 9 Feb 2026, reporting SecurityScorecard STRIKE's count. <a href="https://www.theregister.com/2026/02/09/openclaw_instances_exposed_vibe_code/">theregister.com</a></li>
```

## Note on source quality during this research

Several search hits for OpenClaw's February 2026 crisis (dev.to posts, Medium posts,
"signalcage.com," "vibegraveyard.ai," "penligent.ai") read as low-effort or
AI-generated aggregation of the same story, repeating and sometimes inflating the
instance counts (140,000; 220,000; 346,000 stars) without new reporting. None of
those were used as a basis for the verdicts above; only vendor primary sources
(Postmark, Koi Security, Snyk, BlueRock, SecurityScorecard, Antiy Labs) and
reputable outlets with their own bylines (The Register, Bitdefender, The Hacker
News, CSO Online, cybersecuritynews.com) were treated as evidence.
