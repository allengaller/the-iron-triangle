<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-2.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Questions

Quantitatively benchmark the performance of systems in
 retrieving, analyzing, and reporting on images to meet customer
 expectations. Tests should realistically capture the network
 bandwidth, annual volume of data ingested (estimate the types
 and number of imaging modalities generating data), and the
 number of concurrent users that the solution will support.

Collect quantitative performance metrics under simulated loads
 and representative network speeds to provide an acceptable end
 user experience. Test your solution under accurately simulated
 loads (such as number of concurrent users and realistic last
 mile network bandwidth). Radiologists demand high performance
 from PACS and VNA solutions, and are sensitive to image
 retrieval latencies. For example, collect metrics like time to
 first image display that quantify how long it takes for an end
 user to see a medical image after requesting it.

Once performance requirements are met, systems can be cost
 optimized by balancing image retrieval performance with use of
 cost-effective storage services (such as right sizing cache volumes
 and
 [throughput
 provisioning](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)).

Optimize the throughput of medical image data between backends
 and viewer applications with high-performance, parallelized
 network protocols like HTTP/2. Also, leverage compression
 algorithms to reduce the volume of data transferred.

Medical imaging study data may consist of multiple images or a
 single large image with regions of varying importance. End user
 experience can be optimized by prioritizing transmission of the
 images or
 [areas](https://meridian.allenpress.com/aplm/article/143/2/222/64743/A-Practical-Guide-to-Whole-Slide-Imaging-A-White)
 that will be of highest initial interest. In this way, the end
 user can begin their work while data of less interest is
 transmitted.

Quantify the overall user-experience using metrics (like first
 image display time). Provision cloud services that are
 appropriate for each component’s performance requirements. For
 example, high IOPS EBS volumes may increase cost but may not
 improve user experience if the overall solution performance is
 limited by network connectivity.

Further, collect data on medical image access frequency and use
 it to optimize the cost of storage through each image’s
 lifecycle. As noted above, medical images tend to be accessed
 frequently when created and then see less access with time.
 Decrease storage costs by moving images to lower-cost cloud
 storage tiers as access becomes less frequent.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/healthcare-industry-lens/questions-2.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
