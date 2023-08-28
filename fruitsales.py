import pandas as pd

fruits = pd.DataFrame(columns = ["Apples", "Banana"])
fruits.loc[0] = [30,21]

fruit_sales = pd.DataFrame(columns = ["Apples", "Bananas"],
             index = ["2017 Sales", "2018 Sales"],
             data = [[35,21],[41,34]]
             )
fruit_sales

fruit_sales.to_csv('fruit.csv', index=True)