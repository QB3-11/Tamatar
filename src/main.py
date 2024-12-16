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

        self.Font = QFont("Anton", 90)

        self.setWindowTitle(title)
        self.setFixedSize(300, 200)

        layout_vert = QVBoxLayout()
        layout_hori = QHBoxLayout()
        self.layout_stak = QStackedLayout()

        self.timer = Timer()                   
        self.timer.setFont(self.Font)

        self.timer_input = Time_input(0, 10)             # Change to default value from a config file
        self.timer_input.setFont(self.Font)
        self.timer_input.minutes.setPlaceholderText("00")
        self.timer_input.seconds.setPlaceholderText("10")

        self.start_btn = QPushButton(text="Start")
        self.reset_btn = QPushButton(text="Reset")

        self.start_btn.clicked.connect(self.hide_input)
        self.reset_btn.clicked.connect(self.show_input)

        layout_hori.addWidget(self.start_btn)
        layout_hori.addWidget(self.reset_btn)
        self.layout_stak.addWidget(self.timer)
        self.layout_stak.addWidget(self.timer_input) #index = 1
        self.layout_stak.setCurrentIndex(1)

        layout_vert.addLayout(self.layout_stak)
        layout_vert.addLayout(layout_hori)

        widget = QWidget()
        widget.setLayout(layout_vert)
        self.setCentralWidget(widget)

        self.show()

    def hide_input(self):
        self.layout_stak.setCurrentIndex(0)
        self.timer.update_time(self.timer_input.return_input())
        self.timer.countdown()

    def show_input(self):
        for thread in self.timer.threads:
            thread.terminate()
        self.layout_stak.setCurrentIndex(1)
        

class Timer(QWidget):
    def __init__(self):
        super(Timer, self).__init__()

        self.t = 0
        self.threads = []

        self.layout = QHBoxLayout()
        self.layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        self.label = QLabel()
  
        self.layout.addWidget(self.label)

    def countdown(self):
        self.thread = Worker(self.t)
        self.threads.append(self.thread)
        self.thread.start()
        self.thread.progress.connect(self.update_timer)

    def update_timer(self, inp:tuple):
        self.label.setText("{:02d}:{:02d}".format(inp[0], inp[1]))
    
    def update_time(self, inp:tuple):
        self.t = inp[0] * 60 + inp[1]

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
    def __init__(self, def_min, def_sec):
        super(Time_input, self).__init__()

        self.def_min = def_min
        self.def_sec = def_sec

        widget = QWidget

        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.minutes = QLineEdit()
        self.seconds = QLineEdit()

        self.minutes.setFixedSize(130, 140)
        self.seconds.setFixedSize(130, 140)

        self.layout.addWidget(self.minutes)
        self.layout.addWidget(self.seconds)

        self.setFocus()

    def return_input(self):
        minutes = self.minutes.text()
        seconds = self.seconds.text()

        if minutes == "":
            minutes = self.def_min
        if seconds == "":
            seconds = self.def_sec
        
        return (int(minutes), int(seconds))


if __name__ == "__main__":

    app = QApplication([])
    window = Main_window("Tamatar")

    app.exec()
