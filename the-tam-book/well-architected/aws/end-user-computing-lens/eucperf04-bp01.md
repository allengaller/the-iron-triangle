<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp01.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# EUCPERF04-BP01 Evaluate available instance types (AppStream) and hardware bundles (WorkSpaces)

WorkSpaces Applications groups instances into families, such as General Purpose (stream.standard).
 Within each family, there are different instance sizes, such as stream.standard.medium and
 stream.standard.large. Each size has a different number of vCPUs and memory. Graphics
 optimized families include instances with one or more GPUs. For more information on the
 Graphics G4 (stream.graphics.g4dn), Graphics G5 (stream.graphics.g5), and Memory Optimized
 (stream.memory.z1d) families, see [Amazon EC2
 Instance Types](https://aws.amazon.com/ec2/instance-types/).

**Level of risk exposed if this best practice is not
 established:** Medium

## Implementation guidance

WorkSpaces bundle selection begins with determining if your workload requires a GPU. If it
 does, evaluate the Graphics G4 and Graphics G5 families. If it does not require a GPU,
 evaluate the General Purpose, Compute Optimized, and Memory Optimized families. In
 addition to large amounts of memory, stream.memory.z1d instances offer the highest CPU
 clock rates of the WorkSpaces Applications instance family.

WorkSpaces provides hardware bundles with different amounts of vCPUs and memory.
 Graphics.G4dn and GraphicsPro.G4dn bundles include GPUs.

For specifications and recommended uses cases, see [Amazon WorkSpaces](https://aws.amazon.com/workspaces-family/workspaces/pricing/).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucperf04-bp01.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
