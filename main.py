import sys
from PyQt6.QtCore import QSize, Qt, pyqtSlot
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication,
    QLineEdit,
    QLabel,
    QMainWindow,
    QWidget,
    QPushButton,
    QGridLayout
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 320, 500)
        self.setWindowIcon(QIcon('icon\icon.png'))
        backspace_button = QPushButton('<-')
        plus_button = (QPushButton('+'))
        minus_button = QPushButton('-')
        multiply_button = QPushButton('x')
        equal_button = QPushButton('=')
        divide_button = QPushButton(':')
        percent_button = QPushButton('%')
        empty1_button = QPushButton('')
        n7_button = QPushButton('7')
        n4_button = QPushButton('4')
        n1_button = QPushButton('1')
        empty2_button = QPushButton('')
        CE_button = QPushButton('CE')
        empty3_button = QPushButton('')
        n8_button = QPushButton('8')
        n2_button = QPushButton('2')
        n5_button = QPushButton('5')
        n0_button = QPushButton('0')
        C_button = QPushButton('C')
        empty4_button = QPushButton('')
        n9_button = QPushButton('9')
        n6_button = QPushButton('6')
        n3_button = QPushButton('3')
        dot_button = QPushButton('.')

        buttons = [
            backspace_button, plus_button, minus_button, multiply_button, equal_button, divide_button,
            percent_button, empty1_button, n7_button, n4_button, n1_button, empty2_button,
            CE_button, empty3_button, n8_button, n5_button, n2_button, n0_button , C_button , empty4_button,
            n9_button , n6_button , n3_button , dot_button
        ]
        
        for btn in buttons:
            btn.setFixedSize(75, 50)

        display = QLineEdit(parent=self)
        display.setFixedHeight(50)
        central_widget = QWidget()
        layout = QGridLayout()
        
        configs = [
            (percent_button,   2, 0, Qt.AlignmentFlag.AlignCenter),
            (empty1_button,    3, 0, Qt.AlignmentFlag.AlignCenter),
            (n7_button,        4, 0, Qt.AlignmentFlag.AlignCenter),
            (n4_button,        5, 0, Qt.AlignmentFlag.AlignCenter),
            (n1_button,        6, 0, Qt.AlignmentFlag.AlignCenter),
            (empty2_button,    7, 0, Qt.AlignmentFlag.AlignCenter),

            (CE_button,        2, 1, Qt.AlignmentFlag.AlignCenter),
            (empty3_button,    3, 1, Qt.AlignmentFlag.AlignCenter),
            (n8_button,        4, 1, Qt.AlignmentFlag.AlignCenter),
            (n5_button,        5, 1, Qt.AlignmentFlag.AlignCenter),
            (n2_button,        6, 1, Qt.AlignmentFlag.AlignCenter),
            (n0_button,        7, 1, Qt.AlignmentFlag.AlignCenter),

            (C_button,     2, 2, Qt.AlignmentFlag.AlignCenter),
            (empty4_button,    3, 2, Qt.AlignmentFlag.AlignCenter),
            (n9_button,        4, 2, Qt.AlignmentFlag.AlignCenter),
            (n6_button,        5, 2, Qt.AlignmentFlag.AlignCenter),
            (n3_button,        6, 2, Qt.AlignmentFlag.AlignCenter),
            (dot_button,       7, 2, Qt.AlignmentFlag.AlignCenter),

            (backspace_button, 2, 3, Qt.AlignmentFlag.AlignCenter),
            (divide_button,    3, 3, Qt.AlignmentFlag.AlignCenter),
            (multiply_button,  4, 3, Qt.AlignmentFlag.AlignCenter),
            (minus_button,     5, 3, Qt.AlignmentFlag.AlignCenter),
            (plus_button,      6, 3, Qt.AlignmentFlag.AlignCenter),
            (equal_button,     7, 3, Qt.AlignmentFlag.AlignCenter)
        ]

        layout.addWidget(display, 0, 0, 1, 3)
   
        for btn, row, col, align in configs:
            layout.addWidget(btn, row, col, alignment=align)

        central_widget.setStyleSheet("QPushButton { font-size: 20px; font-weight: bold; }")
        self.setLayout(layout)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())    
