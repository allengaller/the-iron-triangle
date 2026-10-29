<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-your-network-topology.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Plan your network topology

Workloads often exist in multiple environments. These include multiple cloud environments
 (both publicly accessible and private) and possibly your existing data center infrastructure.
 Plans must include network considerations, such as intrasystem and intersystem connectivity,
 public IP address management, private IP address management, and domain name resolution.

When architecting systems using IP address-based networks, you must plan network topology
 and addressing in anticipation of possible failures, and to accommodate future growth and
 integration with other systems and their networks.

Amazon Virtual Private Cloud (Amazon VPC) lets you provision a private, isolated section of the AWS Cloud where
 you can launch AWS resources in a virtual network.

###### Best practices

- [REL02-BP01 Use highly available network connectivity for your workload public endpoints](./rel_planning_network_topology_ha_conn_users.html)
- [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](./rel_planning_network_topology_ha_conn_private_networks.html)
- [REL02-BP03 Ensure IP subnet allocation accounts for expansion and availability](./rel_planning_network_topology_ip_subnet_allocation.html)
- [REL02-BP04 Prefer hub-and-spoke topologies over many-to-many mesh](./rel_planning_network_topology_prefer_hub_and_spoke.html)
- [REL02-BP05 Enforce non-overlapping private IP address ranges in all private address spaces where they are connected](./rel_planning_network_topology_non_overlap_ip.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/plan-your-network-topology.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
