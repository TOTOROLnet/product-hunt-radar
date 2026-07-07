# 监测目标

本文件用于定义 Product Hunt 新品监测的关注范围、降权范围和评分规则。

目标不是收集所有 AI 产品，而是筛出对 AI 产品经理有启发的新产品、新交互、新基础设施和新工作流。

---

## 我重点关注

### 1. AI Agent 基础设施

优先关注能让 Agent 更稳定、更可控、更可观测、更能生产化落地的产品。

包括但不限于：

* Tool Use
* Function Calling
* MCP
* Remote MCP Server
* API to MCP
* Agent Runtime
* Agent Sandbox
* Agent Permission / Approval
* Agent Memory
* Agent State Management
* Agent Observability
* Agent Evaluation
* Agent Guardrails
* Agent Trace / Replay
* Agent Workflow
* Multi-agent Orchestration
* Browser Use / Computer Use
* Long-running Agent
* Human-in-the-loop Agent

重点判断：

* 它是否解决 Agent 落地中的真实瓶颈？
* 它是否让工具调用、权限、安全、记忆、状态、评估或追踪更容易产品化？
* 它是否能迁移到大模型 API、Agent 平台或开发者工具产品中？

---

### 2. Context Engineering / Memory / Skill 类产品

优先关注围绕上下文组织、记忆、技能沉淀、任务复用和经验迁移的产品。

包括但不限于：

* Context Engineering
* Prompt / Context Management
* Long Context Workflow
* Memory Layer
* Personal / Team / Project Memory
* Skill / Skill Library
* Skill Generation
* Trace-to-Skill
* Auto Skill Discovery
* SkillOpt / SkillClaw / AutoSkill 类方向
* Workflow-to-Skill
* Task Replay / Task Generalization
* Reusable Agent Capability
* Knowledge-to-Action
* SOP / Playbook for Agent

重点判断：

* 它是否把一次性任务沉淀成可复用能力？
* 它是否能提升 Agent 在复杂任务中的稳定性和复用性？
* 它是否代表 memory、skill、context 从“提示词技巧”走向“产品机制”？

---

### 3. 大模型 API 与开发者平台

优先关注对大模型 API、模型服务、开发者体验和 Agent 开发链路有启发的产品。

包括但不限于：

* LLM API Platform
* AI Developer Platform
* SDK / CLI / Workflow
* Structured Output
* File / Search / Retrieval
* Web Search / Deep Research
* RAG / Knowledge Base
* Prompt Cache
* Batch API / Async API
* Model Routing
* Model Evaluation
* Cost / Latency / Reliability Observability
* Playground / Debugger
* Agent Builder
* Tool Builder
* API Gateway for AI

重点判断：

* 它是否改善开发者构建 AI 应用或 Agent 的链路？
* 它是否在协议、工具、状态、上下文、评估、调试、成本或可靠性上有产品机制创新？
* 它是否对混元 API、Responses API、Anthropic 兼容、工具调用或 Agent 平台设计有参考价值？

---

### 4. Coding Agent / Developer Tools

优先关注软件开发、代码生成、代码审查、测试、部署、工程协作相关的 AI 原生工具。

包括但不限于：

* Coding Agent
* Code Review Agent
* CI Repair Agent
* Test Generation
* Debugging Agent
* Repo Understanding
* PR Review / PR Summary
* Dev Environment for Agents
* Terminal / Browser / IDE Agent
* Documentation Agent
* API / SDK Generation
* DevOps Agent
* Security Agent
* Penetration Testing Agent
* Agentic IDE / Workspace

重点判断：

* 它是否改变开发者工作流，而不只是“生成一段代码”？
* 它是否让 Agent 能在真实工程环境中读仓库、跑命令、看日志、改代码、验证结果？
* 它是否体现 coding agent 从辅助问答走向工程执行？

---

### 5. AI 原生生产力工具

优先关注不是简单接入 AI，而是围绕 AI 重新设计工作流、协作方式和任务完成方式的生产力产品。

包括但不限于：

* AI-native Workspace
* AI-native Inbox
* AI-native Calendar
* AI-native Docs
* AI-native Slides
* AI-native Spreadsheet
* AI-native Research
* AI-native Meeting
* AI-native Knowledge Work
* Personal Assistant
* Team Assistant
* Proactive Agent
* Approval-based Automation
* Cross-app Workflow
* Desktop Agent
* Voice Agent
* Work OS with AI

重点判断：

* 它是否不是“在旧产品里加一个 Chatbot”，而是重构了任务流？
* 它是否有主动发现问题、准备材料、生成草稿、跨工具执行、等待人类确认的机制？
* 它是否体现 AI 原生生产力从“提效工具”走向“任务代理”？

---

### 6. 新型人机交互

优先关注能改变人与 AI 互动方式的产品。

包括但不限于：

* Conversational UI
* Proactive UI
* Agentic UI
* Human Approval / Takeover
* Co-pilot to Operator
* Voice Interaction
* Multimodal Interaction
* Desktop Control
* Browser Control
* Interactive Video
* Interactive Document
* AI Artifact
* Canvas / Workspace Agent
* Ambient AI
* Second Cursor / AI Cursor
* Agent Timeline / Trace UI

重点判断：

