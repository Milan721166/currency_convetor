from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')  

@app.route('/submit', methods=['POST'])
def submit():
    
    name = request.form['name']
    roll_number = request.form['roll_number']
    dsa_score = int(request.form['DSA'])
    oops_score = int(request.form['OOPS'])
    os_score = int(request.form['OS'])

    
    total_score = dsa_score + oops_score + os_score
    average_score = total_score / 3

    
    result = "PASS" if average_score >= 50 else "FAIL"

    
    return render_template('result.html', name=name, roll_number=roll_number, result=result, average_score=average_score)

if __name__ == '__main__':
    app.run(debug=True)
