<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel02.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# FSIREL02: Are you practicing continuous resilience to ensure that your services meet regulatory availability and recovery requirements?

Your workload, and the environment in which it operates, is
 constantly changing. To keep pace, resiliency practices should
 not be considered a one-time effort. Make resilience a regular
 part of your feature delivery and operational cadence
 throughout a workload's lifetime. To this end, resiliency
 testing should be part of your CI/CD testing pipelines.

Furthermore, you should establish a resiliency review on a
 regular interval to validate that changes have not impacted
 the application's resiliency posture. In addition to this, the
 rise of generative AI have added a recommended pattern to
 allow
 [cross-region
 inference](https://docs.aws.amazon.com/bedrock/latest/userguide/cross-region-inference.html) or
 [provisioned
 throughput](https://docs.aws.amazon.com/bedrock/latest/userguide/prov-throughput.html) to facilitate more reliable calls to
 generative AI models.

## FSIREL02-BP01 Practice regular resilience testing

Resilience is not a one-time effort. Resilience should be
 part of your day-to-day operations and practiced
 continuously. Perform chaos engineering experiments and
 scenario testing like
 [Fault
 Injection Service](https://aws.amazon.com/fis/) or Cross-Region connectivity faults
 regularly to increase your team's understanding of how your
 workload behaves in adverse conditions such as excessive
 load, slow or failed network links, or a combination of
 adverse conditions. Continuous testing for resilience helps
 you to anticipate, observe, and respond to faults, as well
 as find blind spots that you didn't know existed. By
 practicing continuous resilience testing and
 [chaos
 engineering](https://aws.amazon.com/blogs/architecture/chaos-testing-with-aws-fault-injection-simulator-and-aws-codepipeline/), your teams can improve observability and
 gain confidence in their ability to quickly detect and
 recover from incidents as recovery procedures are practiced
 and improved.

## FSIREL02-BP02 Implement an operational readiness review process

To capture learnings from previous incidents and minimize reoccurrence across
 teams, implement an [operational readiness review
 process](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) within your organization. As part of your incident
 analysis process, identify key questions that, if asked prior to the incident, may
 have prevented the incident from occurring. Maintain a list of these key questions so
 that, as new features are released, your developers can refer back to the list and
 make sure that they don't repeat the same mistakes that have disrupted other
 workloads.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/financial-services-industry-lens/fsirel02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
