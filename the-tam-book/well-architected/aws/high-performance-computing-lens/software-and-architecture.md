<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/software-and-architecture.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Software and architecture

By enabling remote visualization of simulation results, rather
 than transferring and storing large datasets locally,
 organizations can minimize network traffic, optimize resource
 usage, and improve overall sustainability of their HPC operations.

## HPCSUS02-BP01 Use a VDI solution to reduce data movement

In
 [SUS03-BP05
 Use software patterns and architectures that best support data
 access and storage patterns](https://docs.aws.amazon.com/wellarchitected/latest/sustainability-pillar/sus_sus_software_a6.html), you understand how data is
 used within your workload, consumed by your users, transferred,
 and stored. For HPC workloads, Virtual Desktop Infrastructure
 (VDI) technologies help you reduce network traffic between the
 end-users' clients rather than transferring the entire data set
 and duplicating storage on-premises. In addition, optimizing
 data movement across the network reduces the total networking
 resources required for the workload and lowers its environmental
 impact.

### Implementation guidance

Use a remote visualization technology, such as Amazon DCV or
 Amazon AppStream 2.0, to visualize the results of your
 simulations without the need of copying back the results.

## Key AWS services

- [Amazon
 DCV](https://aws.amazon.com/hpc/dcv/)
- [Amazon
 AppStream 2.0](https://aws.amazon.com/appstream2/)
- [Research
 and Engineering Studio on AWS](https://aws.amazon.com/hpc/res/)

## Resources

- [Empowering
 Researchers to Run HPC Workloads on AWS with Research
 Gateway](https://aws.amazon.com/blogs/apn/empowering-researchers-to-run-hpc-workloads-on-aws-with-research-gateway/)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/high-performance-computing-lens/software-and-architecture.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
