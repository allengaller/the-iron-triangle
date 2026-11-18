<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/definitions.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Definitions

Following is a list of definitions related to the AWS
 Well-Architected Framework and EUC workloads.

## AWS Definitions

- EUC
**Amazon WorkSpaces Applications:** Secure, reliable, and
 scalable application streaming and low-cost virtual
 desktop service**Amazon WorkSpaces Family:** Comprehensive, fully
 persistent, Virtual Desktop Infrastructure for most worker
 types**Amazon WorkSpaces Core :** Virtual desktop
 infrastructure APIs for third-party VDI software**Amazon WorkSpaces Secure Browser :** Secure,
 low-cost browser service for access to internal websites
 and Software as a Service apps**Amazon
 WorkDocs :** Secure document sharing and
 content collaboration—connecting teams everywhere**Amazon
 DCV :** Amazon DCV is a high-performance
 remote display protocol that provides secure remote
 desktop delivery and application streaming, avoiding the
 need for expensive dedicated workstations.
- Hardware
**Amazon WorkSpaces Thin Client :** Reduce costs,
 simplify logistics, and accelerate deployment using
 virtual desktops
- Storage
**Amazon FSx :** Launch, run, and scale feature-rich
 and highly performant file systems with just a few clicks**Amazon S3 :** Object storage built to retrieve any
 amount of data from anywhere**Amazon EFS :** Share file data without
 provisioning storage
- Compute
**Amazon EC2 :** Secure and resizable compute
 capacity for virtually any workload
- Cost
**Amazon WorkSpaces Family Pricing :** Pricing
 across the Amazon WorkSpaces Family services is designed
 to be flexible and cost-effective, allowing you to pay for
 the resources you need without over provisioning.**Bring
 Your Own Windows Desktop Licenses
 (BYOL) :** If your licensing agreement with
 Microsoft allows it, you can bring and deploy your Windows
 10 or 11 desktop on your WorkSpaces.**Cost
 Optimizer for Amazon WorkSpaces Applications :**
 Monitors your WorkSpaces Applications app block builders and image**Cost
 Optimizer for Amazon WorkSpaces :** Monitor
 Amazon WorkSpaces usage and optimize costs builders and
 notifies you and/or stops them when they are active for
 longer than specified thresholds.
- Managed directories for WorkSpaces
**AD
 Connector :** A directory gateway with
 which you can redirect directory requests to your
 on-premises Microsoft Active Directory without caching any
 information in the cloud.**AWS Managed Microsoft AD :** Directory Service lets you run Microsoft Active Directory (AD) as a
 managed service.**Simple
 AD :** Provides a subset of the features
 offered by AWS Managed Microsoft AD, including the ability
 to manage user accounts and group memberships, create and
 apply group policies, securely connect to Amazon EC2
 instances, and provide Kerberos-based single sign-on
 (SSO).**Cross
 Trust :** You can establish a trust
 relationship between your AWS Managed Microsoft AD
 directory and your on-premises domain.
