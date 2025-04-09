import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class FormValidationApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Validation")
        self.resize(300, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("Rafa Maulana Rahman - F1D022153"))

        self.name_input = QLineEdit()
        layout.addWidget(QLabel("Name:"))
        layout.addWidget(self.name_input)

        self.email_input = QLineEdit()
        layout.addWidget(QLabel("Email:"))
        layout.addWidget(self.email_input)

        self.age_input = QLineEdit()
        layout.addWidget(QLabel("Age:"))
        layout.addWidget(self.age_input)

        self.phone_input = QLineEdit()
        self.phone_input.setInputMask("+62 999 9999 9999")
        layout.addWidget(QLabel("Phone Number:"))
        layout.addWidget(self.phone_input)

        self.address_input = QTextEdit()
        layout.addWidget(QLabel("Address:"))
        layout.addWidget(self.address_input)

        self.gender_cb = QComboBox()
        self.gender_cb.addItems(["", "Male", "Female", "Other"])
        layout.addWidget(QLabel("Gender:"))
        layout.addWidget(self.gender_cb)

        self.education_cb = QComboBox()
        self.education_cb.addItems(["", "Elementary School", "Junior High School", "Senior High School", 
                                    "Diploma", "Bachelor's Degree", "Master's Degree", "Doctoral Degree"])
        layout.addWidget(QLabel("Education:"))
        layout.addWidget(self.education_cb)

        button_layout = QHBoxLayout()
        self.save_btn = QPushButton("Save")
        self.save_btn.clicked.connect(self.validate_form)
        self.clear_button = QPushButton("Clear")
        self.clear_button.clicked.connect(self.clear_fields)
        button_layout.addWidget(self.save_btn)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)

        quit_shortcut = QShortcut(QKeySequence("Q"), self)
        quit_shortcut.activated.connect(self.close)

        self.setLayout(layout)

    def validate_form(self):
        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        age = self.age_input.text().strip()
        phone = self.phone_input.text().strip()
        address = self.address_input.toPlainText().strip()
        gender = self.gender_cb.currentText()
        education = self.education_cb.currentText()

        if not name:
            self.show_warning("Name is required.")
            return

        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.show_warning("Invalid email format.")
            return

        if not age.isdigit():
            self.show_warning("Age must be a number.")
            return

        if len(phone) < 17: 
            self.show_warning("Phone number must be 13 digits (format: +62 999 9999 9999).")
            return

        if not address:
            self.show_warning("Address is required.")
            return

        if gender == "-- Select Gender --":
            self.show_warning("Please select a gender.")
            return

        if education == "-- Select Education --":
            self.show_warning("Please select an education level.")
            return

        QMessageBox.information(self, "Success", "Data saved successfully!")
        self.clear_fields()

    def show_warning(self, message):
        QMessageBox.warning(self, "Validation Error", message)

    def clear_fields(self):
        self.name_input.clear()
        self.email_input.clear()
        self.age_input.clear()
        self.phone_input.clear()
        self.address_input.clear()
        self.gender_cb.setCurrentIndex(0)
        self.education_cb.setCurrentIndex(0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FormValidationApp()
    window.show()
    sys.exit(app.exec_())
