# Day 3: Flask with Forms! 📝

# Step 1: Import Flask, render_template, and request
from flask import Flask, render_template, request

# Step 2: Create our app
app = Flask(__name__)

# Step 3: Routes
@app.route('/')
def home():
    """Main page with links to all forms"""
    return render_template('home.html')

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """Simple greeting form"""
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        return render_template('greet_result.html', user_name=name)
    # If GET request, show the form
    return render_template('greet_form.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """Simple calculator"""
    if request.method == 'POST':
        num1 = float(request.form.get('number1'))
        num2 = float(request.form.get('number2'))
        operation = request.form.get('operation')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        
        return render_template('calculator_result.html', 
                             num1=num1, num2=num2, 
                             operation=operation, result=result)
    return render_template('calculator_form.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    """Fun survey form"""
    if request.method == 'POST':
        name = request.form.get('name')
        favorite_color = request.form.get('color')
        favorite_food = request.form.get('food')
        hobbies = request.form.getlist('hobbies')  # Gets multiple checkboxes
        
        return render_template('survey_result.html',
                             name=name, color=favorite_color,
                             food=favorite_food, hobbies=hobbies)
    return render_template('survey_form.html')

# Step 4: Run the app
if __name__ == '__main__':
    app.run(debug=True)
