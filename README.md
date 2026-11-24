# pairwise-arrow-ballistics-wind

## 领域

游戏、图形与多媒体

## 主题

弓箭弹道与风偏

## 说明

逐帧风场、距离步扫掠与逐发射者预测。

初始状态下 `gameplay/arrow_ballistics_wind.py` 中所有函数抛出 `NotImplementedError`，测试全部失败。
修复实现后运行：

```bash
python -m pytest -q
```

期望全部通过。
