<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/responding-to-events.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Responding to events

You should anticipate operational events, both planned (for
 example, sales promotions, deployments, and failure tests) and
 unplanned (for example, surges in utilization and component
 failures). You should use your existing runbooks and playbooks to
 deliver consistent results when you respond to alerts. Defined
 alerts should be owned by a role or a team that is accountable for
 the response and escalations. You will also want to know the
 business impact of your system components and use this to target
 efforts when needed. You should perform a root cause analysis
 (RCA) after events, and then prevent recurrence of failures or
 document workarounds.

AWS simplifies your event response by providing tools supporting
 all aspects of your workload and operations as code. These tools
 allow you to script responses to operations events and start
 their initiation in response to monitoring data.

In AWS, you can improve recovery time by replacing failed
 components with known good versions, rather than trying to repair
 them. You can then carry out analysis on the failed resource out
 of band.

###### Best practices

- [OPS10-BP01 Use a process for event, incident, and problem management](./ops_event_response_event_incident_problem_process.html)
- [OPS10-BP02 Have a process per alert](./ops_event_response_process_per_alert.html)
- [OPS10-BP03 Prioritize operational events based on business impact](./ops_event_response_prioritize_events.html)
- [OPS10-BP04 Define escalation paths](./ops_event_response_define_escalation_paths.html)
- [OPS10-BP05 Define a customer communication plan for service-impacting events](./ops_event_response_push_notify.html)
- [OPS10-BP06 Communicate status through dashboards](./ops_event_response_dashboards.html)
- [OPS10-BP07 Automate responses to events](./ops_event_response_auto_event_response.html)

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/responding-to-events.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
