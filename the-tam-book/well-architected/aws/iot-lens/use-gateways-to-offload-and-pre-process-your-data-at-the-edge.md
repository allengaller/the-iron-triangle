<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/use-gateways-to-offload-and-pre-process-your-data-at-the-edge.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Use gateways to offload and pre-process your data at the edge

The decision to connect a device directly to the cloud or via a
 gateway will depend on a variety of factors, including the
 specific requirements of the application and the characteristics
 of the sensor and network. It may be more power-efficient to
 use a gateway to receive and preprocess data locally, reducing
 the need for higher power radios on the device, reducing
 long-haul communications traffic and extending battery life.

If the device generates a large amount of data, it may be more
 efficient to use a gateway to pre-process and filter the data
 before sending it to the cloud, reducing long-haul network
 traffic. In addition, if the long-haul network connection
 is unreliable, it may be more practical to use a gateway with
 [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) to buffer data and make sure that it is
 delivered reliably to the cloud.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/use-gateways-to-offload-and-pre-process-your-data-at-the-edge.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
