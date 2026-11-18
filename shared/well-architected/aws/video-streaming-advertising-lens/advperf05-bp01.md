<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF05-BP01 Establish private connections between your VPC and AWS services to improve performance

A private network not only enhances the overall stability and
 security of your system, but it also improves the latency and user experience
 for advertising customers.

## Implementation guidance

Use [AWS PrivateLink](https://aws.amazon.com/privatelink/) to establish private connections between your
 VPC and AWS services, such as Amazon S3, Amazon DynamoDB, or
 Amazon ElastiCache. This approach enhances security by avoiding
 the public internet and improves performance by reducing network
 hops and latency.

## Resources

- [Access
 AWS services through AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/privatelink-access-aws-services.html)
- [Simplify
 private connectivity to Amazon DynamoDB with AWS PrivateLink](https://aws.amazon.com/blogs/database/simplify-private-connectivity-to-amazon-dynamodb-with-aws-privatelink/)
- [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html)
- [AWS services that integrate with AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/aws-services-privatelink-support.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf05-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
