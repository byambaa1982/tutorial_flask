# 🎨 Day 4 Tasks & Challenges

Complete these tasks to master CSS styling! Work through them in order and watch your website transform! 🚀

---

## ⭐ Task 1: Change the Main Colors (EASY)

**Goal:** Customize the color scheme!

**What to do:**
1. Open `static/css/style.css`
2. Find the `body` section
3. Change the background color:

```css
body {
    background-color: #ffe6f0;  /* Light pink! */
}
```

**Try these colors:**
- `#e6f3ff` - Light blue
- `#fff4e6` - Light orange
- `#e6ffe6` - Light green
- `#f0e6ff` - Light purple

**Success:** Your page has a new background color! ✅

---

## ⭐ Task 2: Make Headings More Colorful (EASY)

**Goal:** Change heading colors!

**What to do:**
In `style.css`, modify:

```css
h1 {
    color: #ff6b6b;     /* Red */
    font-size: 3em;      /* Even bigger! */
}

h2 {
    color: #4ecdc4;     /* Turquoise */
}
```

**Experiment with:**
- `#ff6b6b` - Red
- `#ffd93d` - Yellow
- `#6bcf7f` - Green
- `#a29bfe` - Purple

**Success:** Headings are colorful and eye-catching! ✅

---

## ⭐⭐ Task 3: Style a Specific Page (MEDIUM)

**Goal:** Create a custom style for just one page!

**What to do:**

**Step 1:** Create a new CSS file: `static/css/special.css`

```css
/* Special styles for greeting page */
body {
    background: linear-gradient(to right, #667eea, #764ba2);
    color: white;
}

.container {
    background-color: rgba(255, 255, 255, 0.95);
    color: #333;
}

h1 {
    color: #667eea;
    font-size: 3.5em;
    text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
}
```

**Step 2:** Link it ONLY in `greet_result.html`:

```html
<head>
    <title>Hello!</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/special.css') }}">
</head>
```

**Success:** Greeting page has a unique gradient background! ✅

---

## ⭐⭐ Task 4: Create Styled Buttons (MEDIUM)

**Goal:** Make different button styles!

**What to do:**
Add these classes to your `style.css`:

```css
.btn-success {
    background-color: #4ecdc4;
    color: white;
    padding: 12px 30px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

.btn-success:hover {
    background-color: #3ab0a8;
}

.btn-danger {
    background-color: #ff6b6b;
}

.btn-danger:hover {
    background-color: #ee5a52;
}

.btn-warning {
    background-color: #ffd93d;
    color: #333;
}

.btn-warning:hover {
    background-color: #f0c419;
}
```

**Use them in HTML:**
```html
<button class="btn-success">Submit</button>
<button class="btn-danger">Delete</button>
<button class="btn-warning">Warning</button>
```

**Success:** You have multiple button styles! ✅

---

## ⭐⭐ Task 5: Add Hover Effects to Links (MEDIUM)

**Goal:** Make links more interactive!

**What to do:**
Update the link styling in `style.css`:

```css
a {
    color: #4a90e2;
    text-decoration: none;
    padding: 5px 10px;
    border-radius: 3px;
    transition: all 0.3s ease;
}

a:hover {
    background-color: #4a90e2;
    color: white;
    text-decoration: none;
    transform: scale(1.05);
}
```

The `transition` makes changes smooth!
The `transform: scale(1.05)` makes links slightly bigger on hover!

**Success:** Links have smooth animated hover effects! ✅

---

## ⭐⭐⭐ Task 6: Create a Card Layout (HARD)

**Goal:** Make form elements look like cards!

**What to do:**
Add to `style.css`:

```css
.card {
    background-color: white;
    border-radius: 10px;
    padding: 25px;
    margin: 20px 0;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s, box-shadow 0.3s;
}

.card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
}

.card h2 {
    margin-top: 0;
    color: #4a90e2;
}
```

**Use in HTML (home.html):**
```html
<div class="card">
    <h2>👋 Greeting Form</h2>
    <p>Enter your name and get a personalized greeting!</p>
    <a href="/greet">Try It →</a>
</div>
```

**Success:** Forms appear in floating cards that lift on hover! ✅

---

## ⭐⭐⭐ Task 7: Style Form Inputs with Focus Effects (HARD)

**Goal:** Make inputs highlight when selected!

**What to do:**
Update input styling in `style.css`:

```css
input[type="text"],
input[type="number"],
select {
    width: 100%;
    padding: 12px;
    margin-bottom: 15px;
    border: 2px solid #e0e0e0;
    border-radius: 5px;
    font-size: 16px;
    transition: border-color 0.3s, box-shadow 0.3s;
}

input[type="text"]:focus,
input[type="number"]:focus,
select:focus {
    border-color: #4a90e2;
    box-shadow: 0 0 0 3px rgba(74, 144, 226, 0.1);
    outline: none;
}
```

