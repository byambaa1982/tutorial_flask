# 🗄️ Day 5: SQLite Database with Flask

Welcome to **Day 5**! Today you're going to learn about **databases** - how to save, search, update, and delete data! 🎉

## 📚 What You'll Learn

- What is a database and why we need it
- How to use SQLite (a simple database)
- **Basic SQL commands** (the language databases speak!)
  - **CREATE TABLE** - Make a new table
  - **INSERT** - Add new data
  - **SELECT** - Get data
  - **UPDATE** - Change existing data
  - **DELETE** - Remove data
  - **WHERE** - Filter results
  - **COUNT, AVG, GROUP BY** - Statistics!
- How to use databases in Flask

---

## 🤔 What is a Database?

A **database** is like a digital filing cabinet that stores information in an organized way.

**Think of it like this:**
- A **spreadsheet** = A database table
- **Columns** = Different types of information (name, age, grade)
- **Rows** = Individual records (each student)

**Why use a database?**
- ✅ Data stays even when you close the app
- ✅ Can store thousands (or millions!) of records
- ✅ Fast searching and filtering
- ✅ Multiple people can use it at once
- ✅ Organized and structured

---

## 📊 What is SQLite?

**SQLite** is a simple, file-based database perfect for learning!

**Advantages:**
- No server needed (just a file!)
- Built into Python (no installation!)
- Perfect for small to medium apps
- Easy to learn
- Used in phones, browsers, and apps everywhere!

**The database file:**
- In this project: `students.db`
- It's a file that stores all your data
- You can delete it to start fresh

---

## 🔤 SQL - The Language of Databases

**SQL** (Structured Query Language) is how we talk to databases!

Think of SQL like English sentences for data:
- "**SELECT** all students **FROM** the database"
- "**INSERT** a new student named Alice"
- "**DELETE** the student **WHERE** id is 5"

---

## 📖 SQL Commands Explained

### 1. CREATE TABLE - Making a Table

Creates a new table to store data.

**Syntax:**
```sql
CREATE TABLE table_name (
    column1 datatype,
    column2 datatype,
    column3 datatype
);
```

**Our Example:**
```sql
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    favorite_subject TEXT NOT NULL,
    grade TEXT NOT NULL
);
```

**Explained:**
- `students` = Name of the table
- `id INTEGER PRIMARY KEY AUTOINCREMENT` = Unique number for each student (auto-generated!)
- `TEXT` = Stores text/words
- `INTEGER` = Stores whole numbers
- `NOT NULL` = This field is required
- `IF NOT EXISTS` = Only create if it doesn't exist already

---

### 2. INSERT - Adding Data

Adds new records to the table.

**Syntax:**
```sql
INSERT INTO table_name (column1, column2, column3)
VALUES (value1, value2, value3);
```

**Our Example:**
```python
conn.execute('''
    INSERT INTO students (name, age, favorite_subject, grade)
    VALUES (?, ?, ?, ?)
''', (name, age, favorite_subject, grade))
```

**Explained:**
- `INSERT INTO students` = Add to the students table
- `(name, age, favorite_subject, grade)` = These columns
- `VALUES (?, ?, ?, ?)` = The `?` are placeholders (Python fills them in safely!)
- `(name, age, favorite_subject, grade)` = The actual values from our variables

**Why use `?` placeholders?**
- ✅ Safe from SQL injection attacks
- ✅ Automatically handles quotes and special characters
- ✅ Cleaner code

---

### 3. SELECT - Getting Data

Retrieves data from the database.

**Syntax:**
```sql
SELECT column1, column2 FROM table_name;
SELECT * FROM table_name;  -- * means all columns
```

**Our Examples:**

**Get ALL students:**
```python
cursor = conn.execute('SELECT * FROM students ORDER BY name')
students = cursor.fetchall()
```

**Explained:**
- `SELECT *` = Get all columns
- `FROM students` = From the students table
- `ORDER BY name` = Sort alphabetically by name
- `fetchall()` = Get all results as a list

**Get ONE student:**
```python
cursor = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
student = cursor.fetchone()
```

**Explained:**
- `WHERE id = ?` = Only get the student with this ID
- `fetchone()` = Get just one result

---

### 4. UPDATE - Changing Data

Modifies existing records.

**Syntax:**
```sql
UPDATE table_name
SET column1 = value1, column2 = value2
WHERE condition;
```

**Our Example:**
```python
conn.execute('''
    UPDATE students 
    SET name = ?, age = ?, favorite_subject = ?, grade = ?
    WHERE id = ?
''', (name, age, favorite_subject, grade, student_id))
```

**Explained:**
- `UPDATE students` = Change data in students table
- `SET name = ?, age = ?, ...` = Change these columns to new values
- `WHERE id = ?` = **ONLY** for this specific student

