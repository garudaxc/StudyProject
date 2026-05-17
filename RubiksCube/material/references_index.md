# 参考资料索引

## 魔方群论 - 核心资源

### 1. Jaap's Cube Page ⭐⭐⭐（必读）
- **URL**: https://www.jaapsch.net/puzzles/cubic2.htm
- **描述**: 魔方群论最权威的在线参考资料
- **重点章节**: 
  - "2×2×2 Cube" - 二阶魔方数学结构
  - "Mathematics of the Cube" - 群论基础
- **收获**: 状态空间计算、朝向守恒律、God's Number

---

## 群论理论

### 2. Artin《Algebra》
- **章节**: 第6章 "Symmetry"
- **重点**: 
  - Section 6.7: Group Actions
  - Section 6.9: The Operation on Cosets
  - 轨道-稳定子定理
- **推荐**: 理论奠基，适合深入理解

### 3. Keith Conrad 讲义 ⭐⭐（在线免费）
- **URL**: https://kconrad.math.uconn.edu/blurbs/grouptheory/orbitstabilizer.pdf
- **主题**: 轨道-稳定子定理
- **优势**: 清晰、简洁、带例子
- **推荐**: 快速复习或补充

### 4. Dummit & Foote《Abstract Algebra》
- **章节**: 第4章 "Group Actions"
- **特点**: 百科全书式参考，习题丰富
- **适合**: 需要深度理论支撑时查阅

---

## 编程实现

### 5. pycuber (PyPI)
- **URL**: https://pypi.org/project/pycuber/
- **类型**: Python魔方库
- **用途**: 参考实现、API设计
- **安装**: `pip install pycuber`

### 6. rubik-cube (GitHub)
- **URL**: https://github.com/pglass/cube
- **类型**: 开源Python实现
- **用途**: 学习算法实现技巧
- **特点**: 代码清晰，有注释

### 7. Kociemba 算法
- **URL**: https://kociemba.org/cube.htm
- **类型**: 专业求解算法
- **用途**: 学习降群法思想
- **特点**: 可下载源码，业界标准

---

## 在线工具与可视化

### 8. Cube Explorer
- **URL**: http://kociemba.org/cubeexplorer.htm
- **功能**: 魔方状态可视化、求解演示
- **用途**: 验证你的算法结果

### 9. Ruwix 魔方教程
- **URL**: https://ruwix.com/the-rubiks-cube/
- **内容**: 魔方基础、符号系统
- **用途**: 复习标准记号

---

## 学术论文与深度阅读

### 10. God's Number is 20
- **作者**: Tomas Rokicki et al.
- **URL**: http://www.cube20.org/
- **主题**: 证明三阶魔方 God's Number = 20
- **意义**: 群论与计算结合的杰作

### 11. Lower Bounds for God's Number
- **主题**: 群论在魔方距离下界中的应用
- **搜索关键词**: "God's Number group theory lower bounds"

---

## 快速参考卡片

### 核心公式

**二阶魔方群阶数**:
```
|G| = (8! × 3^7) / 24 = 3,674,160
```

**朝向约束**:
```
∑(orientation[i]) ≡ 0 (mod 3)
```

**BFS复杂度**（分支因子b=6，深度d）:
```
节点数 ≈ 6^d
对于 d=11: 6^11 ≈ 362,797,056
```

### 标准记号

| 记号 | 含义 | 动作描述 |
|------|------|----------|
| F | Front | 前面顺时针旋转90° |
| B | Back | 后面顺时针旋转90° |
| U | Up | 上面顺时针旋转90° |
| D | Down | 下面顺时针旋转90° |
| L | Left | 左面顺时针旋转90° |
| R | Right | 右面顺时针旋转90° |
| F' | Front inverse | 前面逆时针旋转90° |
| F2 | Front double | 前面旋转180° |

---

## 学习路径推荐

### 快速通道（10-15小时）
1. Jaap's Cube Page（二阶部分）- 30分钟
2. Keith Conrad轨道-稳定子讲义 - 20分钟
3. 直接开始编程实现 - 边做边查

### 深度通道（20-30小时）
1. Artin《Algebra》第6章 - 3小时
2. Jaap's Cube Page全篇 - 1小时
3. 推导群阶公式并证明 - 2小时
4. 完整实现+优化 - 10小时
5. 写作产出 - 2小时

---

## 资源评价标准

⭐ = 可选参考  
⭐⭐ = 推荐阅读  
⭐⭐⭐ = 必读核心

---

*最后更新：2026-05-05*
