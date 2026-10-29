<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/reliability.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Reliability

When agents reason, plan, and act through large language models, reliability takes on dimensions that traditional infrastructure patterns don't address. LLM decisions are stochastic, multi-agent coordination introduces new failure modes, and memory integrity becomes a first-class concern. An agent that works perfectly in testing may behave unpredictably in production when context windows fill up, models return unexpected outputs, or downstream agents become unavailable. This pillar provides best practices for building agent systems that execute tasks predictably, recover from failures automatically, and maintain partial functionality even under adverse conditions.

**Capabilities**

- [Predictable agent behavior](agentrel01.html)
- [Predictable task execution](agentrel02.html)
- [Agent memory and state management](agentrel03.html)
- [Multi-agent orchestration](agentrel04.html)
- [Agent cognition](agentrel05.html)
- [Legacy system integration](agentrel06.html)
- [Agent monitoring, management and recovery](agentrel07.html)
- [Graceful degradation and configuration management](agentrel08.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/reliability.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
