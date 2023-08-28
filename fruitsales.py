import pandas as pd

fruit_df = pd.DataFrame({'Apples': ['35', '41'], 'Bananas': ['21', '34']})
fruit_df.index = ["2017 Sales", "2018 Sales"]
fruit_df

fruit_df.to_csv('fruit.csv', index=True)