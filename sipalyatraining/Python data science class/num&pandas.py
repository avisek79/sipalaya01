import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

def generate_and_sales_data(num_records=1000):
    #generate synthetic sales data
    np.random.seed(42)
    customers_id=np.arange(1,num_records+1)
    products=np.random.choice(["A","B","C","D","E"],size=num_records)
    quantities=np.random.randint(1,10,size=num_records)
    prices=np.random.uniform(10,100,size=num_records)
    dates=pd.date_range(start="2022-01-01",end="2022-12-30",periods=num_records)

    print(customers_id)
    print(products)
    print(quantities)
    print(prices)
    print(dates)

generate_and_sales_data()