**⚠️ IMPORTANT:** Always use WHERE! Without it, you'll update EVERY row!

---

### 5. DELETE - Removing Data

Removes records from the table.

**Syntax:**
```sql
DELETE FROM table_name WHERE condition;
```

**Our Example:**
```python
conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
```

**Explained:**
- `DELETE FROM students` = Remove from students table
- `WHERE id = ?` = Only delete this student

**⚠️ WARNING:** Without WHERE, you'll delete EVERYTHING!

---

### 6. WHERE - Filtering Results

Filters which rows to affect.

**Examples:**
```sql
-- Exact match
SELECT * FROM students WHERE name = 'Alice'

-- Greater than
SELECT * FROM students WHERE age > 12

-- LIKE for partial matches
SELECT * FROM students WHERE name LIKE '%Al%'  -- Finds names containing "Al"
```

**Our Search Example:**
```python
cursor = conn.execute('''
    SELECT * FROM students 
    WHERE name LIKE ? OR favorite_subject LIKE ?
    ORDER BY name
''', (f'%{search_term}%', f'%{search_term}%'))
```

**Explained:**
- `LIKE ?` = Pattern matching
- `%{search_term}%` = % means "anything before or after"
- `OR` = Match either condition

---

### 7. Aggregate Functions - Statistics!

**COUNT** - Count rows:
```sql
SELECT COUNT(*) FROM students
```

**AVG** - Average:
```sql
SELECT AVG(age) FROM students
```

**SUM, MIN, MAX** also available!

---

### 8. GROUP BY - Grouping Data

Groups rows that have the same values.

**Our Example:**
```python
cursor = conn.execute('''
    SELECT favorite_subject, COUNT(*) as count 
    FROM students 
    GROUP BY favorite_subject 
    ORDER BY count DESC
''')
```

**Explained:**
- `SELECT favorite_subject, COUNT(*)` = Show subject and count
- `GROUP BY favorite_subject` = Group students by subject
- `ORDER BY count DESC` = Highest count first

**Result might be:**
```
Math: 5 students
Science: 3 students
Art: 2 students
```

---

## 💻 Using Databases in Flask

### Step 1: Import sqlite3
```python
import sqlite3
```

### Step 2: Create a connection function
```python
def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row  # Access columns by name!
    return conn
```

### Step 3: Execute SQL
```python
conn = get_db_connection()
cursor = conn.execute('SELECT * FROM students')
students = cursor.fetchall()
conn.close()
```

### Step 4: Always commit changes!
```python
conn = get_db_connection()
conn.execute('INSERT INTO students ...')
conn.commit()  # ← Save changes!
conn.close()
```

### Step 5: Always close connections!
```python
conn.close()  # ← Free up resources!
```

---

## 🔍 Understanding the Code

### Pattern 1: Reading Data (SELECT)
```python
@app.route('/students')
def students_list():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM students ORDER BY name')
    students = cursor.fetchall()
    conn.close()
    return render_template('students_list.html', students=students)
```

**Flow:**
1. Open connection
2. Execute SELECT query
3. Get all results
4. Close connection
5. Send to template

---

### Pattern 2: Adding Data (INSERT)
```python
@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        name = request.form.get('name')
        age = request.form.get('age')
        # ... get other fields
        
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO students (name, age, favorite_subject, grade)
            VALUES (?, ?, ?, ?)
        ''', (name, age, favorite_subject, grade))
        conn.commit()  # ← SAVE!
        conn.close()
        
        return redirect(url_for('students_list'))
    
    return render_template('add_student.html')
```

**Flow:**
1. Get data from form
2. Open connection
3. Execute INSERT query with placeholders
4. **COMMIT** to save
5. Close connection
6. Redirect to list

---

### Pattern 3: Updating Data (UPDATE)
```python
@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    conn = get_db_connection()
    
    if request.method == 'POST':
        # Get new data
        name = request.form.get('name')
        # ...
        
        conn.execute('''
            UPDATE students 
            SET name = ?, age = ?, favorite_subject = ?, grade = ?
            WHERE id = ?
        ''', (name, age, favorite_subject, grade, student_id))
        conn.commit()
        conn.close()
        return redirect(url_for('view_student', student_id=student_id))
    
    # GET - show current data
    cursor = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return render_template('edit_student.html', student=student)
```

---

### Pattern 4: Deleting Data (DELETE)
```python
@app.route('/students/<int:student_id>/delete', methods=['POST'])
def delete_student(student_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('students_list'))
```

**Note:** DELETE is only POST (not GET) to prevent accidental deletions!

---

## 🎯 Important Concepts

