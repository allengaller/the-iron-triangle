<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/reliability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Reliability

The reliability pillar encompasses the ability of a workload to
 perform its intended function correctly and consistently when it's
 expected to. This includes the ability to operate and test the
 workload through its entire lifecycle. This section provides
 in-depth, best practice guidance for implementing reliable workloads
 on AWS.

The reliability pillar provides an overview of design principles,
 best practices, and questions. You can find implementation guidance in the
 [Reliability
 Pillar whitepaper](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html).

## Design principles

There are three key dimensions that define Reliability in the
 advertising industry: latency, uptime, data security. While this
 is similar to the range of criticality in transactional systems
 found in the financial industry, there are unique expectations of
 resiliency for SSPs, exchanges, and DSPs. We will use RPO and RTO,
 which are established in the reliability pillar of the
 Well-Architected Framework

## Definitions

- **Recovery Point
 Objective (RPO):** The maximum amount of data loss
 allowed as the result of a system failure expressed in units
 of time.
- **Recovery Time
 Objective (RTO):** The maximum amount of time allowed
 for a system to resume its normal operations after a failure.
- **Uptime:** A measure of system
 reliability, expressed as the period of time a machine,
 typically a computer, has been continuously working and
 available.
- **Microservices:** An
 architectural pattern that arranges an application as a
 collection of loosely-coupled, fine-grained services
 communicating through lightweight protocols. One of its goals
 is to enable teams to develop and deploy their services
 independently.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/reliability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
