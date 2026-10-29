<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/use-an-event-driven-architecture-in-your-iot-devices.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Use an event driven architecture in your IoT devices

Using an event-driven architecture in IoT device firmware
 reduces processing and communication overhead, and helps reduce
 energy consumption. There are a number of mechanisms that can
 be used in IoT devices to realize an event-driven architecture.

Design device software to minimize the amount of energy IoT
 devices consume while checking for events or data. By using
 interrupts instead of continuous polling, the CPU can sleep
 until an event occurs, reducing the time the device spends
 actively checking for data or events.

Another mechanism is
 [Pub/Sub](https://aws.amazon.com/pub-sub-messaging/benefits/)
 topics (such as those used by the
 [MQTT](https://mqtt.org/) protocol).
 Devices that subscribe to specific topics receive notifications
 when new messages are available, allowing for appropriate
 processing to be triggered.

Asynchronous callbacks are another technique used to realize an
 event driven architecture. In this model, the device firmware
 registers callback functions to be executed when specific events
 occur. This enables efficient processing of events without the
 need for polling or continuous querying.

Real time operating systems such as FreeRTOS are built for event
 driven firmware by employing the use of priority interrupts,
 pointers to callback functions, and multi-threading.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/use-an-event-driven-architecture-in-your-iot-devices.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
