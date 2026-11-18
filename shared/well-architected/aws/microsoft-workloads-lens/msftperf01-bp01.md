<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf01-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# MSFTPERF01-BP01 Consider AWS Elastic Beanstalk for running traditional Windows servers hosting your Microsoft application

In scenarios where the traditional virtual machine approach is a
 requirement, evaluate the EC2 instance families that better address
 your Microsoft workload needs. Using data-driven decisions for
 architectural considerations, you can also opt for Elastic Beanstalk
 to reduce the operational overhead on managing the EC2 instances and
 surrounding infrastructure resources, such as Elastic Load Balancing, and Auto Scaling Groups.

**Desired outcome:** Optimize
 performance efficiency for traditional Microsoft applications by
 leveraging AWS Elastic Beanstalk to reduce operational overhead
 while maintaining the familiar Windows Server environment, enabling
 faster deployments, automated scaling, and simplified infrastructure
 management without sacrificing application performance or
 functionality.

**Common anti-patterns:**

- Managing EC2 instances manually for Microsoft applications
 without leveraging platform services, leading to increased
 operational complexity, slower deployment cycles, and higher
 maintenance overhead for load balancing and scaling
 configurations.
- Choosing inappropriate EC2 instance families for Microsoft
 workloads without considering performance requirements,
 resulting in either over-provisioned resources that waste costs
 or under-provisioned instances that impact application
 performance.
- Implementing traditional deployment approaches without
 considering managed platform services, missing opportunities to
 improve deployment speed, reliability, and operational
 efficiency through automation and best practices.

**Benefits of establishing this best
 practice:**

- Reduced operational overhead through automated infrastructure
 management, including load balancing, auto scaling, and health
 monitoring, allowing teams to focus on application development
 rather than infrastructure maintenance.
- Improved deployment efficiency and reliability through AWS Elastic Beanstalk's automated deployment processes, version
 management, and rollback capabilities that streamline
 application updates and reduce deployment risks.
- Enhanced performance optimization through automatic scaling
 capabilities and integrated monitoring that ensures Microsoft
 applications maintain optimal performance during varying load
 conditions.

**Level of risk exposed if this best practice
 is not established:** Low

## Implementation guidance

Implementing AWS Elastic Beanstalk for Microsoft applications
 requires understanding your application requirements and
 configuring the platform appropriately for Windows workloads.
 Begin by assessing your current application architecture and
 deployment processes, then configure Elastic Beanstalk with the
 appropriate instance types and platform settings to optimize
 performance while reducing operational complexity.

### Implementation steps

1. Assess your Microsoft application requirements including
 runtime dependencies, performance needs, and scaling
 patterns to determine appropriate Elastic Beanstalk
 configuration.
2. Choose the appropriate AWS Elastic Beanstalk platform
 version that supports your .NET Framework or .NET Core
 application requirements.
3. Select optimal EC2 instance families based on your
 application's compute, memory, and I/O requirements,
 considering options like m7i, r7i, or c7i instances.
4. Configure AWS Elastic Beanstalk environment settings
 including auto scaling policies, load balancer
 configuration, and health check parameters.
5. Set up application deployment processes using AWS Elastic Beanstalk deployment methods such as rolling deployments or
 blue/green deployments.
6. Implement monitoring and logging integration with Amazon CloudWatch to track application performance and
 infrastructure metrics.
7. Configure environment variables and application settings
 through AWS Elastic Beanstalk configuration options to
 maintain environment-specific configurations.
8. Establish backup and disaster recovery procedures using AWS Elastic Beanstalk's configuration management and version
 control capabilities.

## Resources

**Related documents:**

- [Using
 Elastic Beanstalk with .NET](https://docs.aws.amazon.com/elasticbeanstalk/latest/platforms/platforms-supported.html#platforms-supported.net)
- [Seamless
 Production Deployment with Elastic Beanstalk](https://aws.amazon.com/blogs/dotnet/seamless-production-deployment-with-elastic-beanstalk/)

**Related tools:**

- [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/Welcome.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/microsoft-workloads-lens/msftperf01-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
