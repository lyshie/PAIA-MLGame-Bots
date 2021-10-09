"""
Author: HSIEH Li-Yi
"""

import argparse


class Bricker():
    def __init__(self, offset_x=0, offset_y=50):
        self.offset_x = offset_x
        self.offset_y = offset_y
        self._bricks = []

    def input(self, lines=[]):
        for y, line in enumerate(lines):
            for x, brick in enumerate(list(line.rstrip())):
                self._bricks.append({'x': x, 'y': y, 'brick': brick})

    def output(self):
        result = ["%d %d %d" % (self.offset_x, self.offset_y, -1)]
        for b in self._bricks:
            if b['brick'] == '=':
                result.append("%d %d %d" % (25 * b['x'], 10 * b['y'], 0))
            elif b['brick'] == '#':
                result.append("%d %d %d" % (25 * b['x'], 10 * b['y'], 1))

        return "\n".join(result)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-x",
                        "--offset-x",
                        type=int,
                        help="x offset",
                        default=0)
    parser.add_argument("-y",
                        "--offset-y",
                        type=int,
                        help="y offset",
                        default=25)
    parser.add_argument("-f", "--file", type=str, help="map file")

    args = parser.parse_args()

    if args.file:
        bricker = Bricker(args.offset_x, args.offset_y)
        with open(args.file, "r") as f:
            lines = f.readlines()
            bricker.input(lines)
            print(bricker.output())


if __name__ == "__main__":
    main()
