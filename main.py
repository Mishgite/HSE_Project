import csv
import matplotlib.pyplot as plt


def string_conversion(a):
    a1 = []
    a = list(a)
    for i in a:
        if i != ',':
            a1.append(i)
    return ''.join(a1)


name_company = {}
name_country = {}
country_many = {}
years_flie = {}
with open("Space_Corrected.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    for row in file_reader:
        if count != 0:
            if row[2] != '':
                if row[2] in name_company.keys():
                    name_company[row[2]] += 1
                else:
                    name_company[row[2]] = 1
            if row[9] != '':
                if row[9] in name_country.keys():
                    name_country[row[9]] += 1
                else:
                    name_country[row[9]] = 1
                if row[9] in country_many.keys():
                    if row[7] != '':
                        country_many[row[9]] += float(string_conversion(row[7]))
                        country_many[row[9]] = float('{:.2f}'.format(country_many[row[9]]))
                else:
                    if row[7] != '':
                        country_many[row[9]] = float(string_conversion(row[7]))
                        country_many[row[9]] = float('{:.2f}'.format(country_many[row[9]]))
            if row[4] != '':
                if row[4].split(',')[1].split()[0] in years_flie:
                    years_flie[row[4].split(',')[1].split()[0]] += 1
                else:
                    years_flie[row[4].split(',')[1].split()[0]] = 1

        count += 1


sorted_data = dict(sorted(name_company.items(), key=lambda item: item[1], reverse=True))
sorted_country = dict(sorted(name_country.items(), key=lambda item: item[1], reverse=True))
sorted_many = dict(sorted(country_many.items(), key=lambda item: item[1], reverse=True))

fig = plt.figure()

ax1 = fig.add_subplot(211)
ax1.bar(sorted_data.keys(), sorted_data.values())

for i, v in enumerate(sorted_data.values()):
    ax1.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=80)

plt.xlabel('Организации')
plt.ylabel('Количество запусков')


ax2 = fig.add_subplot(212)
ax2.bar(sorted_country.keys(), sorted_country.values())

for i, v in enumerate(sorted_country.values()):
    ax2.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=80)
plt.xlabel('Страны')
plt.ylabel('Количество запусков')

plt.tight_layout()

plt.show()
fig = plt.figure()
ax3 = fig.add_subplot(211)
ax3.bar(sorted_many.keys(), sorted_many.values())

for i, v in enumerate(sorted_many.values()):
    ax3.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=80)

plt.xlabel('Страны')
plt.ylabel('Стоимость всех миссии: в миллионах долларов')
plt.tight_layout()

plt.show()
fig = plt.figure()
ax4 = fig.add_subplot(111)
ax4.plot(years_flie.values(), years_flie.keys())

for i, v in enumerate(years_flie.values()):
    ax4.text(i, v, str(v), ha='center', va='bottom', fontsize=7)

plt.xticks(rotation=80)

plt.xlabel('Годы')
plt.ylabel('Количество запусков')

plt.tight_layout()

plt.show()
