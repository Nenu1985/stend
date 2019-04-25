from PyQt5 import QtCore


class ChartProperties:
    def __init__(self, color='#55aa00', thick=2, type=QtCore.Qt.SolidLine):
        self.line_thick = thick
        self.color = color
        self.type = type

    def __str__(self):
        return 'color: {}; thick: {}; type: {}'.format(
            self.color, self.line_thick, self.type
        )

    def __repr__(self):
        return self.__str__()
