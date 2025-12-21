# 🗄️ Day 5 Tasks & Challenges

Complete these tasks to master SQL and databases! Work through them in order and become a database expert! 🚀

---

## ⭐ Task 1: Add Your First Student (EASY)

**Goal:** Practice using INSERT to add data!

**What to do:**
1. Run the app: `python app.py`
2. Go to http://127.0.0.1:5000/students/add
3. Add yourself to the database:
   - Your name
   - Your age
   - Your favorite subject
   - Your grade

**SQL you're using:**
```sql
INSERT INTO students (name, age, favorite_subject, grade)
VALUES (?, ?, ?, ?)
```

**Success:** You appear in the students list! ✅

---

## ⭐ Task 2: Find the SQL Code (EASY)

**Goal:** Understand where SQL happens in the code!

**What to do:**
1. Open `app.py`
2. Find these SQL commands:
   - `CREATE TABLE` - Where is the table created?
   - `INSERT` - Where do we add students?
   - `SELECT *` - Where do we get all students?
   - `UPDATE` - Where do we change student data?
   - `DELETE` - Where do we remove students?

**Challenge:** Write down the line numbers for each one!

**Success:** You found all 5 SQL commands! ✅

---

## ⭐ Task 3: View and Edit (EASY)

**Goal:** Practice SELECT and UPDATE!

**What to do:**
1. Click on a student to view their details
2. Click "Edit"
3. Change their favorite subject
4. Save

**SQL you're using:**
```sql
-- View
SELECT * FROM students WHERE id = ?

-- Edit
UPDATE students 
SET name = ?, age = ?, favorite_subject = ?, grade = ?
WHERE id = ?
```

**Success:** Student's subject changed! ✅

---

## ⭐⭐ Task 4: Search Like a Pro (MEDIUM)

**Goal:** Master the LIKE operator!

**What to do:**
1. Go to the search page
2. Try these searches:
   - Search for "Al" - finds Alice, Alicia, etc.
   - Search for "Math" - finds students who like Math
   - Search for "a" - finds anyone with 'a' in name or subject

**SQL you're using:**
```sql
SELECT * FROM students 
WHERE name LIKE '%search%' OR favorite_subject LIKE '%search%'
```

**Challenge:** What does `%` mean in SQL?

**Success:** You understand pattern matching! ✅

---

## ⭐⭐ Task 5: Add a Teacher Field (MEDIUM)

**Goal:** Modify the database structure!

**What to do:**

**Step 1:** Stop the app (Ctrl+C)

**Step 2:** Delete the old database:
```bash
del students.db    # Windows
rm students.db     # Mac/Linux
```

**Step 3:** Modify `init_db()` in `app.py`:

Find this:
```python
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    favorite_subject TEXT NOT NULL,
    grade TEXT NOT NULL
)
```

Change to:
```python
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    favorite_subject TEXT NOT NULL,
    grade TEXT NOT NULL,
    teacher TEXT NOT NULL
)
```

**Step 4:** Update the INSERT in `init_db()`:
```python
sample_students = [
    ('Alice', 12, 'Math', 'A', 'Mr. Smith'),
    ('Bob', 13, 'Science', 'B', 'Ms. Johnson'),
    ('Charlie', 12, 'Art', 'A', 'Mrs. Davis')
]

conn.execute('''
    INSERT INTO students (name, age, favorite_subject, grade, teacher)
    VALUES (?, ?, ?, ?, ?)
''', student)
```

**Step 5:** Update `add_student()` route to include teacher field

**Step 6:** Update templates to show and input teacher

**Success:** Database has a teacher field! ✅

---

## ⭐⭐ Task 6: Count Students by Grade (MEDIUM)

**Goal:** Practice GROUP BY and COUNT!

**What to do:**

Add this code to your `statistics()` function in `app.py`:

```python
# Count students by grade
cursor = conn.execute('''
    SELECT grade, COUNT(*) as count 
    FROM students 
    GROUP BY grade 
    ORDER BY grade
''')
grades = cursor.fetchall()
```

