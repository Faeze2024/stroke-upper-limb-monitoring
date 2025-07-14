# src/report_generator.py
from fpdf import FPDF
import matplotlib.pyplot as plt
import pandas as pd

def generate_pdf_report(csv_path, output_path='report.pdf'):
    # داده‌ها رو بخون
    df = pd.read_csv(csv_path)

    # نمودار زاویه‌ها رو رسم کن
    plt.figure(figsize=(10, 5))
    plt.plot(df['timestamp'], df['left_elbow'], label='Left Elbow')
    plt.plot(df['timestamp'], df['right_elbow'], label='Right Elbow')
    plt.plot(df['timestamp'], df['left_shoulder'], label='Left Shoulder')
    plt.plot(df['timestamp'], df['right_shoulder'], label='Right Shoulder')
    plt.xlabel('Timestamp')
    plt.ylabel('Angle')
    plt.title('Joint Angles Over Time')
    plt.legend()
    chart_path = 'angles_chart.png'
    plt.savefig(chart_path)
    plt.close()

    # PDF ایجاد کن
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=14)
    pdf.cell(200, 10, "Joint Angles Report", ln=True, align='C')

    # نمودار رو اضافه کن
    pdf.image(chart_path, x=10, y=30, w=180)

    # ذخیره کن
    pdf.output(output_path)
    print(f"PDF report saved to {output_path}")
