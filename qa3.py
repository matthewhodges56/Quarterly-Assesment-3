# Imports
from tkinter import *
from tkinter import ttk
import sqlite3
import random

# -- Course Questions --
# Econ questions
econ_questions = [
    {"question": "What is the basic economic problem?", "choice_a": "Scarcity", "choice_b": "Inflation", "choice_c": "Trade", "choice_d": "Technology", "correct_answer": "A", "feedback": "The basic economic problem is scarcity."}, 
    {"question": "What is GDP short for?", "choice_a": "Gross Domestic Product", "choice_b": "Global Demand Price", "choice_c": "General Domestic Production", "choice_d": "Government Development Plan", "correct_answer": "A", "feedback": "GDP stands for Gross Domestic Product."},
    {"question": "Which sector does NOT directly contribute to GDP?", "choice_a": "Households", "choice_b": "Government", "choice_c": "Exports", "choice_d": "Black Market", "correct_answer": "D", "feedback": "The black market is not counted in official GDP calculations."},
    {"question": "What is inflation?", "choice_a": "An increase in prices over time", "choice_b": "A decrease in prices over time", "choice_c": "A rise in unemployment", "choice_d": "An increase in supply", "correct_answer": "A", "feedback": "Inflation refers to an increase in prices over time."},
    {"question": "Who controls monetary policy in the United States?", "choice_a": "The Congress", "choice_b": "The Federal Reserve", "choice_c": "The President", "choice_d": "The Supreme Court", "correct_answer": "B", "feedback": "The Federal Reserve controls monetary policy in the U.S."},
    {"question": "What does a recession mean?", "choice_a": "A period of economic decline", "choice_b": "An increase in government spending", "choice_c": "A rise in prices", "choice_d": "A rapid economic growth", "correct_answer": "A", "feedback": "A recession is a period of economic decline."},
    {"question": "What is the main goal of fiscal policy?", "choice_a": "To control inflation", "choice_b": "To influence government spending and taxation", "choice_c": "To reduce prices", "choice_d": "To decrease exports", "correct_answer": "B", "feedback": "Fiscal policy is aimed at influencing government spending and taxation."},
    {"question": "What term describes the total amount of goods and services produced?", "choice_a": "GDP", "choice_b": "GNP", "choice_c": "CPI", "choice_d": "PPP", "correct_answer": "A", "feedback": "GDP measures the total production of goods and services."},
    {"question": "What does CPI stand for?", "choice_a": "Consumer Price Index", "choice_b": "Cost Price Index", "choice_c": "Currency Production Index", "choice_d": "Capital Product Index", "correct_answer": "A", "feedback": "CPI stands for Consumer Price Index."},
    {"question": "What is the main cause of demand-pull inflation?", "choice_a": "High demand for goods and services", "choice_b": "Decrease in supply", "choice_c": "Increase in production costs", "choice_d": "Lower demand", "correct_answer": "A", "feedback": "Demand-pull inflation is caused by high demand for goods and services."}
]

# Art questions
art_questions = [
    {"question": "Who painted the Mona Lisa?", "choice_a": "Michelangelo", "choice_b": "Leonardo da Vinci", "choice_c": "Raphael", "choice_d": "Donatello", "correct_answer": "B", "feedback": "Leonardo da Vinci painted the Mona Lisa."},
    {"question": "What is the name of the technique that uses light and shadow to create depth?", "choice_a": "Sfumato", "choice_b": "Chiaroscuro", "choice_c": "Fresco", "choice_d": "Pointillism", "correct_answer": "B", "feedback": "Chiaroscuro uses light and shadow to create depth."},
    {"question": "Which period came before the Renaissance?", "choice_a": "Medieval", "choice_b": "Baroque", "choice_c": "Modern", "choice_d": "Impressionism", "correct_answer": "A", "feedback": "The Medieval period came before the Renaissance."},
    {"question": "What is the Sistine Chapel famous for?", "choice_a": "Its dome", "choice_b": "Its sculptures", "choice_c": "Its ceiling paintings", "choice_d": "Its stained glass", "correct_answer": "C", "feedback": "The Sistine Chapel is famous for its ceiling paintings."},
    {"question": "Who painted 'The Starry Night'?", "choice_a": "Van Gogh", "choice_b": "Monet", "choice_c": "Picasso", "choice_d": "Dali", "correct_answer": "A", "feedback": "Vincent Van Gogh painted 'The Starry Night'."},
    {"question": "Which country is known for the Gothic architecture?", "choice_a": "Italy", "choice_b": "France", "choice_c": "Spain", "choice_d": "Germany", "correct_answer": "B", "feedback": "France is known for its Gothic architecture."},
    {"question": "What does 'Impressionism' focus on?", "choice_a": "Detailed realism", "choice_b": "Abstract shapes", "choice_c": "Light and color", "choice_d": "Historical events", "correct_answer": "C", "feedback": "Impressionism focuses on light and color."},
    {"question": "What type of art is Michelangelo's David?", "choice_a": "Painting", "choice_b": "Sculpture", "choice_c": "Mosaic", "choice_d": "Fresco", "correct_answer": "B", "feedback": "Michelangelo's David is a sculpture."},
    {"question": "What is the main characteristic of Cubism?", "choice_a": "Realism", "choice_b": "Geometric shapes", "choice_c": "Religious themes", "choice_d": "Nature focus", "correct_answer": "B", "feedback": "Cubism uses geometric shapes to depict subjects."},
    {"question": "Who is known for the Surrealism art movement?", "choice_a": "Salvador Dali", "choice_b": "Claude Monet", "choice_c": "Georgia O'Keeffe", "choice_d": "Andy Warhol", "correct_answer": "A", "feedback": "Salvador Dali is known for Surrealism."}
]

