# Installation via pyinstaller:
# pip install pyinstaller
#
# RUN:
# pyinstaller --hidden-import python-docx --hidden-import pyqtgraph --onefile main_ui.py
import sys
import collections
import json
from typing import List

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QColorDialog
import pyqtgraph as pg
import numpy as np
import ui
from cmath import rect
from chart import Chart
from chart_properties import ChartProperties as ChartProps

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
        self.files_smp = json_data['files_smp']
        self.impedance = json_data['impedance']
        self.files_to_plot = json_data['files_to_plot']
        self.files_to_plot_smp = json_data.get('files_to_plot_smp', '')
        self.chart_legend_offset = json_data.get('chart_legend_offset', (600, 30))
        self.title = 'График'
        self.chart_properties = []
        self.freqs_last = []
        self.values_last = []
        for prop in json_data['chart_properties']:
            self.chart_properties.append(ChartProps(
                color=prop['color'],
                thick=prop['line_thick'],
                type=prop['type'],
                marker=prop.get('marker', ''),

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
        self.checkBox_filePlot1_smp.stateChanged.connect(self.set_files_to_plot_smp)
        self.checkBox_filePlot2_smp.stateChanged.connect(self.set_files_to_plot_smp)
        self.checkBox_filePlot3_smp.stateChanged.connect(self.set_files_to_plot_smp)
        self.checkBox_filePlot4_smp.stateChanged.connect(self.set_files_to_plot_smp)
        self.checkBox_filePlot5_smp.stateChanged.connect(self.set_files_to_plot_smp)
        self.checkBox_filePlot6_smp.stateChanged.connect(self.set_files_to_plot_smp)

        self.checkBox_vert_line_show.stateChanged.connect(self.plot_chart)
        self.checkBox_hor_line_show.stateChanged.connect(self.plot_chart)

        self.pushButton_open_file1.clicked.connect(self.onclick_open_file1)
        self.pushButton_open_file2.clicked.connect(self.onclick_open_file2)
        self.pushButton_open_file3.clicked.connect(self.onclick_open_file3)
        self.pushButton_open_file4.clicked.connect(self.onclick_open_file4)
        self.pushButton_open_file5.clicked.connect(self.onclick_open_file5)
        self.pushButton_open_file6.clicked.connect(self.onclick_open_file6)
        self.pushButton_open_file1_smp.clicked.connect(self.onclick_open_file1_smp)
        self.pushButton_open_file2_smp.clicked.connect(self.onclick_open_file2_smp)
        self.pushButton_open_file3_smp.clicked.connect(self.onclick_open_file3_smp)
        self.pushButton_open_file4_smp.clicked.connect(self.onclick_open_file4_smp)
        self.pushButton_open_file5_smp.clicked.connect(self.onclick_open_file5_smp)
        self.pushButton_open_file6_smp.clicked.connect(self.onclick_open_file6_smp)

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

        self.spinBox_vert_line_low_freq.valueChanged.connect(self.plot_chart)
        self.spinBox_vert_line_freq_high.valueChanged.connect(self.plot_chart)
        self.doubleSpinBox_hor_line.valueChanged.connect(self.plot_chart)
        # self.spinBox_vert_line_low_freq.valueChanged.connect(self.spinBox_vert_line_low_freq_valueChanged)

        self.comboBox_linetype1.currentTextChanged.connect(self.comboBox_linetype1_changed)
        self.comboBox_linetype2.currentTextChanged.connect(self.comboBox_linetype2_changed)
        self.comboBox_linetype3.currentTextChanged.connect(self.comboBox_linetype3_changed)
        self.comboBox_linetype4.currentTextChanged.connect(self.comboBox_linetype4_changed)
        self.comboBox_linetype5.currentTextChanged.connect(self.comboBox_linetype5_changed)
        self.comboBox_linetype6.currentTextChanged.connect(self.comboBox_linetype6_changed)

        self.comboBox_marker1.currentTextChanged.connect(self.comboBox_marker1_changed)
        self.comboBox_marker2.currentTextChanged.connect(self.comboBox_marker2_changed)
        self.comboBox_marker3.currentTextChanged.connect(self.comboBox_marker3_changed)
        self.comboBox_marker4.currentTextChanged.connect(self.comboBox_marker4_changed)
        self.comboBox_marker5.currentTextChanged.connect(self.comboBox_marker5_changed)
        self.comboBox_marker6.currentTextChanged.connect(self.comboBox_marker6_changed)
        # self.dialog.comboBox_marker.currentTextChanged.connect(self.comboBox_marker_changed)
        # self.comboBox_marker1.currentTextChanged.connect(self.comboBox_marker1_changed)

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

        self.pushButton_S11_ang.clicked.connect(self.calc_S11_ang_data)
        self.pushButton_S12_ang.clicked.connect(self.calc_S12_ang_data)
        self.pushButton_S21_ang.clicked.connect(self.calc_S21_ang_data)
        self.pushButton_S22_ang.clicked.connect(self.calc_S22_ang_data)

        self.pushButton_smp_plot_vswr.clicked.connect(self.pushButton_smp_plot_vswr_click)
        self.pushButton_smp_plot_phase.clicked.connect(self.pushButton_smp_plot_phase_click)



        self.freq_values = []
        self.y_values = []
        # при нажатии кнопки

    def set_init_values_to_controls(self):
        self.dialog.setWindowTitle('График')

        self.setWindowTitle('Входные характеристики')
        self.spinBox_impedance.setValue(self.impedance)

        self.lineEdit_filename1.setText(self.files[0])
        self.lineEdit_filename2.setText(self.files[1])
        self.lineEdit_filename3.setText(self.files[2])
        self.lineEdit_filename4.setText(self.files[3])
        self.lineEdit_filename5.setText(self.files[4])
        self.lineEdit_filename6.setText(self.files[5])
        self.lineEdit_filename1_smp.setText(self.files_smp[0])
        self.lineEdit_filename2_smp.setText(self.files_smp[1])
        self.lineEdit_filename3_smp.setText(self.files_smp[2])
        self.lineEdit_filename4_smp.setText(self.files_smp[3])
        self.lineEdit_filename5_smp.setText(self.files_smp[4])
        self.lineEdit_filename6_smp.setText(self.files_smp[5])

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
        self.checkBox_filePlot1_smp.setCheckState(self.files_to_plot_smp[0])
        self.checkBox_filePlot2_smp.setCheckState(self.files_to_plot_smp[1])
        self.checkBox_filePlot3_smp.setCheckState(self.files_to_plot_smp[2])
        self.checkBox_filePlot4_smp.setCheckState(self.files_to_plot_smp[3])
        self.checkBox_filePlot5_smp.setCheckState(self.files_to_plot_smp[4])
        self.checkBox_filePlot6_smp.setCheckState(self.files_to_plot_smp[5])

        items = ChartProps.get_line_types()
        keys = list(items.keys())

        self.comboBox_linetype1.addItems(keys)
        self.comboBox_linetype2.addItems(keys)
        self.comboBox_linetype3.addItems(keys)
        self.comboBox_linetype4.addItems(keys)
        self.comboBox_linetype5.addItems(keys)
        self.comboBox_linetype6.addItems(keys)

        self.comboBox_linetype1.setCurrentIndex(list(items.values()).index(self.chart_properties[0].type))
        self.comboBox_linetype2.setCurrentIndex(list(items.values()).index(self.chart_properties[1].type))
        self.comboBox_linetype3.setCurrentIndex(list(items.values()).index(self.chart_properties[2].type))
        self.comboBox_linetype4.setCurrentIndex(list(items.values()).index(self.chart_properties[3].type))
        self.comboBox_linetype5.setCurrentIndex(list(items.values()).index(self.chart_properties[4].type))
        self.comboBox_linetype6.setCurrentIndex(list(items.values()).index(self.chart_properties[5].type))

        items = ChartProps.get_line_markers()
        keys = list(items.keys())
        # self.dialog.comboBox_marker.addItems(keys)
        self.comboBox_marker1.addItems(keys)
        self.comboBox_marker2.addItems(keys)
        self.comboBox_marker3.addItems(keys)
        self.comboBox_marker4.addItems(keys)
        self.comboBox_marker5.addItems(keys)
        self.comboBox_marker6.addItems(keys)
        self.comboBox_linetype1.setCurrentIndex(keys.index(self.chart_properties[0].marker))
        self.comboBox_linetype2.setCurrentIndex(keys.index(self.chart_properties[1].marker))
        self.comboBox_linetype3.setCurrentIndex(keys.index(self.chart_properties[2].marker))
        self.comboBox_linetype4.setCurrentIndex(keys.index(self.chart_properties[3].marker))
        self.comboBox_linetype5.setCurrentIndex(keys.index(self.chart_properties[4].marker))
        self.comboBox_linetype6.setCurrentIndex(keys.index(self.chart_properties[5].marker))


    def get_files_to_plot(self):
        """
        Check checkboxes for plotting file
        :return: list of boolean values
        """
        files_to_plots = [
            self.checkBox_filePlot1.isChecked(),
            self.checkBox_filePlot2.isChecked(),
            self.checkBox_filePlot3.isChecked(),
            self.checkBox_filePlot4.isChecked(),
            self.checkBox_filePlot5.isChecked(),
            self.checkBox_filePlot6.isChecked(),
        ]

        return files_to_plots

    def get_files_to_plot_smp(self):
        files_to_plots_smp = [
            self.checkBox_filePlot1_smp.isChecked(),
            self.checkBox_filePlot2_smp.isChecked(),
            self.checkBox_filePlot3_smp.isChecked(),
            self.checkBox_filePlot4_smp.isChecked(),
            self.checkBox_filePlot5_smp.isChecked(),
            self.checkBox_filePlot6_smp.isChecked(),
        ]
        return files_to_plots_smp

    def set_files_to_plot(self):
        self.files_to_plot = self.get_files_to_plot()

    def set_files_to_plot_smp(self):
        self.files_to_plot_smp = self.get_files_to_plot_smp()

    def plot_chart(self):

        self.dialog.is_v_lines_plot = self.checkBox_vert_line_show.isChecked()
        self.dialog.is_h_lines_plot = self.checkBox_hor_line_show.isChecked()

        if not self.checkBox_do_not_delete_current_plots.isChecked():
            self.dialog.delete_plot_items()

        chart_plot_item = self.dialog.chart
        chart_plot_item.setTitle(self.title, **{'color': '#000', 'size': '14pt'})

        plots_number = self.dialog.get_chart_plot_items_number()

        freqs = []
        valueses = []
        if self.tabWidget.currentIndex() == 1:
            freqs = self.freq_values
            valueses = self.y_values
        elif self.tabWidget.currentIndex() == 2:
            freqs = self.freq_values_smp
            valueses = self.y_values_smp

        if not freqs:
            freqs = self.freqs_last
            valueses = self.values_last

        self.freqs_last = freqs
        self.values_last = valueses

        for i, y_value in enumerate(valueses):
            if self.chart_properties[i].marker:
                symb = self.chart_properties[i].marker
            else:
                symb = None

            plot_item = pg.PlotDataItem()
            plot_item.setData(
                x=freqs[i],
                y=y_value,
                symbol=symb,
                pen=self.get_pen_by_int(i + plots_number),
                name='график {}'.format(i + plots_number),
            )

            chart_plot_item.addItem(plot_item)

        # self.enableCrossHairs(chart_pw)
        self.dialog.plot_chart()

        self.dialog.view_box.vLine_freq_low.setPos(self.spinBox_vert_line_low_freq.value())
        self.dialog.view_box.vLine_freq_high.setPos(self.spinBox_vert_line_freq_high.value())
        self.dialog.view_box.hLine_y.setPos(self.doubleSpinBox_hor_line.value())

        file_name_list_to_dialog = []
        if self.tabWidget.currentIndex() == 1:  # 1 tab
            for i, file in enumerate(self.files):
                if self.get_files_to_plot()[i]:
                    file_name_list_to_dialog.append(file)
        if self.tabWidget.currentIndex() == 2:  # 2 tab
            for i, file in enumerate(self.files_smp):
                if self.get_files_to_plot_smp()[i]:
                    file_name_list_to_dialog.append(file)

        self.dialog.files_names = file_name_list_to_dialog
        self.dialog.show()

    def get_pen_by_int(self, chart_num):
        N = len(self.chart_properties)

        if N > chart_num:
            pen = pg.mkPen(
                self.chart_properties[chart_num].color,
                width=self.chart_properties[chart_num].line_thick,
                style=self.chart_properties[chart_num].type,
            )
        else:
            pen = pg.mkPen('k')
        return pen

    def to_json(self):
        data = dict()
        data['files'] = self.files
        data['files_smp'] = self.files_smp
        data['chart_properties'] = [i.__dict__ for i in self.chart_properties]
        data['impedance'] = self.impedance
        data['main_geometry'] = self.geometry().getRect()
        data['child_geometry'] = self.dialog.geometry().getRect()
        data['files_to_plot'] = self.get_files_to_plot()
        data['files_to_plot_smp'] = self.get_files_to_plot_smp()
        # data['chart_legend_offset'] = self.dialog.widget.plotItem.legend.offset

        with open('data.txt', 'w') as outfile:
            json.dump(data, outfile, indent=4)
    # -------------------------------------- CLASS METHODS ----------------------#

    @staticmethod
    def read_data_file(filename):
        data = {}

        try:
            with open(filename) as file:
                content = file.readlines()
        except FileNotFoundError:
            print('No such file (read_data_file funct)')
            return np.asarray([]).astype(np.float), np.asarray([]).astype(np.float)

        if content and filename[-3:] == 'smp':
            content = content[:]
        elif content:
            content = content[5:]
        else:
            return np.asarray([]).astype(np.float), np.asarray([]).astype(np.float)

        for line in content:
            line = line.split()
            if len(line) == 9:  # case for s2p
                f, *values = line
                data[float(f) / 10 ** 6] = list(map(float, values))
            if len(line) == 3 and filename and filename[-3:] == 's1p':  # case for s1p
                f, *values = line
                data[float(f) / 10 ** 6] = list(map(float, values))
            if len(line) == 3 and filename and filename[-3:] == 'smp':  # case for smp
                f, *values = line
                data[float(f)] = list(map(float, values))

        data = collections.OrderedDict(sorted(data.items()))
        freq_values = list(data.keys())
        freq_values = np.asarray(freq_values).astype(np.float)
        values_correct_format = np.asarray(list(data.values())).astype(np.float)

        return freq_values, values_correct_format

    def get_data_values(self, column_number, data_files):
        """

        :param column_number: column in s2p file (0 - freq, 1 - s11_abs, 2-s11_and...)
        :param data_files: list of files are need to plot
        :return: tuple (freqs : list, values: list)
        """
        freq_values_out = []
        values = []
        if self.tabWidget.currentIndex() == 1:
            for i, data_file in enumerate(data_files):
                if self.files_to_plot[i]:
                    freq_values,  values_correct_format = self.read_data_file(data_file)
                    if not freq_values.any() and not values_correct_format.any():
                        continue
                    if column_number <= values_correct_format.shape[1] - 1:
                        freq_values_out.append(freq_values)
                        values.append(values_correct_format[:, column_number])
        else:
            for i, data_file in enumerate(data_files):
                if self.files_to_plot_smp[i]:
                    freq_values,  values_correct_format = self.read_data_file(data_file)
                    if not freq_values.any() and not values_correct_format.any():
                        continue
                    if column_number <= values_correct_format.shape[1] - 1:
                        freq_values_out.append(freq_values)
                        values.append(values_correct_format[:, column_number])
        return freq_values_out, values

    def calc_vswr(self, port_number, data_files):

        if port_number == 2:
            freqs, values = self.get_data_values(6, data_files)  # abs(S22)
        else:
            freqs, values = self.get_data_values(0, data_files)  # abs(S11)

        vswr = []  # type: List[float]
        for value in values:
            vswr.append((1 + value) / (1 - value))

        return freqs, vswr

    def calc_rx(self, port_number, data_files, z0):

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
        if self.tabWidget.currentIndex() == 1:  # plots s1p - s2p
            return QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл')[0]
        else:  # plots smp
            return QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите файл', filter="smp(*.smp)")[0]



# -------------------------------------- EVENT HANDLERS ----------------------#
#     def spinBox_vert_line_low_freq_valueChanged(self, value):

    # ------------ ТИП (штрих и т.д.) -------------------#
    def comboBox_linetype1_changed(self, value):
        self.chart_properties[0].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_linetype2_changed(self, value):
        self.chart_properties[1].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_linetype3_changed(self, value):
        self.chart_properties[2].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_linetype4_changed(self, value):
        self.chart_properties[3].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_linetype5_changed(self, value):
        self.chart_properties[4].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_linetype6_changed(self, value):
        self.chart_properties[5].type = ChartProps.get_line_types().get(value, QtCore.Qt.SolidLine)
        self.plot_chart()

    def comboBox_marker1_changed(self, value):
        self.chart_properties[0].marker = value
        self.plot_chart()

    def comboBox_marker2_changed(self, value):
        self.chart_properties[1].marker = value
        self.plot_chart()

    def comboBox_marker3_changed(self, value):
        self.chart_properties[2].marker = value
        self.plot_chart()

    def comboBox_marker4_changed(self, value):
        self.chart_properties[3].marker = value
        self.plot_chart()

    def comboBox_marker5_changed(self, value):
        self.chart_properties[4].marker = value
        self.plot_chart()

    def comboBox_marker6_changed(self, value):
        self.chart_properties[5].marker = value
        self.plot_chart()

    def comboBox_marker_changed(self, value):
        # self.chart_properties[0].marker = value
        self.plot_chart()

    # ------------ ТОЛЩИНА -------------------#
    def spinBox_thickness1_valueChanged(self):
        self.chart_properties[0].line_thick = int(self.spinBox_thickness1.value())
        self.plot_chart()

    def spinBox_thickness2_valueChanged(self):
        self.chart_properties[1].line_thick = int(self.spinBox_thickness2.value())
        self.plot_chart()

    def spinBox_thickness3_valueChanged(self):
        self.chart_properties[2].line_thick = int(self.spinBox_thickness3.value())
        self.plot_chart()

    def spinBox_thickness4_valueChanged(self):
        self.chart_properties[3].line_thick = int(self.spinBox_thickness4.value())
        self.plot_chart()

    def spinBox_thickness5_valueChanged(self):
        self.chart_properties[4].line_thick = int(self.spinBox_thickness5.value())
        self.plot_chart()

    def spinBox_thickness6_valueChanged(self):
        self.chart_properties[5].line_thick = int(self.spinBox_thickness6.value())
        self.plot_chart()

    # ------------ СОПРОТИВЛЕНИЕ -------------------#
    def spinBox_impedance_valueChanged(self):
        self.impedance = int(self.spinBox_impedance.value())
        self.plot_chart()

    # ------------ ОТКРЫТЬ ФАЙЛ -------------------#
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

    def onclick_open_file1_smp(self):
        self.files_smp[0] = self.browse_folder()
        self.lineEdit_filename1_smp.setText(self.files_smp[0])

    def onclick_open_file2_smp(self):
        self.files_smp[1] = self.browse_folder()
        self.lineEdit_filename2_smp.setText(self.files_smp[1])

    def onclick_open_file3_smp(self):
        self.files_smp[2] = self.browse_folder()
        self.lineEdit_filename3_smp.setText(self.files_smp[2])

    def onclick_open_file4_smp(self):
        self.files_smp[3] = self.browse_folder()
        self.lineEdit_filename4_smp.setText(self.files_smp[3])

    def onclick_open_file5_smp(self):
        self.files_smp[4] = self.browse_folder()
        self.lineEdit_filename5_smp.setText(self.files_smp[4])

    def onclick_open_file6_smp(self):
        self.files_smp[5] = self.browse_folder()
        self.lineEdit_filename6_smp.setText(self.files_smp[5])
    # ------------ ЦВЕТ -------------------#
    def onclick_color1(self):
        color = QColorDialog.getColor()
        self.chart_properties[0].color = color.name()
        self.pushButton_color1.setStyleSheet("background-color: {}".format(self.chart_properties[0].color))
        self.plot_chart()

    def onclick_color2(self):
        color = QColorDialog.getColor()
        self.chart_properties[1].color = color.name()
        self.pushButton_color2.setStyleSheet("background-color: {}".format(self.chart_properties[1].color))
        self.plot_chart()

    def onclick_color3(self):
        color = QColorDialog.getColor()
        self.chart_properties[2].color = color.name()
        self.pushButton_color3.setStyleSheet("background-color: {}".format(self.chart_properties[2].color))
        self.plot_chart()

    def onclick_color4(self):
        color = QColorDialog.getColor()
        self.chart_properties[3].color = color.name()
        self.pushButton_color4.setStyleSheet("background-color: {}".format(self.chart_properties[3].color))
        self.plot_chart()

    def onclick_color5(self):
        color = QColorDialog.getColor()
        self.chart_properties[4].color = color.name()
        self.pushButton_color5.setStyleSheet("background-color: {}".format(self.chart_properties[4].color))
        self.plot_chart()

    def onclick_color6(self):
        color = QColorDialog.getColor()
        self.chart_properties[5].color = color.name()
        self.pushButton_color6.setStyleSheet("background-color: {}".format(self.chart_properties[5].color))
        self.plot_chart()

    # ------------ КНОПКИ РАСЧЁТА -------------------#
    def calc_Rx1_re_data(self):
        self.freq_values, zx =  self.calc_rx(1, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.real)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)
        self.title = 'Rx 1 порт real'
        self.plot_chart()

    def calc_Rx1_im_data(self):
        self.freq_values, zx =  self.calc_rx(1, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.imag)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)
        self.title = 'Rx 1 порт imag'
        self.plot_chart()

    def calc_Rx2_re_data(self):
        self.freq_values, zx =  self.calc_rx(2, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.real)
        self.y_values = values_to_plot
        self.title = 'Rx 2 порт real'
        self.plot_chart()

    def calc_Rx2_im_data(self):
        self.freq_values, zx =  self.calc_rx(2, self.files, self.impedance)
        values_to_plot = []
        for values in zx:
            values_to_plot.append(values.imag)
        self.y_values = values_to_plot
        # self.y_values.append(zx[0].real)
        # self.y_values.append(zx[0].imag)
        self.title = 'Rx 2 порт imag'
        self.plot_chart()

    def calc_VSWR1_data(self):
        self.freq_values, self.y_values =  self.calc_vswr(1, self.files)
        self.title = 'КСВН 1 порт'
        self.plot_chart()

    def calc_VSWR2_data(self):
        self.freq_values, self.y_values = self.calc_vswr(2, self.files)
        self.title = 'КСВН 2 порт'
        self.plot_chart()

    def calc_s11_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(0, self.files)
        if not self.checkBox_do_not_delete_current_plots.isChecked():
            self.title = 'S11'
        else:
            self.title += ' + S11'
        self.plot_chart()

    def calc_s12_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(2, self.files)
        self.y_values = 20 * np.log10(self.y_values)
        self.title = 'S12'
        self.plot_chart()

    def calc_s21_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(4, self.files)
        self.y_values = 20 * np.log10(self.y_values)
        self.title = 'S21'
        self.plot_chart()

    def calc_s22_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(6, self.files)
        if not self.checkBox_do_not_delete_current_plots.isChecked():
            self.title = 'S22'
        else:
            self.title += ' + S22'
        self.plot_chart()

    def calc_S11_ang_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(1, self.files)
        self.title = 'S11 фаза'
        self.plot_chart()

    def calc_S12_ang_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(3, self.files)
        self.title = 'S12 фаза'
        self.plot_chart()

    def calc_S21_ang_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(5, self.files)
        self.title = 'S21 фаза'
        self.plot_chart()

    def calc_S22_ang_data(self):
        self.y_values = []
        self.freq_values, self.y_values = self.get_data_values(7, self.files)
        self.title = 'S22 фаза'
        self.plot_chart()

    def pushButton_smp_plot_vswr_click(self):
        self.y_values_smp = []
        self.freq_values_smp, self.y_values_smp = self.get_data_values(0, self.files_smp)
        self.title = 'КСВН'
        self.plot_chart()

    def pushButton_smp_plot_phase_click(self):
        self.y_values_smp = []
        self.freq_values_smp, self.y_values_smp = self.get_data_values(1, self.files_smp)
        self.title = 'Фаза'
        self.plot_chart()




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()

    app.exec_()
    window.to_json()


if __name__ == '__main__':
    main()
