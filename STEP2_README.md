# 🎨 Day 2: Templates & HTML Pages!

Welcome to Day 2! Today you'll make your website look like a REAL website with HTML templates!

## 🎯 What You'll Learn Today
- What templates are and why they're cool
- How to create HTML files
- How to pass data from Python to HTML
- How to use loops in templates
- How to make your pages look connected

## 📚 What are Templates?

Remember on Day 1 when we put HTML inside Python strings? That got messy fast! 

Templates let us:
- Write HTML in separate files (cleaner!)
- Send data from Python to HTML
- Reuse the same layout on different pages
- Make our website look professional

Think of it like this:
- **Python (app.py)** = The brain (handles logic and data)
- **HTML (templates)** = The face (what people see)

## 🛠️ Setup Instructions

### Step 1: Clone Day 2 Code
```bash
git clone -b step-2 https://github.com/byambaa1982/tutorial_flask.git flask-day2
cd flask-day2
```

### Step 2: Check Your Files
You should see:
```
flask-day2/
├── app.py
├── templates/
│   ├── home.html
│   ├── about.html
│   └── favorites.html
└── requirements.txt
```

The `templates/` folder is special - Flask looks there for HTML files!

### Step 3: Install Flask (if you haven't already)
```bash
pip install flask
```

## 🎨 Understanding the Code

### What's New in app.py?

#### 1. New Import
```python
from flask import Flask, render_template
```
We added `render_template` - this loads HTML files!

#### 2. Using Templates
```python
@app.route('/')
def home():
    return render_template('home.html')
```
Instead of returning text, we return an HTML file!

#### 3. Passing Variables
```python
@app.route('/about')
def about():
    my_name = "Young Coder"
    my_age = 10
    return render_template('about.html', name=my_name, age=my_age)
```
We can send data to the template!
- `name=my_name` means the template can use `{{ name }}`
- `age=my_age` means the template can use `{{ age }}`

#### 4. Passing Lists
```python
@app.route('/favorites')
def favorites():
    favorite_things = ['Pizza', 'Video Games', 'Coding', 'My Pet']
    return render_template('favorites.html', items=favorite_things)
```
We can send entire lists to templates!

### Understanding HTML Templates

#### Basic HTML Structure
```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
</head>
<body>
    <h1>Main Heading</h1>
    <p>Some text here</p>
</body>
</html>
```

Every HTML page has:
- `<head>` - Information about the page
- `<body>` - What you actually see

#### Template Variables: `{{ }}`
```html
<p>My name is {{ name }}</p>
```
The `{{ }}` gets replaced with data from Python!

If Python sends `name="Alex"`, you'll see:
```html
<p>My name is Alex</p>
```

#### Template Loops: `{% %}`
```html
<ul>
    {% for item in items %}
        <li>{{ item }}</li>
    {% endfor %}
</ul>
```

This creates a list item for each thing in the Python list!

If Python sends `items=['Pizza', 'Games', 'Coding']`, you'll see:
```html
<ul>
    <li>Pizza</li>
    <li>Games</li>
    <li>Coding</li>
</ul>
```

## 🏃 Running Your App

1. Make sure you're in the `flask-day2` folder
2. Run:
```bash
python app.py
```

3. Open your browser: **http://localhost:5000**

4. Click the links to see different pages!

🎉 **Look at that!** You have a real website with multiple pages!

## ✅ Success Checklist
- [ ] I cloned the step-2 code
- [ ] I can see the templates folder
- [ ] The app runs without errors
- [ ] I can see the home page with links
- [ ] The About page shows name and age
- [ ] The Favorites page shows a list
- [ ] I understand what `{{ }}` does
- [ ] I understand what `{% %}` does

## 🎮 Understanding Templates Better

### Example 1: How Variables Work

In `app.py`:
```python
return render_template('about.html', name="Alex", age=10)
```

In `about.html`:
```html
<p>Name: {{ name }}</p>
<p>Age: {{ age }}</p>
```

Browser shows:
```
Name: Alex
Age: 10
```

### Example 2: How Loops Work

In `app.py`:
```python
colors = ['Red', 'Blue', 'Green']
return render_template('page.html', my_colors=colors)
```

In `page.html`:
```html
{% for color in my_colors %}
    <p>I like {{ color }}</p>
{% endfor %}
```

Browser shows:
```
I like Red
I like Blue
I like Green
```

## 🐛 Troubleshooting

### "TemplateNotFound: home.html"
- Make sure you have a `templates/` folder
- Check the file is named exactly `home.html` (lowercase!)
- The templates folder must be in the same place as app.py

### "Undefined variable: name"
- You forgot to pass the variable from Python
- Check: `render_template('page.html', name="YourName")`

### Changes don't show up
- Hard refresh: `Ctrl+F5` (or `Cmd+Shift+R` on Mac)
- Make sure you saved the file
- Check if the server restarted (should happen automatically with debug=True)

### HTML shows on screen instead of rendering
- You're probably using `return` instead of `render_template`
- Make sure you imported `render_template`

## 📖 New Words You Learned
- **Template**: A file that mixes HTML with special codes for dynamic content
- **render_template**: Flask function that loads and processes HTML files
- **Variable**: Data sent from Python to HTML using `{{ }}`
- **Loop**: Repeating code in templates using `{% for %}`
- **Jinja2**: The template engine Flask uses (fancy word for the `{{ }}` stuff!)

## 🎯 Next Time
In Step 3, you'll learn how to get user input with forms! You'll make interactive pages!

## 💡 Remember
Templates separate your Python code from your HTML - this makes everything cleaner and easier to manage! Professional developers use templates all the time! 🌟

---

### Questions?
Check the DAY2_TASKS.md file for practice exercises! Happy coding! 💻✨
