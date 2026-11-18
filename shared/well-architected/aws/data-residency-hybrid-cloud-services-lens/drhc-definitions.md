<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhc-definitions.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Definitions

The following definitions are provided related to Data Residency
 and Hybrid Computing for AWS customers using the Well-Architected
 Framework. For additional information, see
 [AWS Glossary](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html)**.**

## AWS definitions

- **AWS Outposts
 Server :** AWS Outposts Servers are
 rack-mountable servers in 1U and 2U form factors for
 locations with limited space or smaller capacity
 requirements.
- **AWS Outposts
 rack :** AWS Outposts rack is a fully managed
 service that extends AWS infrastructure, services, APIs, and
 tools on premises for a truly consistent hybrid experience.
- **AWS Local
 Zones :** AWS Local Zones are a type of
 infrastructure deployment that places select AWS services
 closer to your end users and workloads.
- **Region :**
 AWS Regions are physical locations around the world where we
 cluster data centers. We call each group of logical data
 centers an Availability Zone. Each AWS Region consists of a
 minimum of three isolated and physically-separated
 Availability Zones within a geographic area.
- **Availability
 Zone (AZ) :** One or more discrete data
 centers with redundant power, networking, and connectivity
 in an AWS Region.
- **Parent
 Availability Zone or Region :** The Region
 and Availability Zone pair that the Outposts service
 connects to in the Region.
- **Local
 gateway :** A local gateway connects your
 Outpost subnets and your on-premises network.
- **Service
 link :** The service link is a necessary
 connection between your Outposts and your chosen AWS Region
 (or home Region) and allows for the management of the
 Outposts.

## Industry definitions

- **Data residency:** The
 requirement of keeping data in a certain region or country
 to comply with local laws and regulations.
- **Data sovereignty:** Refers
 to an organization or country's ability to have full control
 and ownership over the data they generate and store,
 including where that data is stored, who can access it, and
 providing resilience and self-sufficiency from external factors.
 Key aspects include data residency, operator access
 restrictions, resiliency and survivability, and
 technological autonomy.
- **Low latency:** A technical
 use-case where application components need under ten
 millisecond latency between each other.
- **Local data processing:** A
 technical use-case where it is optimal to process the data
 where it is generated (locally) as opposed to sending it to
 a cloud region. This could be due to transfer costs,
 transfer time, and the size of the dataset.
- **Control plane:** Provides
 the administrative APIs used to create, read or describe,
 update, delete, and list resources. Example control plane
 actions are launching a new Amazon EC2 instance, creating an
 [Amazon S3](https://aws.amazon.com/s3/) bucket, and describing an Amazon SQS queue. When
 you launch an Amazon EC2 instance, the control plane has to
 perform multiple tasks such as finding a physical host with
 capacity, allocating the network interface, preparing an
 [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volume, generating
 AWS Identity and Access Management (AWS IAM) credentials,
 adding the security group rules, and more. Control planes
 tend to be complicated orchestration and aggregation
 systems.
- **Data plane:** Provides the
 primary function of the service. For example, the data plane
 includes the running Amazon EC2 instance itself, reading and
 writing to an Amazon EBS volume, getting and putting objects
 in an Amazon S3 bucket, and Amazon Route 53 answering DNS
 queries and performing health checks.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhc-definitions.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
