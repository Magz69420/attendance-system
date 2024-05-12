from flask import Flask, render_template, request , jsonify
import sqlite3
from datetime import datetime
from io import StringIO
import csv
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', selected_date='', no_data=False)

@app.route('/attendance', methods=['POST'])
def attendance():
    selected_date = request.form.get('selected_date')
    selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    formatted_date = selected_date_obj.strftime('%Y-%m-%d')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
    attendance_data = cursor.fetchall()

    conn.close()

    if not attendance_data:
        return render_template('index.html', selected_date=selected_date, no_data=True)
    
    return render_template('index.html', selected_date=selected_date, attendance_data=attendance_data)

@app.route('/download', methods=['POST'])
def download_attendance_data():
    selected_date = request.form['download_date']
    selected_date_obj = datetime.strptime(selected_date, '%Y-%m-%d')
    formatted_date = selected_date_obj.strftime('%Y-%m-%d')

    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()

    cursor.execute("SELECT name, time FROM attendance WHERE date = ?", (formatted_date,))
    attendance_data = cursor.fetchall()

    conn.close()

    if attendance_data:
        # Prepare CSV data
        csv_data = StringIO()
        csv_writer = csv.writer(csv_data)
        csv_writer.writerow(['Name', 'Time'])
        csv_writer.writerows(attendance_data)
        csv_data.seek(0)

        # Return CSV file as response
        return csv_data.getvalue(), 200, {
            'Content-Type': 'text/csv',
            'Content-Disposition': 'attachment; filename=attendance_data.csv'
        }
    else:
        return "No data available for download", 404

if __name__ == '__main__':
    app.run(debug=True)
