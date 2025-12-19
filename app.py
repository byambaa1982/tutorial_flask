# My First Flask App! 🚀

# Step 1: Import Flask
from flask import Flask

# Step 2: Create our app
app = Flask(__name__)

# Step 3: Create a route (a page on our website)
@app.route('/')
def home():
    """This function runs when someone visits the main page"""
    return "Hello, World! 🌍"

# Step 4: Run the app
if __name__ == '__main__':
    # debug=True helps us see errors and reloads automatically
    app.run(debug=True)
