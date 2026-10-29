<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel03-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# DRHCREL03-BP01 Use AWS Outposts or Local Zones for scenarios where data must reside within a country or jurisdiction without a local AWS Region

To meet data residency requirements in Regions without local AWS
 infrastructure, leverage AWS Outposts across multiple locations or
 AWS Local Zones with redundancy, while utilizing services like
 Amazon S3 on Outposts for resilient local data management.

**Desired outcome:** Achieve
 seamless integration of AWS Cloud capabilities into local
 operations while maintaining strict adherence to data residency
 requirements even in countries with no AWS Regions.

**Benefits of establishing this best
 practice:** AWS Outposts and Local Zones enable
 organizations to use AWS services while keeping data within
 specific geographical boundaries, facilitating compliance with
 local data sovereignty laws and regulations.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

When data must remain within the country and a local AWS Region
 isn't available, deploy on Outposts in different physical
 locations with redundant power and network sources or AWS Local
 Zones. Use services like Amazon S3 on Outposts for backup and
 recovery to achieve high availability while adhering to data
 residency regulations.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/drhcrel03-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
