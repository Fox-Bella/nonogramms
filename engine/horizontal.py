class Horizontal:

    def __init__(self, maps):
        for y in range(len(maps)):
            for x in range(len(maps[y])):
                print(f"{maps[y][x]} ", end="")
            print()