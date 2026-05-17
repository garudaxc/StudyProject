# 子任务2：实现单次旋转操作

## 目标
把“群元素作用在状态空间上”落实为代码：给定一个状态 `S=(p,o)` 和一个基本操作（`U/R/F/D/L/B`），能计算旋转后的新状态。

---

## 1. 状态与操作的代码接口

当前状态（沿用子任务1）：
- `permutation[i]`：位置 `i` 上是哪个角块；
- `orientation[i]`：位置 `i` 上角块的朝向（`0/1/2`）。

本项目统一位置编码（经典 cubie 顺序）：
- `0..7 = URF, UFL, ULB, UBR, DFR, DLF, DBL, DRB`

核心接口：
- `apply_basic_move(permutation, orientation, move)`：执行一次 90° 顺时针基础面转；
- `PocketCube.apply_move(move)`：支持 `U/R/F/D/L/B`、逆时针 `'`、半转 `2`；
- `PocketCube.apply_sequence(moves)`：执行操作序列。

---

## 2. 置换规则（Permutation）

我们为每个基础面转定义角块置换表 `cp`：

- `cp[dest] = src`  
  表示旋转后目标位置 `dest` 的角块来自旋转前位置 `src`。

更新公式：

```python
new_permutation[dest] = old_permutation[cp[dest]]
```

---

## 3. 朝向规则（Orientation）

对角块，朝向更新采用：

```python
new_orientation[dest] = (old_orientation[src] + co_delta[dest]) % 3
```

其中：
- `co_delta[dest]` 是该 move 在目标位置上的朝向增量；
- `U/D` 转动不改变角块朝向（增量全 0）；
- `R/F/L/B` 会改变部分角块朝向（增量非零）。

该更新方式自动保持朝向守恒（和 mod 3）。

---

## 4. 本任务产出文件

- `code/moves.py`
  - 定义 `MOVE_TABLES`（六个基础面转）；
  - 提供 `apply_basic_move(...)`。
- `code/PocketCube.py`
  - 增加 `copy()`、`apply_move()`、`apply_sequence()`；
  - 支持 `U/R/F/D/L/B`、`'`、`2` 记号。

---

## 5. 最小验证清单

你可以用下面这些性质做快速自测：

1. **四次回到原状**：`X X X X = I`（`X∈{U,R,F,D,L,B}`）
2. **逆操作正确**：`X X' = I`
3. **半转正确**：`X2 = X X`
4. **守恒律保持**：任意序列后 `sum(orientation) % 3 == 0`

---

## 6. 与群论的对应关系

- 每个 move 是状态集合上的一个双射；
- move 复合对应群乘法；
- 单次旋转实现完成后，后续 BFS 求解器就是在 Cayley 图上找最短路（子任务5）。

---

## 完成检验标准

- [x] `PocketCube` 能执行 `U/R/F/D/L/B`
- [x] 支持 `X'` 与 `X2`
- [x] 操作后能得到新的 `(permutation, orientation)`
- [x] 状态仍满足朝向守恒约束
- [x] 为子任务5（BFS）准备好可复用 move 接口
