---
name: The TAM Book of AI Era — 在线阅读器
description: 按标准作业程序排出来的技术书：白纸、一条细线切出的层级、一个功能蓝承担全部语义。
colors:
  blue: "#0f62fe"
  blue-deep: "#0043ce"
  blue-tint: "#edf5ff"
  blue-line: "#d0e2ff"
  paper: "#ffffff"
  desk: "#f4f4f4"
  ink: "#161616"
  ink-secondary: "#525252"
  ink-tertiary: "#6f6f6f"
  line: "#e0e0e0"
  line-strong: "#c6c6c6"
typography:
  display:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Source Han Sans SC, Noto Sans SC, Microsoft YaHei, Segoe UI, Roboto, system-ui, sans-serif"
    fontSize: "clamp(38px, 6.4vw, 68px)"
    fontWeight: 300
    lineHeight: 1.16
    letterSpacing: "-0.015em"
  headline:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Source Han Sans SC, Noto Sans SC, Microsoft YaHei, Segoe UI, Roboto, system-ui, sans-serif"
    fontSize: "30px"
    fontWeight: 600
    lineHeight: 1.38
    letterSpacing: "-0.005em"
  title:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Source Han Sans SC, Noto Sans SC, Microsoft YaHei, Segoe UI, Roboto, system-ui, sans-serif"
    fontSize: "20.5px"
    fontWeight: 600
    lineHeight: 1.5
  body:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Source Han Sans SC, Noto Sans SC, Microsoft YaHei, Segoe UI, Roboto, system-ui, sans-serif"
    fontSize: "17px"
    fontWeight: 400
    lineHeight: 1.85
  data:
    fontFamily: "ui-monospace, SF Mono, SFMono-Regular, Menlo, Consolas, Liberation Mono, monospace"
    fontSize: "26px"
    fontWeight: 500
  label:
    fontFamily: "-apple-system, BlinkMacSystemFont, PingFang SC, Hiragino Sans GB, Source Han Sans SC, Noto Sans SC, Microsoft YaHei, Segoe UI, Roboto, system-ui, sans-serif"
    fontSize: "10.5px"
    fontWeight: 600
    letterSpacing: "0.1em"
rounded:
  none: "0px"
spacing:
  xs: "8px"
  sm: "14px"
  md: "22px"
  lg: "34px"
  gutter: "44px"
components:
  button-primary:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "0 22px"
    height: "48px"
  button-primary-hover:
    backgroundColor: "{colors.blue-deep}"
    textColor: "{colors.paper}"
  button-secondary:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.none}"
    padding: "0 22px"
    height: "48px"
  button-toolbar:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-secondary}"
    rounded: "{rounded.none}"
    size: "32px"
  nav-item-active:
    backgroundColor: "{colors.blue}"
    textColor: "{colors.paper}"
    rounded: "{rounded.none}"
    padding: "5px 14px"
  table-header:
    backgroundColor: "{colors.desk}"
    textColor: "{colors.ink}"
    padding: "9px 13px"
  chip:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink-secondary}"
    rounded: "{rounded.none}"
    padding: "2px 7px"
---

# Design System: The TAM Book of AI Era — 在线阅读器

> **适用范围**：三书阅读站共用本设计契约，样式实现为 `shared/tooling/reader.css`。当前落地为 TAM 书站点；SA／BTE 站点建设时直接复用本契约与 token，不另立一套。

## Overview

**Creative North Star: "作业手册"（The Operations Handbook）**

这本书的样子，应该像一份按标准作业程序排出来的技术文档：白纸、一条细线切出的层级、一个蓝色承担全部功能语义。它拒绝的是把书做成文玩——暖纸底、宋体、朱红印章、圆角、投影、纸面颗粒，这些属于被替换掉的旧世界。

