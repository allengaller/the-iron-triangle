<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp04.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL01-BP04 Implement chaos engineering practices

Accept that "everything fails, all the time," (Dr. Werner Vogels,
 Amazon CTO), and safely disrupt things on your terms to discover
 faults and fragility so that you can later improve services.

## Implementation guidance

Advertising systems have components that are sensitive to
 disconnects, latency, and bandwidth changes. Use tools like
 [AWS Fault
 Injection Service (FIS)](https://aws.amazon.com/fis/) or open-source tools like
 [Chaos
 Monkey](https://netflix.github.io/chaosmonkey/) to inject failures into your workload which
 simulate network disruptions or resource unavailability. Based
 on the results, update responses to failure scenarios, how you
 monitor, and what you alert on, then adapt runbooks and
 playbooks before practicing failure response with relevant
 teams.

## Key AWS services

- [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/)

## Resources

**Related documentation:**

- [AWS chaos engineering blogs](https://aws.amazon.com/blogs/architecture/tag/chaos-engineering/)
- [Continuous
 integration and continuous delivery](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-caf-platform-perspective/ci-cd.html)
- [Leverage
 AWS Resilience Lifecycle Framework to assess and improve the resilience of application using AWS Resilience Hub](https://aws.amazon.com/blogs/mt/leverage-aws-resilience-lifecycle-framework-to-assess-and-improve-the-resilience-of-application-using-aws-resilience-hub/index.html)
- [[QA.NT.6]
 Experiment with failure using resilience testing to build recovery preparedness](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/qa.nt.6-experiment-with-failure-using-resilience-testing-to-build-recovery-preparedness.html)

**Related
 videos:**

- [AWS re:Invent 2020 - Developer Keynote with Dr. Werner Vogels](https://www.youtube.com/watch?v=jt-gV1YwmnI)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp04.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