# Statistics questions
statistics_questions = [
    {"question": "What is the mean?", "choice_a": "Most frequent value", "choice_b": "Sum divided by number of values", "choice_c": "Middle value", "choice_d": "Range of values", "correct_answer": "B", "feedback": "The mean is the sum divided by the number of values."},
    {"question": "What is the median?", "choice_a": "Most frequent value", "choice_b": "Sum of all values", "choice_c": "Middle value", "choice_d": "Largest value", "correct_answer": "C", "feedback": "The median is the middle value in a dataset."},
    {"question": "What does probability measure?", "choice_a": "The likelihood of an event", "choice_b": "The frequency of events", "choice_c": "The size of an event", "choice_d": "The cost of an event", "correct_answer": "A", "feedback": "Probability measures the likelihood of an event."},
    {"question": "What is a sample?", "choice_a": "All members of a group", "choice_b": "A subset of a population", "choice_c": "The largest value", "choice_d": "A random event", "correct_answer": "B", "feedback": "A sample is a subset of a population."},
    {"question": "What is a histogram used for?", "choice_a": "Showing categories", "choice_b": "Showing data distribution", "choice_c": "Measuring probability", "choice_d": "Finding mean values", "correct_answer": "B", "feedback": "A histogram shows data distribution."},
    {"question": "What does standard deviation measure?", "choice_a": "The center of data", "choice_b": "The spread of data", "choice_c": "The total number of values", "choice_d": "The highest value", "correct_answer": "B", "feedback": "Standard deviation measures the spread of data."},
    {"question": "What is the mode?", "choice_a": "Middle value", "choice_b": "Most frequent value", "choice_c": "Sum of values", "choice_d": "Largest value", "correct_answer": "B", "feedback": "The mode is the most frequent value."},
    {"question": "What is a frequency table?", "choice_a": "A table of percentages", "choice_b": "A chart of means", "choice_c": "A count of occurrences", "choice_d": "A probability table", "correct_answer": "C", "feedback": "A frequency table shows the count of occurrences."},
    {"question": "What is a population?", "choice_a": "Sample of data", "choice_b": "Subset of a sample", "choice_c": "Entire group being studied", "choice_d": "One data value", "correct_answer": "C", "feedback": "A population is the entire group being studied."},
    {"question": "What is correlation?", "choice_a": "Relationship between variables", "choice_b": "Difference between values", "choice_c": "Sum of values", "choice_d": "Total frequency", "correct_answer": "A", "feedback": "Correlation shows the relationship between variables."}
]

