# Product Hunt AI Radar — Agent Instructions

本仓库每天由一个 Cursor Automation 生成**一份** AI 新品监测日报 `reports/YYYY-MM-DD.md`，
同时覆盖「技术向 / B2B / 基础设施 AI」（板块 A）与「2C 消费向 AI」（板块 B）两大板块。

## 执行流程

1. 运行 `python3 scripts/fetch_producthunt.py`
2. 读取 `data/latest.json`
3. 读取 `config/focus.md`
4. 先过硬门槛（只保留 AI 产品），再分板块 A / B 两视角做机制判断、官网核实、评分
5. 按 `config/focus.md` 的报告结构写入 `reports/YYYY-MM-DD.md`
6. 提交到 `cursor/product-hunt-*` 分支并 push（CI 负责同步进 main + 删分支）

## 约束

* 只监测 **AI 产品**；非 AI 产品不进正文。
* **两个板块每天都要覆盖**：某板块无达标产品时明确写「今日无高价值 X 类新品」，不留空、不凑数。
* 不编造融资、用户量、票数、排名、团队背景。
* 板块 A 正文 1-3 个产品（附录最多 10 个）；板块 B 正文 1-3 个（附录最多 5 个）。
* 不要在本地手动合并；报告直接写入单一文件，由 CI 同步到 main。
