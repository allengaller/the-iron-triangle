<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp03.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# ADVPERF03-BP03 Use a cloud file system to store shared data between applications

File storage services (such as Amazon EFS) provide a simple way to
 set up and scale file systems and are widely used for big data and
 analytics workloads, media processing workflows, and content
 management scenarios. They are well-suited for distributed
 workloads and applications that need to share files across
 multiple EC2 instances.

## Implementation guidance

[Amazon EFS](https://aws.amazon.com/efs/)
 is a scalable and fully managed cloud file system that provides
 a simple, serverless way to share file data across AWS Cloud
 services and on-premises resources. In the advertising industry,
 Amazon EFS can be used to store and share log files,
 configuration files, and other data that needs to be accessed
 concurrently by multiple applications or instances. This is
 particularly useful for log processing and analysis pipelines,
 where data needs to be shared across multiple stages.

- **Performance
 modes :** Amazon EFS offers both General
 Purpose and Max I/O performance modes.
- **Throughput
 modes :** Choosing the correct throughput mode for your file system
 depends on your workload's performance requirements.
- **Cost optimization:** Use Amazon EFS lifecycle policies to
 automatically move infrequently accessed files to the [EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/) storage class,
 reducing stor
- **High availability:** Create Amazon EFS mount targets in all
 availability zones to provide high availability and low latency access to your file
 system.
- age costs.

## Resources

- [Encrypting
 data in Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/encryption.html)
- [Create an Amazon EFS
 file system and mount it on an Amazon EC2 instance using the AWS CLI](https://docs.aws.amazon.com/efs/latest/ug/wt1-getting-started.html)
- [Mounting
 considerations for Linux](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs-mount-cmd-general.html)
- [Managing
 automatic backups of Amazon EFS file systems](https://docs.aws.amazon.com/efs/latest/ug/automatic-backups.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advperf03-bp03.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
