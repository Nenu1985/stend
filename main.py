import os
import sys
import collections

from PyQt5 import QtWidgets, QtCore
import pyqtgraph as pg
import numpy as np
import form

# Команда для преобразования файла QtDesigner в питоновский:
#$ pyuic5 path/to/design.ui -o output/path/to/design.py

class MainApp(QtWidgets.QDialog, form.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.openButton.clicked.connect(self.browse_folder)  # Выполнить функцию browse_folder
        # при нажатии кнопки

    def browse_folder(self):
        files = QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл','./.')
        #
        # for f in files:
        #     self.listWidget.addItem(f)

        data = {}
        with open(files[0]) as chart_file:
            content = chart_file.readlines()

        content = content[5:]
        x_dates = []
        y_dates = []

        for line in content:
            line = line.split()
            if len(line) == 9:
                f, *values = line
                # x_dates.append(value_x)
                # y_dates.append(value_y)
                data[float(f)/10**6] = list(map(float, values))

        ordered_data = collections.OrderedDict(sorted(data.items()))

        for key, value in ordered_data.items():
            x_dates.append(key)
            y_dates.append(value[0])

        x_dates = np.asarray(x_dates).astype(np.float)
        y_dates = np.asarray(y_dates).astype(np.float)
        axes = pg.AxisItem(orientation='right')
        axes.setPen(color=pg.mkColor('b'))
        chart = pg.PlotWidget(background=pg.mkColor('w'))

        chart.getPlotItem().axes['left']['item'].setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        chart.getPlotItem().axes['left']['item'].setGrid(255)
        chart.getPlotItem().axes['bottom']['item'].setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        chart.getPlotItem().axes['bottom']['item'].setGrid(255)

        # symbol = in ['o', 's', 't', 't1', 't2', 't3','d', '+', 'x', 'p', 'h', 'star']
        chart.plot(x=x_dates, y=y_dates, pen=pg.mkPen('k', width=2))
        chart.plot(x=x_dates, y=y_dates/2, pen=pg.mkPen('r', width=2))

        self.widget = chart

        # self.horizontalLayout.widget = chart
        if self.horizontalLayout.count() > 0:
            self.horizontalLayout.takeAt(0)
        self.horizontalLayout.addWidget(chart)

        # self.horizontalLayout


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()



if __name__ == '__main__':
    main()
