from dataclasses import dataclass
from queue import PriorityQueue
from aoc_2019.day_20.common import Map, Portal
from aoc_2019.day_20.parser import Parser


@dataclass
class Day20PartASolver:
    map: Map

    @property
    def solution(self) -> int:
        start = self.map.start
        goal = self.map.goal

        queue = PriorityQueue[tuple[int, Portal]]()
        queue.put((0, start))
        while True:
            dist, portal = queue.get()
            if portal == goal:
                return dist
            for connection in self.map.connections[portal]:
                delta = self.map.dists[(portal, connection)]
                d = dist + delta

                shadow = self.map.shadows.get(connection)
                if shadow:
                    queue.put((d + 1, shadow))
                else:
                    queue.put((d, connection))


def solve(input: str) -> int:
    data = Parser.parse(input)
    solver = Day20PartASolver(data)

    return solver.solution


def get_solution() -> int:
    with open("aoc_2019/day_20/input.txt", "r") as f:
        input = f.read()
    return solve(input)


if __name__ == "__main__":
    print(get_solution())
