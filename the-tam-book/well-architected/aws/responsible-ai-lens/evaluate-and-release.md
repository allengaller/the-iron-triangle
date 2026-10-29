<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/evaluate-and-release.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Evaluate and release

The evaluate and release focus area provides best practices for
 making a responsible release decision, given the release criteria
 from [Release criteria](./release-criteria.html), the evaluation datasets from [Dataset planning](./dataset-planning.html), and the AI system design from [System planning](./system-planning.html). The release
 decision is a binary (yes or no) decision that aggregates the results
 of testing the AI system against each individual release criterion.
 A well-designed decision factors in the compounded uncertainty in
 the individual criterion decisions, that is have we met each
 criterion with the required confidence (for example, are we at
 least 95% confident that the release criteria have been satisfied?).
 If a specific release criterion is not met, release may still be
 possible if the residual risk is disclosed through Monitoring
 transparency mechanisms. Otherwise, you should return to [System planning](./system-planning.html) to review options for baking and filtering
 mitigations.

###### Focus areas

- [System evaluation](./raier01.html)
- [Aggregate results](./raier02.html)
- [Address unmet release criteria](./raier03.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/responsible-ai-lens/evaluate-and-release.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
