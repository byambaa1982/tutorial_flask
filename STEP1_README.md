# 🚀 Day 1: Hello Flask!

Welcome to Day 1! Today you're going to create your very first web application!

## 🎯 What You'll Learn Today
- What Flask is and why it's awesome
- How to install Flask
- How to create a simple web server
- How to see your website in a browser

## 📚 What is Flask?
Flask is a tool that helps you build websites using Python! Think of it like LEGO blocks for websites - you start simple and can build bigger things step by step.

## 🛠️ Setup Instructions

### Step 1: Make Sure Python is Installed
Open your terminal (or Command Prompt) and type:
```bash
python --version
```
You should see something like `Python 3.x.x`. If not, ask your instructor for help!

### Step 2: Create a Virtual Environment (Optional but Recommended)
This keeps your project organized:
```bash
python -m venv venv
```

Activate it:
- **Windows**: `venv\Scripts\activate`
- **Mac/Linux**: `source venv/bin/activate`

### Step 3: Install Flask
```bash
pip install -r requirements.txt
```

Or install Flask directly:
```bash
pip install flask
```

## 🎨 Your First Flask App

### What's in the Files?
- **app.py** - This is your main Python file where the magic happens!
- **requirements.txt** - Lists the tools (packages) you need

### Understanding app.py

Let's look at what each part does:

```python
from flask import Flask
```
This imports Flask - it's like opening a toolbox!

```python
app = Flask(__name__)
```
This creates your web application. `__name__` is just Python magic - don't worry about it!

```python
@app.route('/')
def home():
    return "Hello, World!"
```
This is a **route** - it's like a door to a page on your website!
- `@app.route('/')` means "when someone visits the main page..."
- `def home():` is a function that runs when they visit
- `return "Hello, World!"` is what they'll see on the page!

```python
if __name__ == '__main__':
    app.run(debug=True)
```
This starts your web server! `debug=True` helps you see errors.

## 🏃 Running Your App

1. Make sure you're in the tutorial folder
2. Run this command:
```bash
python app.py
```

3. You should see something like:
```
 * Running on http://127.0.0.1:5000
```

4. Open your web browser and go to: **http://localhost:5000**

5. You should see: **Hello, World!**

🎉 **CONGRATULATIONS!** You just made a website!

## ✅ Success Checklist
- [ ] Python is installed
- [ ] Flask is installed
- [ ] app.py file exists
- [ ] You ran `python app.py` without errors
- [ ] You can see "Hello, World!" in your browser
- [ ] You're super excited! 🎈

## 🎮 Challenge Tasks (Optional)

Want to do more? Try these:

1. **Change the message**: Instead of "Hello, World!", make it say something else!
2. **Add your name**: Make it say "Hello, [YourName]!"
3. **Add another route**: Try adding `@app.route('/fun')` with a different message!

### Example Challenge:
```python
@app.route('/fun')
def fun_page():
    return "This is the fun page! 🎉"
```
Then visit: http://localhost:5000/fun

## 🐛 Troubleshooting

### "Command not found: python"
Try `python3` instead of `python`

### "Module not found: flask"
You need to install Flask: `pip install flask`

### "Address already in use"
Another program is using port 5000. Stop the other program or change the port:
```python
app.run(debug=True, port=5001)
```

### The page won't load
- Make sure app.py is still running (check your terminal)
- Check for typos in the URL
- Try http://127.0.0.1:5000 instead of localhost

## 🔄 Stopping Your Server
Press `Ctrl + C` in the terminal where the app is running

## 📖 New Words You Learned
- **Flask**: A tool for building websites with Python
- **Route**: A URL path that shows a page
- **Server**: A program that serves web pages
- **localhost**: Your own computer (when you're testing)

## 🎯 Next Time
In Step 2, you'll learn how to create multiple pages and make them link together!

## 💡 Remember
Every web developer started exactly where you are now. You're doing great! 🌟

---

### Questions?
Ask your instructor or check with a friend. Happy coding! 💻✨
