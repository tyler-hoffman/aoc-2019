class Parser:
    @staticmethod
    def parse(input: str) -> list[int]:
        line = input.strip().splitlines()[0]
        return [int(x) for x in line.split(",")]
