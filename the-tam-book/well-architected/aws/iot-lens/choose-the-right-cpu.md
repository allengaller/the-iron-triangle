<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/choose-the-right-cpu.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Choose the right CPU

To optimize energy consumption, choose a CPU that meets the
 performance requirements of your application without exceeding
 them. Keep in mind that a more powerful processor may have
 higher performance per watt compared to a less powerful
 processor, and can perform more work per unit of power consumed,
 resulting in lower energy consumption. Newer CPU architectures
 or higher-end processors may have better power efficiency at
 higher workloads due to advancements in technology or
 microarchitecture, resulting in a more energy-efficient solution
 overall. Use performance per watt as a guideline, and test CPUs
 against your actual workload to make a final choice.

Choose a CPU that is designed for power efficiency. These CPUs
 feature sleep and idle states to reduce power consumption during
 periods of inactivity. These states allow the CPU to minimize
 power usage by either reducing the clock frequency, halting
 execution, or shutting down certain components when they are not
 required.

The Instruction Set Architecture (ISA) of a CPU, which defines
 its instruction set and programming model, can also impact power
 consumption. Some features, such as complex out-of-order
 execution and speculative execution, can increase power
 consumption due to the increased hardware complexity and
 activity. RISC (Reduced Instruction Set Computing)
 architectures, such as ARM and RISC-V, are generally known for
 their power efficiency compared to CISC (Complex Instruction Set
 Computing) architectures, such as x86.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/choose-the-right-cpu.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