- Protocols for Amazon WorkSpaces
**Amazon
 WSP (WorkSpaces Streaming Protocol) :**
 Built using
 [Amazon
 DCV](https://aws.amazon.com/hpc/dcv/) technology, enabling high-performance remote
 access to Amazon WorkSpaces instances for a wide range of
 workloads and use cases.**PCoIP
 (PC over IP) :** Amazon WorkSpaces supports
 PCoIP when needed based on the type of devices your users
 will be accessing their WorkSpaces from, which operating
 system is on your WorkSpaces, what network conditions your
 users will be facing, and whether your users require
 bidirectional video support.
- Networking
**Internet
 gateway :** Horizontally scaled, redundant,
 and highly available VPC component that allows
 communication between your VPC and the internet. It
 supports IPv4 and IPv6 traffic.**NAT gateway :**
 Allow resources in private subnets to connect to the
 internet, other VPCs, or on-premises networks. These
 instances can communicate with services outside the VPC,
 but they cannot receive unsolicited connection requests.**Public
 subnets :** Subnet which has a direct route
 to an internet gateway. Resources in a public subnet can
 access the public internet.**Private
 subnets :** Subnet which does not have a
 direct route to an internet gateway. Resources in a
 private subnet require a
 [NAT
 device](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat.html) to access the public internet.**Amazon Virtual Private Cloud (VPC) :** Launch AWS
 resources in a logically isolated virtual network that
 you've defined. This virtual network closely resembles a
 traditional network that you'd operate in your own data
 center, with the benefits of using the scalable
 infrastructure of AWS.**AWS Regions :** Each Region is designed to be
 isolated from the other Regions. This achieves the
 greatest possible fault tolerance and stability.[Availability
 Zone:](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) Each Region has multiple, isolated
 locations known as Availability Zones.**Amazon Route 53 :** A reliable and cost-effective
 way to route end users to your Internet applications. As
 such, Amazon Route 53 is a highly available and scalable
 Domain Name System (DNS) web service that connects user
 requests to internet applications running on AWS or
 on-premises.**DHCP
 Option Sets in Amazon VPC :** Network
 devices in your VPC use Dynamic Host Configuration
 Protocol (DHCP). You can use DHCP option sets to
 control: The DNS servers, domain names, or Network Time
 Protocol (NTP) servers used by the devices in your VPC and
 whether DNS resolution is enabled in your VPC.
- Security
**AWS Identity and Access Management (IAM):**
 Helps an administrator securely control access to AWS
 resources.**Security
 groups :** Controls the traffic that is
 allowed to reach and leave the resources that it is
 associated with.
- Monitoring
**Amazon CloudWatch :** Provides a reliable,
 scalable, and flexible monitoring solution that you can
 start using within minutes. You no longer need to set up,
 manage, and scale your own monitoring systems and
 infrastructure.**Amazon EventBridge :** Serverless event bus to
 build event-driven applications at scale.**VPC
 Flow Logs :** Enables you to capture
 information about the IP traffic going to and from network
 interfaces in your VPC.
- Management
**AWS Management Console :** Everything you need
 to access and manage the AWS Cloud in one web interface**AWS Command Line Interface (CLI) :** A unified
 tool to manage your AWS services. You can control multiple
 AWS services from the command line and automate them
 through scripts.**Amazon WorkSpaces API :** Provides detailed
 information about the actions, data types, parameters, and
 errors of the WorkSpaces service.**Tag
 Editor :** Tags are key and value pairs
 that act as metadata for organizing your AWS resources.**AWS Organizations :** An account management
 service that enables you to consolidate multiple AWS accounts into an organization that you create and
 centrally manage. AWS Organizations includes account
 management and consolidated billing capabilities that
 enable you to better meet the budgetary, security, and
 compliance needs of your business.**End
 User Compute (EUC) Toolkit :** Offers a
 range of features to help manage EUC workloads at scale.**Service
 control policies (SCPs) :** A type of
 organization policy that you can use to manage permissions
 in your organization. SCPs offer central control over the
 maximum available permissions for the accounts in your
 organization. SCPs help you to verify that your accounts
 stay within your organization's access control guidelines.
- WorkSpaces
**Running
 mode :**
**AlwaysOn:** Use when
 paying a fixed monthly fee for unlimited usage of your
 WorkSpaces. This mode is best for users who use their
 WorkSpace full time as their primary desktop.**AutoStop:** Use when
 paying for your WorkSpaces by the hour. With this
 mode, your WorkSpaces stop after a specified period of
 disconnection, and the state of apps and data is
 saved.**WorkSpace
 bundles and images :**
**WorkSpace bundle:** A
 WorkSpace bundle is a combination of an operating
 system, and storage, compute, and software resources.
 When you launch a WorkSpace, you select the bundle
 that meets your needs. The default bundles available
 for WorkSpaces are called public bundles.**Custom image:** If
 you have launched a Windows or Linux WorkSpace and
 have customized it, you can create a custom image from
 that WorkSpace. A custom image contains only the OS,
 software, and settings for the WorkSpace.**Custom bundle:**
 After you create a custom image, you can build a
 custom bundle that combines the custom WorkSpace image
 and the underlying compute and storage configuration
 that you select. You can then specify this custom
 bundle when you launch new WorkSpaces to make sure
 that the new WorkSpaces have the same consistent
 configuration (hardware and software).
- WorkSpaces Applications
**Fleet
 types :**
**OnDemand:** Streaming
 instances run only when users are streaming
 applications and desktops.**Always-On:**
 Streaming instances run constantly, even when no users
 are streaming applications and desktops.**Elastic:** The pool
 of streaming instances is managed by WorkSpaces Applications.
 When your users select their application or desktop to
 launch, they will start streaming after the app block
 has been downloaded and mounted to a streaming
 instance.**Images :** You
 can create Amazon WorkSpaces Applications images that contain
 applications you can stream to your users and default
 system and application settings to enable your users to
 get started with those applications quickly.**Image
 Builders :** Amazon WorkSpaces Applications uses EC2
 instances to stream applications. You launch instances
 from base images, called image builders, which AppStream
 2.0 provides. To create your own custom image, you connect
 to an image builder instance, install and configure your
 applications for streaming, and then create your image by
 creating a snapshot of the image builder instance.

## Partner software

- **WorkSpot:** A software
 partner that provides cloud-native virtual desktop
 infrastructure (VDI) turnkey solutions.
- **LeoStream:** A software
 partner that provides remote desktop access solutions
 supporting hosted desktop deployments.
- **VMWare:** A virtualization
 software provider.
- **ControlUp:** Provides support
 to IT teams when monitoring and troubleshooting virtual
 desktop systems. Offers real-time monitoring, troubleshooting,
 automation, and data analytics.
- **Nuvens:** A member of AWS'
 Partner Network (APN) that supports AWS' virtual desktop
 services, namely Amazon WorkSpaces Manager and WorkSpaces Applications.
 Our services support AWS' customers to provision, secure, and
 extract intelligence from end-point devices, end-user apps,
 and data on AWS.
- **LiquidWare:** Provides a
 bundle of solutions including ProfileUnity, FlexApp and
 Stratusphere UX that can be used to begin as on-premises VDI
 desktops and can provide a migration path to cloud-hosted or
 desktops as a service (DaaS), with a secure, high-quality
 work-from-anywhere desktop experience.
- **Lakeside Software:** Offers a
 suite of virtual solutions such as ProActiveIT, DEX, HelpDesk,
 Digital Workplace, and Systrack.

## Industry definitions

- **Security
 Assertion Markup Language (SAML) 2.0 :** A
 standard for exchanging authentication and authorization
 identities between security domains.
- **Pooled:** Creates a set (or
 pool) of virtual desktops. Users are connected to one of the
 machines and it is users' machine for the duration they are
 connected to it. Once the user disconnects, the machine
 becomes available to the pool again and a different user will
 be allocated to it.
- **Non-pooled
 (dedicated):** Provides each user with a persistent
 dedicated virtual machine. This approach offers individual
 isolation and customization options.
- **Federal
 Risk and Authorization Management Program
 (FedRAMP) :** A US government-wide program that
 delivers a standard approach to the security assessment,
 authorization, and continuous monitoring for cloud products
 and services.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/definitions.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
