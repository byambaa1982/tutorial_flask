# 🎨 Day 2 Tasks & Challenges

Complete these tasks to master Flask templates! Work through them in order and have fun! 🚀

---

## ⭐ Task 1: Personalize the About Page (EASY)

**Goal:** Make the about page show YOUR information!

**What to do:**
1. Open `app.py`
2. Find the `/about` route
3. Change these lines:
   ```python
   my_name = "Young Coder"  # ← Put your real name!
   my_age = 10               # ← Put your real age!
   ```
4. Save and refresh the browser
5. Visit: http://localhost:5000/about

**Success:** You see your own name and age! ✅

---

## ⭐ Task 2: Add More Favorites (EASY)

**Goal:** Expand your favorites list!

**What to do:**
1. In `app.py`, find the `/favorites` route
2. Add more items to the list:
   ```python
   favorite_things = [
       'Pizza', 
       'Video Games', 
       'Coding', 
       'My Pet',
       'Swimming',      # Add your favorites!
       'Reading',
       'Art'
   ]
   ```
3. Save and check http://localhost:5000/favorites

**Success:** All your favorites appear in the list! ✅

---

## ⭐⭐ Task 3: Create a Hobbies Page (MEDIUM)

**Goal:** Make a new page showing your hobbies!

**What to do:**

**Step 1:** Add route in `app.py`:
```python
@app.route('/hobbies')
def hobbies():
    my_hobbies = ['Soccer', 'Drawing', 'Gaming', 'Coding']
    return render_template('hobbies.html', hobbies_list=my_hobbies)
```

**Step 2:** Create `templates/hobbies.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Hobbies</title>
</head>
<body>
    <h1>My Hobbies! 🎮</h1>
    
    <ul>
        {% for hobby in hobbies_list %}
            <li>{{ hobby }}</li>
        {% endfor %}
    </ul>
    
    <br>
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Step 3:** Add link to home page! In `templates/home.html`, add:
```html
<li><a href="/hobbies">My Hobbies</a></li>
```

**Success:** You can click to hobbies page from home! ✅

---

## ⭐⭐ Task 4: Add a Fun Fact with Variable (MEDIUM)

**Goal:** Create a page that shows a random fun fact!

**What to do:**

**In app.py:**
```python
@app.route('/funfact')
def funfact():
    fact = "Honey never spoils! Archaeologists found 3000-year-old honey that's still edible!"
    return render_template('funfact.html', fun_fact=fact)
```

**Create templates/funfact.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Fun Fact</title>
</head>
<body>
    <h1>🤯 Fun Fact of the Day!</h1>
    
    <p>{{ fun_fact }}</p>
    
    <br>
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Success:** Your fun fact appears on the page! ✅

---

## ⭐⭐⭐ Task 5: Create a Friends Page (MEDIUM)

**Goal:** Show a list of friends with their ages!

**What to do:**

**In app.py:**
```python
@app.route('/friends')
def friends():
    my_friends = [
        {'name': 'Alex', 'age': 10},
        {'name': 'Sam', 'age': 11},
        {'name': 'Jordan', 'age': 10}
    ]
    return render_template('friends.html', friends=my_friends)
```

**Create templates/friends.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Friends</title>
</head>
<body>
    <h1>My Friends! 👥</h1>
    
    <ul>
        {% for friend in friends %}
            <li>{{ friend.name }} is {{ friend.age }} years old</li>
        {% endfor %}
    </ul>
    
    <br>
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Success:** Each friend shows with their name and age! ✅

---

## ⭐⭐⭐ Task 6: Add Conditional Logic (HARD)

**Goal:** Show different messages based on conditions!

**What to do:**

**In app.py:**
```python
@app.route('/weather')
def weather():
    is_sunny = True
    temperature = 25
    return render_template('weather.html', sunny=is_sunny, temp=temperature)
```

**Create templates/weather.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>Weather</title>
</head>
<body>
    <h1>Today's Weather ☀️</h1>
    
    {% if sunny %}
        <p>It's sunny outside! Perfect for playing! ☀️</p>
    {% else %}
        <p>It's cloudy today. Maybe read a book? 📚</p>
    {% endif %}
    
    <p>Temperature: {{ temp }}°C</p>
    
    {% if temp > 20 %}
        <p>It's warm! Wear a t-shirt! 👕</p>
    {% else %}
        <p>It's cold! Wear a jacket! 🧥</p>
    {% endif %}
    
    <br>
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Experiment:** Change `is_sunny` to `False` and `temperature` to `15` - see what changes!

**Success:** Different messages appear based on the values! ✅

---

## ⭐⭐⭐ Task 7: Build a Pet Profile Page (HARD)

**Goal:** Create a detailed page about a pet!

**What to do:**

**In app.py:**
```python
@app.route('/pet')
def pet():
    pet_info = {
        'name': 'Buddy',
        'type': 'Dog',
        'age': 3,
        'tricks': ['Sit', 'Roll over', 'High five', 'Play dead']
    }
    return render_template('pet.html', pet=pet_info)
