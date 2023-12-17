from aoc_2019.common.point import Point
from aoc_2019.day_20.common import Map, Portal


class Parser:
    @staticmethod
    def parse(input: str) -> Map:
        lines = [line for line in input.splitlines() if line]
        widths = set(len(line) for line in lines)
        assert len(widths) == 1

        return Map(
            points=Parser.parse_points(lines),
            outer_portals={p.label: p for p in Parser.parse_outer_portals(lines)},
            inner_portals={p.label: p for p in Parser.parse_inner_portals(lines)},
        )

    @staticmethod
    def parse_points(lines: list[str]) -> set[Point]:
        output = set[Point]()
        for y, line in enumerate(lines):
            for x, ch in enumerate(line):
                if ch == ".":
                    output.add(Point(x - 2, y - 2))
        return output

    @staticmethod
    def parse_outer_portals(lines: list[str]) -> set[Portal]:
        output = set[Portal]()
        width = len(lines[0])
        height = len(lines)
        for y in range(height):
            if lines[y][0] != " ":
                output.add(Portal(lines[y][:2], Point(2 - 2, y - 2), outside=True))
            if lines[y][-1] != " ":
                output.add(Portal(lines[y][-2:], Point(width - 5, y - 2), outside=True))
        for x in range(width):
            if lines[0][x] != " ":
                output.add(
                    Portal(
                        f"{lines[0][x]}{lines[1][x]}", Point(x - 2, 2 - 2), outside=True
                    )
                )
            if lines[-1][x] != " ":
                output.add(
                    Portal(
                        f"{lines[-1][x]}{lines[-2][x]}",
                        Point(x - 2, height - 5),
                        outside=True,
                    )
                )
        return output

    @staticmethod
    def parse_inner_portals(lines: list[str]) -> set[Portal]:
        output = set[Portal]()
        donut_width = Parser.donut_width(lines)
        width = len(lines[0])
        height = len(lines)

        for y in range(donut_width, height - donut_width):
            if lines[y][donut_width] != " ":
                output.add(
                    Portal(
                        lines[y][donut_width : donut_width + 2],
                        Point(donut_width - 3, y - 2),
                        outside=False,
                    )
                )
            if lines[y][-donut_width - 1] != " ":
                output.add(
                    Portal(
                        lines[y][-donut_width - 2 : -donut_width],
                        Point(width - donut_width - 1, y - 2),
                        outside=False,
                    )
                )
        for x in range(donut_width, width - donut_width):
            if lines[donut_width][x] != " ":
                output.add(
                    Portal(
                        f"{lines[donut_width][x]}{lines[donut_width+1][x]}",
                        Point(x - 2, donut_width - 3),
                        outside=False,
                    )
                )
            if lines[-donut_width - 1][x] != " ":
                output.add(
                    Portal(
                        f"{lines[-donut_width - 2][x]}{lines[-donut_width - 1][x]}",
                        Point(x - 2, height - donut_width - 1),
                        outside=False,
                    )
                )
        return output

    @staticmethod
    def donut_width(lines: list[str]) -> int:
        for val in range(2, len(lines)):
            if lines[val][val] == " ":
                return val
        assert False
