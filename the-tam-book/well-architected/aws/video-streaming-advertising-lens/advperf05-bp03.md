<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF05-BP03 Use load balancers to improve high availability and load distribution in your workload

Use the load balancing service provided by AWS to enhance the high
 availability of applications. In the event of disruptions that cause targets to become unhealthy, load balancers can automatically exclude unhealthy targets from traffic routing.

## Implementation guidance

Elastic Load Balancing (ELB) employs various load balancing
 algorithms, such as round-robin, least outstanding requests, or
 IP hash, to distribute traffic evenly across healthy targets,
 which optimizes resource utilization and prevents overloading of
 individual targets. It supports content-based routing, which
 routes traffic based on the content of the request, such as the
 URL path or headers, efficiently handling different types of
 requests. ELB can offload SSL/TLS decryption and encryption from
 your targets, reducing the computational overhead on your
 application servers and improving overall performance.

## Key AWS services

- [Amazon Elastic
 Load balancer (ELB)](https://aws.amazon.com/elasticloadbalancing/)
- [Amazon Elastic Compute Cloud (EC2)](https://aws.amazon.com/ec2/)

## Resources

- [What's
 the Difference Between Application, Network, and Gateway Load Balancing?](https://aws.amazon.com/compare/the-difference-between-the-difference-between-application-network-and-gateway-load-balancing/)
- [Monitor
 your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-monitoring.html)
- [ELB
 Best Practices Guides](https://aws.github.io/aws-elb-best-practices/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
