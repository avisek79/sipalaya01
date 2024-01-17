import numpy as np 
import pandas as pd 
from matplotlib import pyplot as plt

def generate_and_visualize_data(num_points=100):
    #Generate synthetic data
    np.random.seed(42)
    x=np.linspace(0,10,num_points)
    y=2*x+1+np.random.normal(scale=2,size=num_points)
    
    #create a pandas dataframe
    data={"X":x,"Y":y}

    df=pd.DataFrame(data)

    #perform data manipulations

    df["Y_predicted"]=2*df["X"]+1
    df["Residuals"]=df["Y"]-df["Y-Predicted"]

    #visualize the data
    plt.figure(figsize=(10,6))

    #sCATTER PLOT OF THE data points
    plt.scatter(df["X"],df["Y"],label= "Actual Data",Color="blue")

    #Plot the trend line
    plt.plot(df["X"],df["Y_predicted"],label="trend line" , Color ="red")

generate_and_visualize_data()