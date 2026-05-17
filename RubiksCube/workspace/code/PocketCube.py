from __future__ import annotations

from typing import Iterable, List

from moves import CORNER_NAMES, apply_basic_move


class PocketCube:
    """
    二阶魔方状态表示（仅角块模型）。

    属性:
        permutation: 长度为8，permutation[i] 表示位置 i 上角块编号
        orientation: 长度为8，orientation[i] ∈ {0,1,2}
    """

    def __init__(self, permutation=None, orientation=None):
        self.permutation = list(range(8)) if permutation is None else list(permutation)
        self.orientation = [0] * 8 if orientation is None else list(orientation)

    def copy(self) -> "PocketCube":
        """返回当前状态的深拷贝。"""
        return PocketCube(self.permutation[:], self.orientation[:])

    def is_valid(self) -> bool:
        """验证当前状态是否满足编码与角块朝向守恒约束。"""
        return (
            all(0 <= o < 3 for o in self.orientation)
            and sum(self.orientation) % 3 == 0
            and set(self.permutation) == set(range(8))
        )

    def apply_move(self, move: str) -> "PocketCube":
        """
        原地执行一步操作，支持:
        - 基础面转: U R F D L B
        - 逆时针:  U' R' F' D' L' B'
        - 半转:    U2 R2 F2 D2 L2 B2
        """
        if not move:
            raise ValueError("操作字符串不能为空")

        base = move[0]
        if base not in {"U", "R", "F", "D", "L", "B"}:
            raise ValueError(f"不支持的操作: {move}")

        if len(move) == 1:
            times = 1
        elif len(move) == 2 and move[1] == "'":
            times = 3
        elif len(move) == 2 and move[1] == "2":
            times = 2
        else:
            raise ValueError(f"不支持的操作格式: {move}")

        for _ in range(times):
            self.permutation, self.orientation = apply_basic_move(
                self.permutation, self.orientation, base
            )
        return self

    def apply_sequence(self, moves: Iterable[str]) -> "PocketCube":
        """按顺序执行一串操作。"""
        for move in moves:
            self.apply_move(move)
        return self

    def __repr__(self) -> str:
        return (
            f"PocketCube(permutation={self.permutation}, "
            f"orientation={self.orientation})"
        )

    def to_pretty_string(self) -> str:
        """输出便于检查的文本表示。"""
        rows = []
        for pos, cubie in enumerate(self.permutation):
            rows.append(
                f"{CORNER_NAMES[pos]} <- cubie{cubie} (ori={self.orientation[pos]})"
            )
        return "\n".join(rows)