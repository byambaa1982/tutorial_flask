# Day 5: Flask with SQLite Database! 🗄️

# Step 1: Import what we need
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os

# Step 2: Create our app
app = Flask(__name__)

# Step 3: Database setup
DATABASE = 'students.db'

def get_db_connection():
    """
    Create a connection to the database.
    This function opens a connection to our SQLite database.
    """
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row  # This lets us access columns by name
    return conn

def init_db():
    """
    Initialize the database and create the students table if it doesn't exist.
    This function runs when the app starts.
    """
    conn = get_db_connection()
    
    # CREATE TABLE - This creates a new table in the database
    conn.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            favorite_subject TEXT NOT NULL,
            grade TEXT NOT NULL
        )
    ''')
    
    # Check if table is empty and add sample data
    cursor = conn.execute('SELECT COUNT(*) FROM students')
    count = cursor.fetchone()[0]
    
    if count == 0:
        # INSERT - Add sample students to start
        sample_students = [
            ('Alice', 12, 'Math', 'A'),
            ('Bob', 13, 'Science', 'B'),
            ('Charlie', 12, 'Art', 'A')
        ]
        
        for student in sample_students:
            conn.execute('''
                INSERT INTO students (name, age, favorite_subject, grade)
                VALUES (?, ?, ?, ?)
            ''', student)
    
    conn.commit()
    conn.close()

# Initialize database when app starts
init_db()

# Step 4: Routes
@app.route('/')
def home():
    """Main page with links to all features"""
    return render_template('home.html')

# ===== DATABASE ROUTES =====

@app.route('/students')
def students_list():
    """Show all students from the database"""
    conn = get_db_connection()
    
    # SELECT - Get all students from the database
    cursor = conn.execute('SELECT * FROM students ORDER BY name')
    students = cursor.fetchall()
    
    conn.close()
    return render_template('students_list.html', students=students)

@app.route('/students/add', methods=['GET', 'POST'])
def add_student():
    """Add a new student to the database"""
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        age = request.form.get('age')
        favorite_subject = request.form.get('favorite_subject')
        grade = request.form.get('grade')
        
        # INSERT - Add new student to database
        conn = get_db_connection()
        conn.execute('''
            INSERT INTO students (name, age, favorite_subject, grade)
            VALUES (?, ?, ?, ?)
        ''', (name, age, favorite_subject, grade))
        conn.commit()
        conn.close()
        
        # Redirect to the students list
        return redirect(url_for('students_list'))
    
    # If GET request, show the form
    return render_template('add_student.html')

@app.route('/students/<int:student_id>')
def view_student(student_id):
    """View details of a specific student"""
    conn = get_db_connection()
    
    # SELECT with WHERE - Get one specific student
    cursor = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    
    conn.close()
    
    if student is None:
        return "Student not found!", 404
    
    return render_template('view_student.html', student=student)

@app.route('/students/<int:student_id>/edit', methods=['GET', 'POST'])
def edit_student(student_id):
    """Edit a student's information"""
    conn = get_db_connection()
    
    if request.method == 'POST':
        # Get updated data from form
        name = request.form.get('name')
        age = request.form.get('age')
        favorite_subject = request.form.get('favorite_subject')
        grade = request.form.get('grade')
        
        # UPDATE - Modify existing student data
        conn.execute('''
            UPDATE students 
            SET name = ?, age = ?, favorite_subject = ?, grade = ?
            WHERE id = ?
        ''', (name, age, favorite_subject, grade, student_id))
        conn.commit()
        conn.close()
        
        return redirect(url_for('view_student', student_id=student_id))
    
    # GET request - show the form with current data
    cursor = conn.execute('SELECT * FROM students WHERE id = ?', (student_id,))
    student = cursor.fetchone()
    conn.close()
    
    if student is None:
        return "Student not found!", 404
    
    return render_template('edit_student.html', student=student)

@app.route('/students/<int:student_id>/delete', methods=['POST'])
def delete_student(student_id):
    """Delete a student from the database"""
    conn = get_db_connection()
    
    # DELETE - Remove student from database
    conn.execute('DELETE FROM students WHERE id = ?', (student_id,))
    conn.commit()
    conn.close()
    
    return redirect(url_for('students_list'))

@app.route('/students/search', methods=['GET', 'POST'])
def search_students():
    """Search for students by name or subject"""
    students = []
    search_term = ''
    
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        conn = get_db_connection()
        
        # SELECT with LIKE - Search for students
        cursor = conn.execute('''
            SELECT * FROM students 
            WHERE name LIKE ? OR favorite_subject LIKE ?
            ORDER BY name
        ''', (f'%{search_term}%', f'%{search_term}%'))
        students = cursor.fetchall()
        
        conn.close()
    
    return render_template('search_students.html', students=students, search_term=search_term)

@app.route('/stats')
def statistics():
    """Show database statistics"""
    conn = get_db_connection()
    
    # COUNT - Total number of students
    cursor = conn.execute('SELECT COUNT(*) as total FROM students')
    total_students = cursor.fetchone()['total']
    
    # Average age
    cursor = conn.execute('SELECT AVG(age) as avg_age FROM students')
    avg_age = cursor.fetchone()['avg_age']
    
    # COUNT by subject
    cursor = conn.execute('''
        SELECT favorite_subject, COUNT(*) as count 
        FROM students 
        GROUP BY favorite_subject 
        ORDER BY count DESC
    ''')
    subjects = cursor.fetchall()
    
    # COUNT by grade
    cursor = conn.execute('''
        SELECT grade, COUNT(*) as count 
        FROM students 
        GROUP BY grade 
        ORDER BY grade
    ''')
    grades = cursor.fetchall()
    
    conn.close()
    
    return render_template('statistics.html', 
                         total_students=total_students,
                         avg_age=avg_age,
                         subjects=subjects,
                         grades=grades)

# ===== OLD ROUTES FROM DAY 3 (Still work!) =====

@app.route('/greet', methods=['GET', 'POST'])
def greet():
    """Simple greeting form"""
    if request.method == 'POST':
        # Get data from the form
        name = request.form.get('name')
        return render_template('greet_result.html', user_name=name)
    # If GET request, show the form
    return render_template('greet_form.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    """Simple calculator"""
    if request.method == 'POST':
        num1 = float(request.form.get('number1'))
        num2 = float(request.form.get('number2'))
        operation = request.form.get('operation')
        
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero!"
        
        return render_template('calculator_result.html', 
                             num1=num1, num2=num2, 
                             operation=operation, result=result)
    return render_template('calculator_form.html')

@app.route('/survey', methods=['GET', 'POST'])
def survey():
    """Fun survey form"""
    if request.method == 'POST':
        name = request.form.get('name')
        favorite_color = request.form.get('color')
        favorite_food = request.form.get('food')
        hobbies = request.form.getlist('hobbies')  # Gets multiple checkboxes
        
        return render_template('survey_result.html',
                             name=name, color=favorite_color,
                             food=favorite_food, hobbies=hobbies)
    return render_template('survey_form.html')

# Step 5: Run the app
if __name__ == '__main__':
    app.run(debug=True)
