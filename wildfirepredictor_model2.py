import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

class wildFirePredictor: 
    def __init__(self): 
        ######### TRAINING THE MODEL #########
        data = pd.read_csv("./data/updated_la_fires_data.csv")

        data = data[["temp", "humidity", "Air pressure", "Fire? Y/N"]]
        
        data = data.rename(columns={"Air pressure": "air_pressure", "Fire? Y/N": "wildfire_likelihood"})
        
        data["wildfire_likelihood"] = data["wildfire_likelihood"].astype(int)

        data = data.dropna()

        x = data[["temp", "humidity", "air_pressure"]]
        y = data["wildfire_likelihood"]

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
        
        model = RandomForestClassifier(random_state=100)
        model.fit(x_train, y_train)
        
        self.model = model 
        self.columns = x.columns 
        
        y_pred = model.predict(x_test)
        print("Accuracy:", accuracy_score(y_test, y_pred))
        print("Classification Report:\n", classification_report(y_test, y_pred))
        ####################################

    def predict_wildfire(self, temp, humidity, air_pressure):
        # Create input data
        input_data = {
            "temp": [temp],
            "humidity": [humidity],
            "air_pressure": [air_pressure],
        }

        input_df = pd.DataFrame(input_data)
        
        # Ensure all columns match the training data (same names and order)
        input_df = input_df.reindex(columns=self.columns, fill_value=0)

        prediction = self.model.predict(input_df)
        return prediction[0]

# EXAMPLE USAGE
# temp = 50  # Example temperature in Celsius
# humidity = 0
# air_pressure = 10 

# predictor = wildFirePredictor()
# prediction = predictor.predict_wildfire(temp, humidity, air_pressure)
# print("Wildfire Likely (1=Yes, 0=No):", prediction)