**Success:** Inputs glow blue when you click on them! ✅

---

## ⭐⭐⭐⭐ Task 8: Create a Responsive Navigation Bar (EXPERT)

**Goal:** Build a stylish navigation menu!

**What to do:**

**Add to style.css:**
```css
.navbar {
    background-color: #333;
    padding: 15px 0;
    margin: -30px -30px 30px -30px;
    border-radius: 10px 10px 0 0;
}

.navbar ul {
    list-style: none;
    margin: 0;
    padding: 0;
    text-align: center;
}

.navbar li {
    display: inline-block;
    margin: 0 15px;
    background: none;
    border: none;
}

.navbar a {
    color: white;
    padding: 10px 20px;
    display: block;
    border-radius: 5px;
}

.navbar a:hover {
    background-color: #4a90e2;
    color: white;
}
```

**Add to home.html (inside container, at top):**
```html
<nav class="navbar">
    <ul>
        <li><a href="/">Home</a></li>
        <li><a href="/greet">Greet</a></li>
        <li><a href="/calculator">Calculator</a></li>
        <li><a href="/survey">Survey</a></li>
    </ul>
</nav>
```

**Success:** Professional navigation bar at the top! ✅

---

## 🏆 Bonus Challenges (Super Expert!)

### Challenge A: Animated Button
```css
.btn-animated {
    animation: pulse 2s infinite;
}

@keyframes pulse {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.05); }
}
```

### Challenge B: Gradient Background
```css
body {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}
```

### Challenge C: Styled Lists
```css
ul {
    list-style: none;
}

li {
    padding-left: 30px;
    position: relative;
}

li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: #4ecdc4;
    font-weight: bold;
}
```

### Challenge D: Add Icons to Buttons
Use emoji or find free icon fonts:
```html
<button>✓ Submit</button>
<button>✗ Cancel</button>
<button>⟲ Refresh</button>
```

### Challenge E: Create a Dark Mode
```css
.dark-mode {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

.dark-mode .container {
    background-color: #2d2d2d;
    color: #e0e0e0;
}
```

---

## 📊 Task Tracker

Check off each task as you complete it:

- [ ] Task 1: Changed main colors
- [ ] Task 2: Made headings colorful
- [ ] Task 3: Styled specific page
- [ ] Task 4: Created styled buttons
- [ ] Task 5: Added hover effects
- [ ] Task 6: Created card layout
- [ ] Task 7: Styled input focus effects
- [ ] Task 8: Built navigation bar
- [ ] Bonus A: Animated button
- [ ] Bonus B: Gradient background
- [ ] Bonus C: Styled lists
- [ ] Bonus D: Icon buttons
- [ ] Bonus E: Dark mode

---

## 💡 CSS Cheat Sheet

### Colors
```css
color: #ff0000;              /* Hex */
color: rgb(255, 0, 0);       /* RGB */
color: rgba(255, 0, 0, 0.5); /* RGBA (with transparency) */
```

### Spacing
```css
margin: 10px;                /* All sides */
margin: 10px 20px;           /* Top/bottom, Left/right */
padding: 10px 15px 10px 15px; /* Top, Right, Bottom, Left */
```

### Borders
```css
border: 2px solid black;
border-radius: 10px;         /* Rounded corners */
```

### Shadows
```css
box-shadow: 0 2px 4px rgba(0,0,0,0.1);
text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
```

### Transitions & Animations
```css
transition: all 0.3s ease;
transform: scale(1.1);
transform: translateY(-5px);
```

### Flexbox (Advanced)
```css
display: flex;
justify-content: center;
align-items: center;
```

---

## 🎨 Color Palettes to Try

**Ocean:**
- `#006994` (dark blue)
- `#13a8c4` (cyan)
- `#90dce9` (light blue)

**Sunset:**
- `#ff6b6b` (red)
- `#feca57` (yellow)
- `#ee5a6f` (pink)

**Forest:**
- `#2d6a4f` (dark green)
- `#52b788` (green)
- `#b7e4c7` (light green)

**Purple Dream:**
- `#5f27cd` (purple)
- `#a29bfe` (light purple)
- `#dfe6e9` (gray)

---

## 🎯 What You've Learned

By completing these tasks, you now know:
- ✅ How to link CSS files to HTML
- ✅ How to style elements with CSS
- ✅ How to use colors, fonts, and spacing
- ✅ How to create hover effects
- ✅ How to use transitions and animations
- ✅ How to build professional-looking layouts
- ✅ How to make websites beautiful!

**You're now a web designer!** 🎉🎨

---

**Keep designing beautiful things!** 💻✨
