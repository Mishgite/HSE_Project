import sys
import pandas as pd
from PyQt5.QtWidgets import *


class SpaceDataApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Space Data Entry')

        # Создаем вертикальный layout
        layout = QVBoxLayout()

        # Поля ввода
        self.company_name_input = QLineEdit(self)
        self.company_name_input.setPlaceholderText('Company Name')
        layout.addWidget(self.company_name_input)

        self.location_input = QLineEdit(self)
        self.location_input.setPlaceholderText('Location')
        layout.addWidget(self.location_input)

        self.datum_input = QLineEdit(self)
        self.datum_input.setPlaceholderText('Datum')
        layout.addWidget(self.datum_input)

        self.detail_input = QLineEdit(self)
        self.detail_input.setPlaceholderText('Detail')
        layout.addWidget(self.detail_input)

        self.country_input = QLineEdit(self)
        self.country_input.setPlaceholderText('Country')
        layout.addWidget(self.country_input)

        self.rocket_input = QLineEdit(self)
        self.rocket_input.setPlaceholderText('Rocket')
        layout.addWidget(self.rocket_input)

        self.rocket_status_label = QLabel('Status Rocket:')
        self.rocket_status_combo = QComboBox(self)
        self.rocket_status_combo.addItems(['Status Active', 'Status Retired'])
        layout.addWidget(self.rocket_status_label)
        layout.addWidget(self.rocket_status_combo)

        # ComboBox для статуса миссии
        self.mission_status_label = QLabel('Status Mission:')
        self.mission_status_combo = QComboBox(self)
        self.mission_status_combo.addItems(['Success', 'Failure', 'Prelaunch Failure'])
        layout.addWidget(self.mission_status_label)
        layout.addWidget(self.mission_status_combo)

        self.save_button = QPushButton('Save', self)
        self.save_button.clicked.connect(self.save_to_csv)
        layout.addWidget(self.save_button)

        self.message = QLabel('', self)
        layout.addWidget(self.message)

        self.setLayout(layout)

    def save_to_csv(self):
        data = {
            'Unnamed: 0': None,
            'Company Name': self.company_name_input.text(),
            'Location': self.location_input.text(),
            'Datum': self.datum_input.text(),
            'Detail': self.detail_input.text(),
            'Status Rocket': self.get_rocket_status(),
            'Rocket': self.rocket_input.text(),
            'Status Mission': self.get_mission_status(),
            'Country': self.country_input.text()
        }

        df = pd.DataFrame([data])

        try:
            df.to_csv('Space_Corrected.csv', mode='a', header=not pd.io.common.file_exists('Space_Corrected.csv'))
            self.message.setText('Data saved successfully!')
        except Exception as e:
            self.message.setText(f'Error saving data: {str(e)}')

    def get_rocket_status(self):
        return self.rocket_status_combo.currentText()

    def get_mission_status(self):
        return self.mission_status_combo.currentText()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpaceDataApp()
    ex.show()
    sys.exit(app.exec_())
