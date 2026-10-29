<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL01-BP03 Architect for variable demand

Architect to elastically launch resources for variable demand,
 including the most challenging peak events, like flash crowds or
 thundering herds.

## Implementation guidance

Depending on the advertising channel, such as retail stores,
 video streaming, or audio apps, loads will peak at different
 times in different locations. Know your historical load
 statistics, and adjust load testing scenarios based on
 historical peaks to determine how the workload performs in
 unexpected situations and peak demand. With
 [Amazon CloudWatch Real-User Monitoring (RUM)](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html), you can collect
 and view client-side data about your web application performance
 from actual user sessions in near real-time.
 [CloudWatch](https://aws.amazon.com/cloudwatch/)
 Synthetics are configurable scripts that run on a schedule to
 monitor your endpoints and APIs.

If this a new workload without historical data, load testing is
 part of this process. Until enough historical data is obtained,
 use [Auto
 Scaling](https://aws.amazon.com/autoscaling/) groups and Elastic Load Balancers (ELB) to meet
 compute demands and send requests to healthy hosts. Networking
 demands must also be considered and capacity planned to prevent
 congestion. For critical workloads, consider private AWS Direct Connect networking to connect to partners or on-premise
 infrastructure to provide sufficient capacity and more stable
 latency.

## Resources

- [Predictive
 scaling for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-predictive-scaling.html)
- [Guidance
 for AdTech Private Network on AWS](https://aws.amazon.com/solutions/guidance/adtech-private-network-on-aws/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel01-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
