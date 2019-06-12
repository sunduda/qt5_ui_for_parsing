from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QComboBox


class MessageParsingMainWindow:
    def __init__(self):
        self.app = QApplication([])
        self.window = QWidget()
        self.layout = QGridLayout()

        # Define tags and value of ComboBoxes
        time_labels = ("Year", "Month", "Day", "Hour", "Min.", "Sec.")
        # Add widgets to the grid layout
        self.layout.addWidget(QLabel("Start date and time:"), 1, 0)
        self.layout.addWidget(QLabel("End date and time:"), 2, 0)
        [self.layout.addWidget(QLabel(time_labels[i]), 0, i + 1) for i in range(len(time_labels))]
        time_comboboxes = [QComboBox() for _ in range(2 * len(time_labels))]
        # Start time selection
        time_comboboxes[0].addItems([str(year) for year in range(2014, 2020)])
        time_comboboxes[1].addItems([str(month) for month in range(1, 13)])
        time_comboboxes[2].addItems([str(day) for day in range(1, 32)])
        time_comboboxes[3].addItems([str(hour) for hour in range(0, 24)])
        time_comboboxes[4].addItems([str(minute) for minute in range(0, 60)])
        time_comboboxes[5].addItems([str(second) for second in range(0, 60)])
        # End time selection
        time_comboboxes[6].addItems([str(year) for year in range(2014, 2020)])
        time_comboboxes[7].addItems([str(month) for month in range(1, 13)])
        time_comboboxes[8].addItems([str(day) for day in range(1, 32)])
        time_comboboxes[9].addItems([str(hour) for hour in range(0, 24)])
        time_comboboxes[10].addItems([str(minute) for minute in range(0, 60)])
        time_comboboxes[11].addItems([str(second) for second in range(0, 60)])

        # Connect SIGNAL with matching SLOT
        time_comboboxes[0].currentTextChanged.connect(lambda: self.on_year_month_change(time_comboboxes[0],
                                                                                        time_comboboxes[1],
                                                                                        time_comboboxes[2]))
        time_comboboxes[1].currentTextChanged.connect(lambda: self.on_year_month_change(time_comboboxes[0],
                                                                                        time_comboboxes[1],
                                                                                        time_comboboxes[2]))

        [self.layout.addWidget(time_comboboxes[i], int(i / 6) + 1, i % 6 + 1) for i in range(len(time_comboboxes))]

        self.window.setLayout(self.layout)

    def show(self):
        self.window.show()

    def exec(self):
        self.app.exec()

    @staticmethod
    @QtCore.pyqtSlot(QComboBox, QComboBox, QComboBox)
    def on_year_month_change(y, m, d):
        if m.currentText() in ('1', '3', '5', '7', '8', "10", "12"):
            [d.model().item(i).setEnabled(True) for i in range(28, 31)]
        elif m.currentText() in ('4', '6', '9', '11'):
            [d.model().item(i).setEnabled(True) for i in range(28, 30)]
            d.model().item(30).setEnabled(False)
        elif int(y.currentText()) % 4 == 0:
            [d.model().item(i).setEnabled(False) for i in range(29, 31)]
            d.model().item(28).setEnabled(True)
        else:
            [d.model().item(i).setEnabled(False) for i in range(28, 31)]
