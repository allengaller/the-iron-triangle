<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF01-BP03 Design for low latency with appropriate compute, storage, and network considerations

Use features from AWS compute, storage, and network services that
 cater to low latency advertising workload needs.

## Implementation guidance

Consider the following guidance for compute, storage, and
 network:

**Compute**

- Use
 [compute-optimized](https://aws.amazon.com/ec2/instance-types/)
 instances. Use benchmarking based on parameters like CPU,
 memory, launch time, and burst performance to choose the
 appropriate instance type.
- Cluster
 your [EC2
 instances](https://aws.amazon.com/ec2/) into
 
 [placement
 groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) for ad serving components for the lowest
 possible latency between instances.

**Storage**

- Implement instance-attached SSD
 [Amazon EBS](https://aws.amazon.com/ebs/) volumes for lowest latency storage.
- Implement provisioned IOPS SSDs if you have an IOPS-intensive workload.
- Implement
 [Amazon EFS](https://aws.amazon.com/efs/) for shared file storage with burst capability.
- Implement
 [Elasticache
 Redis](https://aws.amazon.com/elasticache/) or Memcached to cache frequently accessed data.

**Networking**

- Implement enhanced networking for higher I/O and packet per
 second performance.
- Implement [VPC
 endpoints](https://aws.amazon.com/vpc/) to access AWS services within the network.

## Resources

- [Leveraging
 Amazon EKS managed node group with placement group for low latency critical applications](https://aws.amazon.com/blogs/containers/leveraging-amazon-eks-managed-node-group-with-placement-group-for-low-latency-critical-applications)
- [New Amazon EC2 Instances (C7gd, M7gd, and R7gd) Powered by AWS Graviton3 Processor with Local NVMe-based SSD Storage](https://aws.amazon.com/blogs/aws/new-amazon-ec2-instances-c7gd-m7gd-and-r7gd-powered-by-aws-graviton3-processor-with-local-nvme-based-ssd-storage/)
- [Enhanced
 Networking](https://docs.aws.amazon.com/pdfs/AWSEC2/latest/UserGuide/ec2-ug.pdf#enhanced-networking)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf01-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