# Business Database Management questions
business_database_management_questions = [
    {"question": "What is a database?", "choice_a": "A software program", "choice_b": "An organized collection of data", "choice_c": "A single table", "choice_d": "A type of algorithm", "correct_answer": "B", "feedback": "A database is an organized collection of data."},
    {"question": "What is SQL used for?", "choice_a": "Designing websites", "choice_b": "Querying databases", "choice_c": "Editing videos", "choice_d": "Analyzing images", "correct_answer": "B", "feedback": "SQL is used for querying databases."},
    {"question": "What is a primary key?", "choice_a": "A key for encrypting data", "choice_b": "A unique identifier for a record", "choice_c": "A column with duplicates", "choice_d": "An error code", "correct_answer": "B", "feedback": "A primary key uniquely identifies each record."},
    {"question": "What does 'CRUD' stand for?", "choice_a": "Create, Read, Update, Delete", "choice_b": "Copy, Rewrite, Upload, Download", "choice_c": "Create, Retrieve, Use, Display", "choice_d": "Control, Run, Update, Delete", "correct_answer": "A", "feedback": "CRUD stands for Create, Read, Update, Delete."},
    {"question": "What is a table in a database?", "choice_a": "A list of files", "choice_b": "A collection of rows and columns", "choice_c": "A summary of data", "choice_d": "An error log", "correct_answer": "B", "feedback": "A table is a collection of rows and columns in a database."},
    {"question": "What is a foreign key?", "choice_a": "A unique identifier", "choice_b": "A key in another table", "choice_c": "An encrypted code", "choice_d": "A duplicate value", "correct_answer": "B", "feedback": "A foreign key is a key that links to another table."},
    {"question": "What does 'JOIN' do in SQL?", "choice_a": "Combines rows from tables", "choice_b": "Creates a new table", "choice_c": "Deletes records", "choice_d": "Encrypts data", "correct_answer": "A", "feedback": "JOIN combines rows from tables."},
    {"question": "What is a relational database?", "choice_a": "A network of tables", "choice_b": "A flat file system", "choice_c": "A set of spreadsheets", "choice_d": "A non-digital archive", "correct_answer": "A", "feedback": "A relational database organizes data in tables related to each other."},
    {"question": "What is a database schema?", "choice_a": "A query result", "choice_b": "The structure of a database", "choice_c": "A type of SQL command", "choice_d": "A database backup", "correct_answer": "B", "feedback": "A schema defines the structure of a database."},
    {"question": "What is normalization?", "choice_a": "Organizing data to reduce redundancy", "choice_b": "Encrypting data", "choice_c": "Summarizing data", "choice_d": "Deleting duplicates", "correct_answer": "A", "feedback": "Normalization organizes data to reduce redundancy."}
]

# Business Organizational Behavior questions
business_organizational_behavior_questions = [
    {"question": "What is organizational behavior?", "choice_a": "Study of individuals in organizations", "choice_b": "Analyzing market trends", "choice_c": "Company budgeting", "choice_d": "Training employees", "correct_answer": "A", "feedback": "Organizational behavior studies individuals in organizations."},
    {"question": "What is motivation?", "choice_a": "Financial incentives", "choice_b": "Internal drive to achieve goals", "choice_c": "Company training", "choice_d": "Supervision style", "correct_answer": "B", "feedback": "Motivation is the internal drive to achieve goals."},
    {"question": "What does a manager do?", "choice_a": "Only hires employees", "choice_b": "Sets goals, organizes, and leads", "choice_c": "Only monitors tasks", "choice_d": "Only deals with finances", "correct_answer": "B", "feedback": "A manager sets goals, organizes, and leads teams."},
    {"question": "What is corporate culture?", "choice_a": "Workplace norms and values", "choice_b": "Company's annual revenue", "choice_c": "Office layout", "choice_d": "Product strategy", "correct_answer": "A", "feedback": "Corporate culture includes workplace norms and values."},
    {"question": "What is teamwork?", "choice_a": "Employees competing", "choice_b": "Collaboration to achieve goals", "choice_c": "Only managers working together", "choice_d": "Following individual tasks", "correct_answer": "B", "feedback": "Teamwork is collaboration to achieve goals."},
    {"question": "What is leadership?", "choice_a": "Directing others toward goals", "choice_b": "Only enforcing rules", "choice_c": "Punishing employees", "choice_d": "Completing tasks independently", "correct_answer": "A", "feedback": "Leadership is directing others toward goals."},
    {"question": "What is a conflict in an organization?", "choice_a": "Agreement among employees", "choice_b": "Disagreement or clash of interests", "choice_c": "Employee promotion", "choice_d": "Salary increase", "correct_answer": "B", "feedback": "Conflict is a disagreement or clash of interests."},
    {"question": "What is a group?", "choice_a": "Only employees in one department", "choice_b": "Two or more people working together", "choice_c": "Individual employees", "choice_d": "Management only", "correct_answer": "B", "feedback": "A group consists of two or more people working together."},
    {"question": "What is job satisfaction?", "choice_a": "Employee's feeling about their job", "choice_b": "Workload level", "choice_c": "Company revenue", "choice_d": "Employee's pay", "correct_answer": "A", "feedback": "Job satisfaction is an employee's feeling about their job."},
    {"question": "What is a formal group?", "choice_a": "An official group within an organization", "choice_b": "A casual team meeting", "choice_c": "Temporary employees", "choice_d": "A non-productive team", "correct_answer": "A", "feedback": "A formal group is an official group within an organization."}
]
# -- Course Questions --

