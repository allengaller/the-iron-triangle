<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/release-criteria.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Release criteria

The Release Criteria focus area assists you to translate benefits,
 risks, and organizational obligations from the previous focus areas
 into a single list of criteria that you use to assess the readiness
 of the AI solution for release. The list of release criteria defines
 a high-level specification for the design of system datasets and the
 AI system. You should consider defining release criteria for the
 full set of expected benefits and potential harms to reduce
 downstream surprises post deployment. For AI solutions using machine
 learning, a full set of criteria would cover factors such as overall
 usability performance, latency, and uptime, as well as responsible
 AI factors such as safety, controllability, security, privacy,
 robustness, fairness, veracity, explainability and transparency.

A release criterion is a binary test that consists of a quantitative
 assessment and a decision threshold. The quantitative assessment
 should specify a minimum degree of confidence that the measured
 value meets the decision threshold. For example:

1. Are we at least 95% confident that mean latency measured from
 last input token to last output token < 100 milliseconds (yes or no)?
2. Are we at least 99% confident that the maximum disparity between
 false positive rates across all product categories < 10% (yes or no)?

The release decision itself is also a binary decision that
 aggregates the results from each individual release criterion. [Evaluate and release](./evaluate-and-release.html) addresses the release decision.

###### Focus areas

- [Define release criteria](./rairc01.html)
- [Measure test properties](./rairc02.html)
- [Select metrics](./rairc03.html)
- [Release criteria thresholds](./rairc04.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/release-criteria.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