* 它是否提供了新的 AI 交互范式？
* 它是否让用户能更好地理解、控制、接管或追踪 Agent？
* 它是否降低了复杂任务中用户与 Agent 协作的摩擦？

---

### 7. 垂直 Agent 工作流

优先关注将 Agent 深入具体专业场景，而不是泛泛聊天的产品。

包括但不限于：

* Research Agent
* Data Agent
* Analyst Agent
* Marketing Agent
* Sales Agent
* Customer Support Agent
* Design Agent
* CAD Agent
* Creative Agent
* Security Agent
* Finance Agent
* Legal Agent
* Healthcare Workflow Agent
* E-commerce Ops Agent
* Enterprise Workflow Agent

重点判断：

* 它是否有明确的专业对象、专业工具和专业验证标准？
* 它是否把 Agent 接入了真实业务系统，而不只是生成建议？
* 它是否具备可追踪、可审核、可回放、可纠错的工作流机制？

---

### 8. 创新 AI 应用

关注不一定属于 Agent 基础设施，但在产品形态、交互方式、商业场景或用户心智上有明显新意的 AI 应用。

包括但不限于：

* 新型 AI 消费应用
* 新型内容交互
* 新型教育 / 学习产品
* 新型创作工具
* 新型社交 / 陪伴 / 协作方式
* 新型搜索 / 发现 / 推荐方式
* 新型组织知识管理
* 新型个人知识管理
* 新型 AI 硬件 / 端侧 AI 体验
* 新型 AI 工作流入口

重点判断：

* 它是否让用户用 AI 完成了过去难以完成的任务？
* 它是否形成了新的使用场景、交互习惯或产品入口？
* 它是否可能启发 Agent、AI 应用或大模型 API 的产品设计？

---

## 降权或过滤

以下产品通常不进入正文，除非有非常明确的机制创新：

* 普通 ChatGPT wrapper
* 只有一个聊天框的通用 AI 助手
* 单点文案生成工具
* 单点图片生成、头像生成、滤镜工具
* 普通待办、笔记、日历、邮箱增强
* 普通浏览器插件
* 普通网站生成器
* 普通营销增长工具
* 纯 SEO / backlink / 广告投放工具
* Crypto / NFT / Web3 概念包装
* 纯娱乐或低频玩具型产品
* 只有落地页，没有可核实机制
* 只是接入 AI，但没有新的工作流、交互或基础设施机制
* 明显缺少产品完成度、可信来源或可验证信息的项目

注意：

* “AI 原生生产力工具”不要因为属于邮箱、日历、文档、会议、浏览器等常见品类就直接过滤。
* 只有当它只是旧工具加 AI 文案功能时才降权。
* 如果它重构了任务流、协作流、审批流、上下文流或跨工具执行流，应进入重点评估。

---

## 评分规则

总分 18 分：

1. 相关度：0-5
   是否贴合 AI Agent、大模型 API、Context Engineering、Memory、MCP、Tool Use、AI 原生生产力、Coding Agent、Developer Tools、Skill 类方向或创新 AI 应用。

2. 产品机制新颖度：0-5
   是否有新的机制、工作流、交互方式、系统架构或产品组织方式，而不只是包装概念。

3. 对 AI 产品设计的启发：0-5
   是否能启发 API、Agent 产品、上下文工程、工具调用、记忆、技能、评估、开发者平台或 AI 应用设计。

4. 市场信号：0-3
   是否有明确用户场景、可信官方来源、开源活跃度、生态势能、品牌背书、社区讨论或可观察的早期 traction。

---

## 正文展开标准

报告正文只展开最值得关注的 1-3 个产品。

其他达到 11 分的产品只进入附录表格，最多 10 个。

如果当天没有明显高价值产品，可以不强行推荐。

宁可少报，不要凑数。

---

## 每个重点产品必须回答

1. 它解决 Agent / AI 产品落地里的哪个真实瓶颈？
2. 它的核心机制是什么？
3. 它为什么现在值得关注？
4. 它如果失败，最可能失败在哪里？
5. 它对混元 API / Agent 产品 / AI 应用设计有什么迁移价值？
6. 它代表的是短期噱头，还是长期产品结构变化？

---

## 趋势判断规则

趋势不是关键词堆叠，必须满足至少一个条件：

1. 至少 2 个产品体现了相同方向。
2. 某个产品代表了大平台、重要生态或关键基础设施变化。
3. 某个产品体现了 AI 产品形态的明显结构性变化。

趋势输出最多 3 条。

如果没有明显趋势，写“今日未形成明确趋势信号”。

---

## 输出偏好

报告要面向 AI 产品经理，而不是面向普通消费者。

优先输出判断，不要堆砌产品介绍。

正文控制在 1200-1800 中文字。

不要为了显得全面列太多产品。

报告应该帮助读者快速决定：

* 今天哪些产品值得看？
* 它们为什么值得看？
* 背后反映了什么 AI 产品趋势？
* 哪个方向值得进一步体验、拆解或进入竞品库？


---

> **2C 消费监测**为独立 Agent 任务：配置见 `config/focus-2c.md`，partial 写入 `reports/partials/`，合并脚本 `scripts/merge_daily_report.py` 产出单一日报 `reports/YYYY-MM-DD.md`。不要在同一次 Automation 中加载 focus-2c.md。
