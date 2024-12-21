from flask import Flask, request, render_template, redirect, url_for
import requests

app = Flask(__name__)

API_URL = "https://api.currencyapi.com/v3/latest?apikey=fca_live_1ge071DX5A2Iey0OyooCiyKom3jicXoHKVVfQCgY"

@app.route("/", methods=["GET", "POST"])
def currency_converter():
    result = None
    error = None

    if request.method == "POST":
        try:

            amount = float(request.form.get("currency"))
            from_currency = request.form.get("from")
            to_currency = request.form.get("to")

            response = requests.get(API_URL)
            if response.status_code == 200:
                data = response.json()
                rates = data["data"]

                from_rate = rates[from_currency.upper()]["value"]
                to_rate = rates[to_currency.upper()]["value"]

                result = round((amount / from_rate) * to_rate, 2)

                return render_template("results.html", result=result, from_currency=from_currency, to_currency=to_currency)

            else:
                error = "Error fetching exchange rates. Please try again later."
        except Exception as e:
            error = "An error occurred. Please ensure all inputs are valid."

    return render_template("index.html", result=result, error=error)


@app.route("/results")
def currency_results():
    return render_template("results.html")


if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)