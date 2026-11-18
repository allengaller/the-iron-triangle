<!-- source: https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Implement zero trust

# Implement zero trust Stay organized with collections Save and categorize content based on your preferences.

This principle in the security pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
helps you ensure comprehensive security across your cloud workloads. The principle
of zero trust emphasizes the following practices:

- Eliminating implicit trust
- Applying the principle of least privilege to access control
- Enforcing explicit validation of all access requests
- Adopting an *assume-breach* mindset to enable continuous verification and
security posture monitoring

## Principle overview

The *zero-trust* model shifts the security focus from perimeter-based security
to an approach where no user or device is considered to be inherently
trustworthy. Instead, every access request must be verified, regardless of its
origin. This approach involves authenticating and authorizing every user and
device, validating their context (location and device posture), and granting
least privilege access to only the necessary resources.

Implementing the zero-trust model helps your organization enhance its
security posture by minimizing the impact of potential breaches and protecting
sensitive data and applications against unauthorized access. The zero-trust
model helps you ensure confidentiality, integrity, and availability of data and
resources in the cloud.

## Recommendations

To implement the zero-trust model for your cloud workloads, consider the
recommendations in the following sections:

- [Secure your network](#secure_your_network)
- [Verify every access attempt explicitly](#verify_every_access_attempt_explicitly)
- [Monitor and maintain your network](#monitor_and_maintain_your_network)

### Secure your network

This recommendation is relevant to the following
[focus area](/architecture/framework/security#focus_areas_of_cloud_security):
Infrastructure security.

Transitioning from conventional perimeter-based security to a zero-trust model
requires multiple steps. Your organization might have already integrated certain
zero-trust controls into its security posture. However, a zero-trust model
isn't a singular product or solution. Instead, it's a holistic integration of
multiple security layers and best practices. This section describes
recommendations and techniques to implement zero trust for network security.

- **Access control**: Enforce access controls based on user identity and
context by using solutions like
[Chrome Enterprise Premium](https://chromeenterprise.google/products/chrome-enterprise-premium/) 
and
[Identity-Aware Proxy (IAP)](/iap/docs/concepts-overview).
By doing this, you shift security from the network perimeter to individual
users and devices. This approach enables granular access control and
reduces the attack surface.
- **Network security**: Secure network connections between your
on-premises, Google Cloud, and multicloud environments.
Use the private connectivity methods from
[Cloud Interconnect](/network-connectivity/docs/interconnect/concepts/overview) 
and
[IPsec VPNs](/network-connectivity/docs/vpn/concepts/overview).
To help secure access to Google Cloud services and APIs, use
[Private Service Connect](/vpc/docs/private-service-connect).
To help secure outbound access from workloads deployed on
[Google Kubernetes Engine (GKE)](/kubernetes-engine/docs/concepts/kubernetes-engine-overview) and related products,
use
[Cloud Service Mesh egress gateways](/service-mesh/docs/security/egress-gateways-best-practices).
- **Network design**: Prevent potential security risks by deleting default
networks in existing projects and disabling the creation of default
networks in new projects.
To avoid conflicts, plan your network and IP address allocation
carefully.
To enforce effective access control, limit
the number of Virtual Private Cloud (VPC) networks per project.
- **Segmentation**: Isolate workloads but maintain centralized network
management.
To segment your network environments, use multiple VPC networks and
define firewall policies and rules at the organization, folder, and VPC
network levels.
To centralize network administration for resources that are in separate
projects, use
[Shared VPC](/vpc/docs/shared-vpc).
For example, administrators of a service project can create
Compute Engine instances that use approved subnets from the project
that hosts a centrally administered Shared VPC network.
To prevent
[data exfiltration](https://en.wikipedia.org/wiki/Data_exfiltration),
establish secure perimeters around sensitive Google Cloud APIs and
services by using
[VPC Service Controls](/vpc-service-controls/docs/overview),
and use strict egress firewall rules to restrict internet-bound traffic.
- **Perimeter security**: Protect against DDoS attacks and web application
threats.
To protect against threats, use
[Google Cloud Armor](/armor/docs).
Configure security policies to allow, deny, or redirect traffic at the
Google Cloud edge.
- **Automation**: Automate infrastructure provisioning by embracing
infrastructure as code (IaC) principles and by using tools like Terraform,
Jenkins, and
[Cloud Build](/build/docs/overview).
IaC helps to ensure consistent security configurations, simplified
deployments, and rapid rollbacks in case of issues.
- **Secure foundation**: Establish a secure application environment by
using the
[Enterprise foundations blueprint](/architecture/blueprints/security-foundations).
This blueprint provides prescriptive guidance and automation scripts to
help you implement security best practices and configure your
Google Cloud resources securely.

### Verify every access attempt explicitly

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Identity and access management
- Security operations (SecOps)
- Logging, auditing, and monitoring

Implement strong authentication and authorization mechanisms for any user,
device, or service that attempts to access your cloud resources. Don't rely on
location or network perimeter as a security control. Don't automatically trust
any user, device, or service, even if they are already inside the network.
Instead, every attempt to access resources must be rigorously authenticated and
authorized. You must implement strong identity verification measures, such as
multi-factor authentication (MFA). You must also ensure that access decisions
are based on granular policies that consider various contextual factors like
user role, device posture, and location.

To implement this recommendation, use the following methods, tools, and
technologies:

- **Unified identity management**: Ensure consistent identity management
across your organization by using a single identity provider (IdP).
Google Cloud supports federation with most IdPs, including
on-premises
[Active Directory](/architecture/identity/federating-gcp-with-active-directory-introduction).
Federation lets you extend your existing identity management infrastructure
to Google Cloud and enable single sign-on (SSO) for users.
If you don't have an existing IdP, consider using
[Cloud Identity Premium](/identity/docs/editions) 
or
[Google Workspace](https://workspace.google.com/).
- **Limited service account permissions**: Use
[service accounts](/iam/docs/service-account-overview) 
carefully, and adhere to the principle of least privilege.
Grant only the
necessary permissions required for each service account to perform its
designated tasks.
Use
[Workload Identity Federation](/iam/docs/workload-identities) 
for applications that run on Google Kubernetes Engine (GKE) or run outside
Google Cloud to access resources securely.
- **Robust processes**: Update your identity processes to align with cloud
security best practices.
To help ensure compliance with regulatory
requirements, implement identity governance to track access, risks, and
policy violations.
Review and update your existing processes for granting
and auditing access-control roles and permissions.
- **Strong authentication**: Implement SSO for user authentication and
implement MFA for privileged accounts.
Google Cloud supports various
MFA methods, including
[Titan Security Keys](https://cloud.google.com/security/products/titan-security-key),
for enhanced security.
For workload authentication, use OAuth 2.0 or signed JSON Web Tokens (JWTs).
- **Least privilege**: Minimize the risk of unauthorized access and data
breaches by enforcing the principles of least privilege and separation of
duties.
Avoid overprovisioning user access.
Consider implementing just-in-time privileged access for sensitive
operations.
- **Logging**: Enable audit logging for administrator and data access
activities.
For analysis and threat detection, scan the logs by using
[Security Command Center Enterprise](/security-command-center/docs/service-tiers#enterprise-tier) 
or
[Google Security Operations](/chronicle/docs/secops/secops-overview).
Configure appropriate log retention policies to balance security needs
with storage costs.

### Monitor and maintain your network

This recommendation is relevant to the following
[focus areas](/architecture/framework/security#focus_areas_of_cloud_security):

- Logging, auditing, and monitoring
- Application security
- Security operations (SecOps)
- Infrastructure security

When you plan and implement security measures, assume that an attacker is
already inside your environment. This proactive approach involves using the following
multiple tools and techniques to provide visibility into your network:

- **Centralized logging and monitoring**: Collect and
analyze security logs from all of your cloud resources through centralized
[logging and monitoring](/stackdriver/docs).
Establish baselines for normal network behavior, detect anomalies, and
identify potential threats.
Continuously analyze network traffic flows to identify suspicious patterns
and potential attacks.
- **Insights into network performance and security**: Use tools like
[Network Analyzer](/network-intelligence-center/docs/network-analyzer/overview).
Monitor traffic for unusual protocols, unexpected connections, or sudden spikes
in data transfer, which could indicate malicious activity.
- **Vulnerability scanning and remediation**: Regularly scan your network and applications for vulnerabilities.
Use [Web Security Scanner](/security-command-center/docs/concepts-vulnerabilities-findings),
which can automatically identify vulnerabilities in your
Compute Engine instances, containers, and GKE clusters.
Prioritize remediation based on the severity of vulnerabilities and their
potential impact on your systems.
- **Intrusion detection**: Monitor network traffic for malicious activity and
automatically block or get alerts for suspicious events by using
[Cloud IDS](/intrusion-detection-system/docs/overview) 
and
[Cloud NGFW intrusion prevention service](/firewall/docs/about-intrusion-prevention).
- **Security analysis**: Consider implementing
[Google SecOps](/chronicle/docs/secops/secops-overview) 
to correlate security events from various sources, provide real-time analysis of
security alerts, and facilitate incident response.
- **Consistent configurations**: Ensure that you have consistent security
configurations across your network by using configuration management tools.

---

> 原页面：https://docs.cloud.google.com/architecture/framework/security/implement-zero-trust（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
