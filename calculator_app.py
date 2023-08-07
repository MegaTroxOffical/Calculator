import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QFont

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Calculator')
        self.setGeometry(100, 100, 300, 400)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout()

        self.entry = QLineEdit(self)
        self.layout.addWidget(self.entry)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        grid = QHBoxLayout()
        row = []
        for text in buttons:
            button = QPushButton(text)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            row.append(button)
            if text == '=':
                button.setObjectName('equal_button')
            grid.addWidget(button)
            if len(row) == 4:
                self.layout.addLayout(grid)
                row = []
                grid = QHBoxLayout()

        self.central_widget.setLayout(self.layout)

        # Apply font and button styles
        font = QFont('Product Sans Regular', 16)
        self.setFont(font)

        for button in self.findChildren(QPushButton):
            button.setFont(font)
            button.setStyleSheet("""
                QPushButton {
                    width: 40px;
                    height: 40px;
                    background-color: rgb(211, 211, 211);  /* Light gray */
                    border-radius: 50%;
                }

                QPushButton#equal_button {
                    background-color: rgb(30, 144, 255);  /* Dodger blue */
                    color: white;
                }
            """)
            button.clicked.connect(self.on_button_click)  # Corrected method name

    def on_button_click(self):  # Corrected method name
        sender = self.sender()
        text = sender.text()
        current_text = self.entry.text()

        if text == '=':
            try:
                result = str(eval(current_text))
            except:
                result = "Error"
            self.entry.setText(result)
        else:
            self.entry.insert(text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    calc_app = CalculatorApp()
    calc_app.show()
    sys.exit(app.exec_())
