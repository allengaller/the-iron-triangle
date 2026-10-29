<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# SCPERF01-BP02 Factor in rate of increase in load, traffic, and scale-out intervals

Identify the upper bounds of the peak load against a system, as
 well as the amount of time needed to reach peak load. Load tests
 often overlook the rate of increase in traffic and create tests
 that scale up too quickly or too slowly.

**Desired**
**outcome:** You mimic the traffic
 and load situation of the system and see how the user experience
 in such situations, this will help to fine-tune the underlying
 resources of the architecture to achieve better results.

**Benefits of establishing this best
 practice:** System resiliency prediction, and system
 behavior during peak hours/loads.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Identify the upper bounds of the peak load against a system, as
 well as the amount of time needed to reach peak load. Load tests
 often overlook the rate of increase in traffic and create tests
 that scale up too quickly or too slowly. If the load test ramps
 up too quickly, the system may not be able to add capacity
 rapidly enough to meet the demand, which degrades performance
 and introduces errors. Load tests need to be run periodically
 and with every major release of the system or when new systems
 or architecture is introduced in the supply chain eco-system.

### Implementation steps

1. Analyze historical traffic patterns to identify peak load
 periods and growth rates specific to supply chain
 operations.
2. Design load tests that accurately simulate realistic
 traffic ramp-up patterns based on actual usage scenarios.
3. Establish automated scaling policies that can respond
 appropriately to gradual and sudden load increases.
4. Implement comprehensive monitoring during load tests to
 identify performance bottlenecks and capacity constraints.
5. Create regular load testing schedules that coincide with
 major system releases and supply chain system
 integrations.
6. Document and analyze load test results to continuously
 improve system performance and scaling capabilities.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/supply-chain-lens/scperf01-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
