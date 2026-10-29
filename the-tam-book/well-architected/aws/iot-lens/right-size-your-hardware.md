<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/right-size-your-hardware.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Right-size your hardware

The choices made in hardware component selection can greatly
 influence the operational phase impact of devices and therefore
 must be carefully considered. The use case should dictate the
 required CPU/MCU, peripherals and communication modules on the
 device. When choosing the processor, amount of RAM, and amount
 of flash storage, the designer must focus on resource
 optimization; over-provisioning hardware can lead to choosing a
 processor that has a large power draw but stays mostly idle or
 has an excess of memory that never gets used, increasing the
 overall carbon footprint of the device unnecessarily.
 Under-sizing hardware can lead to long execution times or a lack
 of extensibility necessary to insure the longevity of the
 device.

Your design will typically fall into one of three broad classes
 of devices – Microcontroller (MCU) class devices, Microprocessor
 (MPU) class devices, and devices that use hardware acceleration
 for machine learning use cases (which we refer to as "Inference
 class" devices).

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/right-size-your-hardware.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
