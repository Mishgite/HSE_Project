import csv
import matplotlib.pyplot as plt


name_company = {}
name_country = {}
with open("Space_Corrected.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    for row in file_reader:
        if count != 0:
            if row[2] in name_company.keys():
                name_company[row[2]] += 1
            else:
                name_company[row[2]] = 1
            if row[9] in name_country.keys():
                name_country[row[9]] += 1
            else:
                name_country[row[9]] = 1
        count += 1


sorted_data = dict(sorted(name_company.items(), key=lambda item: item[1], reverse=True))
sorted_country = dict(sorted(name_country.items(), key=lambda item: item[1], reverse=True))


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