密度偏紧，但不挤压。目录条目 29px 高、表格单元 9px 内边距，读者可以在一屏里扫过十几个条目或四五行比对项；正文栏固定 760px、行高 1.85，任何一章连续读三万字不疲劳。层级不靠阴影、不靠色块堆叠，只靠字重、尺度、留白和 1px 细线——所以整页在视觉上是平的，深度由灰阶分层提供。

克制是这套系统的核心主张：全书 32 万字正文里，蓝色只出现在「当前在哪」（侧栏当前章满行铺蓝、章号、小节钩子、进度线）和「可以点」（链接、主按钮、焦点环）上，其余一律灰阶。

**Key Characteristics:**
- 零圆角、零阴影、1px 细线分层；唯一的柔和阴影属于抽屉与检索浮层这类功能性覆层
- 单一功能蓝 #0f62fe 承担导航状态、强调与行动，出现面积永远小于 10%
- 全部字符走系统无衬线（离线/内网可用，零外部字体请求）；数字与路径走等宽 + tabular-nums
- 表格与清单是一等公民：灰-10 表头、1px 行线、无斑马纹，窄屏横向滑动且行首吸住
- 顶端 3px 蓝线是唯一的常驻装饰——它是阅读进度，不是花纹

## Colors

一套灰阶加一个蓝，没有第二个色相。

### Primary
- **Carbon 蓝**（#0f62fe）：当前章整行底色、章首大号章号、h2 上方 48×2px 钩子、进度线、主按钮底色、焦点环、选中态。它是页面上唯一的高饱和色。
- **深蓝**（#0043ce）：正文链接与大纲当前项文字——在白色正文里比 #0f62fe 更稳，不与正文黑抢。
- **蓝调底**（#edf5ff）与**蓝细线**（#d0e2ff）：引文块与检索命中项的方框，不用左侧色条。

### Neutral
- **纸白**（#ffffff）：正文栏、顶栏、侧栏、封面 —— 一切「纸面」。
- **桌面灰**（#f4f4f4）：正文栏之外的工作台、表头、行内代码底、代码块底、悬停态。
- **墨**（#161616）：正文与标题；章首 2px 横线；封面规格块的顶线。
- **次级墨**（#525252）：目录条目、图注、按钮文字。
- **三级墨**（#6f6f6f）：元信息、章号标签、页脚、大纲标题。
- **细线**（#e0e0e0）：所有分隔——表格行、栏边界、h2 上边线。
- **控件线**（#c6c6c6）：按钮与标签的 1px 描边，比分隔线重一档。

### Named Rules

**The One Blue Rule.** 蓝色只回答两个问题：我在哪、什么能点。任何既不是状态也不是行动的元素，一律回到灰阶——包括标题、图标、装饰线。

**The No Warmth Rule.** 底色只有 #ffffff 与 #f4f4f4，且两者都不含暖调。任何偏米、偏象牙、偏宣纸的底色都属于被替换的旧世界。

## Typography

**Display Font:** 系统无衬线（-apple-system / PingFang SC / Source Han Sans / system-ui）
**Body Font:** 同一套系统无衬线，17px
**Label/Mono Font:** ui-monospace / SF Mono / Menlo（数字、路径、章号、键帽）

**Character:** 一种字体，靠字重与尺度分层——300 只给封面大标题，600 给标题与标签，400 给正文。等宽只承担「可核对的字符串」：字数、路径、章号、快捷键。全系统零外部字体请求，这是内网与离线的硬约束，也是视觉上的克制来源。

### Hierarchy
- **Display**（300，clamp(38px, 6.4vw, 68px)，1.16）：只用于封面书名，两行折行，字距收紧 -0.015em。
- **Headline**（600，30px，1.38）：每章唯一的主标题；移动端降到 23px。
- **Title**（600，20.5px，1.5）：h2 小节标题，上方一条 1px 细线 + 48×2px 蓝钩子。
- **Subtitle**（600，17.5px，1.65）：h3，无装饰线。
- **Body**（400，17px，1.85）：正文；引文块降到 16px/1.85；表格降到 14px/1.6。
- **Data**（等宽 500，26px，tabular-nums）：封面规格数字；正文里的字数、路径同族但 10.5–11px。
- **Label**（600，10.5px，字距 .1em）：目录分组标题、「本章小节」；类型徽标 10px 大写 + 1px #c6c6c6 描边。

