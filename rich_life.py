import time

from rich.live import Live
from rich.table import Table

from life import Life

width = 20
height = 20

game = Life(width, height)
game.seed([
    [4, 8],
    [5, 8],
    [6, 8],
    [7, 8],
    [7, 9],
    [7, 1],
    [10, 5],
    [10, 4],
    [11, 4],
])


def generate_table():
    table = Table(show_header=False)

    for row in range(0, height):
        cells = ["0" if cell.is_alive() else "-" for cell in game.grid[row]]
        table.add_row(*cells)

    return table


with Live(generate_table(), refresh_per_second=4) as live:
    for tick in range(0, 50):
        live.update(generate_table())
        time.sleep(1)
        game.tick()
