<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/choose-a-power-efficient-programming-language.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Choose a power efficient programming language

Programming languages have varying levels of efficiency when it
 comes to power consumption. Some languages, such as C and C++,
 are known for their low-level, close-to-hardware nature, which
 allows for fine-grained control over system resources and can
 result in more power-efficient code. On the other hand,
 interpreted languages like Python or JavaScript, may have higher
 levels of abstraction and runtime overhead, which can result in
 several times higher power consumption, as outlined in this
 [AWS blog](https://aws.amazon.com/blogs/opensource/sustainability-with-rust/).

Modern compilers often provide optimization options that can
 reduce code size, remove unnecessary computations, and optimize
 register usage, which can lead to more power-efficient code. For
 code sections that are executed at a high frequency (or are time
 sensitive), enabling compiler optimizations, such as loop
 unrolling, function inlining, and dead code reduction, can
 result in more efficient code execution and lower power
 consumption.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/choose-a-power-efficient-programming-language.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
