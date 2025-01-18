# TF
[Get Started](https://www.tensorflow.org/tutorials/quickstart/beginner)

# ARIMA / ARIMAX
* These are only conceptual, we will need to find appropriate libraries in Python
* ARIMA = Univariate, ARIMAX = Multivariate
* [8.1-8.4](https://www.youtube.com/watch?v=brn4NWIQXTw&list=PL27amhF9jj-Ku47tMX9-Kh1GubWJYltcb&index=116)
  * Use differencing to remove trends or seasonality
  * The data needs to have [constant variance](/info/constvar/README.md)
* [8.6-8.7](https://www.youtube.com/watch?v=FvQjv3w3y5M&list=PL27amhF9jj-Ku47tMX9-Kh1GubWJYltcb&index=121)
  * Use ADF when data is clearly not stationary, use KPSS to prove data is stationary
  * Don't worry about the code or the math, just understand the concept
* [8.14-8.18](https://www.youtube.com/watch?v=FvQjv3w3y5M&list=PL27amhF9jj-Ku47tMX9-Kh1GubWJYltcb&index=129)
  * These determine the upper bound of p, q, Lower bound is 0
  * We will use grid search to find the optimal parameters
* [8.19](https://youtu.be/vo76VSUmlXI?si=v6rfE-e32QE0r1Bq)
  * We will be following this procedure to obtain ARIMA result
  * We will select model order ourself
  * Instead of step 5, search across all possible p and q values, and choose the hyperparameters with lowest AIC
    * This is called a grid search
* [9.1-9.2](https://www.youtube.com/watch?v=G3mEVb0nkZ4&list=PL27amhF9jj-Ku47tMX9-Kh1GubWJYltcb&index=140)
  * ARIMAX is basically combining ARIMA and linear model
  * We will be using method one from 9.2
* (Optional) [Coding Example](https://www.projectpro.io/article/how-to-build-arima-model-in-python/544)
  * This is just for reference of different libraries for different parts
  * We will NOT follow this step by step
* (Optional) [IBM guide](https://www.ibm.com/think/topics/arima-model)
  * Don't worry about the math, conceptual understanding is enough
* (Optional) [Remaining Chapter 8](https://www.youtube.com/watch?v=brn4NWIQXTw&list=PL27amhF9jj-Ku47tMX9-Kh1GubWJYltcb&index=116)
* (Optional) [Application to stocks](https://www.investopedia.com/terms/a/autoregressive-integrated-moving-average-arima.asp)

# Neural Networks
* [Google guide](https://developers.google.com/machine-learning/crash-course/neural-networks)
  * Complete *Introduction* through *Backpropagation* sections
  * It may be helpful to do an additional Google search on pros and cons for most common activation functions
* [Coding example](https://www.geeksforgeeks.org/artificial-neural-network-in-tensorflow/)
* [Coding example](https://www.tensorflow.org/tutorials/quickstart/beginner)
* (Optional) [Video tutorial](https://www.youtube.com/watch?v=CqOfi41LfDw&list=PLblh5JKOoLUIxGDQs4LFFD--41Vzf-ME1&index=2&ab_channel=StatQuestwithJoshStarmer)
  * Longer but more in-depth and easy to understand mathematical examples for more intuition
  * Complete Videos 2-9

# Integrating ARIMAX + Neural Networks
* Neural Network inputs all features from dataset PLUS the output of ARIMAX model
* (Optional)[Research Paper](https://www.tandfonline.com/doi/full/10.1080/13675567.2020.1803246#d1e693)
  * My idea for this project came from here
  * Who likes reading research papers when tutorials are easier to understand
  * But, reading research papers is a big part of ML

# (Optional) Other Models
* We will not use these models for this project unless we are doing special topics
* [ARIMA vs SARIMA vs LSTM](https://medium.com/@yennhi95zz/a-guide-to-time-series-models-in-machine-learning-usage-pros-and-cons-ac590a75e8b3)
  * If this requires a subscription, I can post a PDF in the Discord instead
* [Zoo of Best Models](https://www.sciencedirect.com/science/article/pii/S2212827122004036)