#! /usr/bin/python

# usage:
#   python correct-ttf-font-family-name.py filename.ttf

import sys

from fontTools.ttLib import TTFont


def main():
    filename = sys.argv[1]

    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    originFontUniqueID = fontName.getName(3, 1, 0, 0).toUnicode()
    originFontFullname = fontName.getName(4, 1, 0, 0).toUnicode()
    originFontPreferredStyle = fontName.getName(17, 1, 0, 0).toUnicode()

    for entry in fontName.names:
        nameID = entry.nameID
        platformID = entry.platformID
        platEncID = entry.platEncID
        langID = entry.langID

        if langID in [1028, 1041, 2052, 3076]:
            string = (
                entry.toUnicode()
                .replace(" CL", " CL Nerd Font")
                .replace(" TC", " TC Nerd Font")
                .replace(" J", " J Nerd Font")
                .replace(" SC", " SC Nerd Font")
                .replace(" HC", " HC Nerd Font")
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID in [1, 16]:
            string = originFontUniqueID.replace(
                f" {originFontPreferredStyle}", " Nerd Font"
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 3:
            string = originFontUniqueID.replace(
                f" {originFontPreferredStyle}", f" Nerd Font {originFontPreferredStyle}"
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 6:
            fontName.setName(originFontFullname, nameID, platformID, platEncID, langID)

    font.save(filename)
    font.close()


if __name__ == "__main__":
    main()
