import csv
import matplotlib.pyplot as plt


name_company = {}
with open("Space_Corrected.csv", encoding='utf-8') as r_file:
    file_reader = csv.reader(r_file, delimiter=",")
    count = 0
    for row in file_reader:
        if count != 0:
            if row[2] in name_company.keys():
                name_company[row[2]] += 1
            else:
                name_company[row[2]] = 1
        count += 1


sorted_data = dict(sorted(name_company.items(), key=lambda item: item[1], reverse=True))

plt.bar(sorted_data.keys(), sorted_data.values())

for i, v in enumerate(sorted_data.values()):
  plt.text(i, v, str(v), ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=80)

plt.xlabel('Организации')
plt.ylabel('Количество запусков')

plt.tight_layout()

plt.show()