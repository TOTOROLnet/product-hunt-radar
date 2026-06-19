每天执行一次 Product Hunt 新品监测。

步骤：
1. 阅读 AGENTS.md 和 config/focus.md
2. 运行 python3 scripts/fetch_producthunt.py
3. 如果脚本成功，读取 data/latest.json
4. 如果 RSS 失败，使用浏览器打开 Product Hunt 当日榜单作为备用数据源，并在报告中注明
5. 对新品做初筛，不要只做关键词匹配
6. 对可能入选的产品，打开 Product Hunt 页面和官网核实
7. 按 18 分制评分，只保留 >=11 分的产品
8. 生成 reports/YYYY-MM-DD.md，日期使用北京时间
9. 最终回复：今天最值得关注的 1-3 个产品、为什么值得关注、报告文件路径
10. 没有高价值产品时，明确写“今日无高价值新品”
