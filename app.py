# Day 2: Flask with Templates! 🎨

# Step 1: Import Flask and render_template
from flask import Flask, render_template

# Step 2: Create our app
app = Flask(__name__)

# Step 3: Routes that use templates
@app.route('/')
def home():
    """Main page using a template"""
    return render_template('home.html')

@app.route('/about')
def about():
    """About page with variables"""
    my_name = "Young Coder"
    my_age = 10
    return render_template('about.html', name=my_name, age=my_age)

@app.route('/favorites')
def favorites():
    """Favorites page with a list"""
    favorite_things = ['Pizza', 'Video Games', 'Coding', 'My Pet']
    return render_template('favorites.html', items=favorite_things)

# Step 4: Run the app
if __name__ == '__main__':
    app.run(debug=True)
