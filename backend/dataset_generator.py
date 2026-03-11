import random
import pandas as pd

sources = [
"Mumbai","Chennai","Kolkata","Delhi","Visakhapatnam","Singapore","Shanghai","Shenzhen",
"Guangzhou","Hong Kong","Tokyo","Osaka","Busan","Bangkok","Jakarta","Dubai","Doha",
"Riyadh","Jeddah","Istanbul","Hamburg","Rotterdam","Antwerp","London","Le Havre",
"Barcelona","Genoa","Athens","New York","Los Angeles","San Francisco","Seattle",
"Houston","Miami","Vancouver","Toronto","Montreal","Sydney","Melbourne","Auckland",
"Cape Town","Durban","Lagos","Nairobi","Santos","Rio de Janeiro","Buenos Aires",
"Lima","Panama City","Manila","Ho Chi Minh City","Kuala Lumpur"
]

destinations = sources

cargo_types = ["normal","fragile"]

data = []

for s in sources:
    for d in destinations:

        weather = random.randint(1,5)
        congestion = random.randint(1,5)
        distance = random.randint(1000,12000)
        cargo = random.choice(cargo_types)

        risk = weather*10 + congestion*8 + (15 if cargo=="fragile" else 5)

        data.append([s,d,weather,congestion,distance,cargo,risk])

df = pd.DataFrame(data, columns=[
"source","destination","weather","congestion","distance","cargo","risk"
])

df.to_csv("cargo_risk_dataset.csv", index=False)

print("Dataset generated successfully")