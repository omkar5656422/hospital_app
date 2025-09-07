from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import csv
import os

app = Flask(__name__)
CORS(app)  # allows cross-origin requests

# Create CSV file with headers if it doesn't exist
if not os.path.exists("appointments.csv"):
    with open("appointments.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Department", "Date", "Time"])

# Serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")
    # Menu page
@app.route("/menu")
def menu():
    return render_template("menu.html")

# Appointment page (optional)
@app.route("/appointments")
def appointments():
    return render_template("appointments.html")

# Save appointment data from form
@app.route('/save-appointment', methods=['POST'])
def save_appointment():
    data = request.get_json()

    name = data.get('name')
    department = data.get('department')
    date = data.get('date')
    time = data.get('time')

    # Append to CSV
    with open("appointments.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, department, date, time])

    return jsonify({"message": "Appointment saved successfully"}), 200


if __name__ == '__main__':
    app.run(debug=True)
