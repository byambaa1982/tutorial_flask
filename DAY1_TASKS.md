# 🎮 Day 1 Tasks & Challenges

Complete these tasks to become a Flask master! Start with Task 1 and work your way down. Don't worry if you don't finish all of them - the important thing is to have fun and learn! 🚀

---

## ⭐ Task 1: Change Your Welcome Message (EASY)

**Goal:** Make your website say something different!

**What to do:**
1. Open `app.py` in your text editor
2. Find this line:
   ```python
   return "Hello, World! 🌍"
   ```
3. Change it to something fun! Ideas:
   - `"Welcome to my awesome website!"`
   - `"Hi! I'm learning Flask!"`
   - `"This is MY website! 🎉"`

4. Save the file
5. Stop your server (press `Ctrl+C` in the terminal)
6. Start it again: `python app.py`
7. Refresh your browser - see the change!

**Success:** You see your new message in the browser! ✅

---

## ⭐⭐ Task 2: Add Your Name (EASY)

**Goal:** Personalize your website with your name!

**What to do:**
1. Change the message to include your name:
   ```python
   return "Hello! I'm [YOUR NAME] and I made this website!"
   ```
2. Add some emoji to make it fun! 🎈 🚀 ⭐ 🎉
3. Save, restart, and check!

**Example:**
```python
return "Hello! I'm Alex and I made this website! 🎨"
```

**Success:** Your browser shows YOUR name! ✅

---

## ⭐⭐ Task 3: Create an About Page (MEDIUM)

**Goal:** Add a second page to your website!

**What to do:**
1. Add this new route to `app.py` (below the home route):
   ```python
   @app.route('/about')
   def about():
       return "This is my about page! I'm learning Flask."
   ```

2. Make sure the spacing (indentation) looks exactly like the home route!
3. Save and restart your server
4. Visit: `http://localhost:5000/about`

**Success:** You can see a different message at /about! ✅

---

## ⭐⭐ Task 4: Add More Pages (MEDIUM)

**Goal:** Create at least 3 different pages!

**What to do:**
Create these pages (or make up your own!):

**Page 1: Favorites**
```python
@app.route('/favorites')
def favorites():
    return "My favorite color is blue and I love pizza! 🍕"
```

**Page 2: Hobbies**
```python
@app.route('/hobbies')
def hobbies():
    return "I like to code, play games, and draw! 🎮"
```

**Page 3: Fun Fact**
```python
@app.route('/funfact')
def funfact():
    return "Did you know? Octopuses have 3 hearts! 🐙"
```

**Test each page:**
- http://localhost:5000/favorites
- http://localhost:5000/hobbies
- http://localhost:5000/funfact

**Success:** All 3 pages work! ✅

---

## ⭐⭐⭐ Task 5: Create a Joke Page (MEDIUM)

**Goal:** Make people laugh!

**What to do:**
1. Create a `/joke` route
2. Add your favorite joke!

**Example:**
```python
@app.route('/joke')
def joke():
    return "Why don't scientists trust atoms? Because they make up everything! 😂"
```

**Bonus Challenge:**
- Add 2-3 different jokes!
- Try `/joke1`, `/joke2`, `/joke3`

**Success:** Your joke makes people smile! ✅

---

## ⭐⭐⭐ Task 6: Use HTML Tags (HARD)

**Goal:** Make your text look fancier!

**What to do:**
You can use HTML tags to format your text!

```python
@app.route('/fancy')
def fancy():
    return "<h1>This is BIG text!</h1><p>This is normal text.</p><b>This is BOLD!</b>"
```

**Try these HTML tags:**
- `<h1>Big Heading</h1>` - Very big text
- `<h2>Medium Heading</h2>` - Medium text
- `<p>Paragraph</p>` - Normal text
- `<b>Bold text</b>` - Bold
- `<i>Italic text</i>` - Italic
- `<br>` - New line

**Example:**
```python
@app.route('/mypage')
def mypage():
    return "<h1>Welcome!</h1><p>My name is <b>Alex</b></p><p>I am learning <i>Flask</i>!</p>"
```

**Success:** You see different text sizes and styles! ✅

---

## ⭐⭐⭐ Task 7: Create a List Page (HARD)

