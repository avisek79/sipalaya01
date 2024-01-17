import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def data_learning_program():
    #generate synthetic data
    np.random.seed(42)
    data={
        "Feature_A":np.random.rand(100), #generate integers from 0 to 1 exclusively 
        "Feature_B":np.random.randint(0,2,size=100), #generate integers from o(inclusively to 2(exclusively) i.e. [0,2))
        "Target":3*np.random.rand(100)+2 #generate a random inetgers inclusively from [0,1)
    }

    #create a pandas data frame
    df=pd.DataFrame(data)
    # print(df.to_csv())

    #Dispalys the first few rows of the dataframe

    print("Dataframe Preview:")
    print(df.head())

    #Basic Statistics using pandas
    summary_stats=df.describe()
    print("\nsummary_statistics :")
    print(summary_stats)

    #select and filter datas
    selected_data=df[["Feature_A","Target"]]
    filtered_data=df[df["Feature_B"]==1 ]

    #print the selected and filtered datas

    print("selected datas:")
    print(selected_data)
    print("filtered_data : ",filtered_data)

    #group by feature B and calculate the mean for each group
    grouped_data=df.groupby("Feature_B").mean()
    print(f"grouped data (mean for each group of Feature_B): {grouped_data}")

    #Add a new column "Feature_C" with random values
    df["feature_C"]=np.random.randn(100)
    print("\n Dataframe with new_feature_c :")
    print(df.head())



data_learning_program()

# # import numpy as np

# # print(np.random.rand(5))
# # print(np.random.randn(5))

#numpy shape and reshape functions

# import numpy as np
# original_aray=np.arange(16)
# reshaped_array=original_aray.reshape(8,2)
# print(reshaped_array)

# re_reshaped_aaray=reshaped_array.shape
# print("the shape array again is :",re_reshaped_aaray)




