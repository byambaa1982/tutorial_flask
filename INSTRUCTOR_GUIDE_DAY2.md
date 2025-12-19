# 👨‍🏫 Instructor Guide - Day 2

## 🎯 Class Objective
Teach kids to use HTML templates and understand the separation between Python logic and HTML presentation.

---

## ⚙️ Pre-Class Setup (What YOU Do Before Class)

### 1. Push step-2 Branch to GitHub
```bash
git checkout step-2
git add -A
git commit -m "Day 2: Templates and HTML pages"
git push -u origin step-2
```

### 2. Test the Clone Command
```bash
# Test in a different folder:
git clone -b step-2 https://github.com/byambaa1982/tutorial_flask.git test-day2
cd test-day2
pip install flask
python app.py
```

### 3. Prepare the Clone URL for Students
```bash
git clone -b step-2 https://github.com/byambaa1982/tutorial_flask.git flask-day2
```

### 4. Write on Board (or share on screen):
```
📋 Day 2 Commands:

1. Clone: git clone -b step-2 https://github.com/byambaa1982/tutorial_flask.git flask-day2
2. Enter: cd flask-day2
3. Install: pip install flask
4. Run: python app.py
5. Visit: http://localhost:5000
```

### 5. Have Example Ready
Prepare a simple example to code live with students

---

## 📅 Class Flow (60 minutes)

### **Part 1: Review & Introduction (8 minutes)**

#### Quick Review of Day 1:
"Who remembers what we did last time?"
- Created routes
- Returned text/HTML from Python
- Made multiple pages

#### The Problem:
"Mixing HTML and Python got messy, right? Today we fix that!"

#### Show the Goal:
Open the finished app and navigate through pages
- "See how clean these pages look?"
- "We're separating Python (the brain) from HTML (the face)"

---

### **Part 2: Clone & Setup (10 minutes)**

#### Guide Through Clone:
```bash
cd Desktop
git clone -b step-2 https://github.com/byambaa1982/tutorial_flask.git flask-day2
cd flask-day2
```

#### Show the New Folder Structure:
```bash
dir  # or ls on Mac/Linux
```

**Point out the new templates/ folder:**
"This is where our HTML files live!"

#### Check Files Together:
```bash
cd templates
dir
cd ..
```

#### Install & Run:
```bash
pip install flask
python app.py
```

#### Visit in Browser:
http://localhost:5000

**Celebrate:** "Look! A real website with links!"

---

### **Part 3: Understanding Templates (15 minutes)**

#### Explain the Concept:

**Analogy 1 - Mad Libs:**
"Remember Mad Libs? You fill in blanks in a story. Templates are like that!"
- The HTML is the story
- Python fills in the blanks

**Analogy 2 - Form Letter:**
"Like a form letter: 'Dear [NAME], you won [PRIZE]!'"
- Template: "Dear {{ name }}, you won {{ prize }}!"
- Python provides the actual name and prize

#### Walk Through app.py Together:

**1. New Import:**
```python
from flask import Flask, render_template
```
👉 "render_template loads our HTML files"

**2. Simple Template:**
```python
@app.route('/')
def home():
    return render_template('home.html')
```
👉 "Instead of returning text, we return an HTML file!"

**3. Passing Variables:**
```python
@app.route('/about')
def about():
    my_name = "Young Coder"
    my_age = 10
    return render_template('about.html', name=my_name, age=my_age)
```
👉 "We send data to the template!"
- Left side (`name`) = what template uses
- Right side (`my_name`) = Python variable

**4. Passing Lists:**
```python
favorite_things = ['Pizza', 'Video Games', 'Coding', 'My Pet']
return render_template('favorites.html', items=favorite_things)
```
👉 "We can send whole lists!"

#### Open about.html Together:

```html
<p>My name is <b>{{ name }}</b></p>
<p>I am <b>{{ age }}</b> years old</p>
```

**Explain {{ }}:**
- "These curly braces are special!"
- "They get replaced with data from Python"
- "Like filling in the blanks!"

#### Open favorites.html Together:

```html
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
```

**Explain {% %}:**
- "This is a loop - it repeats!"
- "For each item in the list, make a list item"
- "It's like Python's for loop, but in HTML!"

---

### **Part 4: Hands-On Practice (15 minutes)**

#### Exercise 1: Personalize About Page (5 min)
"Let's make it show YOUR information!"

**Guide them:**
1. Open app.py
2. Find the /about route
3. Change name and age to their own
4. Save and refresh browser

**Walk around and help!**

#### Exercise 2: Add More Favorites (5 min)
"Add your own favorite things!"

**Guide them:**
1. In app.py, find favorite_things list
2. Add more items
3. Save and refresh

"See? The template automatically shows all items!"

#### Exercise 3: Create New Page Together (5 min)
"Let's create a hobbies page together!"

**Live code with them:**

**Step 1 - app.py:**
```python
@app.route('/hobbies')
def hobbies():
    my_hobbies = ['Soccer', 'Reading', 'Gaming']
    return render_template('hobbies.html', hobbies_list=my_hobbies)
```

**Step 2 - Create templates/hobbies.html:**
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
    
    <a href="/">← Back to Home</a>
