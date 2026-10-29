<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/detective-controls.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Detective controls

**Ensure that your images are scanned for vulnerabilities**

After images are built, it is important to maintain a regular cadence of scanning those images to ensure no new or existing vulnerabilities have surfaced. There are two basic categories to consider when discussing image scanning: static scanning and dynamic scanning.
 
 Static scanning is performed before the image is deployed. This is important because it allows organizations to detect vulnerabilities in a container image before a container is deployed into an environment. Many registry offerings provide native static image scanning that can scan container images for common vulnerabilities and exposures (CVEs) without having to integrate and maintain a third-party image scanning tool. The scanning process is performed by comparing parent container images, dependencies, and libraries that are used by the container image to known CVEs.
 
 Dynamic container scanning is a process that scans the underlying infrastructure where containers run. It is executed post container deployment, and identifies vulnerabilities that may have been introduced by other software installed on the infrastructure itself. These vulnerabilities can be either modifications to an existing running container, or communication with a container that is exposed externally to other processes or hosts.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/container-build-lens/detective-controls.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
