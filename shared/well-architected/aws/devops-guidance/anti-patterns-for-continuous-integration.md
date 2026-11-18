<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-integration.html -->
<!-- captured: 2026-10-25 -->
<!-- vendor: aws -->

# Anti-patterns for continuous integration

- **Infrequent check-in of code**: To detect issues as early
 as possible, developers should check-in their changes to the code base as often as
 possible. If developers are committing code infrequently, it can lead to longer feedback
 loops, and problems may go unnoticed for longer periods of time.
- **Manually building and testing changes**: A key benefit of
 continuous integration is the ability to automatically build and test code changes. If
 teams rely on manual testing or building, it will slow down the development process and
 make it harder to detect issues early on.
- **Having builds run on a preset schedule rather than on
 commit**: One of the main benefits of continuous integration is that it
 enables teams to detect issues as soon as possible, which is why builds should be
 triggered automatically every time changes are committed to the repository. If builds
 are only run on a preset schedule, it can lead to longer feedback loops and more issues
 slipping through.
- **Low coverage or inaccurate tests:** The quality of the
 tests used during the continuous integration process is essential to its overall
 effectiveness. If tests are incomplete, missing, or inaccurate, issues are likely to
 slip through undetected.
- **Only testing in production**: Continuous integration
 requires building, testing, and validating new changes to the code base. If teams are
 waiting to test changes only in production, it can lead to longer feedback loops, and
 issues may go unnoticed until they reach the end users.
- **Failure to provide useful feedback to developers during a
 build**: Rapid and consistent feedback to developers is one of the core
 benefits of continuous integration. If feedback is not useful, it can be hard for
 developers to address issues, and it can slow down the development process.
- **Lack of collaboration**: Continuous integration requires
 collaboration between developers, operations, security, and other stakeholders. If teams
 are not collaborating effectively, it can lead to issues slipping through, longer
 feedback loops, and slower development times.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/anti-patterns-for-continuous-integration.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