```

**Create templates/pet.html:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>My Pet</title>
</head>
<body>
    <h1>Meet {{ pet.name }}! 🐕</h1>
    
    <p><b>Type:</b> {{ pet.type }}</p>
    <p><b>Age:</b> {{ pet.age }} years old</p>
    
    <h2>Tricks {{ pet.name }} knows:</h2>
    <ul>
        {% for trick in pet.tricks %}
            <li>{{ trick }}</li>
        {% endfor %}
    </ul>
    
    <br>
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Success:** Pet profile shows all information nicely! ✅

---

## ⭐⭐⭐⭐ Task 8: Create a Complete "All About Me" Site (EXPERT)

**Goal:** Build a multi-page website about yourself!

**What to do:**

Create these pages:
1. **Home** - Welcome message with your name
2. **About** - Your name, age, school, favorite subject
3. **Hobbies** - List of hobbies
4. **Favorites** - Favorite foods, colors, movies, etc.
5. **Goals** - Things you want to learn or do

**Navigation:** Make sure EVERY page has links to all other pages!

**Example Home Page:**
```html
<!DOCTYPE html>
<html>
<head>
    <title>All About Me</title>
</head>
<body>
    <h1>Welcome to {{ name }}'s Website! 🌟</h1>
    
    <p>Explore my website to learn all about me!</p>
    
    <h2>Navigation:</h2>
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/about">About Me</a></li>
        <li><a href="/hobbies">My Hobbies</a></li>
        <li><a href="/favorites">My Favorites</a></li>
        <li><a href="/goals">My Goals</a></li>
    </ul>
</body>
</html>
```

**Success:** Complete website with working navigation! ✅

---

## 🏆 Bonus Challenges (Super Expert!)

### Challenge A: Number Guessing Game Setup
Create a page that shows numbers 1-10:

```python
@app.route('/numbers')
def numbers():
    number_list = list(range(1, 11))  # Creates [1, 2, 3, ..., 10]
    return render_template('numbers.html', numbers=number_list)
```

```html
<h2>Numbers 1 to 10:</h2>
{% for num in numbers %}
    <span>{{ num }}</span>
    {% if num < 10 %}, {% endif %}
{% endfor %}
```

### Challenge B: Even/Odd Checker
```html
{% for num in numbers %}
    {% if num % 2 == 0 %}
        <p>{{ num }} is EVEN</p>
    {% else %}
        <p>{{ num }} is ODD</p>
    {% endif %}
{% endfor %}
```

### Challenge C: Build a Mini Blog
Create a blog with posts:

```python
@app.route('/blog')
def blog():
    posts = [
        {'title': 'My First Day Learning Flask', 'date': 'Dec 19, 2025'},
        {'title': 'Templates Are Cool!', 'date': 'Dec 20, 2025'},
        {'title': 'I Built a Website!', 'date': 'Dec 21, 2025'}
    ]
    return render_template('blog.html', posts=posts)
```

---

## 📊 Task Tracker

Check off each task as you complete it:

- [ ] Task 1: Personalized about page
- [ ] Task 2: Added more favorites
- [ ] Task 3: Created hobbies page
- [ ] Task 4: Added fun fact page
- [ ] Task 5: Created friends page
- [ ] Task 6: Used conditional logic
- [ ] Task 7: Built pet profile
- [ ] Task 8: Complete "All About Me" site
- [ ] Bonus A: Numbers list
- [ ] Bonus B: Even/Odd checker
- [ ] Bonus C: Mini blog

---

## 💡 Template Cheat Sheet

### Showing Variables:
```html
{{ variable_name }}
```

### Loops:
```html
{% for item in list %}
    {{ item }}
{% endfor %}
```

### If Statements:
```html
{% if condition %}
    <p>Show this if true</p>
{% else %}
    <p>Show this if false</p>
{% endif %}
```

### Accessing Dictionary Values:
```html
{{ person.name }}
{{ person['name'] }}  <!-- Also works! -->
```

---

## 🎯 What You've Learned

By completing these tasks, you now know:
- ✅ How to use templates instead of strings
- ✅ How to pass variables to templates
- ✅ How to use loops in templates
- ✅ How to use if/else in templates
- ✅ How to work with lists and dictionaries
- ✅ How to build multi-page websites!

**You're becoming a real web developer!** 🎉👨‍💻👩‍💻

---

## 🔄 Tips for Success

1. **Save your files** before refreshing the browser!
2. **Check the terminal** for error messages
3. **Indentation matters** in both Python and HTML
4. **Template file names** must match what's in `render_template()`
5. **Variable names** must match between Python and HTML

---

**Keep building awesome things!** 💻✨
