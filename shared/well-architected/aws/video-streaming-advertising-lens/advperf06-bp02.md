<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF06-BP02 Optimize your intake request format (like HTTP/2 or HTTP/3) for faster processing

Use optimization in next generation networking protocols to
 address low latency needs for advertising workloads.

## Implementation guidance

Implement HTTP/2 protocol, which offers features like
 multiplexing (multiple requests and responses are sent over the
 same TCP connection), header compression, and binary protocol.
 These features improve latency and throughput.

AWS services do support HTTP/2 and HTTP/3 protocols for gains in
 performance efficiency.

## Key AWS services

- [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
- [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)

## Resources

- [New
 – HTTP/3 Support for Amazon CloudFront](https://aws.amazon.com/blogs/aws/new-http-3-support-for-amazon-cloudfront/)
- [Application Load Balancers enables gRPC workloads with end to end HTTP/2 support](https://aws.amazon.com/about-aws/whats-new/2020/10/application-load-balancers-enable-grpc-workloads-end-to-end-http-2-support/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf06-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
