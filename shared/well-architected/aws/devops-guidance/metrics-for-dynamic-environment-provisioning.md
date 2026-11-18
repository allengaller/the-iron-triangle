<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-dynamic-environment-provisioning.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Metrics for dynamic environment provisioning

- **Environment provisioning lead
 time**: The average time it takes to provision an
 environment. A reduced lead time indicates an ability to
 meet changing requirements, an enhanced developer
 experience, and increased readiness for disaster recovery
 scenarios. Assess this metric by tracking the duration
 from the moment a provisioning request is initiated to
 when the environment becomes operational.
- **Configuration drift
 rate**: The percentage of environments deviating
 from their baseline configuration within a specific time
 frame. Improve this metric by implementing observability
 capabilities, applying infrastructure-as-code practices,
 and regularly review and update environment
 baselines. Compare current environment configurations to
 baseline configurations regularly. Calculate the ratio of
 drifted environments to total environments, then multiply
 by 100 for the percentage.
- **Self-service tool adoption
 rate**: The percentage of developers using
 self-service tools for environment management. This metric
 can indicate the ease-of-use and effectiveness of provided
 self-service capabilities. Improve this metric by
 optimizing user interfaces, developing APIs and CLIs,
 conducting training sessions, and gathering feedback to
 make necessary enhancements. Monitor usage over a
 specified period to determine the number of users actively
 using the tool. Calculate the ratio of users adopting the
 tool to the total in the expected user base, then multiply
 by 100 for the percentage.
- **Environment overhead
 cost**: Measuring overhead costs resulting from
 underutilized or over-provisioned environments. This
 metric provides insight into potential cost savings and
 optimal resource allocation. Improve this metric by
 implementing automated right-sizing capabilities,
 monitoring environment utilization, and de-provisioning
 unused environments. Track costs associated with
 maintaining environments and compare against their actual
 utilization or workload.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/metrics-for-dynamic-environment-provisioning.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
