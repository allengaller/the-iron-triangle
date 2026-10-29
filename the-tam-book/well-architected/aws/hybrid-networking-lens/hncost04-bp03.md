<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# HNCOST04-BP03 Implement compression and caching for repetitive data transfers

Reduce data transfer volumes by compressing in-transit data and
 caching frequently accessed content at the edge.

**Desired outcome:** Reduction in
 data transfer volumes and associated costs.

**Level of risk exposed if this best practice
 is not established:** Low

**Benefits of establishing this best
 practice:**

- Lower bandwidth consumption
- Faster transfer times
- Reduced storage costs for compressed data

## Implementation guidance

- Enable compression for payloads
- Configure TTL for static assets in content delivery network
 such as Amazon CloudFront
- Use compression for file/volume syncs using services such as
 AWS Storage Gateway

## Resources

- [Manage
 how long content stays in the cache](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Expiration.html)
- [Payload
 compression for REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-gzip-compression-decompression.html)
- [AWS Storage Gateway FAQ](https://aws.amazon.com/storagegateway/faqs/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/hybrid-networking-lens/hncost04-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
