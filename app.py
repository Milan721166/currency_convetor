from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')  # Render the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    # Get the form data
    name = request.form['name']
    roll_number = request.form['roll_number']
    dsa_score = int(request.form['DSA'])
    oops_score = int(request.form['OOPS'])
    os_score = int(request.form['OS'])

    # Calculate the total and average score
    total_score = dsa_score + oops_score + os_score
    average_score = total_score / 3

    # Determine if the student passed or failed
    result = "PASS" if average_score >= 50 else "FAIL"

    # Render the result page with the student's details and result
    return render_template('result.html', name=name, roll_number=roll_number, result=result, average_score=average_score)

if __name__ == '__main__':
    app.run(debug=True)
