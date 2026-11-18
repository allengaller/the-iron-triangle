<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Fraud detection

Traffic fraud in digital advertising could impact the
 advertising solution by affecting ad spend through fake clicks,
 bot traffic, and manipulation schemes. Workloads benefit from
 resilient and secure systems that implement defense in depth
 strategies for fraud prevention. Effective protection assists
 advertisers optimize budgets by focusing on genuine traffic and
 properly represented inventory, while publishers can maintain
 reputation and revenue by addressing fraudulent activities on
 their solution.

Consider using AWS WAF to evaluate traffic to your advertising
 solution and filter out suspicious or un-wanted bot traffic
 through customizable rules. Amazon GuardDuty can also be
 utilized to help protect your AWS accounts, workloads, and data
 from threats.

###### Best practices

- [ADVSEC05-BP01 Validate and sanitize content before running a campaign](./advsec05-bp01.html)
- [Key AWS services](#key-aws-services-7)
- [Resources](#resources-12)

## Key AWS services

- AWS WAF
- Amazon GuardDuty
- Amazon Fraud Detector

## Resources

- [Amazon GuardDuty](https://aws.amazon.com/guardduty/)
- [AWS WAF rules](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rules.html)
- [Amazon Fraud Detector FAQs](https://aws.amazon.com/fraud-detector/faqs/#topic-0)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsec05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
