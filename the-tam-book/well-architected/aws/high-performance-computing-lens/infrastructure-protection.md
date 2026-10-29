<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/infrastructure-protection.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Infrastructure protection

HPC clusters can be separated by workload components into
 different network layers based on their data sensitivity, access
 requirements, and functional purpose. When separated by layers,
 traffic can be controlled between layers and additional controls
 can be applied based on layer requirements as part of a
 defense-in-depth security approach.

###### Best practices

- [HPCSEC01-BP01 Separate HPC cluster components in different network layers](#hpcsec01-bp01)
- [HPCSEC01-BP02 Control traffic flow within your HPC cluster](#hpcsec01-bp02)

## HPCSEC01-BP01 Separate HPC cluster components in different network layers

When architecting for
 [SEC05-BP01](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_create_layers.html),
 you create network layers and separate components into different
 layers. In HPC clusters, you can separate different cluster
 components, such as head node, login nodes, and compute
 resources. For example, with AWS ParallelCluster, the cluster
 head node can be separated from the compute resources. The head
 node could be running in a public subnet with the compute fleet
 running in a private subnet. Additionally, you could further
 isolate your cluster by running in private subnets with private
 connectivity to the cluster.

## HPCSEC01-BP02 Control traffic flow within your HPC cluster

According to
 [SEC05-BP02](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_network_protection_layered.html),
 you control traffic flow within your network layers. You permit
 only the network flows necessary for the components of your
 workloads to communicate. When running tightly coupled HPC
 workloads with Elastic Fabric Adapter (EFA), EFA requires being
 a member of a security group allowing all inbound and outbound
 traffic to and from itself. Each cluster member will allow all
 traffic between members when processing the same EFA-based job.

Clusters are commonly used with multiple running jobs and a
 single security group would be used for all EFA traffic without
 separation by job. If your environment requires further security
 separation by job, consider an alternative design, such as
 multiple clusters or a more advanced security group mapping,
 rather than having one security group for all traffic between
 members.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/infrastructure-protection.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
