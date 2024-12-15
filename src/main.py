import time

from PyQt5.QtWidgets import (
    QStackedLayout,
    QApplication,
    QSizePolicy,
    QMainWindow,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QWidget,
    QLabel
)
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QFont

class Main_window(QMainWindow):
    def __init__(self, title:str):
        super(Main_window, self).__init__()

        self.setWindowTitle(title)
        self.setFixedSize(300, 200)
        layout_vert = QVBoxLayout()
        layout_hori = QHBoxLayout()
        self.layout_stak = QStackedLayout()

        self.timer = Timer(10, 0)
        self.timer_input = Time_input()

        start_btn = QPushButton(text="Start")
        reset_btn = QPushButton(text="Reset")

        start_btn.clicked.connect(self.hide_input)
        reset_btn.clicked.connect(self.show_input)

        layout_hori.addWidget(start_btn)
        layout_hori.addWidget(reset_btn)
        self.layout_stak.addWidget(self.timer)
        self.layout_stak.addWidget(self.timer_input) #index = 1


        layout_vert.addLayout(self.layout_stak)
        layout_vert.addLayout(layout_hori)

        widget = QWidget()
        widget.setLayout(layout_vert)
        self.setCentralWidget(widget)

        self.show()

    def hide_input(self):
        self.layout_stak.setCurrentIndex(0)
        self.timer.countdown()

    def show_input(self):

        self.layout_stak.setCurrentIndex(1)

class Timer(QWidget):
    def __init__(self, seconds=0, minutes=0):
        super(Timer, self).__init__()

        self.t = seconds + minutes * 60

        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.label = QLabel("{:02d}:{:02d}".format(minutes, seconds))
        self.label.setFont(QFont("Arial", 80))
        self.layout.addWidget(self.label)

    def countdown(self):
        self.thread = Worker(self.t)
        self.thread.start()
        self.thread.progress.connect(self.update_timer)

    def update_timer(self, inp):
        self.label.setText("{:02d}:{:02d}".format(inp[0], inp[1]))

class Worker(QThread):

    def __init__(self, t):
        super(Worker, self).__init__()
        self.t = t
    
    progress = pyqtSignal(tuple)
    def run(self):
        while self.t > -1:
            mins, secs = divmod(self.t, 60)
            self.progress.emit((mins, secs))
            time.sleep(1)

            self.t -= 1

class Time_input(QWidget):
    def __init__(self):

        self.def_sec, self.def_min = 0, 15      # Needs to be taken from a config file
        super(Time_input, self).__init__()

        widget = QWidget

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.minutes = QLineEdit()
        self.minutes.setPlaceholderText = str(self.def_min)
        self.seconds = QLineEdit()
        self.seconds.setPlaceholderText = str(self.def_sec)

        self.layout.addWidget(self.minutes)
        self.layout.addWidget(self.seconds)

    def return_input(self):
        return m

if __name__ == "__main__":

    app = QApplication([])
    window = Main_window("Tamatar")

    app.exec()