### Named Rules

**The Tabular Rule.** 一切会被人核对或纵向比较的数字都走等宽 + tabular-nums：字数、章号、页码、表格数值。正文里的数字保持无衬线，避免文章读起来像表格。

**The No Kicker Rule.** 标题上方不放小号引导词。章首的元信息行（类型徽标、部分、文件路径、字数）放在标题之下——它是出处，不是眉题。

## Layout

三栏骨架，全部由 1px 细线切分，桌面端没有圆角卡片。

- **顶栏**：56px 固定，白底，1px 下边线。左起：32px 方形汉堡（≤1080 出现）、28px 实蓝方块 + 书名 14px/600 + 副题 11px，中部面包屑 12px，右侧工具按钮组 32px 方形。移动端书名文字隐藏，只留方块标记，按钮组靠右。
- **侧栏**：264px 固定，白底，1px 右细线。搜索框、分组标签（10.5px/600 字距 .1em + 上细线）、条目 29px 高（两位等宽章号右对齐 + 13px 标题）。当前项整行铺蓝、文字转白。≤1080 变成 320px 抽屉 + 40% 墨色遮罩。
- **正文栏**：`width: min(100%, 760px)`，白底，左右各 1px 细线，内边距 46/44/34。它居中在 #f4f4f4 的桌面灰上，两侧至少留 89px 的灰。
- **本章小节栏**（≥1360px 显示，208px）：吸附在正文栏右侧 30px 处，`sticky` 于顶栏下方 26px，只列 h2。
- **节奏**：段落 1.15em 间距；h2 上 2.6em + 18px 内边距；表格、代码块、配图上下 1.7–1.9em。全站不用垂直栅格，用 em 保持与字号档位（16 / 17 / 18.5 / 20px）同步缩放。

### Named Rules

**The Two-Hairline Rule.** 正文栏的左右边界、表格的行、抽屉的边缘，全部 1px #e0e0e0。需要更重的分隔时加深颜色（章首用 2px #161616），而不是加粗或加阴影。

**The Desk Rule.** 灰只用来区分「纸面」与「桌面」，不用来做区块底色。任何内容块如果需要在白纸上被看见，用 1px 细线围起来，而不是给它一块灰底。

## Elevation & Depth

系统是平的：全站没有任何用于表达层级的 box-shadow。深度由三层灰（#ffffff / #f4f4f4）+ 1px 细线 + 字重提供。唯一的两处阴影都是功能性覆层——侧栏抽屉与检索浮层，作用是把自己从页面上抬起来，与品牌无关。

### Shadow Vocabulary
- **overlay-lift**（`box-shadow: 0 16px 40px -12px rgba(22,22,22,.42)`）：检索浮层，唯一的大型覆层。
- **drawer-edge**（`box-shadow: 4px 0 20px -8px rgba(22,22,22,.3)`）：移动端侧栏抽屉的右缘。

### Named Rules

**The Flat-At-Rest Rule.** 静止的内容永远不投影。除了上面两个覆层，任何元素一旦出现阴影，就是设计错误。

## Shapes

零圆角：按钮、输入框、表格、卡片、徽标、代码块、图片、品牌方块，全部 `border-radius: 0`。形状语言只有两种——直角矩形与细线。控件是高 32px（工具栏）或 48px（行动）的方形；标签是 1px 描边的直角小方块；配图是 1px 描边的直角版画。

页面上唯一的「图形」是 28×28 的实蓝方块（品牌标记）与 3px 高的进度线，两者都不带圆角。

## Components

