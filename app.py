from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def retailer_sales():
    # Load your CSV file
    df = pd.read_csv('CAF_Activation_Report_for_Franchisee (7).csv')

    # Group by retailer and count SIMs
    sales_data = df['Retailer Name'].value_counts().reset_index()
    sales_data.columns = ['Retailer Name', 'SIM Sale Count']

    # Convert to dictionary for Jinja2 template
    data = sales_data.to_dict(orient='records')
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
