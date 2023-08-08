**

# Battery Remaining Useful Life Prediction

**
**

## Dataset

**

The dataset used was the '[Battery Remaining Useful Life (RUL)](https://www.kaggle.com/datasets/ignaciovinuales/battery-remaining-useful-life-rul)' provided by Ignacio Vinuales on Kaggle.

Model**

## Model

**
The model used was a simple linear regressor. I tried other models as well but linear regression gave a high accuracy with negligible training time. I managed to get high accuracy using KNN but it took significantly longer to train and predict.

**

## Approach

**
The approach was to first clean the dataset as it had a lot of outliers (such as negative numbers for columns representing time, time multiple orders of magnitude higher than expected).

The approach I took to clean this dataset was to remove every row for which the value of any column was an outlier. 

Outliers were defined as values with a z-score of >= 3

After training the model was saved and this model is being used in the GUI for predictions.

**

## Results

**
The model has a R2 score of **0.976977**

**

## Using the GUI

**
To ease the process of using this model for prediction, I have created a GUI. 

You need to enter all the data which is listed in the GUI and then click the button at the bottom to get a prediction.