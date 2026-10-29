<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVREL02-BP02 Implement a caching strategy

Implementing caching strategies enhances system reliability and
 performance. Evaluate different caching levels from client-side to
 server-side, and explore various caching solutions, including
 ElastiCache, third-party databases, and CDNs for optimizing ad
 payload delivery and reducing backend load.

## Implementation guidance

Caching can be applied at various levels, such as client-side
 caching of user-profiles and server-side caching for bid
 enhancement. Distributed caching solutions include Amazon ElastiCache Redis or Memcached. Third-party databases such as
 Aerospike, Cassandra, and Scylla Cache are also commonly
 deployed for server-side caching. Ad Creative payloads are very
 effectively cached by CDNs, such as CloudFront, further reducing
 the load on web-servers.

## Key AWS services

- [Amazon ElastiCache](https://aws.amazon.com/elasticache/) is a fully managed in-memory
 data store
- [Amazon API Gateway](https://aws.amazon.com/api-gateway/) also provides a built-in
 caching layer
- [AWS Lambda](https://aws.amazon.com/lambda/), a serverless compute service, can
 be used to implement caching at the application layer

## Resources

**Related documentation:**

- [Amazon ElastiCache (Memcached)](https://aws.amazon.com/elasticache/memcached/index.html)
- [Data Caching Across Microservices in a Serverless Architecture](https://aws.amazon.com/blogs/architecture/data-caching-across-microservices-in-a-serverless-architecture/index.html)
- [Caching for high-volume workloads with Amazon ElastiCache](https://aws.amazon.com/getting-started/hands-on/purpose-built-databases/elasticache/index.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advrel02-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