### 1. cursor vs connection
- **Connection** = The link to the database
- **Cursor** = Executes queries and holds results

### 2. fetchall() vs fetchone()
- `fetchall()` = List of all matching rows
- `fetchone()` = Just the first matching row

### 3. Accessing Row Data
```python
# Method 1: By index
student[0]  # First column

# Method 2: By name (better!)
student['name']
student['age']
```

### 4. Always Use Placeholders!
```python
# ❌ DANGEROUS! Vulnerable to SQL injection
conn.execute(f"SELECT * FROM students WHERE name = '{name}'")

# ✅ SAFE! Use placeholders
conn.execute("SELECT * FROM students WHERE name = ?", (name,))
```

---

## 🛠️ Setup & Run

### 1. Clone the Repository
```bash
git clone -b step-5 https://github.com/byambaa1982/tutorial_flask.git flask-day5
cd flask-day5
```

### 2. Install Flask (if needed)
```bash
pip install flask
```

### 3. Run the App
```bash
python app.py
```

### 4. Open Browser
```
http://127.0.0.1:5000
```

### 5. Try It Out!
- View students list
- Add new students
- Search for students
- View statistics
- Edit and delete students

---

## 📁 Project Structure

```
flask-day5/
├── app.py                      # Main app with database code
├── students.db                 # Database file (created automatically)
├── templates/
│   ├── home.html              # Main page
│   ├── students_list.html     # Show all students (SELECT *)
│   ├── add_student.html       # Add new student (INSERT)
│   ├── view_student.html      # View one student (SELECT WHERE)
│   ├── edit_student.html      # Edit student (UPDATE)
│   ├── search_students.html   # Search (SELECT LIKE)
│   └── statistics.html        # Stats (COUNT, AVG, GROUP BY)
└── static/
    └── css/
        └── style.css          # CSS from Day 4!
```

---

## 🔄 How the Database Works

### When you start the app:
1. `init_db()` runs
2. Creates `students.db` file
3. Creates `students` table if it doesn't exist
4. Adds 3 sample students if table is empty

### When you visit /students:
1. Opens connection to `students.db`
2. Runs `SELECT * FROM students ORDER BY name`
3. Gets all students
4. Passes to template
5. Template displays in HTML table

### When you add a student:
1. Form submits to `/students/add`
2. Gets data from form
3. Runs `INSERT INTO students ...`
4. **Commits** to save
5. Redirects to students list

---

## 🐛 Troubleshooting

### Database file not created?
- Make sure `init_db()` is called
- Check for errors in terminal
- Try deleting `students.db` and restarting

### Changes not saving?
- Did you call `conn.commit()`?
- Check for error messages

### "table students already exists"?
- That's normal! `IF NOT EXISTS` prevents errors

### Want to start fresh?
```bash
# Delete database and restart
rm students.db  # On Windows: del students.db
python app.py
```

---

## 🎨 CSS for Tables

New CSS added for database features:

```css
table {
    width: 100%;
    border-collapse: collapse;
}

th {
    background-color: #4a90e2;
    color: white;
    padding: 12px;
}

td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
}
```

---

## 🚀 Next Steps

After mastering this lesson, you can:
- Add more fields to the students table
- Create multiple tables (teachers, classes, etc.)
- Add relationships between tables
- Learn about JOIN queries
- Add user authentication
- Deploy your app online!

---

## 📝 Key Takeaways

**Today you learned:**
- ✅ What databases are and why they're important
- ✅ Basic SQL commands (CREATE, INSERT, SELECT, UPDATE, DELETE)
- ✅ How to filter with WHERE
- ✅ How to search with LIKE
- ✅ How to get statistics (COUNT, AVG, GROUP BY)
- ✅ How to connect Flask to SQLite
- ✅ Always use placeholders for safety
- ✅ Always commit changes
- ✅ Always close connections

**Remember:**
- **SELECT** = Get data
- **INSERT** = Add data
- **UPDATE** = Change data
- **DELETE** = Remove data
- **WHERE** = Filter which rows

---

## 🎓 Advanced Topics (Optional)

### Multiple Tables
```sql
CREATE TABLE teachers (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE classes (
    id INTEGER PRIMARY KEY,
    student_id INTEGER,
    teacher_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (teacher_id) REFERENCES teachers(id)
);
```

### JOIN Queries
```sql
SELECT students.name, classes.subject
FROM students
JOIN classes ON students.id = classes.student_id;
```

---

**Congratulations! You now know how to work with databases!** 🎉

**You've built a complete CRUD app:**
- **C**reate (INSERT)
- **R**ead (SELECT)
- **U**pdate (UPDATE)
- **D**elete (DELETE)

**This is real web development!** 💻✨

