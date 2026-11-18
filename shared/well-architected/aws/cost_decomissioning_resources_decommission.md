<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_decomissioning_resources_decommission.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# COST04-BP03 Decommission resources

Decommission resources initiated by events such as periodic audits,
 or changes in usage. Decommissioning is typically performed
 periodically and can be manual or automated.

**Level of risk exposed if this best practice
 is not established:** Medium

## Implementation guidance

The frequency and effort to search for unused resources should reflect the potential savings,
 so an account with a small cost should be analyzed less frequently than an account with
 larger costs. Searches and decommission events can be initiated by state changes in the
 workload, such as a product going end of life or being replaced. Searches and decommission
 events may also be initiated by external events, such as changes in market conditions or
 product termination.

**Implementation steps**

- **Decommission resources:**This is the depreciation stage of 
 AWS resources that are no longer needed or ending of a licensing agreement. Complete all 
 final checks completed before moving to the disposal stage and decommissioning resources 
 to prevent any unwanted disruptions like taking snapshots or backups. Using the 
 decommissioning process, decommission each of the resources that have been identified 
 as unused.

## Resources

**Related documents:**

- [AWS Auto Scaling](https://aws.amazon.com/autoscaling/)
- [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/trustedadvisor/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/framework/cost_decomissioning_resources_decommission.html（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
