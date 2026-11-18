<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNSEC06-BP02 Automate incident response

Implement automated response capabilities to enhance incident
 containment speed and reliability while reducing manual intervention
 requirements. This approach ensures consistent execution of response
 procedures while minimizing human error during critical security
 events.

**Desired outcome:** Faster, more
 reliable containment and recovery from incidents with reduced
 operational burden.

**Level of risk exposed if this best practice
 is not established:** High

**Benefits of establishing this best
 practice:**

- Shortens response times and limits damage
- Reduces alert fatigue and manual workload
- Ensures consistent, repeatable incident handling

## Implementation guidance

- Automate incident response by configuring security findings
 with response actions. For example, you can achieve this by
 integrating AWS Security Hub CSPM findings with AWS Lambda for
 automated actions.
- Test and tune automation playbooks in non-production
 environments.

## Resources

- [Using
 EventBridge for automated response and remediation PDF
 RSS](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-cloudwatch-events.html)
- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/automating-security-responses.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hnsec06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
