<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVCOST02-BP02 Use compression to reduce network traffic and storage costs

Using compression can reduce the amount of data transferred thus reducing network and
 storage costs.

## Implementation guidance

- Use GZIP compression before transferring data to [Amazon S3](https://aws.amazon.com/s3) to reduce traffic between Availability Zones and Regions, as well as
 traffic to the internet.
- Use snappy compression for [Amazon Kinesis](https://aws.amazon.com/kinesis/) Data Streams to reduce the amount of data stored and transferred.
- Implement HTTP/2 for [Application Load Balancers](https://aws.amazon.com/elasticloadbalancing/application-load-balancer/), [Amazon API Gateway](https://aws.amazon.com/api-gateway/) compression, and [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://aws.amazon.com/msk/).
- For databases, consider the following compression techniques to reduce storage
 costs:
Column-level compressionTable-level compressionBackup compressionQuery result compressionIndex compression
- Implement replication compression to reduce data transfer costs.
- Monitor the impact of compression on CPU utilization, and verify that the
 increased CPU costs do not exceed the network transfer costs saved.

## Resources

- [Cost-Optimizing your AWS architectures by utilizing Amazon CloudFront features](https://aws.amazon.com/blogs/networking-and-content-delivery/cost-optimizing-your-aws-architectures-by-utilizing-amazon-cloudfront-features/)
- [Reduce network transfer time with connection compression in Amazon RDS for MySQL and
 Amazon RDS for MariaDB](https://aws.amazon.com/blogs/database/reduce-network-transfer-time-with-connection-compression-in-amazon-rds-for-mysql-and-amazon-rds-for-mariadb/)
- [Enable
 payload compression for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-enable-compression.html)
- [Custom Amazon MSK
 configurations](https://docs.aws.amazon.com/msk/latest/developerguide/msk-configuration-properties.html)
- [Processing large records with Amazon Kinesis Data Streams](https://aws.amazon.com/blogs/big-data/processing-large-records-with-amazon-kinesis-data-streams/)
- [What is AWS
 Transfer Family?](https://docs.aws.amazon.com/transfer/latest/userguide/what-is-aws-transfer-family.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advcost02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
