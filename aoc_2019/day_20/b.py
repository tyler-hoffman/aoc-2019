from dataclasses import dataclass
from queue import PriorityQueue
from aoc_2019.day_20.common import Map, Portal
from aoc_2019.day_20.parser import Parser


@dataclass
class Day20PartBSolver:
    map: Map

    @property
    def solution(self) -> int:
        start = self.map.start
        goal = self.map.goal

        queue = PriorityQueue[tuple[int, Portal, int]]()
        queue.put((0, start, 0))
        while True:
            dist, portal, depth = queue.get()
            assert depth >= 0

            if portal == goal and depth == 0:
                return dist

            connections = self.map.connections[portal]
            for connection in connections:
                delta = self.map.dists[(portal, connection)]
                d = dist + delta

                shadow = self.map.shadows.get(connection)
                if shadow:
                    depth_delta = -1 if connection.outside else +1
                    new_depth = depth + depth_delta
                    if new_depth >= 0:
                        queue.put((d + 1, shadow, new_depth))
                elif depth == 0:
                    queue.put((d, connection, 0))


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartBSolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