class QuestionDisplay:
    def __init__(self, parent, questions):
        self.parent = parent
        self.questions = questions
        self.currentQuestion = 0
        self.correctAnswers = 0

        # Label for question
        self.questionLabel = Label(parent, text="", font=("Arial", 12), wraplength=400)
        self.questionLabel.place(x=50, y=30)

        self.answerVar = StringVar()

        # Radio buttons for choices
        self.choice_a = Radiobutton(parent, text="", variable=self.answerVar, value="A", font=("Arial", 10), tristatevalue="x")
        self.choice_a.place(x=70, y=100)

        self.choice_b = Radiobutton(parent, text="", variable=self.answerVar, value="B", font=("Arial", 10), tristatevalue="x")
        self.choice_b.place(x=70, y=140)

        self.choice_c = Radiobutton(parent, text="", variable=self.answerVar, value="C", font=("Arial", 10), tristatevalue="x")
        self.choice_c.place(x=70, y=180)

        self.choice_d = Radiobutton(parent, text="", variable=self.answerVar, value="D", font=("Arial", 10), tristatevalue="x")
        self.choice_d.place(x=70, y=220)

        # Label for feedback
        self.feedbackLabel = Label(parent, text="", font=("Arial", 10), wraplength=400, fg="green")
        self.feedbackLabel.place(x=50, y=260)

        # Submit answer button (ttk.button is so much better)
        self.submitButton = ttk.Button(parent, text="Submit Answer", command=self.submitAnswer, takefocus=False)
        self.submitButton.place(x=180, y=310)

        # Call load question method
        self.loadQuestion()

    def loadQuestion(self):
        # Get the current question
        questionData = self.questions[self.currentQuestion]

        # Setup question and options
        self.questionLabel.config(text=questionData["question"])
        self.choice_a.config(text=f"A. {questionData['choice_a']}")
        self.choice_b.config(text=f"B. {questionData['choice_b']}")
        self.choice_c.config(text=f"C. {questionData['choice_c']}")
        self.choice_d.config(text=f"D. {questionData['choice_d']}")

        # Reset answer selection
        self.answerVar.set("")
        self.feedbackLabel.config(text="")

    def submitAnswer(self):
        selectedAnswer = self.answerVar.get()
        
        # Check if no answer is selected
        if not selectedAnswer:
            self.feedbackLabel.config(text="Please select an answer before submitting.", fg="red")
            return 

        correctAnswer = self.questions[self.currentQuestion]["correct_answer"]

        # Check if the answer is correct and give feedback
        if selectedAnswer == correctAnswer:
            self.feedbackLabel.config(text="Correct! " + self.questions[self.currentQuestion]["feedback"], fg="green")
            self.correctAnswers += 1
        else:
            self.feedbackLabel.config(text="Incorrect. " + self.questions[self.currentQuestion]["feedback"], fg="red")

        # Move to the next question after a brief delay
        self.parent.after(2000, self.nextQuestion)

    def nextQuestion(self):
        # Check if there are more questions
        self.currentQuestion += 1

        if self.currentQuestion < len(self.questions):
            self.loadQuestion()
        else:
            self.showFinalScore()

    def showFinalScore(self):
        self.questionLabel.config(text=f"You answered {self.correctAnswers} out of {len(self.questions)} questions correctly!")
        self.choice_a.place_forget()
        self.choice_b.place_forget()
        self.choice_c.place_forget()
        self.choice_d.place_forget()
        self.submitButton.place_forget()
        self.feedbackLabel.config(text="")

        # Close the quiz window after displaying the score (2 seconds)
        self.parent.after(2000, self.closeQuizWindow)

    def closeQuizWindow(self):
        # Close the quiz window 
        self.parent.destroy()  

# Database Setup 
conn = sqlite3.connect("quiz_bowl.db")
c = conn.cursor()

# Database functions
def createCourseTable(course):
    c.execute(f"""
    CREATE TABLE IF NOT EXISTS {course} (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT NOT NULL,
        choice_a TEXT NOT NULL,
        choice_b TEXT NOT NULL,
        choice_c TEXT NOT NULL,
        choice_d TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        feedback TEXT NOT NULL
    )
    """)