**SQL Explained:**
- `COUNT(*)` = Count all rows in each group
- `GROUP BY grade` = Make groups by grade (A, B, C, etc.)
- `as count` = Name the count column "count"

**Challenge:** Modify to show highest grade first (ORDER BY grade DESC)

**Success:** You can count by category! ✅

---

## ⭐⭐⭐ Task 7: Add Age Filter (HARD)

**Goal:** Add filtering to the students list!

**What to do:**

**Step 1:** Modify `students_list` route:

```python
@app.route('/students')
def students_list():
    min_age = request.args.get('min_age', type=int)
    
    conn = get_db_connection()
    
    if min_age:
        # Filter by age
        cursor = conn.execute('''
            SELECT * FROM students 
            WHERE age >= ? 
            ORDER BY name
        ''', (min_age,))
    else:
        # No filter - get all
        cursor = conn.execute('SELECT * FROM students ORDER BY name')
    
    students = cursor.fetchall()
    conn.close()
    
    return render_template('students_list.html', students=students)
```

**Step 2:** Add filter form to `students_list.html`:

```html
<form method="GET">
    <label for="min_age">Minimum Age:</label>
    <input type="number" id="min_age" name="min_age" min="5" max="18">
    <button type="submit">Filter</button>
    <a href="{{ url_for('students_list') }}">Clear Filter</a>
</form>
```

**Success:** You can filter by age! ✅

---

## ⭐⭐⭐ Task 8: Create a Subjects Table (HARD)

**Goal:** Work with multiple tables!

**What to do:**

**Step 1:** Add a new table in `init_db()`:

```python
# Create subjects table
conn.execute('''
    CREATE TABLE IF NOT EXISTS subjects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        description TEXT NOT NULL
    )
''')

# Add sample subjects
subjects_data = [
    ('Math', 'Numbers, algebra, geometry'),
    ('Science', 'Biology, chemistry, physics'),
    ('Art', 'Drawing, painting, sculpture'),
    ('History', 'World events and cultures'),
    ('English', 'Reading, writing, literature')
]

# Check if empty
cursor = conn.execute('SELECT COUNT(*) FROM subjects')
if cursor.fetchone()[0] == 0:
    for subject in subjects_data:
        conn.execute('''
            INSERT INTO subjects (name, description)
            VALUES (?, ?)
        ''', subject)
```

**Step 2:** Create route to list subjects:

```python
@app.route('/subjects')
def subjects_list():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM subjects ORDER BY name')
    subjects = cursor.fetchall()
    conn.close()
    return render_template('subjects_list.html', subjects=subjects)
```

**Step 3:** Create `subjects_list.html` template

**Success:** You have multiple tables! ✅

---

## ⭐⭐⭐⭐ Task 9: Advanced Statistics (EXPERT)

**Goal:** Master aggregate functions!

**What to do:**

Add these queries to your statistics page:

**1. Oldest and Youngest Student:**
```python
cursor = conn.execute('SELECT MAX(age) as oldest, MIN(age) as youngest FROM students')
ages = cursor.fetchone()
```

**2. Students per Subject (with percentage):**
```python
cursor = conn.execute('''
    SELECT favorite_subject, 
           COUNT(*) as count,
           ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students), 2) as percentage
    FROM students 
    GROUP BY favorite_subject 
    ORDER BY count DESC
''')
subjects_stats = cursor.fetchall()
```

**3. Grade Distribution:**
```python
cursor = conn.execute('''
    SELECT 
        grade,
        COUNT(*) as count,
        ROUND(AVG(age), 1) as avg_age
    FROM students 
    GROUP BY grade 
    ORDER BY grade
''')
grade_stats = cursor.fetchall()
```

**Success:** You're a SQL statistics expert! ✅

---

## 🏆 Bonus Challenges (Super Expert!)

### Challenge A: Add Sorting to Students List

Allow users to sort by name, age, or grade!

