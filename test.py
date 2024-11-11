import pandas as pd


df = pd.read_csv("Space_Corrected.csv")
pd.set_option('display.max_rows', None)

country_counts1 = df["Location"].value_counts()
print("Количество запусков на разных космодромах:\n", country_counts1)

country_counts2 = df["Country"].value_counts()
print("\nКоличество запусков в разных странах:\n", country_counts2)

company_counts = df["Company Name"].value_counts()
print("\nКоличество запусков по компаниям:\n", company_counts)

mission_success_rate = df["Status Mission"].value_counts(normalize=True) * 100
print("\nПроцент успешности миссий:\n", mission_success_rate)

launch_success_rate = df["Status Rocket"].value_counts(normalize=True) * 100
print("\nПроцент успешности запусков:\n", launch_success_rate)

mission_success_by_country = df.groupby("Country")["Status Mission"].value_counts(normalize=True) * 100
print("\nПроцент успешности миссий в разных странах:\n", mission_success_by_country)

launch_success_by_company = df.groupby("Company Name")["Status Rocket"].value_counts(normalize=True) * 100
print("\nПроцент успешности запусков по компаниям:\n", launch_success_by_company)
