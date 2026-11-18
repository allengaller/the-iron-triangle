<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/scenario-c-maintain-primary-service-copy-within-country-or-jurisdiction.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Scenario C: Maintain primary service copy within country or jurisdiction

In a scenario where the law mandates data residency requirements
 that specify that the primary copy of the data must be
 maintained within the country or jurisdiction, several factors
 should be considered.

In this case, in-scope data can be stored or transferred outside
 the borders, but the primary servicing copy must be held within
 the border of your jurisdiction.

For your deployment needs, you have two options depending on
 the availability of Local Zones in your
 [location](https://aws.amazon.com/about-aws/global-infrastructure/localzones/locations/)
 and the specific workloads you need to deploy, as outlined in
 the following diagrams:

![Reference architecture that uses Local Zones to navigate maintaining a primary service copy of data within a country or jurisdiction](/images/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-C-local-zones.png)

*Scenario C, option one: AWS Local Zones*

The first option for deploying AWS
 services specifically focuses on the use of AWS Local Zones
 and AWS Outposts:

1. Assess data residency requirements specific to the
 organization and regulatory environment, and identify
 regulated data.
2. Plan, order, and deploy
 [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) in the corporate data centers for
 [high
 availability](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html) alongside
 [AWS Local Zones](https://aws.amazon.com/about-aws/global-infrastructure/localzones/).
3. (Optional) Set up the
 [landing
 zone](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html) for centralized management and governance.
 Then add the Outpost accounts to your AWS Organization.
4. Configure access levels for your accounts for proper
 permissions and security.
5. Deploy regulated workloads on AWS Local Zones and AWS Outposts. Optionally, you can configure backups and
 snapshots to be stored within the Region and synchronize
 your Amazon S3 data accordingly.

![Reference architecture that uses Outposts to navigate maintaining a primary service copy of data within a country or jurisdiction](/images/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/scenario-C-outposts.png)

*Scenario C, option two: AWS Outposts*

The second option for deploying AWS
 services focuses on the use of AWS Outposts:

1. Assess data residency requirements specific to the
 organization and regulatory environment, and identify
 regulated data.
2. Plan, order, and deploy
 [AWS Outposts racks](https://aws.amazon.com/outposts/rack/) in the corporate data centers with
 [high
 availability](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/aws-outposts-high-availability-design.html).
3. (Optional) Set up the
 [landing
 zone](https://docs.aws.amazon.com/controltower/latest/userguide/setting-up.html) for centralized management and governance.
 Then add the Outpost accounts to your AWS Organization.
4. Configure access levels for your accounts for proper
 permissions and security.
5. Deploy regulated workloads on AWS Outposts. Optionally,
 you can configure backups and snapshots to be stored
 within the Region and synchronize your Amazon S3 data
 accordingly.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/scenario-c-maintain-primary-service-copy-within-country-or-jurisdiction.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
