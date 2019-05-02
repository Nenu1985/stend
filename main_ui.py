# Installation via pyinstaller:
# pip install pyinstaller
#
# RUN:
# pyinstaller --hidden-import python-docx --hidden-import pyqtgraph --onefile main_ui.py

import sys
import collections
import json
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QColorDialog
from PyQt5.QtGui import QFont
import pyqtgraph as pg
#from pytest import collect

import PGQ_image_exporter # modified pyqtgraph Exporter!
import numpy as np
import ui
import form
from cmath import rect
from chart import Chart
from chart_properties import ChartProperties as chart_prop
# from PyQt4 import QtCore, QtGuif

# Команда для преобразования файла QtDesigner в питоновский:
# -------->  pyuic5 UI.ui -o ui.py
# -------->  pyuic5 form.ui -o form.py


class MainApp(QtWidgets.QDialog, ui.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.dialog = Chart()

        # загрузка сохранённых данных из файла
        try:
            json_data = {}
            with open('data.txt') as json_file:
                json_data = json.load(json_file)
        except FileNotFoundError:
            print('There is no setting file "data.txt"')

        self.files = json_data['files']
        self.impedance = json_data['impedance']
        self.files_to_plot = json_data['files_to_plot']
        self.chart_properties = []
        for prop in json_data['chart_properties']:
            self.chart_properties.append(chart_prop(
                color=prop['color'],
                thick=prop['line_thick'],
                type=prop['type'],
            )
            )
        self.setGeometry(QtCore.QRect(*json_data['main_geometry']))
        self.dialog.setGeometry(QtCore.QRect(*json_data['child_geometry']))


        # Отображаем начальные значения в контролах
        self.set_init_values_to_controls()

        # ----------- ПОДПИСЬ ОБРАБОТЧИКОВ СОБЫТИЙ --------------- #
        self.checkBox_filePlot1.stateChanged.connect(self.set_files_to_plot)
        self.checkBox_filePlot2.stateChanged.connect(self.set_files_to_plot)
        self.checkBox_filePlot3.stateChanged.connect(self.set_files_to_plot)
        self.checkBox_filePlot4.stateChanged.connect(self.set_files_to_plot)
        self.checkBox_filePlot5.stateChanged.connect(self.set_files_to_plot)
        self.checkBox_filePlot6.stateChanged.connect(self.set_files_to_plot)

        self.pushButton_open_file1.clicked.connect(self.onclick_open_file1)
        self.pushButton_open_file2.clicked.connect(self.onclick_open_file2)
        self.pushButton_open_file3.clicked.connect(self.onclick_open_file3)
        self.pushButton_open_file4.clicked.connect(self.onclick_open_file4)
        self.pushButton_open_file5.clicked.connect(self.onclick_open_file5)
        self.pushButton_open_file6.clicked.connect(self.onclick_open_file6)

        self.spinBox_impedance.valueChanged.connect(self.spinBox_impedance_valueChanged)

        self.pushButton_color1.clicked.connect(self.onclick_color1)
        self.pushButton_color2.clicked.connect(self.onclick_color2)
        self.pushButton_color3.clicked.connect(self.onclick_color3)
        self.pushButton_color4.clicked.connect(self.onclick_color4)
        self.pushButton_color5.clicked.connect(self.onclick_color5)
        self.pushButton_color6.clicked.connect(self.onclick_color6)

        self.spinBox_thickness1.valueChanged.connect(self.spinBox_thickness1_valueChanged)
        self.spinBox_thickness2.valueChanged.connect(self.spinBox_thickness2_valueChanged)
        self.spinBox_thickness3.valueChanged.connect(self.spinBox_thickness3_valueChanged)
        self.spinBox_thickness4.valueChanged.connect(self.spinBox_thickness4_valueChanged)
        self.spinBox_thickness5.valueChanged.connect(self.spinBox_thickness5_valueChanged)
        self.spinBox_thickness6.valueChanged.connect(self.spinBox_thickness6_valueChanged)

        self.pushButton_S11.clicked.connect(self.calc_s11_data)
        self.pushButton_S21.clicked.connect(self.calc_s21_data)
        self.pushButton_S12.clicked.connect(self.calc_s12_data)
        self.pushButton_S22.clicked.connect(self.calc_s22_data)
        self.pushButton_VSWR1.clicked.connect(self.calc_VSWR1_data)
        self.pushButton_VSWR2.clicked.connect(self.calc_VSWR2_data)
        self.pushButton_Rx1_re.clicked.connect(self.calc_Rx1_re_data)
        self.pushButton_Rx1_im.clicked.connect(self.calc_Rx1_im_data)
        self.pushButton_Rx2_re.clicked.connect(self.calc_Rx2_re_data)
        self.pushButton_Rx2_im.clicked.connect(self.calc_Rx2_im_data)


        self.freq_values = []
        self.y_values = []
        # при нажатии кнопки

    def set_init_values_to_controls(self):
        self.spinBox_impedance.setValue(self.impedance)

        self.lineEdit_filename1.setText(self.files[0])
        self.lineEdit_filename2.setText(self.files[1])
        self.lineEdit_filename3.setText(self.files[2])
        self.lineEdit_filename4.setText(self.files[3])
        self.lineEdit_filename5.setText(self.files[4])
        self.lineEdit_filename6.setText(self.files[5])

        self.pushButton_color1.setStyleSheet("background-color: {}".format(self.chart_properties[0].color))
        self.pushButton_color2.setStyleSheet("background-color: {}".format(self.chart_properties[1].color))
        self.pushButton_color3.setStyleSheet("background-color: {}".format(self.chart_properties[2].color))
        self.pushButton_color4.setStyleSheet("background-color: {}".format(self.chart_properties[3].color))
        self.pushButton_color5.setStyleSheet("background-color: {}".format(self.chart_properties[4].color))
        self.pushButton_color6.setStyleSheet("background-color: {}".format(self.chart_properties[5].color))

        self.spinBox_thickness1.setValue(self.chart_properties[0].line_thick)
        self.spinBox_thickness2.setValue(self.chart_properties[1].line_thick)
        self.spinBox_thickness3.setValue(self.chart_properties[2].line_thick)
        self.spinBox_thickness4.setValue(self.chart_properties[3].line_thick)
        self.spinBox_thickness5.setValue(self.chart_properties[4].line_thick)
        self.spinBox_thickness6.setValue(self.chart_properties[5].line_thick)

        self.checkBox_filePlot1.setCheckState(self.files_to_plot[0])
        self.checkBox_filePlot2.setCheckState(self.files_to_plot[1])
        self.checkBox_filePlot3.setCheckState(self.files_to_plot[2])
        self.checkBox_filePlot4.setCheckState(self.files_to_plot[3])
        self.checkBox_filePlot5.setCheckState(self.files_to_plot[4])
        self.checkBox_filePlot6.setCheckState(self.files_to_plot[5])

    def get_files_to_plot(self):
        files_to_plots = [
            self.checkBox_filePlot1.isChecked(),
            self.checkBox_filePlot2.isChecked(),
            self.checkBox_filePlot3.isChecked(),
            self.checkBox_filePlot4.isChecked(),
            self.checkBox_filePlot5.isChecked(),
            self.checkBox_filePlot6.isChecked(),
        ]
        return files_to_plots

    def set_files_to_plot(self):
        self.files_to_plot = self.get_files_to_plot()

    def plot_chart(self):
        chart_pw = pg.PlotWidget(background=pg.mkColor('w'))
        chart_pw.addLegend(offset=(600, 30))

        chart_pw.getPlotItem().axes['left']['item'].setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        chart_pw.getPlotItem().axes['left']['item'].setGrid(255)
        chart_pw.getPlotItem().axes['bottom']['item'].setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        chart_pw.getPlotItem().axes['bottom']['item'].setGrid(255)
        chart_pw.plotItem.axes['bottom']['item'].setLabel('Частота', units='МГц')
        chart_pw.plotItem.axes['bottom']['item'].labelStyle = {'font-size': '14pt'}

        p1 = chart_pw.plotItem
        p1.plot()
        for i, y_value in enumerate(self.y_values):
            p1.addItem(pg.PlotCurveItem(
                x=self.freq_values[i],
                y=y_value,
                pen=self.get_pen_by_int(i),
                name='chart {}'.format(i),
            ))

        self.dialog.plot_chart(chart_pw)
        self.dialog.files_names = self.files
        self.dialog.show()
        i = 0;

    def get_pen_by_int(self, chart_num):
        return pg.mkPen(
            self.chart_properties[chart_num].color,
            width=self.chart_properties[chart_num].line_thick,
            style=self.chart_properties[chart_num].type,
        )

    def to_json(self):
        data = {}
        data['files'] = self.files
        data['chart_properties'] = [i.__dict__ for i in self.chart_properties]
        data['impedance'] = self.impedance
        data['main_geometry'] = self.geometry().getRect()
        data['child_geometry'] = self.dialog.geometry().getRect()
        data['files_to_plot'] = self.get_files_to_plot()

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    # -------------------------------------- CLASS METHODS ----------------------#

    def read_data_file(self, filename):
        data = {}

        try:
            with open(filename) as file:
                content = file.readlines()
        except FileNotFoundError:
            print('No such file (read_data_file funct)')
            return np.asarray([]).astype(np.float), np.asarray([]).astype(np.float)

        if content:
            content = content[5:]
        else:
            return np.asarray([]).astype(np.float), np.asarray([]).astype(np.float)

        for line in content:
            line = line.split()
            if len(line) == 9:  # case for s2p
                f, *values = line
                data[float(f) / 10 ** 6] = list(map(float, values))
            if len(line) == 3:  # case for s1p
                f, *values = line
                data[float(f) / 10 ** 6] = list(map(float, values))


        data = collections.OrderedDict(sorted(data.items()))
        freq_values = list(data.keys())
        freq_values = np.asarray(freq_values).astype(np.float)
        values_correct_format = np.asarray(list(data.values())).astype(np.float)

        return freq_values, values_correct_format


    def get_data_values(self, column_number, data_files):
        freq_values_out = []
        values = []
        for i, data_file in enumerate(data_files):
            if self.files_to_plot[i]:
                freq_values,  values_correct_format = self.read_data_file(data_file)
                if not freq_values.any() and not values_correct_format.any():
                    continue
                if column_number <= values_correct_format.shape[1] - 1:
                    freq_values_out.append(freq_values)
                    values.append(values_correct_format[:, column_number])
        return freq_values_out, values

    def calc_VSWR(self, port_number, data_files):

        if port_number == 2:
            freqs, values =  self.get_data_values(6, data_files)  # abs(S22)
        else:
            freqs, values = self.get_data_values(0, data_files)  # abs(S11)

        vswr = []
        for value in values:
            vswr.append((1 + value) / (1 - value))

        return freqs, vswr

    def calc_Rx(self, port_number, data_files, z0):

        if port_number == 2:
            freqs, values_abs =  self.get_data_values(6, data_files)  # abs(S22)
            _, values_ang = self.get_data_values(7, data_files)  # abs(S22)
        else:
            freqs, values_abs = self.get_data_values(0, data_files)  # abs(S22)
            _, values_ang = self.get_data_values(1, data_files)  # abs(S22)

        zx = []
        nprect = np.vectorize(rect)
        for series in range(len(values_abs)):
            value_abs = values_abs[series]
            value_ang_rad = values_ang[series] * np.pi / 180
            complex_ko = nprect(value_abs, value_ang_rad)
            zx.append(z0 * ((1 + complex_ko) / (1 - complex_ko)))

        return freqs, zx

    def browse_folder(self):
        return QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл')[0]


# -------------------------------------- EVENT HANDLERS ----------------------#
#     def checkbox1_state_changed(self):
#         self.files_to_plot = self.get_files_to_plot()

    def spinBox_thickness1_valueChanged(self):
        self.chart_properties[0].line_thick = int(self.spinBox_thickness1.value())

    def spinBox_thickness2_valueChanged(self):
        self.chart_properties[1].line_thick = int(self.spinBox_thickness2.value())

    def spinBox_thickness3_valueChanged(self):
        self.chart_properties[2].line_thick = int(self.spinBox_thickness3.value())

    def spinBox_thickness4_valueChanged(self):
        self.chart_properties[3].line_thick = int(self.spinBox_thickness4.value())

    def spinBox_thickness5_valueChanged(self):
        self.chart_properties[4].line_thick = int(self.spinBox_thickness5.value())

    def spinBox_thickness6_valueChanged(self):
        self.chart_properties[5].line_thick = int(self.spinBox_thickness6.value())

    def spinBox_impedance_valueChanged(self):
        self.impedance = int(self.spinBox_impedance.value())

    def onclick_open_file1(self):
        self.files[0] = self.browse_folder()
        self.lineEdit_filename1.setText(self.files[0])

    def onclick_open_file2(self):
        self.files[1] = self.browse_folder()
        self.lineEdit_filename2.setText(self.files[1])

    def onclick_open_file3(self):
        self.files[2] = self.browse_folder()
        self.lineEdit_filename3.setText(self.files[2])

    def onclick_open_file4(self):
        self.files[3] = self.browse_folder()
        self.lineEdit_filename4.setText(self.files[3])

    def onclick_open_file5(self):
        self.files[4] = self.browse_folder()
        self.lineEdit_filename5.setText(self.files[4])

    def onclick_open_file6(self):
        self.files[5] = self.browse_folder()
        self.lineEdit_filename6.setText(self.files[5])

    def onclick_color1(self):
        color = QColorDialog.getColor()
        self.chart_properties[0].color = color.name()
        self.pushButton_color1.setStyleSheet("background-color: {}".format(self.chart_properties[0].color))

    def onclick_color2(self):
        color = QColorDialog.getColor()
        self.chart_properties[1].color = color.name()
        self.pushButton_color2.setStyleSheet("background-color: {}".format(self.chart_properties[1].color))

    def onclick_color3(self):
        color = QColorDialog.getColor()
        self.chart_properties[2].color = color.name()
        self.pushButton_color3.setStyleSheet("background-color: {}".format(self.chart_properties[2].color))

    def onclick_color4(self):
        color = QColorDialog.getColor()
        self.chart_properties[3].color = color.name()
        self.pushButton_color4.setStyleSheet("background-color: {}".format(self.chart_properties[3].color))

    def onclick_color5(self):
        color = QColorDialog.getColor()
        self.chart_properties[4].color = color.name()
        self.pushButton_color5.setStyleSheet("background-color: {}".format(self.chart_properties[4].color))

    def onclick_color6(self):
        color = QColorDialog.getColor()
        self.chart_properties[5].color = color.name()
        self.pushButton_color6.setStyleSheet("background-color: {}".format(self.chart_properties[5].color))


    def calc_Rx1_re_data(self):
        self.freq_values, zx =  self.calc_Rx(1, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.real)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)

        self.plot_chart()

    def calc_Rx1_im_data(self):
        self.freq_values, zx =  self.calc_Rx(1, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.imag)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)

        self.plot_chart()

    def calc_Rx2_re_data(self):
        self.freq_values, zx =  self.calc_Rx(2, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.real)
        self.y_values = values_to_plot

        self.plot_chart()

    def calc_Rx2_im_data(self):
        self.freq_values, zx =  self.calc_Rx(2, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.imag)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)

        self.plot_chart()

    def calc_VSWR1_data(self):
        self.freq_values, self.y_values =  self.calc_VSWR(1, self.files)
        self.plot_chart()

    def calc_VSWR2_data(self):
        self.freq_values, self.y_values = self.calc_VSWR(2, self.files)
        self.plot_chart()

    def calc_s11_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(0, self.files)
        self.plot_chart()

    def calc_s12_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(2, self.files)
        self.plot_chart()

    def calc_s21_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(4, self.files)
        self.plot_chart()

    def calc_s22_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(6, self.files)
        self.plot_chart()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()

    app.exec_()
    window.to_json()


if __name__ == '__main__':
    main()
