# 📝 Day 3 Tasks & Challenges

Complete these tasks to master Flask forms! Work through them in order and have fun! 🚀

---

## ⭐ Task 1: Personalize the Greeting (EASY)

**Goal:** Modify the greeting to be more fun!

**What to do:**
1. Open `templates/greet_result.html`
2. Change the greeting message to something creative!

**Example:**
```html
<h1>🎉 Welcome, {{ user_name }}! You're awesome! 🎉</h1>
<p>We're so happy {{ user_name }} is here!</p>
```

**Success:** Your greeting is unique and fun! ✅

---

## ⭐ Task 2: Add Age to Greeting Form (EASY)

**Goal:** Ask for name AND age!

**What to do:**

**Step 1:** Update `templates/greet_form.html`:
```html
<form method="POST">
    <label for="name">Enter your name:</label>
    <input type="text" id="name" name="name" required>
    <br><br>
    
    <label for="age">Enter your age:</label>
    <input type="number" id="age" name="age" min="1" max="100" required>
    <br><br>
    
    <button type="submit">Greet Me!</button>
</form>
```

**Step 2:** Update `app.py` greet function:
```python
@app.route('/greet', methods=['GET', 'POST'])
def greet():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        return render_template('greet_result.html', user_name=name, user_age=age)
    return render_template('greet_form.html')
```

**Step 3:** Update `templates/greet_result.html`:
```html
<h1>Hello, {{ user_name }}! 🎉</h1>
<p>You are {{ user_age }} years old!</p>
```

**Success:** Form shows both name and age! ✅

---

## ⭐⭐ Task 3: Create a Favorite Things Form (MEDIUM)

**Goal:** Make a form to collect favorite things!

**What to do:**

**In app.py:**
```python
@app.route('/favorites', methods=['GET', 'POST'])
def favorites():
    if request.method == 'POST':
        name = request.form.get('name')
        color = request.form.get('color')
        animal = request.form.get('animal')
        number = request.form.get('number')
        return render_template('favorites_result.html',
                             name=name, color=color, 
                             animal=animal, number=number)
    return render_template('favorites_form.html')
```

**Create templates/favorites_form.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Favorite Things</title>
</head>
<body>
    <h1>Tell Us Your Favorites! ⭐</h1>
    
    <form method="POST">
        <label>Your Name:</label>
        <input type="text" name="name" required><br><br>
        
        <label>Favorite Color:</label>
        <input type="text" name="color" required><br><br>
        
        <label>Favorite Animal:</label>
        <input type="text" name="animal" required><br><br>
        
        <label>Favorite Number:</label>
        <input type="number" name="number" required><br><br>
        
        <button type="submit">Submit!</button>
    </form>
    
    <br><a href="/">← Back to Home</a>
</body>
</html>
```

**Create templates/favorites_result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Your Favorites</title>
</head>
<body>
    <h1>{{ name }}'s Favorite Things! ⭐</h1>
    
    <p><b>Favorite Color:</b> {{ color }}</p>
    <p><b>Favorite Animal:</b> {{ animal }}</p>
    <p><b>Favorite Number:</b> {{ number }}</p>
    
    <br>
    <a href="/favorites">Do Again</a> | 
    <a href="/">← Home</a>
</body>
</html>
```

**Don't forget to add link in home.html!**

**Success:** Favorites form works perfectly! ✅

---

## ⭐⭐ Task 4: Add More Calculator Operations (MEDIUM)

**Goal:** Add square and percentage operations!

**What to do:**

**Update templates/calculator_form.html:**
```html
<select id="operation" name="operation" required>
    <option value="add">Add (+)</option>
    <option value="subtract">Subtract (-)</option>
    <option value="multiply">Multiply (×)</option>
    <option value="divide">Divide (÷)</option>
    <option value="square">Square (²)</option>
    <option value="percent">Percentage (%)</option>
</select>
```

**Update app.py calculator function:**
```python
if operation == 'square':
    result = num1 ** 2
    result_text = f"{num1}² = {result}"
elif operation == 'percent':
    result = (num1 / 100) * num2
    result_text = f"{num1}% of {num2} = {result}"
```

**Success:** New operations work! ✅

---

## ⭐⭐⭐ Task 5: Create a Quiz Page (HARD)

**Goal:** Build a quiz with multiple choice questions!

**What to do:**

**In app.py:**
```python
@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if request.method == 'POST':
        q1 = request.form.get('question1')
        q2 = request.form.get('question2')
        q3 = request.form.get('question3')
        
        score = 0
        if q1 == 'Paris':
            score += 1
        if q2 == '4':
            score += 1
        if q3 == 'Python':
            score += 1
            
        return render_template('quiz_result.html', score=score)
    return render_template('quiz_form.html')
```

**Create templates/quiz_form.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quick Quiz</title>
</head>
<body>
    <h1>Quick Quiz! 📚</h1>
    
    <form method="POST">
        <p><b>1. What is the capital of France?</b></p>
        <input type="radio" name="question1" value="London" required> London<br>
        <input type="radio" name="question1" value="Paris"> Paris<br>
        <input type="radio" name="question1" value="Berlin"> Berlin<br><br>
        
        <p><b>2. How many sides does a square have?</b></p>
        <input type="radio" name="question2" value="3" required> 3<br>
        <input type="radio" name="question2" value="4"> 4<br>
        <input type="radio" name="question2" value="5"> 5<br><br>
        
        <p><b>3. Which language are we learning?</b></p>
        <input type="radio" name="question3" value="Java" required> Java<br>
        <input type="radio" name="question3" value="Python"> Python<br>
        <input type="radio" name="question3" value="C++"> C++<br><br>
        
        <button type="submit">Submit Quiz!</button>
    </form>
    
    <br><a href="/">← Home</a>
