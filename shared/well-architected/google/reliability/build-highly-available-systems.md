<!-- source: https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems -->
<!-- captured: 2026-10-25 -->
<!-- vendor: google -->

# Build highly available systems through resource redundancy

This principle in the reliability pillar of the
[Google Cloud Well-Architected Framework](/architecture/framework) 
provides recommendations to plan, build, and manage resource redundancy, which
can help you to avoid failures.

This principle is relevant to the *scoping*
[focus area](/architecture/framework/reliability#focus-areas) 
of reliability.

## Principle overview

After you
[decide the level of reliability](/architecture/framework/reliability/set-targets) 
that you need, you must design your systems to avoid any
[single points of failure](/architecture/infra-reliability-guide/design#avoid_single_points_of_failure).
Every critical component in the system must be replicated across multiple
machines, zones, and
[regions](/docs/geography-and-regions#regions_and_zones).
For example, a critical database can't be located in only one region, and a
metadata server can't be deployed in only one single zone or region. In those
examples, if the sole zone or region has an outage, the system has a global
outage.

## Recommendations

To build redundant systems, consider the recommendations in the following
subsections.

### Identify failure domains and replicate services

Map out your system's
[failure domains](/architecture/infra-reliability-guide/building-blocks),
from individual VMs to regions, and design for redundancy across the failure
domains.

To ensure high availability, distribute and replicate your services and
applications across multiple zones and regions. Configure the system for
automatic failover to make sure that the services and applications continue to
be available in the event of zone or region outages.

For examples of multi-zone and multi-region architectures, see
[Design reliable infrastructure for your workloads in Google Cloud](/architecture/infra-reliability-guide/design#deployment_architectures).

### Detect and address issues promptly

Continuously track the status of your failure domains to detect and address
issues promptly.

You can monitor the current status of Google Cloud services in all regions
by using the
[Google Cloud Service Health dashboard](https://status.cloud.google.com/).
You can also view incidents relevant to your project by using
[Personalized Service Health](https://cloud.google.com/service-health).
You can use load balancers to detect resource health and automatically route
traffic to healthy backends. For more information, see
[Health checks overview](/load-balancing/docs/health-check-concepts).

### Test failover scenarios

Like a fire drill, regularly simulate failures to validate the effectiveness of
your replication and failover strategies.

For more information, see
[Simulate a zone outage for a regional MIG](/compute/docs/instance-groups/regional-mig-simulate-zonal-outage) 
and
[Simulate a zone failure in GKE regional clusters](/kubernetes-engine/docs/tutorials/simulate-zone-failure).

---

> 原页面：https://docs.cloud.google.com/architecture/framework/reliability/build-highly-available-systems（抓取时点 2026-10-25；正文为自动抓取，排版已规整，语义未改写）
