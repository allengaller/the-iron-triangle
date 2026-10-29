<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-local-development.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Metrics for local development

- **Local environment provisioning time:** The amount of time
 developers spend on setting up or troubleshooting their local development environment.
 This metric indicates inefficiencies in onboarding or local environment maintenance,
 which can negatively impact productivity. If you are centrally provisioning or fully
 automating this process, use observability tools to monitor the time dedicated to
 environment set up. If individual developers need to take action to set up their
 environment, conduct regular surveys or use time-tracking tools to gather additional
 data points.
- **Post-commit test failure rate:** The percentage of tests
 that fail in an integrated environment after a local commit. This metric allows teams to
 track and optimize the effectiveness of their local testing environments and workflows.
 Monitor this metric by calculating the number of tests that fail post-commit in
 integrated environment divided by the total number of tests run post-commit. Ideally,
 this metric should trend downwards over time, indicating that local environments are
 becoming more consistent with integrated environments and that developers are catching
 more issues before committing changes.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-local-development.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
