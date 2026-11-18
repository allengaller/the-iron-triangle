<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec10-bp02.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCSEC10-BP02 Restrict access to open ports on instances to reduce risks

Restrict use of network ports on end user systems to reduce the
 potential exposure surface of these systems. Block network ports
 that aren't required for the operation and support of end user
 systems using host-based or network firewalls.

**Level of risk exposed if this best
 practice is not established:** High

## Implementation guidance

Implement networking security controls on Amazon EUC
 instances. AWS provides several services and capabilities that
 can help you secure AWS EUC instances for Amazon WorkSpaces
 and WorkSpaces Applications. In addition to these services, consider OS
 capabilities and additional software to provide the required
 level of security.

For AWS networking, the following services and features should
 be evaluated:

- Network ACLs
- Security groups
- AWS Network Firewall
- NAT Gateway

Consider these services to create a baseline of network
 security. Additionally, review and explore
 [best
 practices for VPC and networking in WorkSpaces](https://d1.awsstatic.com/whitepapers/best-practices-vpcs-networking-amazon-workspaces-deployments.pdf), as well
 as
 [best practices for deploying WorkSpaces Applications](https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/best-practices-for-deploying-amazon-appstream-2.html), as you evaluate
 your network security.

In addition to AWS security capabilities and services, when
 users require access to the Internet from browsers installed
 in Amazon WorkSpaces or WorkSpaces Applications instances, consider
 using a web proxy to log web site access and implement
 restrictions on where users can browse.

In Amazon WorkSpaces and WorkSpaces Applications instances, consider
 existing OS software to harden the instances. For example, you
 can use host-based firewalls available within the operating
 system to restrict accessible ports in your instances. In
 addition, consider endpoint protection software to identify
 and mitigate security risks that may be introduced into the
 environment using software local to the instances. For detail
 on the ports required by Amazon WorkSpaces and WorkSpaces Applications,
 see the following:

- [List of ports required by Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/creating-streaming-from-interface-vpc-endpoints.html)
- [List
 of ports required for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-port-requirements.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucsec10-bp02.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
