<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp05.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF05-BP05 Consider the benefits of additional AWS storage services

As an alternative to internal storage, some workloads benefit from shared storage for
 collaboration or to enable persisting data in centralized locations. Using non-internal
 storage services delivers storage with customizable performance, which gives administrators
 more control for common storage attributes like IOPS, throughput, and volume size that
 directly impact performance and user experience.

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

Review additional storage services if any of the workloads you are migrating to AWS
 EUC services require tunable performance, larger volume sizes exceeding those provided by
 the EUC services, or granular control over throughput and IOPs, including
 Amazon FSx for Windows File Server, Amazon FSx for NetApp ONTAP , and Amazon EFS.

For more information, see [Persistent storage for Amazon WorkSpaces Applications Linux Fleets on Amazon Elastic File System](https://aws.amazon.com/blogs/desktop-and-application-streaming/persistent-storage-for-amazon-appstream-2-0-linux-fleets-on-amazon-elastic-file-system/) and
 [Connect Amazon FSx for NetApp ONTAP to Amazon WorkSpaces Applications Linux instances](https://aws.amazon.com/blogs/desktop-and-application-streaming/connect-amazon-fsx-for-netapp-ontap-to-amazon-appstream-2-0-linux-instances/).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf05-bp05.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
