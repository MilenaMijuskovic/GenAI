import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
# Load the data



class wildFirePredictor: 
    def __init__(self): 
        ######### TRAINING THE MODEL #########
        data = pd.read_csv("./data/forestfires.csv")
        data = pd.get_dummies(data, columns=["month", "day"], drop_first=True)
        data["wildfire_likelihood"] = (data["area"] > 0).astype(int)
        data = data.drop(columns=["area"])
        x = data.drop(columns=["wildfire_likelihood"])
        y = data["wildfire_likelihood"]
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
        model = RandomForestClassifier(random_state=42)
        model.fit(x_train, y_train)
        self.model = model 
        self.columns = x.columns 
        y_pred = model.predict(x_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        ####################################

    def predict_wildfire(self, temp, RH, wind=0, rain=0, FFMC=85, DMC=50, DC=100, ISI=5, month="aug", day="fri"):
        # Create input data
        input_data = {
            "temp": [temp],
            "RH": [RH],
            "wind": [wind],
            "rain": [rain],
            "FFMC": [FFMC],
            "DMC": [DMC],
            "DC": [DC],
            "ISI": [ISI],
        }
        # Add one-hot encoded columns for month and day
        for col in self.columns:
            if col.startswith("month_"):
                input_data[col] = [1 if col == f"month_{month}" else 0]
            elif col.startswith("day_"):
                input_data[col] = [1 if col == f"day_{day}" else 0]
        # Convert to DataFrame
        input_df = pd.DataFrame(input_data)
        # Ensure all columns match the training data (same names and order)
        input_df = input_df.reindex(columns=self.columns, fill_value=0)
        # Predict wildfire likelihood
        prediction = self.model.predict(input_df)
        return prediction[0]

# temp = 25.65  # Example temperature in Celsius
# RH = 22.39   # Example relative humidity in %
# prediction = predict_wildfire(temp=temp, RH=RH, month="aug", day="fri")
# print("Wildfire Likely (1=Yes, 0=No):", prediction)