# Product Hunt AI Radar

本项目配合 Cursor Automation，每天自动生成**一份** Product Hunt AI 新品监测日报
（`reports/YYYY-MM-DD.md`），同时覆盖两大板块：

- **板块 A · 技术向 / B2B / 基础设施 AI**：面向 AI 产品经理 / 开发者。
- **板块 B · 2C 消费向 AI**：面向个人消费者的 AI 应用。

只监测 **AI 产品**；技术向与 2C 两端每天都会覆盖，避免只盯技术产品而漏掉消费级市场信号。

## 关键文件

- `config/focus.md` — 关注范围、过滤规则、两个板块的评分标准与报告结构。
- `AUTOMATION_PROMPT.md` — 创建 Cursor Automation 时，复制其内容作为指令。
- `AGENTS.md` — Agent 执行流程与约束。
- `scripts/fetch_producthunt.py` — 抓取 Product Hunt RSS 到 `data/latest.json`。

## 本地测试

```bash
python3 scripts/fetch_producthunt.py
cat data/latest.json
```

## 同步与部署

Automation 把报告提交到 `cursor/product-hunt-*` 分支，
`.github/workflows/auto-merge-cursor.yml` 会把报告同步进 `main` 并删除该分支。
下游 `product-opportunity-lab` 只拉取 `reports/YYYY-MM-DD.md`。
