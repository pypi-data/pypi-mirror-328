import secrets
import sys
from typing import Any
import click
from cellular_automata_grids.grids import (
    SquareGrid,
    TriangularGrid,
    HexagonalGrid,
    TerminalSquareGrid,
)
from cellular_automata_grids import settings

sys.path.insert(0, settings.BASE_DIR.as_posix())
from tests.test_utils import DemoAutomaton  # noqa: E402
from tests.test_utils.demo_automaton import FredkinAutomaton, ConwaysGameOfLife, VON_NEUMANN_NEIGHBORHOOD

grid_types: dict[str, Any] = {
    "square": SquareGrid,
    "hexagonal": HexagonalGrid,
    "triangular": TriangularGrid,
    "terminal": TerminalSquareGrid,
    "sqr": SquareGrid,
    "hex": HexagonalGrid,
    "tri": TriangularGrid,
    "s": SquareGrid,
    "h": HexagonalGrid,
    "t": TriangularGrid,
}

demo_automata = {
    "demo": DemoAutomaton,
    "fredkin": FredkinAutomaton,
    "gol": ConwaysGameOfLife,
}

grid_types_names = list(grid_types.keys())
demo_automata_names = list(demo_automata.keys())


@click.command()
@click.option(
    "-t",
    "--grid-type",
    type=click.Choice(grid_types_names),
    default=grid_types_names[0],
    show_default=True,
    help="Select grid type.",
)
@click.option(
    "-a",
    "--automaton",
    type=click.Choice(demo_automata_names),
    default=demo_automata_names[0],
    show_default=True,
    help="Select automaton.",
)
@click.option("-w", "--width", default=800, show_default=True, help="Set grid number of cols.")
@click.option("-h", "--height", default=600, show_default=True, help="Set grid number or rows.")
@click.option("-f", "--fps", default=60, show_default=True, help="Set grid number or rows.")
@click.option("-s", "--steps", default=-1, show_default=True, help="Number of steps to run.")
@click.option("-c", "--cell-size", default=48, show_default=True, help="Set grid cell size.")
@click.option("-x", "--run", default=False, is_flag=True, show_default=True, help="Run automaton processing on start.")
def main(grid_type: str, automaton: str, height: int, steps: int, width: int, run: bool, fps: int, cell_size: int):
    colors = (
        "white",
        "black",
        "red",
        "green",
        "yellow",
        "blue",
        "cyan",
        "magenta",
        "gray",
        "darkred",
        "pink",
        "darkgreen",
        "darkgrey",
        "darkmagenta",
        "darkblue",
        "darkcyan",
    )

    cols = width // cell_size
    rows = height // cell_size

    click.echo(f"{grid_type=} {automaton=} {height=} {steps=} {width=} {run=} {fps=} {cell_size=}")

    match automaton:
        case "demo":

            states = list(range(len(colors)))
            grid: list[list[int]] = [[secrets.choice(states) for _ in range(cols)] for _ in range(rows)]

            automaton = DemoAutomaton(grid=grid, states=states)

        case "fredkin":

            grid = [[0 for _ in range(cols)] for _ in range(rows)]

            # Crab pattern from the Space Invaders.
            pattern = [
                [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
            ]

            mid_row, mid_col = rows // 2, cols // 2
            start_row, start_col = mid_row - len(pattern) // 2, mid_col - len(pattern[0]) // 2

            for row in range(len(pattern)):
                for col in range(len(pattern[0])):
                    grid[start_row + row][start_col + col] = pattern[row][col]

            automaton = FredkinAutomaton(grid=grid, neighborhood=VON_NEUMANN_NEIGHBORHOOD)

        case "gol":

            grid = [[0 for _ in range(cols)] for _ in range(rows)]
            grid[rows // 2][cols // 2] = 1
            grid[rows // 2 + 1][cols // 2 + 1] = 1
            grid[rows // 2 + 2][cols // 2 + 1] = 1
            grid[rows // 2 + 2][cols // 2 + 0] = 1
            grid[rows // 2 + 2][cols // 2 - 1] = 1

            automaton = ConwaysGameOfLife(grid=grid)

    # count = 1
    # while True:
    #     if steps > 0 and count >= steps:
    #         break
    #     next(automaton)
    #     print(f"* {count}", end="\r", flush=True)
    #     count += 1
    # print()

    grid_types[grid_type](
        title=automaton.name,
        automaton=automaton,
        tile_size=cell_size,
        max_iteration=steps,
        fps=fps,
        run=run,
        colors=colors,
    ).mainloop()


if __name__ == "__main__":
    main()
