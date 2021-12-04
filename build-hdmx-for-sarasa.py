#! /usr/bin/python

# credit: https://github.com/be5invis/Sarasa-Gothic/issues/108#issuecomment-517240248

# usage:
#   python build-hdmx-for-sarasa.py your-sarasa-font.ttf

import sys
import math

from fontTools.ttLib import TTFont, newTable


def main():
    headFlagInstructionsMayAlterAdvanceWidth = 0x0010
    sarasaHintPpemMin = 11
    sarasaHintPpemMax = 48

    filename = sys.argv[1]

    font = TTFont(filename, recalcBBoxes=False)

    originalFontHead = font["head"]
    originalFontHmtx = font["hmtx"]

    originalFontHead.flags |= headFlagInstructionsMayAlterAdvanceWidth

    hdmxTable = newTable("hdmx")
    hdmxTable.hdmx = {}

    # build hdmx table for odd and hinted ppems only.
    for ppem in range(
        math.floor(sarasaHintPpemMin / 2) * 2 + 1, sarasaHintPpemMax + 1, 2
    ):
        halfUpm = originalFontHead.unitsPerEm / 2
        halfPpem = math.ceil(ppem / 2)
        hdmxTable.hdmx[ppem] = {
            name: math.ceil(width / halfUpm) * halfPpem
            for name, (width, _) in originalFontHmtx.metrics.items()
        }

    font["hdmx"] = hdmxTable

    font.save(filename)
    font.close()


if __name__ == "__main__":
    main()
