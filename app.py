from flask import Flask, request
import forecasting_module  # Make sure this module contains your forecasting code, e.g., main_pod()

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Stanford - Forecasting App Deployed Successfully!"

@app.route("/run_forecast", methods=["GET"])
def run_forecast():
    # Optionally, you could get parameters from the request (e.g., forecast horizon) using request.args.
    # For now, we'll simply run your pod-level forecasting pipeline with a 24 month horizon.
    try:
        results = forecasting_module.main_pod(forecast_months=24)
        return "Forecasting pipeline completed successfully!"
    except Exception as e:
        return f"An error occurred during forecasting: {str(e)}", 500

if __name__ == "__main__":
    # When deploying on Azure, you may want to specify the host (0.0.0.0) and port (e.g., 8000)
    app.run(host="0.0.0.0", port=8000, debug=True)
