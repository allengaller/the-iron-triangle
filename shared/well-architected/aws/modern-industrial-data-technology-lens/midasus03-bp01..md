<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus03-bp01..html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MIDASUS03-BP01 Implement edge data and cross-region movement strategies

Implement strategies that process information at the edge when possible and strategically
 manage cross-Region transfers in manufacturing environments. This approach reduces unnecessary
 network traffic, lowers energy consumption, and improves operational efficiency in factory
 environments.

**Desired outcome:** Reduced data transfer across networks, optimized energy usage, faster access to
 manufacturing data, and improved application performance with lower carbon impact.

**Benefits of establishing this best practice:**

- Decreased network bandwidth consumption and associated energy usage
- Reduced carbon footprint from data centers and networking equipment
- Lower latency for manufacturing applications requiring real-time data
- Cost savings from reduced data transfer fees

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

- Process data at the source or edge locations to filter, compress, or aggregate data
 before transmitting to centralized storage, reducing unnecessary data movement and
 processing requirements.
- Implement efficient data transfer mechanisms when cross-region or cross-zone data
 movement is necessary, using compression, batching, and optimized transfer strategies.
- Store data in locations geographically closest to where it will be processed and
 accessed most frequently to minimize network latency and reduce energy consumed during
 data transit.
- Apply data lifecycle management strategies to automatically tier, archive, or
 delete data based on access patterns, compliance requirements, and business value,
 reducing storage footprint and associated energy costs.

### Implementation steps

1. **Edge processing implementation:**
Deploy AWS IoT Greengrass to process sensor data locally at the edgeConfigure data filtering rules to send only aggregated results to the cloudSet up Lambda functions for edge-based data processing and reduction
2. **Efficient data transfer configuration:**
Implement Amazon S3 Transfer Acceleration and AWS Global Accelerator for
 cross-region data movementUse Amazon CloudFront to cache frequently accessed data closer to end users
3. **Geographic data optimization:**
Store data in AWS Regions closest to production facilitiesConfigure Amazon S3 lifecycle policies for efficient data managementMonitor data access patterns using CloudWatch to identify optimization
 opportunities

## Key AWS services

- AWS IoT Greengrass
- Amazon S3 Transfer Acceleration
- AWS Global Accelerator
- Amazon CloudFront

## Resources

- [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/latest/developerguide/what-is-gg.html)
- [Configuring fast, secure file transfers using Amazon S3 Transfer Acceleration](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html)
- [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html)
- [AWS for the Edge](https://aws.amazon.com/edge/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/modern-industrial-data-technology-lens/midasus03-bp01..html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