# Function to add a question to a course
def addQuestion(table_name, questionData):
    c.execute(f"""
        INSERT INTO {table_name} (question, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        questionData["question"], 
        questionData["choice_a"], 
        questionData["choice_b"], 
        questionData["choice_c"], 
        questionData["choice_d"], 
        questionData["correct_answer"], 
        questionData["feedback"]
    ))
    conn.commit()

def removeQuestion(course, questionID):
    c.execute(f"DELETE FROM {course} WHERE id = ?", (questionID,))
    conn.commit()

def getQuestions(course):
    c.execute(f"SELECT * FROM {course}")
    questions = c.fetchall()
    
    # Print each question's details
    for question in questions:
        print(f"ID: {question[0]}")
        print(f"Question: {question[1]}")
        print(f"A: {question[2]}")
        print(f"B: {question[3]}")
        print(f"C: {question[4]}")
        print(f"D: {question[5]}")
        print(f"Correct Answer: {question[6]}")
        print(f"Feedback: {question[7]}")

        # Readability!
        print("="*30)  
    
    return questions

# Loop to create tables for each course
courses = ["econ", "art", "statistics", "business_database_management", "business_organizational_behavior"]
for course in courses:
    createCourseTable(course)

# Dictionary to map each subject list to its corresponding table name
subject_tables = {
    "econ": econ_questions,
    "art": art_questions,
    "statistics": statistics_questions,
    "business_database_management": business_database_management_questions,
    "business_organizational_behavior": business_organizational_behavior_questions
}

# Loop through each subject and its list of questions, then add each question to the database
for table_name, questions_list in subject_tables.items():
    for questionData in questions_list:
        addQuestion(table_name, questionData)

# Setup tkinter and basic window elements
root = Tk()
root.geometry("500x350")
root.title("Quiz")
root.resizable(False, False)

# Label for dropdown box
categoryLabel = ttk.Label(root, text="Select Your Category", font=("Arial", 14))
categoryLabel.place(relx=0.5, rely=0.4, anchor='center')

# List for courses (with formal names)
categories = ["Economics", "Art", "Statistics", "Business Database Mgmt", "Business Org Behavior"]

# Category dropdown box, also made it read only
categoryDropdown = ttk.Combobox(root, values=categories, font=("Arial", 12), state="readonly", width=20)
# Default text for the dropdown
categoryDropdown.set("Select Category")  
categoryDropdown.place(relx=0.5, rely=0.5, anchor='center')

# Start quiz button function
def startQuiz():
    # If user doesn't select a category, show error
    if categoryDropdown.get() == "Select Category":
        errorLabel.config(text="Please select a category.", foreground="red")
    else:
        # Clear the error message if a valid category is selected
        errorLabel.config(text="")

        # Map dropdown selection to table name
        subjects = {
            "Economics": "econ",
            "Art": "art",
            "Statistics": "statistics",
            "Business Database Mgmt": "business_database_management",
            "Business Org Behavior": "business_organizational_behavior"
        }
        selectedCategory = subjects[categoryDropdown.get()]

        # Fetch all 10 questions from the selected table
        c.execute(f"SELECT question, choice_a, choice_b, choice_c, choice_d, correct_answer, feedback FROM {selectedCategory} LIMIT 10")
        questions = [{"question": row[0], "choice_a": row[1], "choice_b": row[2], "choice_c": row[3], "choice_d": row[4], "correct_answer": row[5], "feedback": row[6]} for row in c.fetchall()]

        # Shuffle questions to randomize order
        random.shuffle(questions)

        # Create a new window for the quiz
        quizWindow = Toplevel()
        quizWindow.geometry("500x400")
        # Dynamic title
        quizWindow.title(f"{categoryDropdown.get()} Quiz")

        # Initialize class with the quiz window and questions
        QuestionDisplay(quizWindow, questions)

# Label for error
errorLabel = ttk.Label(root, text="", font=("Arial", 10))
errorLabel.place(relx=0.5, rely=0.75, anchor='center')

# Start quiz button
startButton = ttk.Button(root, text="Start Quiz", takefocus=False, command=startQuiz)
startButton.place(relx=0.5, rely=0.65, anchor='center')

# Open the window
root.mainloop()

# Close the database connection
conn.close()

# cant lie this took me a while, i think i made it way more complicated than it needs to be....
# ↓↓↓↓↓ not sure what this means ↓↓↓↓↓
# "Your GitHub folder should include a way for you to add/remove/read current
#  questions from the database in the back end."
# SO i just added functions for that? i dont use all but they are there