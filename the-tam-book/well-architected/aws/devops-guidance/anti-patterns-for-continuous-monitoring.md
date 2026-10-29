<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-monitoring.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Anti-patterns for continuous monitoring

- **Blame culture**:
 Encouraging a culture where individuals are blamed for
 errors or failures can deter open communication, and the
 collaborative diagnosis of issues. In a blame culture,
 team members may hide or underreport issues for fear of
 retribution. Instead, foster a culture of shared
 responsibility where failures are seen as opportunities
 for learning and improvement. Encourage open discussions
 and retrospectives to understand the root causes and to
 find ways to prevent similar issues in the future.
- **Overlooking derived
 metrics**: Relying solely on surface-level
 metrics without deriving deeper insights can lead to
 unaddressed issues and potential service disruptions.
 Ensure that monitoring includes a comprehensive
 understanding of system performance by analyzing metrics
 in depth, such as distinguishing between latencies based
 on query size or categorizing error types. Use techniques
 like anomaly detection and consider metrics like trimmed
 means for latency to reveal patterns obscured by averages.
- **Inadequate monitoring
 coverage:**Not monitoring every critical system
 or frequently reviewing your monitoring strategy can lead
 to undetected issues or performance degradation. Regularly
 assess and update monitoring coverage, ensuring that all
 systems and applications are being observed. A symptom of
 this anti-pattern is "no dogs barking," where
 the absence of expected alerts or metrics itself can
 indicate an issue.
- **Noisy and unactionable
 alarms:** If alarms frequently sound without
 actionable cause, trust in the alerting system diminishes,
 risking slower response times or overlooked genuine
 alerts. Ensure that alerts are both actionable and
 significant by continuously evaluating the outcomes they
 lead to. Implement mechanisms to mute false positives and
 adjust overly sensitive alarms.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-monitoring.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
