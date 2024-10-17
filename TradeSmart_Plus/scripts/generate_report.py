from fpdf import FPDF

def generate_report(stock_data, signals, filename):
    pdf = FPDF()
    pdf.add_page()

    # Title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, "Backtest Report", ln=True, align='C')

    # Summary of backtest
    pdf.set_font('Arial', '', 12)
    pdf.cell(200, 10, f"Initial Balance: $10000", ln=True)
    pdf.cell(200, 10, f"Final Balance: ${stock_data['Balance'].iloc[-1]:.2f}", ln=True)

    # Save the PDF
    pdf.output(filename)
