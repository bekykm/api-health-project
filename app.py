from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Home route (renders HTML)
@app.route("/")
def home():
    return render_template("index.html")

# API route: accepts user data and returns recommendation
@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.json  # Expecting JSON data from frontend
    weight = data.get("weight")
    height = data.get("height")
    activity = data.get("activity")

    if not weight or not height:
        return jsonify({"error": "Weight and height are required"}), 400

    # BMI calculation
    bmi = weight / (height * height)

    # Simple logic for recommendation
    if bmi < 18.5:
        advice = "You are underweight. Increase calorie intake and consult a nutritionist."
    elif 18.5 <= bmi <= 24.9:
        advice = "You have a healthy weight. Maintain regular exercise and a balanced diet."
    else:
        advice = "You are overweight. Reduce sugar intake and increase physical activity."

    # Adjust advice with activity level
    if activity == "low":
        advice += " Try to walk at least 30 minutes daily."
    elif activity == "high":
        advice += " Great job on staying active!"

    return jsonify({
        "bmi": round(bmi, 2),
        "recommendation": advice
    })

if __name__ == "__main__":
    app.run(debug=True)
