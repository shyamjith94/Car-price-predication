import numpy as np
from flask.views import View, request
from flask import render_template
import pandas as pd
import pickle
from app import DIR_PATH


class Home(View):
    """ home view class
    """
    methods = ['GET']
    FILE_NAME = "clean data.csv"

    def get_unique_data(self):
        """ data unique
        """
        clean_data = DIR_PATH + self.FILE_NAME
        data = pd.read_csv(clean_data)
        company_unique = list(data["company"].unique())
        name_unique = list(data["name"].unique())
        year_unique = list(np.sort(data["year"].unique()))
        fuel_unique = list(data["fuel_type"].unique())
        return dict(companies=company_unique, names=name_unique, years=year_unique, fuel_types=fuel_unique)

    def dispatch_request(self):
        """ templates
        """
        data = self.get_unique_data()
        return render_template("home.html", **data)


class PredictValue(View):
    """ predict price of car
    """
    methods = ['POST']
    FILE_NAME = "PricePredicationLRModel.pkl"

    def get_predicated_value(self, data: []) -> np.array:
        """ find predication
        """
        model = pickle.load(open(DIR_PATH + self.FILE_NAME, "rb"))
        columns = ['name', 'company', 'year', 'kms_driven', 'fuel_type']
        data = np.array(data).reshape(1, 5)
        prediction = model.predict(pd.DataFrame(data=data, columns=columns))
        return prediction

    def dispatch_request(self):
        """ Prediction
        """
        try:
            company = request.form.get("company")
            name = request.form.get("carNames")
            year = request.form.get("year")
            fuel_type = request.form.get("fuelType")
            km_driven = request.form.get("kmDriven")
            data = [name, company, year, km_driven, fuel_type]
            predicted_value = self.get_predicated_value(data)
            return str(round(predicted_value.item(), 4))
        except Exception as e:
            print("error", e)
            return "Error check input values"