</body>
</html>
```

**Step 3 - Add link in home.html:**
```html
<li><a href="/hobbies">My Hobbies</a></li>
```

**Test it together!**

---

### **Part 5: Challenges & Exploration (10 minutes)**

#### Individual Work:
"Now try these on your own!"

**Challenge Options:**
1. Add a fun fact page
2. Create a friends page with names and ages
3. Customize all pages with their own info

**Encourage:**
- Check DAY2_TASKS.md for ideas
- Try different templates
- Experiment with loops

**Walk around and help!**

---

### **Part 6: Show & Tell + Wrap Up (7 minutes)**

#### Show & Tell (5 min):
"Who wants to share what they made?"
- Let 2-3 kids show their pages
- Celebrate creativity!
- Point out cool features

#### Review Key Concepts (2 min):
**Ask questions:**
- "What does render_template do?"
- "What do the {{ }} mean?"
- "What does {% for %} do?"

**Key Takeaways:**
- Templates separate Python from HTML
- {{ }} shows variables
- {% %} does logic (loops, if statements)
- Templates make websites cleaner!

#### Preview Day 3:
"Next time: FORMS! You'll make pages where users can type and click!"

---

## 🎓 Teaching Tips

### Key Analogies That Work:

**Templates = Mad Libs**
- HTML is the story with blanks
- Python fills in the blanks

**{{ }} = Blank Spaces**
- Placeholders for data

**{% %} = Instructions**
- "Do this" commands (loop, if, etc.)

**templates/ Folder = Costume Department**
- Where all the "looks" live
- app.py = Director, tells costumes what to do

---

## 📝 Common Student Questions

**Q: "Why do we need templates?"**
A: "Imagine writing a long HTML string for every page - messy! Templates keep things organized."

**Q: "What's the difference between {{ }} and {% %}?"**
A: "{{ }} shows something. {% %} does something (like loops or decisions)."

**Q: "Why must templates be in templates/ folder?"**
A: "Flask looks there by default. It's like having a special drawer for specific things."

**Q: "Can I name my template anything?"**
A: "Yes! Just make sure render_template('name.html') matches the file name!"

**Q: "What if I misspell a variable name?"**
A: "The template will show nothing or an error. Check Python and HTML match!"

**Q: "Can I use HTML from Day 1?"**
A: "Yes! Templates are just HTML files with special {{ }} and {% %} codes added!"

---

## 🚨 Common Issues & Solutions

### Issue: "TemplateNotFound" Error

**Causes:**
- templates/ folder doesn't exist
- HTML file in wrong location
- Typo in filename

**Solution:**
```bash
# Check folder structure:
ls templates/  # Should show .html files

# Make sure templates/ is next to app.py
```

### Issue: Variable Doesn't Show

**Causes:**
- Variable name mismatch
- Forgot to pass variable

**Solution:**
```python
# Make sure these match:
return render_template('page.html', name="Alex")  # in Python
{{ name }}  # in HTML
```

### Issue: Loop Doesn't Work

**Cause:** Syntax error in template

**Solution:**
```html
<!-- Check for typos: -->
{% for item in items %}
    {{ item }}
{% endfor %}  <!-- Don't forget endfor! -->
```

### Issue: Changes Don't Appear

**Solutions:**
1. Save the file!
2. Hard refresh: Ctrl+F5
3. Check terminal for errors
4. Restart server if needed

---

## 📊 Success Metrics

✅ **Excellent:**
- 90%+ students have working templates
- Students can explain {{ }} vs {% %}
- Students created at least one new page
- High engagement and excitement

✅ **Good:**
- 75%+ students have working templates
- Most understand basic template syntax
- Students making progress on challenges

⚠️ **Needs Review:**
- Less than 70% success
- Confusion about template basics
- Plan: Review concepts next class

---

## 🎯 Differentiation Strategies

### For Fast Learners:
- Challenge: Create conditional templates ({% if %})
- Build a complete "All About Me" site
- Add more complex data structures
- Help others!

### For Struggling Students:
- Focus on basics: one simple template
- Pair with a buddy
- Use pre-made templates, just change variables
- One-on-one help with folder structure

### Visual Learners:
- Draw diagram: Python → Template → Browser
- Show before/after of template rendering
- Use colors to highlight {{ }} and {% %}

### Hands-On Learners:
- More live coding together
- Type-along exercises
- Physical props (cards with {{ }} written on them)

---

## 🛠️ Backup Plans

### If Tech Issues:
- Share screen and code together
- Download as ZIP if Git issues
- Use online Python environment (repl.it)

### If Running Behind:
- Skip individual challenges
- Focus on one complete example
- Send extra tasks as homework

### If Ahead of Schedule:
- Preview forms (Day 3 sneak peek)
- Add CSS styling basics
- Student presentations

---

## 📚 Extension Activities

### Homework Ideas:
1. Create 3 new pages about favorite things
2. Build a page about your family
3. Make a "My Week" page with daily activities

### Next Class Prep:
"Before next time, think about what questions you'd ask a user on your website!"

---

## 🎉 Celebration Points

**Celebrate when:**
- First successful template renders
- Student fixes their own template error
- Creative use of loops
- Helping classmates
- Completing challenges

**Recognition:**
"You're not just coding - you're thinking like a professional web developer! Separating concerns (Python vs HTML) is exactly what pros do!"

---

**Remember:** Templates can be confusing at first. The {{ }} and {% %} syntax looks weird. Be patient, use lots of examples, and celebrate progress! 🌟
