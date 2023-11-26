from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/return')
def return_page():
    return render_template('return.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Handle form submission logic here, if needed
    # For example, you can get the submitted data using request.form.get('input_name')
    
    # After handling the submission, redirect to the 'return' page
    return redirect(url_for('return_page'))

if __name__ == '__main__':
    app.run(debug=True)

