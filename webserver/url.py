from app import app
from application import Home, PredictValue

app.add_url_rule('/', view_func=Home.as_view(name="home"))
app.add_url_rule('/predict-value/', view_func=PredictValue.as_view(name="predict_value"))