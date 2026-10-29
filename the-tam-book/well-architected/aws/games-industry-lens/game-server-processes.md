<!-- source: https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/game-server-processes.html -->
<!-- captured: 2026-10-26 -->
<!-- vendor: aws -->

# Game server processes

The following diagram illustrates a typical game server
 architecture. It describes the logical relationship between a
 game server instance and the game server processes that host
 game sessions.

![Logical game server architecture](/images/wellarchitected/latest/games-industry-lens/images/image1.jpeg)

*Logical game server architecture*

- An Amazon EC2 instance is used as a game server, also known
 as a game server instance. The game server hosts one or more
 game server processes, and each is running a copy of your
 game server build. Typically, multiple game server processes
 are running on a game server instance to utilize compute
 resources efficiently and reduce costs. When a game session
 is active and ready to host player sessions, its status is
 updated with the game backend (usually a matchmaking
 service) so that it can begin to be used to host players.
- The game backend can provide the player with the IP address
 and server port that is hosting a game session so that they
 can connect to play.

Thanks for letting us know we're doing a good job!

If you've got a moment, please tell us what we did right so we can do more of it.

Thanks for letting us know this page needs work. We're sorry we let you down.

If you've got a moment, please tell us how we can make the documentation better.

---

> 原页面：https://docs.aws.amazon.com/wellarchitected/latest/games-industry-lens/game-server-processes.html（抓取时点 2026-10-26；正文为自动抓取，排版已规整，语义未改写）
