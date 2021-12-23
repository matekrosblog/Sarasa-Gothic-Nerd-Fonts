#! /usr/bin/python

# usage:
#   python correct-ttf-font-family-name.py filename.ttf

import sys

from fontTools.ttLib import TTFont


def main():
    filename = sys.argv[1]

    font = TTFont(filename, recalcBBoxes=False)
    fontName = font["name"]

    originalFontUniqueID = fontName.getName(3, 1, 0, 0).toUnicode()
    originalFontFullname = fontName.getName(4, 1, 0, 0).toUnicode()
    originalFontPreferredStyle = fontName.getName(17, 1, 0, 0).toUnicode()

    for entry in fontName.names:
        nameID = entry.nameID
        platformID = entry.platformID
        platEncID = entry.platEncID
        langID = entry.langID

        # Windows language ID
        # https://github.com/fonttools/fonttools/blob/4.28.5/Lib/fontTools/ttLib/tables/_n_a_m_e.py#L558-L783
        zhTW = 0x0404
        ja = 0x0411
        zh = 0x0804
        zhHK = 0x0C04

        if platformID == 3 and langID in [zhTW, ja, zh, zhHK]:
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
            string = originalFontUniqueID.replace(
                f" {originalFontPreferredStyle}", " Nerd Font"
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 3:
            string = originalFontUniqueID.replace(
                f" {originalFontPreferredStyle}",
                f" Nerd Font {originalFontPreferredStyle}",
            )
            fontName.setName(string, nameID, platformID, platEncID, langID)

        elif nameID == 6:
            fontName.setName(
                originalFontFullname, nameID, platformID, platEncID, langID
            )

    font.save(filename)
    font.close()


if __name__ == "__main__":
    main()
