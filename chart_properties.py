from PyQt5 import QtCore
from collections import OrderedDict


class ChartProperties:
    def __init__(self, color='#55aa00', thick=2, type=QtCore.Qt.SolidLine, marker='нет'):
        self.line_thick = thick
        self.color = color
        self.type = type
        self.marker = marker

    def __str__(self):
        return 'Chart property = color {}; thick {}; type {}; marker {}'\
            .format(self.color, self.line_thick, self.type, self.marker)

    def __repr__(self):
        return 'color {}; thick {}; type {}; marker {}'\
            .format(self.color, self.line_thick, self.type, self.marker)

    @classmethod
    def get_line_types(cls):
        return OrderedDict([
            ('сплошная', QtCore.Qt.SolidLine),
            ('штриховая', QtCore.Qt.DashLine),
            ('точки', QtCore.Qt.DotLine),
            ('штрихпунктир', QtCore.Qt.DashDotLine),
            ('штрихпунктирпунктир', QtCore.Qt.DashDotDotLine),
             ])

    @classmethod
    def get_line_markers(cls):
        return OrderedDict([
            ('', ''),
            ('*', ''),
            ('о', ''),
             ])