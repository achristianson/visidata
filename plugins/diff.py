# command setdiff-sheet adds a diff colorizer for all sheets against current sheet

from visidata import Sheet, CellColorizer, vd

__version__ = "0.9"

vd.option('color_diff', 'red', 'color of values different from --diff source')
vd.option('color_diff_add', 'yellow', 'color of rows/columns added to --diff source')


def makeDiffColorizer(othersheet):
    def colorizeDiffs(sheet, col, row, cellval):
        if not row or not col:
            return None
        vcolidx = sheet.visibleCols.index(col)
        rowidx = sheet.rows.index(row)
        if vcolidx < len(othersheet.visibleCols) and rowidx < len(othersheet.rows):
            otherval = othersheet.visibleCols[vcolidx].getDisplayValue(othersheet.rows[rowidx])
            if cellval.display != otherval:
                return 'color_diff'
        else:
            return 'color_diff_add'
    return colorizeDiffs


@Sheet.api
def setDiffSheet(vs):
    Sheet.colorizers.append(CellColorizer(8, None, makeDiffColorizer(vs)))


BaseSheet.addCommand(None, 'setdiff-sheet', 'setDiffSheet()', 'set this sheet as diff sheet for all new sheets')
