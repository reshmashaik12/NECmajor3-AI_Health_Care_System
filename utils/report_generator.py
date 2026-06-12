from fpdf import FPDF
import os

REPORT_FOLDER = "reports/generated_reports"

os.makedirs(
    REPORT_FOLDER,
    exist_ok=True
)

def generate_patient_report(
    patient_name,
    disease,
    prediction,
    confidence,
    doctor_notes=""
):

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    pdf.cell(
        200,
        10,
        "AI Healthcare Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font(
        "Arial",
        size=12
    )

    pdf.cell(
        200,
        10,
        f"Patient Name: {patient_name}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Disease: {disease}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Prediction: {prediction}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Confidence: {confidence} %",
        ln=True
    )

    pdf.multi_cell(
        0,
        10,
        f"Doctor Notes: {doctor_notes}"
    )

    filename = f"{patient_name}_report.pdf"

    filepath = os.path.join(
        REPORT_FOLDER,
        filename
    )

    pdf.output(filepath)

    return filepath