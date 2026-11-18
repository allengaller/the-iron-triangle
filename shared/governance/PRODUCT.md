# Product

<!-- impeccable:product-schema 1 -->

**适用范围**：本文描述三书阅读站的产品规格，三书一体适用。当前落地为 TAM 书站点（`books/the-tam-book/`）；SA／BTE 站点建设时沿用本规格，只替换书籍元信息。

## Platform

web

## Users

一线 TAM（Technical Account Manager）、SA（解决方案架构师）、BTE（技术销售）是主要读者，工作中随时查阅：写方案、备投标、做客户价值论证、复盘大项目。第二读者是企业 IT 管理者与转型中的工程团队负责人，用它在内部对齐岗位边界与交付标准。两者都在工作场景的浏览器里读，不是休闲阅读。

## Product Purpose

《The TAM Book of AI Era｜AI 时代的 TAM 白皮书》是铁三角书系的签单后一卷，在线阅读站是它的正式呈现形态：38 章正文 + 附录 + 23 件模板，约 30 万字。站点存在的理由是让这本书能被连续读完、被检索、被引用，并被直接当成工作手册查用。成功标准：读者能连续读三万字的章节而不疲劳，且任何时刻都知道自己站在全书的哪个部分。

## Positioning

它不是厂商手册，也不是方法论复读机：每条建议都落成清单、模板或可观察行为，且每个数字都带口径标注（〔标准〕〔监管〕〔厂商〕〔经验值〕〔建议值〕）。站点的定位随之确定——一本可检索、可深读、可被反复回查的专业工具书，而不是营销落地页。

## Operating Context

- 内容由 Markdown 撰写，`shared/tooling/build_web.py` 用 pandoc 构建成静态站（`shared/dist/site/`），样式源文件在 `shared/tooling/`（`reader.css`、`template.html`、`cover.html`、`reader.js`）。
- 目录唯一事实源是 `books/the-tam-book/00-outline.md`；阅读顺序、侧栏分组、上一篇/下一篇都从它推导。
- 全书含 901 张表、173 处引文块、1571 个列表、920 个二级标题、17 张 SVG 配图 —— 表格与清单是主要内容形态，不是装饰。读者经常要在表里横向比对条目。
- 章节按 Diátaxis 分为 Tutorial / How-to / Reference / Explanation 四型，页面上以类型标记呈现。
- 站点需要能在离线或内网环境打开（纯静态、无外部依赖），因此只使用系统字体，不引入任何 CDN 字体或第三方资源。
- 生产环境是 `python3 -m http.server` 或任意静态托管；无后端、无登录、无埋点。

## Capabilities and Constraints

已确认功能：全书侧栏目录与当前章高亮、全站检索（`search-index.json` 按小节切分，支持 / 唤起与键盘上下选择）、阅读进度条、字号三档放大缩小、上一篇/下一篇与 ←/→ 翻页、封面页、打印样式、移动端侧栏抽屉。

技术约束：无框架、无构建工具链、原生 CSS + 原生 JS；`template.html` 由构建脚本按 `{{TITLE}}`、`{{SIDEBAR}}`、`{{CONTENT}}` 等占位符填充，改动结构时不得破坏这些占位符；`shared/dist/site/` 是生成物且已 gitignore，一切样式改动落在 `shared/tooling/`。

已决定的产品边界：不加入账号、评论、阅读进度云同步、AI 问答等需要后端的能力。

## Brand Commitments

书名与中英文标题固定；许可为 CC BY-NC-SA 4.0；封面现状信息（38 章 / 29 附录 / 23 件模板 / 17 张配图 / 30.8 万字 / v0.3）来自 `shared/tooling/gen_metadata.py`，不得手改数字。

本轮用户明确指定的视觉约束：企业级 IBM 专业风格，白底 + 蓝色；只保留白底单一主题，不提供深色模式；字体只用系统字体栈，不加载外部字体。

## Evidence on Hand

真实的书稿、目录、模板与配图都在仓库内，可直接作为页面内容：`books/the-tam-book/`（章节 Markdown）、`books/the-tam-book/tpl-*.md`（23 件模板）、`shared/figures/*.svg`（17 张手绘 SVG 配图）、`shared/dist/site/search-index.json`（检索数据）。没有客户 logo、没有推荐语、没有商业数据 —— 未来工作不得编造。

## Product Principles

1. 阅读优先：版式服务于连续阅读与定位，任何装饰让位于文字。
2. 结构即导航：部分 → 章 → 小节的三级结构在页面上始终可见，读者永不迷路。
3. 表格与清单是一等公民：参考材料要能横向扫读、竖向比对。
4. 零外部依赖：离线、内网、纯静态都能完整工作。
5. 克制即专业：色彩只有一个功能蓝，强调靠字重、尺度和留白。

## Accessibility & Inclusion

正文与次级文字对白底均需满足 4.5:1 对比度；键盘可达（焦点环、/ 唤起搜索、方向键翻页、Esc 关闭）；打印时去掉导航只留正文。
