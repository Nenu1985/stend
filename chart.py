import os
import sys
import collections
from docx.opc.exceptions import PackageNotFoundError
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMessageBox
import pyqtgraph as pg
import PGQ_image_exporter # modified pyqtgraph Exporter!
import numpy as np
import ui
import form
from cmath import rect
from docx import Document
import datetime
import cv2
from PyQt5.QtGui import QFont


class CustomViewBox(pg.ViewBox):
    def __init__(self, parent_chart_dialog, *args, **kwds):
        pg.ViewBox.__init__(self, *args, **kwds)
        self.setMouseMode(self.RectMode)
        self.chart = parent_chart_dialog
    ## reimplement right-click to zoom out
    def mouseClickEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            self.autoRange()
            self.chart.spinBox_x_max_valueChanged()
            self.chart.doubleSpinBox_y_max_valueChanged()


    def mouseDragEvent(self, ev):
        if ev.button() == QtCore.Qt.RightButton:
            ev.ignore()
        else:
            pg.ViewBox.mouseDragEvent(self, ev)

    def wheelEvent(self, ev, axis=None):
        ev.ignore()



class Chart(QtWidgets.QDialog, form.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chart = pg.PlotItem()
        self.view = pg.GraphicsView()
        self.files_names = []

        # self.plot_chart_init()

        self.openButton.clicked.connect(self.plot_to_word)

        self.spinBox_x_max.valueChanged.connect(self.spinBox_x_max_valueChanged)
        self.spinBox_x_min.valueChanged.connect(self.spinBox_x_max_valueChanged)
        self.doubleSpinBox_y_max.valueChanged.connect(self.doubleSpinBox_y_max_valueChanged)
        self.doubleSpinBox_y_min.valueChanged.connect(self.doubleSpinBox_y_max_valueChanged)

    def plot_chart_init(self):
        vb = CustomViewBox(self)
        layout = pg.GraphicsLayout()
        layout.layout.setSpacing(150.)
        layout.setContentsMargins(0., 0., 0., 0.)
        # layout.addViewBox(0,0)
        self.view = pg.GraphicsView(background=pg.mkColor('w'))
        self.view.setCentralItem(layout)

        self.chart = layout.addPlot(0, 0, enableMenu=False, viewBox=vb)
        # legend = layout.addLabel('_________________',0,1)

        bottom_axes = self.chart.getAxis('bottom')
        left_axes = self.chart.getAxis('left')
        right_axes = self.chart.getAxis('right')
        top_axes = self.chart.getAxis('top')

        layout.addItem(self.chart.addLegend(size=(200, 100), offset=(1380, 10)), 0, 1)

        left_axes.setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        left_axes.setLabel('----->')

        self.chart.getAxis('left').setGrid(150)
        bottom_axes.setPen(pg.mkPen('k', width=2, style=QtCore.Qt.SolidLine))
        bottom_axes.setGrid(150)
        bottom_axes.setLabel('Частота', units='МГц')

        top_axes.show()
        top_axes.setPen(pg.mkPen('k', width=2))
        top_axes.setTicks([])

        right_axes.setLabel('   ', color='#fff')
        right_axes.setPen(pg.mkPen('k', width=2))
        right_axes.setTicks([])
        right_axes.show()
        # chart_pw.showAxis('right')
        # results_graph(PlotWidget).setLabels(left="Frequency", bottom="Scores")
        bottom_axes.labelStyle = {'font-size': '20pt', 'color': '#000'}

        tick_font = QFont()
        tick_font.setPixelSize(20)
        axis_style = {
            'tickFont': tick_font,
            'tickLength': 10,
            'tickTextOffset': 15,
            'tickTextHeight': 20,
            'tickTextWidth': 20,
            # 'stopAxisAtTick': (False, False),
        }

        bottom_axes.setTickFont(tick_font)
        left_axes.setTickFont(tick_font)

        bottom_axes.setStyle(**axis_style)
        left_axes.setStyle(**axis_style)

        # chart_pw.setBorder('k', width=2)

        self.chart.plot(border=pg.mkPen('k', width=2))
        while self.horizontalLayout.count() > 0:
            self.horizontalLayout.takeAt(0)
        self.horizontalLayout.addWidget(self.view)
        # --self.chart.setTitle(self.title, **{'color': '#000', 'size': '14pt'})

    def delete_plot_items(self):
        self.plot_chart_init()

    def plot_to_word(self):
        FILE_EXIST_FILE = False
        # create an exporter instance, as an argument give it
        # the item you wish to export
        exporter = PGQ_image_exporter.PQG_ImageExporter(self.chart)

        # set export parameters if needed
        # exporter.parameters()['width'] = 600

        # save to file
        exporter.export('fileName.jpg')

        word_file_name = self.lineEdit_word_file_path.text()
        try:
            document = Document(word_file_name)
            FILE_EXIST_FILE = True
        except PackageNotFoundError as e:
            try:
                document = Document()
            except Exception as e:
                print('Error while creating word template: {}'.format(e))
        except Exception as e:
            print('Error while saving to word {}'.format(e))
            return

        document.add_paragraph(
            'График добавлен. {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        document.add_picture('fileName.jpg')

        for file_name in self.files_names:
            document.add_paragraph(file_name)
        document.add_page_break()


        # document.save(word_file_name)
        try:
            document.save(word_file_name)
        except PackageNotFoundError as e:
            print('Package not found exception while saving to word')
            return
        except Exception as e:
            print('Error while saving to word {}'.format(e))
            return

        Chart.display_ok_message('Word saved!')

    @classmethod
    def display_ok_message(cls, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(message)
        msg.setInformativeText("График добавлен в Word!")
        msg.setWindowTitle("")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def plot_chart(self):
        # self.chart = chart_pi
        # self.view = view

        # while self.horizontalLayout.count() > 0:
        #     self.horizontalLayout.takeAt(0)
        # self.horizontalLayout.addWidget(view)

        # graph = next((x for x in self.widget.items() if x is pg.PlotItem), None)

        x_range = [int(i) for i in self.chart.viewRange()[0]]
        y_range = self.chart.viewRange()[1]
        #
        # self.grid_range_settings_x(x_range)
        # self.grid_range_settings_y(y_range)
        #
        self.spinBox_x_min.setValue(x_range[0])
        self.spinBox_x_max.setValue(x_range[1])
        self.doubleSpinBox_y_min.setValue(y_range[0])
        self.doubleSpinBox_y_max.setValue(y_range[1])
        self.spinBox_x_max_valueChanged()
        self.doubleSpinBox_y_max_valueChanged()

    def grid_range_settings_x(self, values_range):
        start = values_range[0]
        end = values_range[1]
        dx = int((end-start)/8)
        delta = [(value, str(value)) for value in list(range(start, end-dx, dx))]
        delta.append((end, str(end)))
        ax = self.chart.getAxis('bottom')
        ax.setTicks([delta, []])

    def grid_range_settings_y(self, values_range):
        start = values_range[0]
        end = values_range[1]
        dy = (end-start)/6
        delta = [(value, '{0:.2g}'.format(value)) for value in list(drange(start, end, dy))]
        delta.append((end, '{0:.2g}'.format(end)))
        ay = self.chart.getAxis('left')
        ay.setTicks([delta, []])

    def spinBox_x_max_valueChanged(self):
        self.grid_range_settings_x(
            [self.spinBox_x_min.value(), self.spinBox_x_max.value()],
        )
        self.chart.setRange(
            xRange=[self.spinBox_x_min.value(), self.spinBox_x_max.value()],
            padding=0,
        )
    def doubleSpinBox_y_max_valueChanged(self):
        self.grid_range_settings_y(
            [self.doubleSpinBox_y_min.value(), self.doubleSpinBox_y_max.value()],
        )
        self.chart.setRange(
            yRange=[self.doubleSpinBox_y_min.value(), self.doubleSpinBox_y_max.value()],
            padding=0,
        )

def drange(start, stop, step):
        r = start
        while r < stop:
            yield r
            r += step
