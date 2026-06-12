def get_treatment_recommendation(disease, risk):

    disease = disease.lower()

    if disease == "diabetes":
        if risk == "High":
            return "Strict diet + insulin + monitoring"
        elif risk == "Moderate":
            return "Controlled diet + exercise"
        else:
            return "Healthy lifestyle"

    if disease == "heart disease":
        if risk == "High":
            return "Immediate cardiology care"
        elif risk == "Moderate":
            return "Diet control + checkups"
        else:
            return "Normal lifestyle"

    if disease == "kidney disease":
        if risk == "High":
            return "Dialysis + strict diet"
        elif risk == "Moderate":
            return "Monitor kidney function"
        else:
            return "Healthy routine"

    return "Consult doctor"