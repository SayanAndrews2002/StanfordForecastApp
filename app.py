from flask import Flask, render_template, request
import forecasting_module  # This is your forecasting project code

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # A homepage template – “Hello Stanford” maybe plus links

@app.route("/forecast", methods=["GET", "POST"])
def forecast():
    if request.method == "POST":
        # Accept parameters here, for example:
        forecast_months = int(request.form.get("forecast_months", 24))
        # Run your forecasting routines (group or pod level as needed)
        results = forecasting_module.main_pod(forecast_months=forecast_months)
        # Optionally, you can pass results to a template for display.
        return render_template("forecast.html", results=results)
    else:
        # or just show a form for input
        return render_template("forecast_form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
