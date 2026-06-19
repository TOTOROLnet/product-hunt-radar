# Product Hunt Radar Agent Instructions

每次执行：

1. 运行 python3 scripts/fetch_producthunt.py
2. 读取 data/latest.json
3. 读取 config/focus.md
4. 根据关注方向筛选 Product Hunt 新产品
5. 对可能入选的产品，打开 Product Hunt 页面和官网核实
6. 按 18 分制评分，只保留 >=11 分的产品
7. 生成 reports/YYYY-MM-DD.md，日期使用北京时间
8. 不要编造融资、用户量、技术实现或团队背景
9. 如果没有高价值产品，写“今日无高价值新品”
