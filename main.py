from fastapi import FastAPI
import json

app = FastAPI()

# Global variable to hold the student data
global data
with open('./data.json') as f:
    data = json.load(f)

# --- TASK ROUTES ---

@app.get('/')
async def hello_world():
    return 'Hello, World!'

@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref:
                filtered_students.append(student)
        return filtered_students
    return data

@app.get('/students/{id}')
async def get_student(id):
    for student in data: 
        if student['id'] == id:
            return student
    return {"error": "Student not found"}

# --- EXERCISE 1: Statistics ---

@app.get('/stats')
async def get_stats():
    stats = {}
    for student in data:
        # Count Meal Preferences
        meal = student.get('pref')
        if meal:
            stats[meal] = stats.get(meal, 0) + 1
        
        # Count Programmes
        programme = student.get('programme')
        if programme:
            stats[programme] = stats.get(programme, 0) + 1
            
    return stats

# --- EXERCISE 2: Calculator ---

@app.get('/add/{a}/{b}')
async def add(a: float, b: float):
    return a + b

@app.get('/subtract/{a}/{b}')
async def subtract(a: float, b: float):
    return a - b

@app.get('/multiply/{a}/{b}')
async def multiply(a: float, b: float):
    return a * b

@app.get('/divide/{a}/{b}')
async def divide(a: float, b: float):
    if b == 0:
        return {"error": "Cannot divide by zero"}
    return a / b