```python
@app.route('/students')
def students_list():
    sort_by = request.args.get('sort', 'name')  # default: name
    
    # Validate sort column (security!)
    allowed_sorts = ['name', 'age', 'grade', 'favorite_subject']
    if sort_by not in allowed_sorts:
        sort_by = 'name'
    
    conn = get_db_connection()
    query = f'SELECT * FROM students ORDER BY {sort_by}'
    cursor = conn.execute(query)
    students = cursor.fetchall()
    conn.close()
    
    return render_template('students_list.html', students=students)
```

Add links in template:
```html
<a href="?sort=name">Sort by Name</a> |
<a href="?sort=age">Sort by Age</a> |
<a href="?sort=grade">Sort by Grade</a>
```

---

### Challenge B: Pagination

Show only 10 students per page!

```python
@app.route('/students')
def students_list():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    offset = (page - 1) * per_page
    
    conn = get_db_connection()
    
    # Get total count
    cursor = conn.execute('SELECT COUNT(*) FROM students')
    total = cursor.fetchone()[0]
    
    # Get paginated results
    cursor = conn.execute('''
        SELECT * FROM students 
        ORDER BY name 
        LIMIT ? OFFSET ?
    ''', (per_page, offset))
    students = cursor.fetchall()
    
    conn.close()
    
    total_pages = (total + per_page - 1) // per_page
    
    return render_template('students_list.html', 
                         students=students,
                         page=page,
                         total_pages=total_pages)
```

---

### Challenge C: Export to CSV

Download student data as a CSV file!

```python
import csv
from flask import make_response

@app.route('/students/export')
def export_students():
    conn = get_db_connection()
    cursor = conn.execute('SELECT * FROM students ORDER BY name')
    students = cursor.fetchall()
    conn.close()
    
    # Create CSV
    output = []
    output.append('ID,Name,Age,Favorite Subject,Grade\n')
    
    for student in students:
        output.append(f"{student['id']},{student['name']},{student['age']},{student['favorite_subject']},{student['grade']}\n")
    
    response = make_response(''.join(output))
    response.headers['Content-Type'] = 'text/csv'
    response.headers['Content-Disposition'] = 'attachment; filename=students.csv'
    
    return response
```

---

### Challenge D: Bulk Delete

Delete multiple students at once with checkboxes!

**Template:**
```html
<form method="POST" action="{{ url_for('bulk_delete') }}">
    {% for student in students %}
    <input type="checkbox" name="student_ids" value="{{ student['id'] }}">
    {{ student['name'] }}<br>
    {% endfor %}
    <button type="submit">Delete Selected</button>
</form>
```

**Route:**
```python
@app.route('/students/bulk-delete', methods=['POST'])
def bulk_delete():
    student_ids = request.form.getlist('student_ids')
    
    conn = get_db_connection()
    for student_id in student_ids:
        conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('students_list'))
```

---

### Challenge E: Add Student Photo URLs

Add a column for photo URLs!

```sql
ALTER TABLE students ADD COLUMN photo_url TEXT;
```

Then show photos in the template:
```html
{% if student['photo_url'] %}
    <img src="{{ student['photo_url'] }}" alt="{{ student['name'] }}" width="100">
{% else %}
    <p>No photo</p>
{% endif %}
```

---

## 📊 Task Tracker

Check off each task as you complete it:

- [ ] Task 1: Added your first student
- [ ] Task 2: Found all SQL commands
- [ ] Task 3: Viewed and edited a student
- [ ] Task 4: Searched with LIKE
- [ ] Task 5: Added teacher field
- [ ] Task 6: Counted by grade
- [ ] Task 7: Added age filter
- [ ] Task 8: Created subjects table
- [ ] Task 9: Advanced statistics
- [ ] Bonus A: Sorting
- [ ] Bonus B: Pagination
- [ ] Bonus C: CSV export
- [ ] Bonus D: Bulk delete
- [ ] Bonus E: Photo URLs

---

## 📖 SQL Quick Reference

