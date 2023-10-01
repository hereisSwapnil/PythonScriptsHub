import sys
import math
import re 
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, \
                               QPushButton, QLineEdit, QGridLayout, QSizePolicy, \
                               QMenuBar, QMenu, QMessageBox
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtGui import QAction


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.init_ui()
        self.answer_given = False

    def init_ui(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        menu_bar = self.create_menu()
        layout.setMenuBar(menu_bar)

        self.result_display = QLineEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setAlignment(Qt.AlignRight)
        self.result_display.setFixedHeight(50)

        display_font = QFont("Calculator", 24)
        self.result_display.setFont(display_font)

        layout.addWidget(self.result_display)

        button_layout = QGridLayout()
        button_layout.setSpacing(5)

        button_font = QFont("Arial", 14, QFont.Bold)
        button_style = '''
            QPushButton {
                background-color: #424242;
                color: white;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #616161;
            }
            QPushButton:pressed {
                background-color: #757575;
            }
        '''

        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('0', 3, 0), ('.', 3, 1), ('+', 3, 2), ('=', 3, 3),
            ('√', 4, 0), ('^', 4, 1),
            ('C', 4, 2), ('CE', 4, 3)
        ]

        for button_text, row, col in buttons:
            button = QPushButton(button_text)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(self.on_button_clicked)
            button.setFont(button_font)
            button.setStyleSheet(button_style)
            button_layout.addWidget(button, row, col)

        layout.addLayout(button_layout)
        central_widget.setLayout(layout)

    def create_menu(self):
        menu_bar = QMenuBar(self)

        file_menu = QMenu("File", self)
        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        menu_bar.addMenu(file_menu)

        help_menu = QMenu("Help", self)
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        menu_bar.addMenu(help_menu)

        return menu_bar

    def show_about_dialog(self):
        QMessageBox.about(self, "About Calculator", "A simple calculator built with PySide6.")

    def on_button_clicked(self):
        sender = self.sender()
        button_text = sender.text()

        if button_text == "=":
            try:
                result = eval(re.sub(r'√(\d+)', r'math.sqrt(\1)', str(self.result_display.text())))
                if result == int(result):
                    result = int(result)
                self.result_display.setText(str(result))
                self.answer_given = True
            except Exception as e:
                QMessageBox.warning(sender, "Warning", str(e))
                self.result_display.setText("")
        elif button_text in {'+', '-', '*', '/', '**', '√'}:
            if self.answer_given:
                self.answer_given = False
            self.result_display.setText(self.result_display.text() + button_text)
        elif button_text.isdigit() or button_text == ".":
            if not self.answer_given:
                self.result_display.setText(self.result_display.text() + button_text)
        elif button_text == "^":
            self.result_display.setText(self.result_display.text() + "**")
        elif button_text == "C":
            self.result_display.setText("")
            self.answer_given = False
        elif button_text == "CE":
            current_text = self.result_display.text()
            self.result_display.setText(current_text[:-1])
            if self.answer_given:
                self.answer_given = False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec())