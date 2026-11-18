<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Plan for Disaster Recovery (DR)

Having backups and redundant workload components in place is the start of your DR
 strategy. [RTO and RPO are your objectives](./disaster-recovery-dr-objectives.html) 
 for restoration of your workload. Set these based on
 business needs. Implement a strategy to meet these objectives, considering locations and
 function of workload resources and data. The probability of disruption and cost 
 of recovery are also key factors that help to inform the business value of providing disaster recovery for a workload.

Both Availability and Disaster Recovery rely on the same best practices such as
 monitoring for failures, deploying to multiple locations, and automatic failover. However
 Availability focuses on components of the workload, while Disaster Recovery focuses on
 discrete copies of the entire workload. Disaster Recovery has different objectives from
 Availability, focusing on time to recovery after a disaster.

###### Best practices

- [REL13-BP01 Define recovery objectives for downtime and data loss](./rel_planning_for_recovery_objective_defined_recovery.html)
- [REL13-BP02 Use defined recovery strategies to meet the recovery objectives](./rel_planning_for_recovery_disaster_recovery.html)
- [REL13-BP03 Test disaster recovery implementation to validate the implementation](./rel_planning_for_recovery_dr_tested.html)
- [REL13-BP04 Manage configuration drift at the DR site or Region](./rel_planning_for_recovery_config_drift.html)
- [REL13-BP05 Automate recovery](./rel_planning_for_recovery_auto_recovery.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-for-disaster-recovery-dr.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