**Goal:** Show a list of your favorite things!

**What to do:**
Use HTML list tags to create a list:

```python
@app.route('/favorites-list')
def favorites_list():
    return """
    <h2>My Favorite Things:</h2>
    <ul>
        <li>Pizza 🍕</li>
        <li>Video games 🎮</li>
        <li>My pet dog 🐕</li>
        <li>Coding! 💻</li>
    </ul>
    """
```

**HTML List Tags:**
- `<ul>` starts an unordered (bullet) list
- `<li>` is each list item
- `</ul>` ends the list

**Bonus:** Try `<ol>` for a numbered list!

**Success:** You see a nice bullet-point list! ✅

---

## ⭐⭐⭐⭐ Task 8: Build a Mini Homepage (EXPERT)

**Goal:** Combine everything you learned!

**What to do:**
Create an awesome homepage with:
- A big heading with your name
- A paragraph about yourself
- A list of your hobbies
- Links to your other pages

**Example:**
```python
@app.route('/')
def home():
    return """
    <h1>Welcome to Alex's Website! 🎨</h1>
    <p>Hi! I'm Alex and I'm 10 years old. I love coding!</p>
    
    <h2>My Hobbies:</h2>
    <ul>
        <li>Building websites 💻</li>
        <li>Playing soccer ⚽</li>
        <li>Reading books 📚</li>
    </ul>
    
    <h2>Check out my other pages:</h2>
    <p>
        <a href="/about">About Me</a> | 
        <a href="/joke">Jokes</a> | 
        <a href="/favorites">Favorites</a>
    </p>
    """
```

**New Tag:**
- `<a href="/about">About Me</a>` - Creates a clickable link!

**Success:** You have an awesome homepage with working links! ✅

---

## 🏆 Bonus Challenges (Super Expert!)

### Challenge A: Add Colors
```python
return '<h1 style="color: blue;">This text is BLUE!</h1>'
```

Try different colors: red, green, purple, orange!

### Challenge B: Add an Image
```python
return '<img src="https://cataas.com/cat" width="300">'
```
(This shows a random cat picture!)

### Challenge C: Create a Quiz
```python
@app.route('/quiz')
def quiz():
    return """
    <h2>Quick Quiz!</h2>
    <p><b>Q: What is 2 + 2?</b></p>
    <p>Go to <a href="/answer">/answer</a> to see the answer!</p>
    """

@app.route('/answer')
def answer():
    return "<h1>The answer is 4! 🎉</h1><a href='/quiz'>Back to Quiz</a>"
```

---

## 📊 Task Tracker

Check off each task as you complete it:

- [ ] Task 1: Changed welcome message
- [ ] Task 2: Added my name
- [ ] Task 3: Created about page
- [ ] Task 4: Made 3+ pages
- [ ] Task 5: Added a joke
- [ ] Task 6: Used HTML tags
- [ ] Task 7: Created a list
- [ ] Task 8: Built mini homepage
- [ ] Bonus A: Added colors
- [ ] Bonus B: Added image
- [ ] Bonus C: Made a quiz

---

## 💡 Tips

**If something doesn't work:**
1. Check your spelling carefully
2. Make sure indentation matches the examples
3. Stop and restart your server: `Ctrl+C` then `python app.py`
4. Refresh your browser
5. Ask for help if stuck!

**Having fun?**
- Add MORE pages!
- Combine different ideas!
- Make pages about your favorite things!
- Show your friends and family!

**Remember:**
- You can't break anything - experiment freely!
- Making mistakes is how you learn!
- Every programmer started exactly where you are!

---

## 🎯 What You've Learned

By completing these tasks, you now know how to:
- ✅ Create routes (pages) in Flask
- ✅ Return text to the browser
- ✅ Use HTML tags to format text
- ✅ Create lists and links
- ✅ Build a multi-page website!

**You're officially a web developer!** 🎉👨‍💻👩‍💻

---

## 📸 Show & Tell

When you finish:
1. Take a screenshot of your coolest page
2. Show it to your instructor or friends
3. Be proud of what you built!
4. Get ready for Day 2 - we'll make it even better! 🚀

---

**Have fun coding!** 💻✨
