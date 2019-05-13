from PyQt5 import QtCore
from collections import OrderedDict


class ChartProperties:
    def __init__(self, color='#55aa00', thick=2, type=QtCore.Qt.SolidLine):
        self.line_thick = thick
        self.color = color
        self.type = type

    def __str__(self):
        return 'Chart property = color {}; thick {}; type {}'.format(self.color, self.line_thick, self.type)

    def __repr__(self):
        return 'color {}; thick {}; type {}'.format(self.color, self.line_thick, self.type)

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
            ('нет', ''),
            ('*', ''),
            ('о', ''),
             ])