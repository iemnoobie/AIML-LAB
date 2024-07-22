import pandas as pd


data = pd.read_csv(r'C:\Users\USER\Documents\ArghyaAIML_5th\Day_1\Dataset.csv')
print(data.isnull().any())

processed_data = data.dropna()
print(processed_data)

print("Mean of Max Pulse: ",data['Max_pulse'].mean())
print("Median of Max Pulse: ",data['Max_pulse'].median())
print("Mode of Max Pulse: ",data['Max_pulse'].mode())

#hist = processed_data.hist('Max_pulse')

