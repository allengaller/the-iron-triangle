<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.5---build-a-disaster-recovery-dr-plan-for-the-analytics-infrastructure-and-the-data..html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Best practice 6.5 – Build a disaster recovery (DR) plan for the analytics infrastructure and the data

Discuss with business stakeholders to understand maximum
 amount of data loss (RPO) and maximum amount of service loss
 (RTO).

## Suggestion 6.5.1 – Confirm the business requirement of the disaster recovery (DR) plan

Agree with the business shareholders what the internal and
 external SLAs are for your analytics processes. For
 example, not all business reports are business critical so
 it’s important that your DR plans are aligned with the
 severity of the outage.

## Suggestion 6.5.2 – Design the disaster recovery (DR) solution for each layer of the solution

Review the architecture for your data and analytics pipeline and select the DR pattern that meets your DR requirements, working backwards from the most important information that must be saved in the event of a DR scenario, to the least important.

## Suggestion 6.5.3 – Implement and test your backup solution based on the RPO and RTO

Backup solutions must be implemented to reduce data loss. Test your backup to ensure it is performing correctly by periodically restoring the data and validating the results.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/best-practice-6.5---build-a-disaster-recovery-dr-plan-for-the-analytics-infrastructure-and-the-data..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