</body>
</html>
```

**Create templates/quiz_result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Quiz Results</title>
</head>
<body>
    <h1>Quiz Results! 🎯</h1>
    
    <h2>You scored: {{ score }} out of 3!</h2>
    
    {% if score == 3 %}
        <p>Perfect score! You're amazing! 🌟</p>
    {% elif score == 2 %}
        <p>Great job! Almost perfect! 👍</p>
    {% elif score == 1 %}
        <p>Good try! Keep learning! 📚</p>
    {% else %}
        <p>Don't give up! Try again! 💪</p>
    {% endif %}
    
    <br>
    <a href="/quiz">Try Again</a> | 
    <a href="/">← Home</a>
</body>
</html>
```

**Success:** Quiz works and shows score! ✅

---

## ⭐⭐⭐ Task 6: Mad Libs Game (HARD)

**Goal:** Create a Mad Libs style game!

**What to do:**

**In app.py:**
```python
@app.route('/madlibs', methods=['GET', 'POST'])
def madlibs():
    if request.method == 'POST':
        name = request.form.get('name')
        adjective1 = request.form.get('adjective1')
        noun = request.form.get('noun')
        verb = request.form.get('verb')
        place = request.form.get('place')
        
        return render_template('madlibs_result.html',
                             name=name, adj1=adjective1,
                             noun=noun, verb=verb, place=place)
    return render_template('madlibs_form.html')
```

**Create templates/madlibs_form.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Mad Libs</title>
</head>
<body>
    <h1>Mad Libs! 🎭</h1>
    <p>Fill in the words to create a funny story!</p>
    
    <form method="POST">
        <label>A person's name:</label>
        <input type="text" name="name" required><br><br>
        
        <label>An adjective (describing word):</label>
        <input type="text" name="adjective1" required><br><br>
        
        <label>A noun (thing):</label>
        <input type="text" name="noun" required><br><br>
        
        <label>A verb (action word):</label>
        <input type="text" name="verb" required><br><br>
        
        <label>A place:</label>
        <input type="text" name="place" required><br><br>
        
        <button type="submit">Create Story!</button>
    </form>
    
    <br><a href="/">← Home</a>
</body>
</html>
```

**Create templates/madlibs_result.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Your Story</title>
</head>
<body>
    <h1>Your Silly Story! 😂</h1>
    
    <p>Once upon a time, <b>{{ name }}</b> found a <b>{{ adj1 }}</b> <b>{{ noun }}</b>.</p>
    <p>They decided to <b>{{ verb }}</b> all the way to <b>{{ place }}</b>!</p>
    <p>Everyone laughed and had a great time!</p>
    <p>The End! 🎉</p>
    
    <br>
    <a href="/madlibs">Make Another Story</a> | 
    <a href="/">← Home</a>
</body>
</html>
```

**Success:** Mad Libs creates funny stories! ✅

---

## ⭐⭐⭐⭐ Task 7: Create a Registration Form (EXPERT)

**Goal:** Build a complete user registration form!

**Features:**
- Name, email, age
- Gender (radio buttons)
- Country (dropdown)
- Interests (checkboxes)
- Password (password field)
- Comments (textarea)

**Hint for password field:**
```html
<input type="password" name="password" required>
```

**Hint for textarea:**
```html
<textarea name="comments" rows="4" cols="50"></textarea>
```

**Hint for dropdown:**
```html
<select name="country">
    <option value="USA">USA</option>
    <option value="UK">UK</option>
    <option value="Canada">Canada</option>
</select>
```

**Success:** Complete registration system works! ✅

---

## 🏆 Bonus Challenges (Super Expert!)

### Challenge A: Form Validation
Add validation messages:
```python
if not name:
    error = "Please enter your name!"
    return render_template('form.html', error=error)
```

### Challenge B: Remember Previous Answers
Pass the previous answer back to the form:
```html
<input type="text" name="name" value="{{ previous_name }}">
```

### Challenge C: Build a Guess the Number Game
- Random number between 1-10
- User guesses
- Show "too high", "too low", or "correct!"

---

## 📊 Task Tracker

Check off each task as you complete it:

- [ ] Task 1: Personalized greeting
- [ ] Task 2: Added age to greeting
- [ ] Task 3: Created favorites form
- [ ] Task 4: Added calculator operations
- [ ] Task 5: Built quiz page
- [ ] Task 6: Created Mad Libs game
- [ ] Task 7: Complete registration form
- [ ] Bonus A: Form validation
- [ ] Bonus B: Remember answers
- [ ] Bonus C: Number guessing game

---

## 💡 Forms Cheat Sheet

### Basic Form:
```html
<form method="POST">
    <input type="text" name="fieldname" required>
    <button type="submit">Submit</button>
</form>
```

### Getting Form Data in Python:
```python
value = request.form.get('fieldname')
multiple = request.form.getlist('checkboxname')
```

### Input Types:
- `type="text"` - Text input
- `type="number"` - Number only
- `type="password"` - Hidden password
- `type="radio"` - Single choice
- `type="checkbox"` - Multiple choices
- `<select>` - Dropdown menu
- `<textarea>` - Multi-line text

---

## 🎯 What You've Learned

By completing these tasks, you now know:
- ✅ How to create HTML forms
- ✅ How to handle GET and POST requests
- ✅ How to get form data with request.form
- ✅ Different input types and when to use them
- ✅ How to validate and process user input
- ✅ How to build interactive web applications!

**You're building real, interactive websites now!** 🎉👨‍💻👩‍💻

---

**Keep building awesome things!** 💻✨
