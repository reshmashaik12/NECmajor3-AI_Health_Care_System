def predict_outcome(severity, age, risk):

    score = (100 - severity * 10) - (age * 0.3)

    if risk == 1:
        score -= 20

    if score > 70:
        return "High Recovery Chance"
    elif score > 40:
        return "Moderate Recovery Chance"
    else:
        return "Low Recovery Chance"