### Basic Commands
```sql
-- Create table
CREATE TABLE table_name (column1 TYPE, column2 TYPE);

-- Insert data
INSERT INTO table_name (col1, col2) VALUES (val1, val2);

-- Select all
SELECT * FROM table_name;

-- Select specific columns
SELECT col1, col2 FROM table_name;

-- Filter
SELECT * FROM table_name WHERE condition;

-- Update
UPDATE table_name SET col1 = val1 WHERE condition;

-- Delete
DELETE FROM table_name WHERE condition;
```

### WHERE Conditions
```sql
WHERE age = 12                 -- Exact match
WHERE age > 12                 -- Greater than
WHERE age >= 12                -- Greater or equal
WHERE age < 12                 -- Less than
WHERE age != 12                -- Not equal
WHERE name LIKE '%Al%'         -- Contains "Al"
WHERE name LIKE 'Al%'          -- Starts with "Al"
WHERE name LIKE '%ice'         -- Ends with "ice"
WHERE age BETWEEN 10 AND 15    -- Range
WHERE grade IN ('A', 'B')      -- In list
WHERE name IS NULL             -- Empty value
WHERE name IS NOT NULL         -- Not empty
```

### Aggregate Functions
```sql
COUNT(*)                       -- Count rows
COUNT(DISTINCT grade)          -- Count unique values
SUM(age)                       -- Add all ages
AVG(age)                       -- Average age
MAX(age)                       -- Highest age
MIN(age)                       -- Lowest age
```

### Grouping & Ordering
```sql
GROUP BY grade                 -- Group by grade
HAVING COUNT(*) > 5            -- Filter groups (use with GROUP BY)
ORDER BY name                  -- Sort ascending
ORDER BY age DESC              -- Sort descending
LIMIT 10                       -- First 10 rows
LIMIT 10 OFFSET 20             -- Rows 21-30 (pagination)
```

### Combining Conditions
```sql
WHERE age > 12 AND grade = 'A'         -- Both conditions
WHERE name = 'Alice' OR name = 'Bob'   -- Either condition
WHERE NOT (age < 10)                   -- Opposite condition
WHERE (age > 15 OR grade = 'A') AND name LIKE 'A%'  -- Complex
```

---

## 🎯 What You've Learned

By completing these tasks, you now know:
- ✅ How to CREATE tables
- ✅ How to INSERT data
- ✅ How to SELECT data (all, specific, filtered)
- ✅ How to UPDATE existing data
- ✅ How to DELETE data
- ✅ How to use WHERE to filter
- ✅ How to use LIKE for searching
- ✅ How to use COUNT, AVG, MAX, MIN
- ✅ How to use GROUP BY for statistics
- ✅ How to ORDER results
- ✅ How placeholders (?) keep queries safe
- ✅ Why you must COMMIT changes
- ✅ Real SQL that works in any database!

**You're now a database developer!** 🎉🗄️

---

## 🔐 Security Tips

**Always use placeholders:**
```python
# ✅ SAFE
cursor.execute('SELECT * FROM students WHERE name = ?', (name,))

# ❌ DANGEROUS - SQL Injection risk!
cursor.execute(f"SELECT * FROM students WHERE name = '{name}'")
```

**Why?** If someone enters `'; DROP TABLE students; --` as their name, the second version would delete your entire table!

**Placeholders protect you from:**
- SQL injection attacks
- Quote/apostrophe issues
- Special characters breaking queries

**Always validate user input:**
```python
allowed_sorts = ['name', 'age', 'grade']
if sort_by not in allowed_sorts:
    sort_by = 'name'  # Default safe value
```

---

## 💡 Debugging Tips

**Query not working?**
- Print the SQL to see what it looks like
- Check for typos in table/column names
- Make sure placeholders match values

**Data not saving?**
- Did you call `conn.commit()`?
- Check terminal for error messages

**Table doesn't exist?**
- Delete `students.db` and restart
- Check `CREATE TABLE` syntax

**Wrong results?**
- Print `students` to see raw data
- Check your WHERE conditions
- Use ORDER BY to see results clearly

**Want to see the database?**
Install DB Browser for SQLite (free tool) to view your database visually!

---

**Keep learning and building amazing database-powered apps!** 💻✨🗄️
