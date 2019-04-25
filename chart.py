import os
import sys
import collections

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

class Chart(QtWidgets.QDialog, form.Ui_Dialog):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.openButton.clicked.connect(self.plot_to_word)

    def plot_to_word(self):

        # create an exporter instance, as an argument give it
        # the item you wish to export
        exporter = PGQ_image_exporter.PQG_ImageExporter(self.widget.plotItem)

        # set export parameters if needed
        exporter.parameters()['width'] = 600

        # save to file
        exporter.export('fileName.png')



        document = Document('test.docx')
        document.add_paragraph(
            'Lorem ipsum dolor sit amet. {}'.format(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
        document.add_picture('fileName.png')
        document.add_page_break()
        document.save('test.docx')
        Chart.display_ok_message('Word saved!')

    @classmethod
    def display_ok_message(cls, message):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText(message)
        msg.setInformativeText("It's ok!")
        msg.setWindowTitle("MessageBox title")
        # msg.setDetailedText("The details are as follows:")
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

    def plot_chart(self, chart):
        self.widget = chart
        # chart.plotItem.items[0]
        # self.horizontalLayout.widget = chart
        if self.horizontalLayout.count() > 0:
            self.horizontalLayout.takeAt(0)
        self.horizontalLayout.addWidget(chart)