### Buttons
- **Shape:** 直角（0px），1px #c6c6c6 描边，白底
- **Primary:** 封面唯一的行动按钮实蓝底 #0f62fe + 白字，高 48px、左右 22px，14px/500；hover 转 #0043ce
- **Secondary:** 白底 + 1px #c6c6c6，墨字；hover 底转 #f4f4f4
- **Toolbar:** 32×32 方形，1px #c6c6c6，图标 16px 描边 stroke 1.5px，文字 12.5px/#525252；hover 底 #f4f4f4，按下转 #e0e0e0
- **Focus:** 全站统一 `outline: 2px solid #0f62fe; outline-offset: 2px`；鼠标点击不显示

### Chips
- **Style:** 10px/600 大写 + 字距 .09em，白底，1px #c6c6c6 描边，文字 #525252，内边距 2px 7px
- **Use:** 章首 Diátaxis 类型（EXPLANATION / HOW-TO / TUTORIAL / REFERENCE），后面接 › 与所属部分

### Cards / Containers
- **Corner Style:** 0
- **Background:** #ffffff；表头与代码块用 #f4f4f4
- **Shadow Strategy:** 无（见 Elevation & Depth）
- **Border:** 1px #e0e0e0；控件用 #c6c6c6
- **Internal Padding:** 表格单元 9px 13px；代码块 14px 16px；引文 14px 18px

### Inputs / Fields
- **Style:** 侧栏搜索框 1px #e0e0e0 白底 36px 高；检索浮层输入框 56px 高、左右 20px 内边距、无边框
- **Focus:** 浮层输入框用 `box-shadow: inset 0 -2px 0 #0f62fe`（Carbon 式底部蓝线）；原生搜索取消按钮已隐藏
- **Placeholder:** #6f6f6f，与三级墨一致

### Navigation
- **Style:** 侧栏条目 13px/400 #525252，29px 高，两位等宽章号右对齐；当前项整行 #0f62fe 底色 + 白字 + 500 字重，无圆角、无左边条
- **Hover:** 整行 #f4f4f4 底色，文字转 #161616
- **Outline rail:** 12.5px，两行截断；当前项 1px 蓝色左边线 + #edf5ff 底 + #0043ce 字（比侧栏弱一档，避免两个「我在哪」打架）
- **Mobile:** 320px 抽屉从左侧推入，汉堡按钮保持可见并可再次点击关闭

### 数据表（签名组件）
参考材料的主要形态（全书 910 张）。外框 1px #e0e0e0，表头 #f4f4f4 + 12px/600 + `white-space: nowrap`，行线 1px #e0e0e0，无斑马纹，数字 tabular-nums。首列 `min-width: 6.5em`，保证「责任对象」这类四字标签不折断。≤620px 时三列以上的表 `min-width: 600px` 内部横向滚动，首列 `position: sticky; left: 0` 吸住，滑动时不断丢失行标签。

## Do's and Don'ts

### Do:
- **Do** 把任何新内容块的层级交给 1px #e0e0e0 细线 + 字重，而不是阴影、圆角或灰底。
- **Do** 让蓝色只出现在导航状态、可点元素、焦点环和进度线上；新增元素先问它是「状态」还是「内容」。
- **Do** 用 `--sans` 排一切文字，用 `--mono` + `tabular-nums` 排一切数字与路径。
- **Do** 表格首列留出 6.5em 下限；窄屏保持横向可滑、首列吸附。
- **Do** 每个交互元素都给 2px 蓝焦点环，并保证 `/`、方向键、Esc 在键盘上可用。

### Don't:
- **Don't** 引入暖色底（米、象牙、宣纸）或第二种强调色；旧世界的朱红 #c8442c 已随整体替换移除。
- **Don't** 在标题上方加小号引导词（kicker/eyebrow）；出处信息放在标题之下。
- **Don't** 用大于 1px 的彩色左边条做装饰；状态用整行底色或 1px 边线表达。
- **Don't** 加圆角、投影或渐变文字；唯一的渐变是 `em` 的单档下划线高亮。
- **Don't** 引入任何外部字体、图标库或 CDN 资源——离线与内网必须完整可用。
