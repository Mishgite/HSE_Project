import sys
import pandas as pd
from PyQt5.QtWidgets import *


text = None
df = pd.read_csv("Space_Corrected.csv")
pd.set_option('display.max_rows', None)


class SpaceDataApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Space Data Entry')
        layout = QVBoxLayout()

        self.message = QLabel('Добро пожаловать в приложение для обработки космических данных', self)
        layout.addWidget(self.message)

        self.open_data_entry_button = QPushButton('Добавить данные', self)
        self.open_data_entry_button.clicked.connect(self.open_data_entry)
        layout.addWidget(self.open_data_entry_button)
        self.open_test_button = QPushButton('Узнать разные последовательности \n в виде таблицы', self)
        self.open_test_button.clicked.connect(self.open_test)
        layout.addWidget(self.open_test_button)

        self.setLayout(layout)

    def open_data_entry(self):
        self.data_entry_window = DataEntryWindow()
        self.data_entry_window.show()
        self.close()  # Закрываем текущее окно

    def open_test(self):

        self.data_entry_window = Data_test()
        self.data_entry_window.show()
        self.close()


class Data_test(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Space Data Entry')

        layout = QVBoxLayout()

        self.save_back = QPushButton('<- Back', self)
        self.save_back.clicked.connect(self.open_data_entry)
        layout.addWidget(self.save_back)

        self.cosmodrome_button = QPushButton('Количество запусков на разных космодромах:', self)
        self.cosmodrome_button.clicked.connect(self.open_cosmodrome)
        layout.addWidget(self.cosmodrome_button)

        self.countries_button = QPushButton('Количество запусков в разных странах:', self)
        self.countries_button.clicked.connect(self.open_countries)
        layout.addWidget(self.countries_button)

        self.kompani_button = QPushButton('Количество запусков по компаниям:', self)
        self.kompani_button.clicked.connect(self.open_kompani)
        layout.addWidget(self.kompani_button)

        self.mission_success_rate = QPushButton('Процент успешности миссий:', self)
        self.mission_success_rate.clicked.connect(self.open_mission_success)
        layout.addWidget(self.mission_success_rate)

        self.launch_success_rate = QPushButton('Процент успешности запусков:', self)
        self.launch_success_rate.clicked.connect(self.open_launch_success)
        layout.addWidget(self.launch_success_rate)

        self.mission_success_rate_country = QPushButton('Процент успешности миссий в разных странах:', self)
        self.mission_success_rate_country.clicked.connect(self.open_mission_country)
        layout.addWidget(self.mission_success_rate_country)

        self.mission_success_rate_kompani = QPushButton('Процент успешности запусков по компаниям:', self)
        self.mission_success_rate_kompani.clicked.connect(self.open_mission_kompani)
        layout.addWidget(self.mission_success_rate_kompani)

        self.setLayout(layout)

    def open_data_entry(self):
        self.data_entry_window = SpaceDataApp()
        self.data_entry_window.show()
        self.close()

    def open_cosmodrome(self):
        global text
        text = 1
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_countries(self):
        global text
        text = 2
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_kompani(self):
        global text
        text = 3
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_mission_success(self):
        global text
        text = 4
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_launch_success(self):
        global text
        text = 5
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_mission_country(self):
        global text
        text = 6
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()

    def open_mission_kompani(self):
        global text
        text = 7
        self.data_entry_window = Percent()
        self.data_entry_window.show()
        self.close()


class Percent(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Space Data Entry')

        layout = QVBoxLayout()
        self.save_back = QPushButton('<- Back', self)
        self.save_back.clicked.connect(self.open_data_entry)
        layout.addWidget(self.save_back)
        self.table = QTableWidget()
        if text == 1:
            country_counts1 = df["Location"].value_counts()
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0]
            del country_counts1[0]
            a = ''
            for j in range(len(country_counts1)):
                if not country_counts1[j].isdigit():
                    a += country_counts1[j]
                else:
                    data.append(a)
                    data.append(country_counts1[j])
                    a = ''
            self.table.setRowCount(len(data) // 2)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels([ab, 'Value',])
            i = 0
            for j in range(len(data)):
                if j % 2 == 0:
                    self.table.setItem(i, 0, QTableWidgetItem(data[j]))
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(data[j]))
                    i += 1
            layout.addWidget(self.table)
        if text == 2:
            country_counts1 = df["Country"].value_counts()
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0]
            del country_counts1[0]
            a = ''
            for j in range(len(country_counts1)):
                if not country_counts1[j].isdigit():
                    a += country_counts1[j]
                else:
                    data.append(a)
                    data.append(country_counts1[j])
                    a = ''
            self.table.setRowCount(len(data) // 2)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels([ab, 'Value',])
            i = 0
            for j in range(len(data)):
                if j % 2 == 0:
                    self.table.setItem(i, 0, QTableWidgetItem(data[j]))
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(data[j]))
                    i += 1
            layout.addWidget(self.table)

        if text == 3:
            country_counts1 = df["Company Name"].value_counts()
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0] + ' ' + country_counts1[1]
            del country_counts1[:2]
            a = ''
            for j in range(len(country_counts1)):
                if not country_counts1[j].isdigit():
                    a += country_counts1[j] + ' '
                else:
                    data.append(a)
                    data.append(country_counts1[j])
                    a = ''
            self.table.setRowCount(len(data) // 2)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels([ab, 'Value',])
            i = 0
            for j in range(len(data)):
                if j % 2 == 0:
                    self.table.setItem(i, 0, QTableWidgetItem(data[j]))
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(data[j]))
                    i += 1
            layout.addWidget(self.table)
        if text == 4:
            country_counts1 = df["Status Mission"].value_counts(normalize=True) * 100
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0] + ' ' + country_counts1[1]
            del country_counts1[:2]
            a = ''
            for j in range(len(country_counts1)):
                if '.' not in country_counts1[j]:
                    a += country_counts1[j] + ' '
                else:
                    data.append(a)
                    data.append(country_counts1[j])
                    a = ''
            self.table.setRowCount(len(data) // 2)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels([ab, 'Value',])
            i = 0
            for j in range(len(data)):
                if j % 2 == 0:
                    self.table.setItem(i, 0, QTableWidgetItem(data[j]))
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(data[j]))
                    i += 1
            layout.addWidget(self.table)
        if text == 5:
            country_counts1 = df["Status Rocket"].value_counts(normalize=True) * 100
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0] + ' ' + country_counts1[1]
            del country_counts1[:2]
            a = ''
            for j in range(len(country_counts1)):
                if '.' not in country_counts1[j]:
                    a += country_counts1[j] + ' '
                else:
                    data.append(a)
                    data.append(country_counts1[j])
                    a = ''
            self.table.setRowCount(len(data) // 2)
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels([ab, 'Value',])
            i = 0
            for j in range(len(data)):
                if j % 2 == 0:
                    self.table.setItem(i, 0, QTableWidgetItem(data[j]))
                else:
                    self.table.setItem(i, 1, QTableWidgetItem(data[j]))
                    i += 1
            layout.addWidget(self.table)
        if text == 6:
            country_counts1 = df.groupby("Country")["Status Mission"].value_counts(normalize=True) * 100
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0] + ' ' + country_counts1[1]
            del country_counts1[:3]
            a = ''
            b = ''
            for j in range(len(country_counts1)):
                if ('.' not in country_counts1[j] and country_counts1[j] != 'Failure' and country_counts1[j] != 'Success'
                        and country_counts1[j] != 'Prelaunch'):
                    a += country_counts1[j] + ' '
                elif country_counts1[j] == 'Failure' or country_counts1[j] == 'Success' or country_counts1[j] == 'Prelaunch':
                    b += country_counts1[j] + ' '
                else:
                    data.append([a, b, country_counts1[j]])
                    a = ''
                    b = ''
            self.table.setRowCount(len(data))
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels([ab, 'Status Mission', '%'])
            for i in range(len(data)):
                for j in range(3):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))
            layout.addWidget(self.table)
        if text == 7:
            country_counts1 = df.groupby("Company Name")["Status Rocket"].value_counts(normalize=True) * 100
            country_counts1 = str(country_counts1).split()
            data = []
            ab = country_counts1[0] + ' ' + country_counts1[1]
            del country_counts1[:3]
            a = ''
            b = ''
            for j in range(len(country_counts1)):
                if ('.' not in country_counts1[j] and country_counts1[j] != 'StatusRetired' and
                        country_counts1[j] != 'StatusActive'):
                    a += country_counts1[j] + ' '
                elif country_counts1[j] == 'StatusRetired' or country_counts1[j] == 'StatusActive':
                    b += country_counts1[j] + ' '
                else:
                    data.append([a, b, country_counts1[j]])
                    a = ''
                    b = ''
            self.table.setRowCount(len(data))
            self.table.setColumnCount(3)
            self.table.setHorizontalHeaderLabels([ab, 'Status Mission', '%'])
            for i in range(len(data)):
                for j in range(3):
                    self.table.setItem(i, j, QTableWidgetItem(data[i][j]))
            layout.addWidget(self.table)
        self.setLayout(layout)

    def open_data_entry(self):
        self.data_entry_window = Data_test()
        self.data_entry_window.show()
        self.close()


class DataEntryWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Space Data Entry')

        layout = QVBoxLayout()

        self.save_back = QPushButton('<- Back', self)
        self.save_back.clicked.connect(self.open_data_entry)
        layout.addWidget(self.save_back)

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

    def open_data_entry(self):
        self.data_entry_window = SpaceDataApp()
        self.data_entry_window.show()
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SpaceDataApp()
    ex.show()
    sys.exit(app.exec_())
