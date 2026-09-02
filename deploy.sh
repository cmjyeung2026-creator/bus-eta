#!/bin/bash
# 部署 23M 小巴到站時間網頁到 GitHub Pages

cd C:/Users/Jimmy/workspace/bus-eta

# 複製到 dist 目錄
cp 23m.html dist/

# 提交並推送
git add -A
git commit -m "Add 23M minibus ETA page"
git push origin main

echo "部署完成！網址：https://cmjyeung2026-creator.github.io/bus-eta/23m.html"
