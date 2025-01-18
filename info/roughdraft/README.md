# Rough Draft
This is a rough draft only. Please refer to [home page](/README.md) for actual material.

# Timeline
Time Length: 1 Quarter
| **Week(s)** | **Group** | **Tasks**                                                                                  |
|-------------|-----------|--------------------------------------------------------------------------------------------|
| Jan 12-18   | *         | Complete [Sections 1-4](/info/README.md)                                                   |
| Jan 19-25   | A         | Complete [Sections 5-6](/info/README.md), do EDA, store and document cleaned data          |
| Jan 19-25   | B         | Complete [Sections 5 and 7](/info/README.md), create models                                |
| Jan 26-Feb 1| A         | Complete [Section 7](/info/README.md)                                                      |
| Jan 26-Feb 1| *         | Make data compatible with the model                                                        |
| Feb 2-15    | *         | Train models, perform hyperparameter tuning, and select the most accurate models           |
| Feb 16-Mar 8| *         | Buffer weeks / (Optional) [Section 8](/info/README.md)                                     |

# 5 - Storing Data
* [Numpy Crash Course](EDA/)
* [Pandas Cheat Sheet](EDA/Pandas_Cheat_Sheet.pdf)
* [Pandas Crash Course](https://www.youtube.com/watch?v=tRKeLrwfUgU&ab_channel=NicholasRenotte)
    * Just understand how a DataFrame works
    * No need to memorize everything!

# 6 - EDA and Data Cleaning
* Objective: Figure out how our data looks and what features are relavent to our response variable
    * Definitions: features = inputs, response = output
* For this project:
    * We will store [data](/dataset/README.md) in data frames
    * Using pairplots and heatmaps for feature relavence will be important
    * We may collectively add other EDA methods if it helps with understanding our data or what models to use
    * I recommend use Microsoft Excel for basic data cleaning and Pandas for advanced data manipulation and analysis
* [Relavent Project](https://www.kaggle.com/code/yasserh/walmart-sales-prediction-best-ml-algorithms)
    * We will NOT be copying this, this is only to understand how the data should look
* Optional: [EDA Crash Course](https://youtu.be/wPcR9Kmv91g?si=sF7eD7pmOnVdwJen)
    * Some parts may be useful, others are not for this project

# 7 - Machine Learning
* Objective: Predict Sales in future years
* For this project:
    * We will need to split the data into past years (training data) and future years (test data)
    * We plan to implement ARIMA + Neural Network Hybrid Model
* [Relavent Project](https://www.kaggle.com/code/yasserh/walmart-sales-prediction-best-ml-algorithms)
    * We will NOT be copying this, this is only to understand the ballpark of how accurate our models should be
* [Resources](model/README.md)

# 8 - (Optional) Special Topics
* If time allows, we can do extra, such as:
    * Deploy, train, and test the model in AWS
    * Apply reinforcement learning
    * Add a ChatBot / LLM (huge learning curve, but very valuable for resume)
* I do not have much knowledge in these areas, so we will learn together, and we can collectively post resources