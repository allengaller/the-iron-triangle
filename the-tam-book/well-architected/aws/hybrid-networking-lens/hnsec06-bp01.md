<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC06-BP01 Monitor your environment for malicious behavior

Responding to any cyber incident requires the ability to detect
 threats and establish a baseline for normal operations in a hybrid
 environment. Continuously monitors your environment for malicious
 behavior to protect your accounts and workloads.

**Desired outcome:** Quick detection
 of malicious activity enables fast containment and limits the impact
 of ransomware and other security incidents.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Early identification of threats and abnormal behaviors
- Reduces containment and remediation time
- Enhances overall security posture with automated, continuous
 monitoring

## Implementation guidance

- Monitor flow logs, API activity, and DNS logs for threats,
 such as using Amazon GuardDuty that monitors and reports
 findings from these sources.
- Regularly review and baseline findings to distinguish normal
 from abnormal activity.

## Resources

- [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
