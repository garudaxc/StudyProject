"""
二阶魔方基础旋转定义（角块模型）。

状态编码约定（与 task1 一致）:
- permutation[i]: 位置 i 上的角块编号
- orientation[i]: 位置 i 上角块朝向（0/1/2）
"""

from __future__ import annotations

from typing import Dict, List, Tuple


# 经典 cubie 角块编号顺序（项目统一采用该顺序）:
# 0 URF, 1 UFL, 2 ULB, 3 UBR, 4 DFR, 5 DLF, 6 DBL, 7 DRB
CORNER_NAMES = ["URF", "UFL", "ULB", "UBR", "DFR", "DLF", "DBL", "DRB"]


# 每个基础顺时针 90° 面转在 std 编号下的 (cp, co_delta)
# cp[dest] = src
# new_ori[dest] = (old_ori[src] + co_delta[dest]) % 3
STD_MOVE_TABLES: Dict[str, Tuple[List[int], List[int]]] = {
    "U": ([3, 0, 1, 2, 4, 5, 6, 7], [0, 0, 0, 0, 0, 0, 0, 0]),
    "R": ([4, 1, 2, 0, 7, 5, 6, 3], [2, 0, 0, 1, 1, 0, 0, 2]),
    "F": ([1, 5, 2, 3, 0, 4, 6, 7], [1, 2, 0, 0, 2, 1, 0, 0]),
    "D": ([0, 1, 2, 3, 5, 6, 7, 4], [0, 0, 0, 0, 0, 0, 0, 0]),
    "L": ([0, 2, 6, 3, 4, 1, 5, 7], [0, 1, 2, 0, 0, 2, 1, 0]),
    "B": ([0, 1, 3, 7, 4, 5, 2, 6], [0, 0, 1, 2, 0, 0, 2, 1]),
}


MOVE_TABLES: Dict[str, Tuple[List[int], List[int]]] = STD_MOVE_TABLES


def apply_basic_move(
    permutation: List[int], orientation: List[int], move: str
) -> Tuple[List[int], List[int]]:
    """
    对状态执行一次基础 90° 顺时针旋转（U/R/F/D/L/B）。
    返回新的 (permutation, orientation)。
    """
    if move not in MOVE_TABLES:
        raise ValueError(f"不支持的基础操作: {move}")

    cp, co_delta = MOVE_TABLES[move]
    new_permutation = [0] * 8
    new_orientation = [0] * 8

    for dest in range(8):
        src = cp[dest]
        new_permutation[dest] = permutation[src]
        new_orientation[dest] = (orientation[src] + co_delta[dest]) % 3

    return new_permutation, new_orientation
