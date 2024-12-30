# remember always to check new columns are generated correctly


import sqlite3
from prettytable import PrettyTable
from tkinter import *
from tkcalendar import Calendar
from tkcalendar import DateEntry
import time
from tkinter import messagebox
import prettytable
from tkinter import ttk  # This imports the ttk module
import tkinter as tk
from tkinter import Toplevel

import sqlite3

from reportlab.lib.pagesizes import letter
from tkinter import filedialog
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkinter import filedialog, messagebox

current_rowid = None  # Global or class-level variable


# Establish a database connection to gracehealth.db
conn = sqlite3.connect('gracehealth.db')
cursor = conn.cursor()
import sqlite3

import sqlite3

def create_student_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("gracehealth.db")
    cursor = conn.cursor()

    # Create the student table with the specified columns
    create_table_query = """
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        date_of_birth TEXT,
        Gender TEXT,
        Class_section TEXT,
        Roll_no INTEGER,
        Aadhaar_No INTEGER,
        Father_or_guardian_name TEXT,
        mother_name TEXT,
        contact_number INTEGER,
        Address TEXT,
        email TEXT,
        Name_teacher TEXT,
        school_name TEXT,
        last_school_name TEXT NOT NULL,
        place_of_birth TEXT NOT NULL,
        known_earlier_disease TEXT NOT NULL,
        covid_vacc_number INTEGER,
        covd_vacc_last_date TEXT,
        weight INTEGER,
        height INTEGER,
        BMI TEXT,
        Vision_both TEXT,
        VISON_left INTEGER,
        VISON_right INTEGER,
        VISION_problem TEXT,
        B1_severe_anemia TEXT,
        B2_Vita_A_deficiency TEXT,
        B3_Vit_D_deficiency TEXT,
        B4_Goitre TEXT,
        B5_Oedema TEXT,
        C1_convulsive_dis TEXT,
        C2_otitis_media TEXT,
        C3_dental_condition TEXT,
        C4_skin_condition TEXT,
        C5_rheumatic_heart_disease TEXT,
        C6_others_TB_asthma TEXT,
        D1_difficulty_seeing TEXT,
        D2_delay_in_walking TEXT,
        D3_stiffness_floppiness TEXT,
        D5_reading_writing_calculatory_difficulty TEXT,
        D6_speaking_difficulty TEXT,
        D7_hearing_problems TEXT,
        D8_learning TEXT,
        D9_attention TEXT,
        E3_depression_sleep TEXT,
        E4_Menarke TEXT,
        E5_regularity_period_difficulties TEXT,
        E6_UTI_STI TEXT,
        E7 TEXT,
        E8_menstrual_pain TEXT,
        E9_remarks TEXT,
        BMI_category TEXT,
        weight_age TEXT,
        length_age TEXT,
        weight_height TEXT,
        age_in_month INTEGER,
        deworming TEXT,
        vaccination TEXT,
        covid TEXT,
        tea_garden TEXT,
        screen_date TEXT,
        age_screening TEXT,
        status TEXT DEFAULT 'active',
        muac INTEGER,
        muac_sam TEXT
    );
    """

    # Execute the query
    cursor.execute(create_table_query)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    print("Table 'student' created successfully in gracehealth.db")

# Call the function to create the table
create_student_table()



def add_status_column():
    """
    Alter the 'student' table to add a 'status' column if it doesn't already exist.
    """
    try:
        # Check if the 'status' column already exists
        cursor.execute("PRAGMA table_info(student);")
        columns = cursor.fetchall()

        # Look for the 'status' column
        column_names = [column[1] for column in columns]

        if 'status' not in column_names:
            # Alter the table to add the 'status' column
            cursor.execute("""
                ALTER TABLE student
                ADD COLUMN status TEXT DEFAULT 'active';
            """)

            # Commit the changes to the database
            conn.commit()




    except Exception as e:
        # Handle any errors during the table alteration process
        messagebox.showerror("Error", f"Failed to add 'status' column: {e}")
        conn.rollback()


# Call the function to add the status column
add_status_column()

def add_muac_column():
    """
    Alter the 'student' table to add a 'status' column if it doesn't already exist.
    """
    try:
        # Check if the 'status' column already exists
        cursor.execute("PRAGMA table_info(student);")
        columns = cursor.fetchall()

        # Look for the 'status' column
        column_names = [column[1] for column in columns]

        if 'muac' not in column_names:
            # Alter the table to add the 'status' column
            cursor.execute("""
                ALTER TABLE student
                ADD COLUMN muac INTEGER
            """)

            # Commit the changes to the database
            conn.commit()




    except Exception as e:
        # Handle any errors during the table alteration process
        messagebox.showerror("Error", f"Failed to add 'muac' column: {e}")
        conn.rollback()


# Call the function to add the status column
add_muac_column()


def add_muac_sam_column():
    """
    Alter the 'student' table to add a 'status' column if it doesn't already exist.
    """
    try:
        # Check if the 'status' column already exists
        cursor.execute("PRAGMA table_info(student);")
        columns = cursor.fetchall()

        # Look for the 'status' column
        column_names = [column[1] for column in columns]

        if 'muac_sam' not in column_names:
            # Alter the table to add the 'status' column
            cursor.execute("""
                ALTER TABLE student
                ADD COLUMN muac_sam TEXT
            """)

            # Commit the changes to the database
            conn.commit()




    except Exception as e:
        # Handle any errors during the table alteration process
        messagebox.showerror("Error", f"Failed to add 'muac_sam' column: {e}")
        conn.rollback()


# Call the function to add the status column
add_muac_sam_column()




def fetch_data_by_id(id_value):
    """
    Fetches all screening records for a given student ID, sorted by screen_date descending.

    Args:
        id_entry_widget (tk.Entry): The Tkinter Entry widget containing the student ID.

    Returns:
        List[Dict]: A list of dictionaries, each representing a screening record.
    """


    conn = sqlite3.connect('gracehealth.db')  # Connect to the database
    cursor = conn.cursor()

    query = """
    SELECT
        name, date_of_birth, Gender, Class_section, Roll_no, Aadhaar_No,
        Father_or_guardian_name, mother_name, contact_number, Address,
        email, Name_teacher, school_name, last_school_name, place_of_birth,
        known_earlier_disease,
        weight, height,muac, muac_sam, BMI, Vision_both, VISON_left, VISON_right, VISION_problem,
        B1_severe_anemia, B2_Vita_A_deficiency, B3_Vit_D_deficiency, B4_Goitre,
        B5_Oedema, C1_convulsive_dis, C2_otitis_media, C3_dental_condition,
        C4_skin_condition, C5_rheumatic_heart_disease, C6_others_TB_asthma,
        D1_difficulty_seeing, D2_delay_in_walking, D3_stiffness_floppiness,
        D5_reading_writing_calculatory_difficulty, D6_speaking_difficulty,
        D7_hearing_problems, D8_learning, D9_attention, E3_depression_sleep,
        E4_Menarke, E5_regularity_period_difficulties, E6_UTI_STI, E7,
        E8_menstrual_pain, E9_remarks, BMI_category, weight_age, length_age,
        weight_height, age_in_month, deworming, vaccination, tea_garden,
        screen_date, age_screening
    FROM student
    WHERE id = ?
    ORDER BY screen_date DESC
    """

    cursor.execute(query, (id_value,))
    rows = cursor.fetchall()  # Fetch all matching rows
    conn.close()  # Always close the connection

    if rows:
        # Get column names from cursor description
        column_names = [description[0] for description in cursor.description]

        # Convert each row to a dictionary
        data_list = [dict(zip(column_names, row)) for row in rows]
        print(f"Number of screenings fetched: {len(data_list)}")
        return data_list
    else:
        print("No data found for the given ID")
        return []




import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import Toplevel
from tkinter import filedialog
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def save_text_as_pdf(text_widget):
    """
    Saves the content of a Tkinter Text widget as a PDF file.

    Args:
        text_widget (tk.Text): The Tkinter Text widget containing the journal content.
    """
    # Ask the user to choose a file location and name
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])

    if not file_path:
        return  # Exit the function if the user cancels the save dialog

    # Get the content from the Text widget
    text_content = text_widget.get("1.0", tk.END).strip()

    # Create a PDF file
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter

    # Set the initial y-position for the text
    y_position = height - 40  # Start near the top with some margin
    line_height = 14  # Line spacing for each line

    # Split text into lines and write each line to the PDF
    for line in text_content.split("\n"):
        if y_position <= 40:  # If there's not enough space, create a new page
            c.showPage()
            y_position = height - 40  # Reset y-position for the new page

        c.drawString(40, y_position, line)
        y_position -= line_height

    # Save the PDF file
    c.save()
    print(f"PDF saved as {file_path}")


def display_journal(id_value, summary_frame):
    """
    Displays all screening records for a given student ID in a new window.

    Args:
        id_entry_widget (tk.Entry): The Tkinter Entry widget containing the student ID.
    """

    data_list = fetch_data_by_id(id_value)
    print("This is display journal")

    if not data_list:

        return  # Exit the function if no data is found

    # Clear existing widgets in the summary_frame
    for widget in summary_frame.winfo_children():
        widget.destroy()

    # Create a new window to display the data
    journal_text = tk.Text(summary_frame, wrap=tk.WORD, height=10, width=45)
    scroll = tk.Scrollbar(summary_frame, command=journal_text.yview)
    journal_text.config(yscrollcommand=scroll.set)
    journal_text.tag_configure("remarks_red", foreground="red")

    # Use grid for both the text widget and scrollbar
    journal_text.grid(row=0, column=0, sticky="nsew")
    scroll.grid(row=0, column=1, sticky="ns")

    # Add a button to save the text as a PDF
    save_pdf_button = ttk.Button(summary_frame, text="Save as PDF", command=lambda: save_text_as_pdf(journal_text))
    save_pdf_button.grid(row=1, column=0, pady=10, sticky="ew")

    # Configure the frame to resize with the Text widget
    summary_frame.grid_rowconfigure(0, weight=1)
    summary_frame.grid_columnconfigure(0, weight=1)
    total_screenings = len(data_list)

    # Iterate through the screening entries
    for index, data in enumerate(data_list):
        # Calculate the screening number in reverse order
        screening_number = total_screenings - index  # This will start from total_screenings down to 1

        # Insert the screening data into the Text widget
        journal_text.insert(tk.END, f"=== SCREENING {screening_number} ===\n")
        # Here, you can include other details from the `data` object as needed

        journal_text.insert(tk.END, f"Screen Date: {data.get('screen_date', 'N/A')}\n")
        journal_text.insert(tk.END, f"Age Screening: {data.get('age_screening', 'N/A')}\n")
        journal_text.insert(tk.END, "-" * 40 + "\n")
        journal_text.insert(tk.END, "=== BIO ===\n")
        journal_text.insert(tk.END, f"Name: {data.get('name', 'N/A')}\n")
        journal_text.insert(tk.END, f"Date of Birth: {data.get('date_of_birth', 'N/A')}\n")
        journal_text.insert(tk.END, f"Gender: {data.get('Gender', 'N/A')}\n")
        journal_text.insert(tk.END, f"Class Section: {data.get('Class_section', 'N/A')}\n")
        journal_text.insert(tk.END, f"Roll No: {data.get('Roll_no', 'N/A')}\n")
        journal_text.insert(tk.END, f"Aadhaar No: {data.get('Aadhaar_No', 'N/A')}\n")
        journal_text.insert(tk.END, f"Father/Guardian Name: {data.get('Father_or_guardian_name', 'N/A')}\n")
        journal_text.insert(tk.END, f"Mother's Name: {data.get('mother_name', 'N/A')}\n")
        journal_text.insert(tk.END, f"Contact Number: {data.get('contact_number', 'N/A')}\n")
        journal_text.insert(tk.END, f"Address: {data.get('Address', 'N/A')}\n")
        journal_text.insert(tk.END, f"Tea Garden: {data.get('tea_garden', 'N/A')}\n")
        journal_text.insert(tk.END, f"Email: {data.get('email', 'N/A')}\n")
        journal_text.insert(tk.END, f"Name of Teacher: {data.get('Name_teacher', 'N/A')}\n")
        journal_text.insert(tk.END, f"School Name: {data.get('school_name', 'N/A')}\n")
        journal_text.insert(tk.END, f"Last School Name: {data.get('last_school_name', 'N/A')}\n")
        journal_text.insert(tk.END, f"Place of Birth: {data.get('place_of_birth', 'N/A')}\n")
        journal_text.insert(tk.END, "-" * 40 + "\n")

        journal_text.insert(tk.END, "=== PHYSICAL MEASUREMENTS ===\n")
        journal_text.insert(tk.END, f"Weight: {data.get('weight', 'N/A')}\n")
        journal_text.insert(tk.END, f"Height: {data.get('height', 'N/A')}\n")
        journal_text.insert(tk.END, f"BMI: {data.get('BMI', 'N/A')}\n")
        journal_text.insert(tk.END, f"MUAC: {data.get('muac', 'N/A')}\n")
        journal_text.insert(tk.END, "-" * 40 + "\n")

        journal_text.insert(tk.END, "=== PHYSICAL CATEGORIES ===\n")
        # Define the BMI category and the data
        bmi_category = data.get('BMI_category', 'N/A')

        def insert_and_highlight_not_normal(condition, value_key):
            # Retrieve value from data, convert to string to handle int/other cases
            value = str(data.get(value_key, 'N/A'))

            # Insert condition and value into the text widget
            journal_text.insert(tk.END, f"{condition}: {value}\n")

            # Highlight if value is not "normal", not empty, and not "N/A"
            def insert_and_highlight_not_normal(condition, value_key):
                # Retrieve value from data, convert to string to handle int/other cases
                value = str(data.get(value_key, 'N/A'))

                # Insert condition and value into the text widget
                journal_text.insert(tk.END, f"{condition}: {value}\n")

                # Highlight if value is not "normal", not empty, not "N/A", and not "None"
                if value.lower() not in ['normal', 'n/a', 'none'] and value.strip():
                    # Calculate start and end indices for the current line
                    start_index = f"{float(journal_text.index('end')) - 2} linestart"
                    end_index = f"{float(journal_text.index('end')) - 1} lineend"

                    # Add the 'highlight' tag to this text range
                    journal_text.tag_add("highlight", start_index, end_index)

        # Apply the logic to all the relevant conditions
        insert_and_highlight_not_normal("BMI Category", "bmi_category")
        insert_and_highlight_not_normal("MUAC Category", "muac_sam")
        insert_and_highlight_not_normal("Weight for Age", "weight_age")
        insert_and_highlight_not_normal("Length for Age", "length_age")
        insert_and_highlight_not_normal("Weight for Height", "weight_height")

        # Insert a separator after all entries
        journal_text.insert(tk.END, "-" * 40 + "\n")

        # Insert and check for highlighting for all conditions




        journal_text.insert(tk.END, "=== EYE ===\n")
        journal_text.insert(tk.END, f"Vision (Both Eyes): {data.get('Vision_both', 'N/A')}\n")
        journal_text.insert(tk.END, f"Vision (Left Eye): {data.get('VISON_left', 'N/A')}\n")
        journal_text.insert(tk.END, f"Vision (Right Eye): {data.get('VISON_right', 'N/A')}\n")
        # Define the Vision problem value from the data
        vision_problem = data.get('VISION_problem', 'N/A')

        # Insert the Vision problem text into the Text widget
        journal_text.insert(tk.END, f"Vision Problem: {vision_problem}\n")

        # Check if the Vision problem is "Yes" and apply highlighting
        if vision_problem.lower() == "yes":
            # Define a tag with the desired background color and other options
            journal_text.tag_configure("highlight", foreground="red")

            # Get the index of the inserted text to apply the tag
            start_index = f"{float(journal_text.index('end')) - 2} linestart"  # Find where the Vision problem text starts
            end_index = f"{float(journal_text.index('end')) - 1} lineend"  # End index of the text

            # Apply the highlight tag to the inserted Vision problem line
            journal_text.tag_add("highlight", start_index, end_index)

        journal_text.insert(tk.END, "-" * 40 + "\n")

        journal_text.insert(tk.END, "=== GENERAL HEALTH ===\n")
        # Configure a tag for highlighting
        journal_text.tag_configure("highlight", foreground="red")

        # Function to insert and highlight text if the value is 'Yes'
        def insert_and_highlight(condition, value_key):
            value = data.get(value_key, 'N/A')
            journal_text.insert(tk.END, f"{condition}: {value}\n")

            # Highlight if value is 'Yes'
            if value.lower() == 'yes':
                start_index = f"{float(journal_text.index('end')) - 2} linestart"
                end_index = f"{float(journal_text.index('end')) - 1} lineend"
                journal_text.tag_add("highlight", start_index, end_index)

        # Example usage for each condition
        insert_and_highlight("Severe Anemia", 'B1_severe_anemia')
        insert_and_highlight("Vitamin A Deficiency", 'B2_Vita_A_deficiency')
        insert_and_highlight("Vitamin D Deficiency", 'B3_Vit_D_deficiency')
        insert_and_highlight("Goitre", 'B4_Goitre')
        insert_and_highlight("Oedema", 'B5_Oedema')
        insert_and_highlight("Convulsive Disorders", 'C1_convulsive_dis')
        insert_and_highlight("Otitis Media", 'C2_otitis_media')
        insert_and_highlight("Dental Condition", 'C3_dental_condition')
        insert_and_highlight("Skin Condition", 'C4_skin_condition')
        insert_and_highlight("Rheumatic Heart Disease", 'C5_rheumatic_heart_disease')
        insert_and_highlight("Others (TB/Asthma)", 'C6_others_TB_asthma')
        insert_and_highlight("UTI/STI", 'E6_UTI_STI')
        insert_and_highlight("Discharge/Foul Smell Issues", 'E7')

        journal_text.insert(tk.END, "-" * 40 + "\n")

        # Developmental and Learning Issues
        journal_text.insert(tk.END, "=== DEVELOPMENTAL AND LEARNING ISSUES ===\n")
        insert_and_highlight("Difficulty Seeing", 'D1_difficulty_seeing')
        insert_and_highlight("Delay in Walking", 'D2_delay_in_walking')
        insert_and_highlight("Stiffness/Floppiness", 'D3_stiffness_floppiness')
        insert_and_highlight("Reading/Writing Difficulty", 'D5_reading_writing_calculatory_difficulty')
        insert_and_highlight("Speaking Difficulty", 'D6_speaking_difficulty')
        insert_and_highlight("Hearing Problems", 'D7_hearing_problems')
        insert_and_highlight("Learning Issues", 'D8_learning')
        insert_and_highlight("Attention Problems", 'D9_attention')

        journal_text.insert(tk.END, "-" * 40 + "\n")

        # Mental Health
        journal_text.insert(tk.END, "=== MENTAL HEALTH ===\n")
        insert_and_highlight("Depression or Sleep Problems", 'E3_depression_sleep')

        journal_text.insert(tk.END, "-" * 40 + "\n")

        # Female Issues
        journal_text.insert(tk.END, "=== FEMALE ISSUES ===\n")
        journal_text.insert(tk.END, f"Menarke: {data.get('E4_Menarke', 'N/A')}\n")
        insert_and_highlight("Menstrual Irregularities", 'E5_regularity_period_difficulties')
        insert_and_highlight("Menstrual Pain", 'E8_menstrual_pain')

        journal_text.insert(tk.END, "-" * 40 + "\n")

        journal_text.insert(tk.END, "=== OTHER ===\n")
        journal_text.insert(tk.END, f"Deworming: {data.get('deworming', 'N/A')}\n")
        journal_text.insert(tk.END, f"Vaccination: {data.get('vaccination', 'N/A')}\n")

        journal_text.insert(tk.END, "=== KNOWN EARLIER DISEASE ===\n")
        journal_text.insert(tk.END, f"Known Earlier Disease: {data.get('known_earlier_disease', 'N/A')}\n")
        journal_text.insert(tk.END, "-" * 40 + "\n")

        # Insert the remarks header
        journal_text.insert(tk.END, "=== REMARKS ===\n")

        # Retrieve and insert the remarks text
        remarks_text = f"{data.get('E9_remarks', 'N/A')}\n"
        journal_text.insert(tk.END, remarks_text)

        # Calculate start and end indices for highlighting the remarks
        # Start index should be at the end of the "=== REMARKS ===" header
        start_index = journal_text.index('end - 1 char')  # Index just after inserting remarks
        start_index = f"{int(start_index.split('.')[0]) - 1}.0"  # Set to the start of the remarks text
        # End index is the end of the remarks text
        end_index = journal_text.index('end - 1 char')  # End index for the last character inserted

        # Add the 'remarks_red' tag to this text range
        journal_text.tag_add("remarks_red", start_index, end_index)

    # Scroll to the top of the text
    journal_text.yview_moveto(0)

    # Add Generate PDF button


# Example usage
# show_student_data(1)  # Replace 1 with the actual ID you want to fetch


def add_column_if_not_exists():
    connection = sqlite3.connect("gracehealth.db")
    cursor = connection.cursor()

    # Check if the column 'age_screening' exists in the 'student' table
    cursor.execute("PRAGMA table_info(student)")
    columns = cursor.fetchall()

    # Column names are in the second position in each row of the result
    column_names = [column[1] for column in columns]

    if 'age_screening' not in column_names:
        # Add the new column 'age_screening' if it doesn't exist
        cursor.execute("ALTER TABLE student ADD COLUMN age_screening TEXT")
        print("Column 'age_screening' added.")
    else:
        print("Column 'age_screening' already exists.")

    connection.commit()
    connection.close()

# Call the function
add_column_if_not_exists()

import tkinter as tk
from tkinter import ttk

class ToolTip:
    def __init__(self, widget, text, delay=500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self.tooltip_window = None
        self.after_id = None  # Store the ID of the scheduled after() call
        self.widget.bind("<Enter>", self.schedule_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def schedule_tooltip(self, event=None):
        self.cancel_scheduled_tooltip()  # Cancel any previous scheduling
        self.after_id = self.widget.after(self.delay, self.show_tooltip)

    def cancel_scheduled_tooltip(self):
        if self.after_id:
            self.widget.after_cancel(self.after_id)
            self.after_id = None

    def show_tooltip(self, event=None):
        if self.tooltip_window:  # Tooltip already exists
            return
        self.tooltip_window = tk.Toplevel(self.widget)
        self.tooltip_window.wm_overrideredirect(True)  # Removes window borders
        x = self.widget.winfo_rootx() + 20
        y = self.widget.winfo_rooty() + 20
        self.tooltip_window.wm_geometry(f"+{x}+{y}")
        label = tk.Label(self.tooltip_window, text=self.text, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_tooltip(self, event=None):
        self.cancel_scheduled_tooltip()  # Ensure no tooltip will be shown
        if self.tooltip_window:
            self.tooltip_window.destroy()
            self.tooltip_window = None

def new_journal():

    # Create the main application window (if not already created)


    def statistic_search():

        def clear_statistic():
            pass


        def show_record_function():
            connection = sqlite3.connect("gracehealth.db")
            cursor = connection.cursor()
            record = sickness_search.get()
            school = school_options.get()
            clear_statistic()




            from tkinter import ttk
            from tkinter import messagebox


            def height_age_cm_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with chronic malnutrition and the selected screening date
                    cursor.execute(f"""
                         SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE length_age = 'chronic malnutrition'
                       AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                    result = cursor.fetchall()

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = '0% of students age 2 - 6 years have chronic malnutrition (measuring stunting)'
                    else:
                        # Query to find total students between 24 and 72 months old with the selected screening date
                        cursor.execute(f"""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 24 AND 72 
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_text = f'{percentage} % ({total_sick} / {total_student}) of students age 2 - 6 years have chronic malnutrition (measuring stunting)'

                    # Update the existing label (assuming `statistic` is defined elsewhere)
                    statistic_label.config(text=statistic_text)  # Use the same label to update the text

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

            def muac_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with severe acute malnutrition and the selected screening date
                    cursor.execute(f"""
                         SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE muac_sam = 'severe acute malnutrition'
                       AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                   (selected_year,))
                    result = cursor.fetchall()

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = '0% of students age 6 - 60 months have severe acute malnutrition based on MUAC'
                    else:
                        # Query to find total students between 24 and 72 months old who were tested for MUAC
                        cursor.execute(f"""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 24 AND 72 
                            AND muac_sam IS NOT NULL  
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                       (selected_year,))
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_text = f'{percentage} % ({total_sick} / {total_student}) of students age 6 - 60 months have severe acute malnutrition based on MUAC'

                    # Update the existing label (assuming `statistic` is defined elsewhere)
                    statistic_label.config(text=statistic_text)  # Use the same label to update the text

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

            def weight_height_statistic(malnutrition_type):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified malnutrition type and the selected screening date
                    cursor.execute(f"""
                        SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE weight_height = ?
                        AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                   (malnutrition_type, selected_year)
                                   )
                    result = cursor.fetchall()

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = f'0% of students age 2 - 5 years have {malnutrition_type} (measuring wasting)'
                    else:
                        # Query to find total students between 24 and 60 months old with the selected screening date
                        cursor.execute(f"""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 24 AND 60 
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                       (selected_year,)
                                       )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_text = f'{percentage}% ({total_sick} / {total_student})of students age 2 - 5 years have {malnutrition_type} (measuring wasting)'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)  # Use the same label to update the text

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

            def B5_Oedema_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with Oedema/swelling of legs and the selected screening date
                    cursor.execute(f"""
                         SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE age_in_month BETWEEN 24 AND 72 
                             AND B5_Oedema = 'yes'  
                       AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                    result = cursor.fetchall()

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = '0% of students age 2 - 6 years oedema'
                    else:
                        # Query to find total students between 24 and 72 months old with the selected screening date
                        cursor.execute(f"""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 24 AND 72 
                          AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_text = f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years have oedema'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def vision_problem_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with vision problems on the selected screening date
                    cursor.execute(f"""
                        SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE vision_problem = 'yes' 
                       AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                    result = cursor.fetchall()

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = '0% of students tested have vision problems'
                    else:
                        # Query to find total students regardless of vision problems on the selected date
                        cursor.execute(f"""
                            SELECT id 
                            FROM student 
                            WHERE (vision_problem = 'yes' OR vision_problem = 'no') 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({total_sick} / {total_student}) of students tested have vision problems'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_all(sickness, problem):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified sickness on the selected screening date
                    cursor.execute(f"""
                         SELECT id, name, school_name, tea_garden 
                        FROM student 
                        WHERE {sickness} = 'yes' 
                        AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                   (selected_year,)
                                   )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = f'0% of students have {problem}'
                    else:
                        # Query to find total students on the selected screening date
                        cursor.execute(f"""
                            SELECT id 
                            FROM student 
                            WHERE '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                       (selected_year,)
                                       )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({total_sick} / {total_student}) of students have {problem} on {selected_year}'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E4_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students who have started their menstrual cycle on the selected screening date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden from student
                        WHERE E4_Menarke = 'yes' AND Gender = 'female' AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = '0% of female students have started menstrual cycle'
                    else:
                        # Query to find total female students on the selected screening date
                        cursor.execute(
                            """SELECT oid FROM student 
                            WHERE Gender = 'female'                             
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({total_sick} / {total_student}) of female students have started menstrual cycle'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E5_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students with regular menstrual periods on the selected screening date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden from student
                        WHERE E4_Menarke = 'yes' AND E5_regularity_period_difficulties = 'no' 
                        AND Gender = 'female' AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )


                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        statistic_text = '0% of female students have irregular periods'
                    else:
                        # Query to find total female students who have started their menstrual cycle on the selected screening date
                        cursor.execute(
                            """SELECT oid FROM student 
                            WHERE E4_Menarke = 'yes' 
                             AND Gender = 'female'AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )

                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({statistic_sick} / {total_student}) of female students have irregular periods'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E6_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified sickness on the selected screening date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden from student
                        WHERE E6_UTI_STI = 'yes'  
                        AND Gender = 'female' AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (selected_year,)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_text = f'0% of students have pain/burning sensation while urinating'
                    else:
                        # Query to find total students on the selected screening date
                        cursor.execute(f"""
                            SELECT id 
                            FROM student 
                            WHERE age_in_month  BETWEEN 120 AND 216  
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                       (selected_year,)
                                       )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({total_sick} / {total_student}) of students have pain/burning sensation while urinating'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E7_all():
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with discharge/foul smell from genito-urinary area on the selected screening date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden from student
                        WHERE E7 = 'yes' 
                        
                        AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )


                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        statistic_text = '0% of students have discharge/foul smell from genito-urinary area'
                    else:
                        # Query to find total students with the selected screening date
                        cursor.execute(
                            """SELECT oid FROM student WHERE 
                             
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (selected_year,)
        )
                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({statistic_sick} / {total_student}) of students have discharge/foul smell from genito-urinary area'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E8_all():
                selected_year = screening_year.get()  # Get the selected screening year from the combobox

                # Check if a year is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students with menstrual pain on the selected screening date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden FROM student
                            WHERE E8_menstrual_pain = 'yes' 
                            AND Gender = 'female' 
                           
                            AND SUBSTR(screen_date, -2) = ? """,
                        (selected_year[-2:],))  # Only pass the last two digits of the year to match the yy format

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        statistic_text = '0% of female students that started menstrual cycle have menstrual pain'
                    else:
                        # Query to find total female students who have started their menstrual cycle on the selected date
                        cursor.execute(
                            """SELECT oid FROM student 
                               WHERE E4_Menarke = 'yes' 
                               AND Gender = 'female' 
                        
                               AND SUBSTR(screen_date, -2) = ?""",
                            (selected_year[-2:],))  # Only pass the last two digits of the year

                        total_students = cursor.fetchall()
                        total_student = len(total_students)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        statistic_text = (
                            f'{percentage}% ({statistic_sick} / {total_student}) of female students that have started menstrual cycle have menstrual pain')

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_bmi(category):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the selected BMI category on the selected screening date
                    cursor.execute(
                        f"""SELECT id, name, school_name, tea_garden FROM student 
                        WHERE BMI_category = ? AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (category, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        statistic_text = f'0% of students aged between 5 to 18 years have {category} BMI'
                    else:
                        # Query to find total students aged between 6 to 18 years on the selected date
                        cursor.execute(
                            """SELECT oid FROM student 
                            WHERE age_in_month BETWEEN 61 AND 216 AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (selected_year,)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        statistic_text = f'{percentage}% ({statistic_sick} / {total_student}) of students aged between 5 to 18 years have {category} BMI'

                    # Update the label with the statistic information
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            # Usage: Call this function with the specific category, e.g., 'severe under', 'under', or 'over'.

            def handle_school_record(school, sickness, problem):
                """Process and display statistics for students with a specific sickness at a given school and year."""

                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a year is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Execute query to find students with the specified sickness and selected date
                    cursor.execute(
                        f"""SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE {sickness} = 'yes' 
                           AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (school, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    # Calculate the statistic text
                    if statistic_sick == 0:
                        statistic_text = f'0% of students have {problem}'
                    else:
                        # Query to find total students in the specified school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE school_name = ? 
                               AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Check if there are no students to avoid division by zero
                        if total_student == 0:
                            statistic_text = f'No students recorded for {problem} at {school}.'
                        else:
                            # Calculate percentage
                            percentage = round(statistic_sick / total_student * 100, 1)
                            statistic_text = f'{percentage}% ({statistic_sick} / {total_student}) of students have {problem}'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end",
                                                values=(item[0], item[1], item[2],item[3]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def weight_age_mu_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students who are 'moderately underweight' in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE weight_age = 'moderately underweight' 
                            AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(text='0% of students age 2 - 6 years are moderately underweight')
                    else:
                        # Query to find total students between 24 and 72 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years are moderately underweight')

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end",
                                                    values=(
                                                    item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def weight_age_su_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students who are 'moderately underweight' in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE weight_age = 'severely underweight' 
                            AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (school, selected_year)
                    )

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(text='0% of students age 2 - 6 years are severly underweight')
                    else:
                        # Query to find total students between 24 and 72 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years are severly underweight')

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end",
                                                    values=(
                                                        item[0], item[1], item[2],
                                                        item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def height_age_cm_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with chronic malnutrition (stunting) in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 72 
                             AND length_age = 'chronic malnutrition' 
                             AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text="0% of students age 2 - 6 years have chronic malnutrition (measuring stunting)"
                        )
                    else:
                        # Query to find total students between 24 and 72 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years have chronic malnutrition (measuring stunting)'
                        )

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def muac_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with moderate acute malnutrition (MAM) in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                            WHERE muac_sam = 'severe acute malnutrition' 
                             AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (school, selected_year)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text='0% of students age 6 - 60 months have severe acute malnutrition based on MUAC'
                        )
                    else:
                        # Query to find total students between 24 and 60 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 6 AND 60 
                                 AND school_name = ? 
                                 AND muac_sam IS NOT NULL  -- Exclude students not tested for MUAC
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of of students age 6 - 60 months have severe acute malnutrition based on MUAC'
                        )

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def weight_height_mam_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with moderate acute malnutrition (MAM) in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 60 
                             AND weight_height = 'moderate acute malnutrition' 
                             AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text='0% of students age 2 - 5 years have moderate acute malnutrition (measuring wasting)'
                        )
                    else:
                        # Query to find total students between 24 and 60 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 60 
                                 AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 5 years have moderate acute malnutrition (measuring wasting)'
                        )

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def weight_height_sam_school(school):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return
                try:
                    # Query to find students with severe acute malnutrition (SAM) in the selected school on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden  
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 60 
                             AND weight_height = 'severe acute malnutrition' 
                              AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text='0% of students age 2 - 5 years have severe acute malnutrition (measuring wasting)'
                        )
                    else:
                        # Query to find total students between 24 and 60 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 60 
                                  AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 5 years have severe acute malnutrition (measuring wasting)'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2]))  # Adjust for the Treeview structure

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def B5_Oedema_school(school):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return



                try:
                    # Query to find students with Oedema in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 72 
                             AND B5_Oedema = 'yes' 
                             AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with Oedema
                        statistic_label.config(text='0% of students age 2 - 6 years have oedema')
                    else:
                        # Query to find total students between 24 and 72 months old in the selected school and date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years have oedema'
                        )

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)


            def statistic_E4_school(school):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students who have started their menstrual cycle in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E4_Menarke = 'yes' 
                             AND Gender = 'female' 
                            AND school_name = ? 
                            
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students have started menstrual cycle
                        statistic_label.config(text='0% of female students have started menstrual cycle')
                    else:
                        # Query to find total female students in the selected school and date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE Gender = 'female' 
                                  AND school_name = ? 
                               
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(text=f'{percentage}% ({statistic_sick} / {total_student}) of female students have started menstrual cycle')

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E5_school(school):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students who have started their menstrual cycle and have no period difficulties in the selected school and date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E4_Menarke = 'yes' 
                             AND E5_regularity_period_difficulties = 'no' 
                             AND Gender = 'female' 
                              AND school_name = ? 
                       
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with irregular periods
                        statistic_label.config(text='0% of female students have irregular periods')
                    else:
                        # Query to find the total female students who have started their menstrual cycle in the selected school and date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE E4_Menarke = 'yes' 
                                 AND Gender = 'female' 
                                 AND school_name = ? 
                      
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(text=f'{percentage}%({statistic_sick} / {total_student}) of female students have irregular periods')

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E6_school(school):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with discharge/foul smell from the genito-urinary area on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E6_UTI_STI = 'yes' 
                           AND school_name = ? 
                        
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (school, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(
                            text='0% of students have pain/burning sensation while urinating')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE school_name = ? 
                        
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of students have pain/burning sensation while urinating'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E7_school(school):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with discharge/foul smell from the genito-urinary area on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E7 = 'yes' 
                           AND school_name = ? 
                          
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(text='0% of students have discharge/foul smell from genito-urinary area')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE school_name = ? 
                           
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of students have discharge/foul smell from genito-urinary area'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E8_school(school):
                print("statisctic schoolE8")
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get() # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students with menstrual pain who have started menstruation
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E8_menstrual_pain = 'yes' 
                             AND Gender = 'female' 
                             AND school_name = ? 
                       
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no female students with menstrual pain
                        statistic_label.config(
                            text='0% of female students that have started menstrual cycle have menstrual pain'
                        )
                    else:
                        # Query to get the total number of female students who have started menstruation
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE E4_Menarke = 'yes' 
                                 AND Gender = 'female' 
                                 AND school_name = ? 
                                 AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )
                        total_female_students = cursor.fetchall()  # Fetch all IDs
                        total_student = len(total_female_students)  # Count them

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of female students that have started menstruation have menstrual pain'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)



            def statistic_BMI(sickness, condition, school, problem):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified sickness and school on the selected date
                    cursor.execute(f""" SELECT id, name, school_name, tea_garden 
                                       FROM student 
                                       WHERE {sickness} = ? 
                                         AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (condition, school, selected_year)
        )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(text=f'0% of students aged 5 to 18 years have {problem}')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 61 AND 216 
                                AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
            (school, selected_year)
        )

                        total_students = cursor.fetchall()  # Fetch all IDs
                        total_student = len(total_students)  # Count them

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(text=f'{percentage}% ({total_sick} / {total_student}) of students aged 5 to 18 years have {problem}')

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)
            def weight_age_statistic(weight_category):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified weight category and the selected screening date
                    cursor.execute(f"""
                        SELECT id, name, school_name, tea_garden  
                        FROM student 
                        WHERE weight_age = ?
                        AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                   (weight_category, selected_year)
                                   )

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_label.config(
                            text=f'0% of students age 2 - 6 years are {weight_category}'
                        )
                    else:
                        # Query to find total students between 24 and 72 months old with the selected screening date
                        cursor.execute(f"""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 24 AND 72 
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                       (selected_year,)
                                       )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years are {weight_category}'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}")

            # Consolidated function to handle 'moderately' or 'severely' underweight cases
            def weight_age_area(area, weight_category):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students by weight category (moderate or severe) in the selected area
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE weight_age = ? 
                             AND tea_garden = ? 
                             AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (weight_category, area, selected_year)
                    )

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Display 0% if no students match
                        statistic_label.config(text=f'0% of students age 2 - 6 years are {weight_category}')
                    else:
                        # Query for total students in the age range (24 - 72 months) in the selected area
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND tea_garden = ? 
                                 AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate and display percentage
                        percentage = round(total_sick / total_student * 100, 1)
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years are {weight_category}'
                        )

                        # Insert the results into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            # Example calls for each category


            def height_age_cm_area(area):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with chronic malnutrition (stunting) in the selected tea garden on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 72 
                             AND length_age = 'chronic malnutrition' 
                             AND tea_garden = ? 
                             AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text="0% of students age 2 - 6 years have chronic malnutrition (measuring stunting)"
                        )
                    else:
                        # Query to find total students between 24 and 72 months old in the selected tea garden on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND tea_garden = ? 
                                 AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years have chronic malnutrition (measuring stunting)'
                        )

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                            item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def muac_area(area):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox
                print(f"Area: {area}")  # Confirm that area is set

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                if not area:
                    messagebox.showerror("Error", "Please select an area.", parent=statistic_window)
                    return

                try:
                    print(f"Selected Year: {selected_year}")  # Debugging output for the selected year
                    print(f"Area: {area}")  # Debugging output for the area

                    # Query to find students with severe acute malnutrition in the selected tea_garden on the selected year
                    query = """
                        SELECT id, name, school_name, tea_garden
                        FROM student 
                        WHERE muac_sam = 'severe acute malnutrition' 
                        AND tea_garden = ? 
                        AND '20' || SUBSTR(screen_date, 7, 2) = ?
                    """
                    print(f"Executing query: {query} with parameters: (area={area}, selected_year={selected_year})")
                    cursor.execute(query, (area, selected_year))

                    result = cursor.fetchall()
                    print(f"Result: {result}")  # Debugging output for the query result

                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        statistic_label.config(
                            text='0% of students age 6 - 60 months have severe acute malnutrition based on MUAC'
                        )
                    else:
                        # Query to find total students between 6 and 60 months old in the selected area
                        cursor.execute("""
                            SELECT oid 
                            FROM student 
                            WHERE age_in_month BETWEEN 6 AND 60 
                            AND tea_garden = ? 
                            AND muac_sam IS NOT NULL  -- Exclude students not tested for MUAC
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?
                        """, (area, selected_year))
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 6 - 60 months have severe acute malnutrition based on MUAC'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(item[0], item[1], item[2], item[3]))


                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

                print(f"After Query - Area: {area}")

            def weight_height_mam_area(area):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with moderate acute malnutrition (MAM) in the selected school on the selected date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 60 
                             AND weight_height = 'moderate acute malnutrition' 
                             AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text='0% of students age 2 - 5 years have moderate acute malnutrition (measuring wasting)'
                        )
                    else:
                        # Query to find total students between 24 and 60 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 60 
                                 AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 5 years have moderate acute malnutrition (measuring wasting)'
                        )

                        # Insert new data into the Treeview, including the tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def weight_height_sam_area(area):
                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return
                try:
                    # Query to find students with severe acute malnutrition (SAM) in the selected school on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden  
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 60 
                             AND weight_height = 'severe acute malnutrition' 
                              AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students
                        statistic_label.config(
                            text='0% of students age 2 - 5 years have severe acute malnutrition (measuring wasting)'
                        )
                    else:
                        # Query to find total students between 24 and 60 months old in the selected school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 60 
                                  AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 5 years have severe acute malnutrition (measuring wasting)'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Adjust for the Treeview structure

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def B5_Oedema_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with Oedema in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE age_in_month BETWEEN 24 AND 72 
                             AND B5_Oedema = 'yes' 
                             AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with Oedema
                        statistic_label.config(text='0% of students age 2 - 6 years have Oedema/swelling of legs')
                    else:
                        # Query to find total students between 24 and 72 months old in the selected school and date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 24 AND 72 
                                 AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate the percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({total_sick} / {total_student}) of students age 2 - 6 years have Oedema/swelling of legs'
                        )

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def vision_problem_school(school):
                print("hello there")
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return
                try:
                    # Query to find students with vision problems in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE vision_problem = 'yes' 
                            AND school_name = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (school, selected_year))

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with vision problems
                        statistic_label.config(text='0% of students tested have vision problems')
                    else:
                        # Query to find total students who were tested for vision problems (either 'yes' or 'no') on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE (vision_problem = 'yes' OR vision_problem = 'no') 
                                 AND school_name = ? 

                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(text=f'{percentage}% ({total_sick} / {total_student}) of students tested have vision problems')

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def vision_problem_area(area):
                print("VISION AREA")
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format



                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return
                try:
                    # Query to find students with vision problems in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE vision_problem = 'yes' 
                            AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year))

                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with vision problems
                        statistic_label.config(text='0% of students tested have vision problems')
                    else:
                        # Query to find total students who were tested for vision problems (either 'yes' or 'no') on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE (vision_problem = 'yes' OR vision_problem = 'no') 
                                 AND tea_garden = ? 

                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(text=f'{percentage}% ({total_sick} / {total_student}) of students tested have vision problems')

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E4_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format



                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students who have started their menstrual cycle in the selected school and date
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E4_Menarke = 'yes' 
                             AND Gender = 'female' 
                            AND tea_garden = ? 
                            AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students have started menstrual cycle
                        statistic_label.config(text='0% of female students have started menstrual cycle')
                    else:
                        # Query to find total female students in the selected school and date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE Gender = 'female' 
                                  AND tea_garden = ? 
                                  AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of female students have started menstrual cycle')

                        # Insert new data into the Treeview, including tea_garden value
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # Assuming item[3] is tea_garden

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E5_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students who have started their menstrual cycle and have no period difficulties in the selected school and date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E4_Menarke = 'yes' 
                             AND E5_regularity_period_difficulties = 'no' 
                             AND Gender = 'female' 
                              AND tea_garden = ? 
                              AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with irregular periods
                        statistic_label.config(text='0% of female students have irregular periods')
                    else:
                        # Query to find the total female students who have started their menstrual cycle in the selected school and date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE E4_Menarke = 'yes' 
                                 AND Gender = 'female' 
                                 AND tea_garden = ? 
                            
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the new percentage
                        statistic_label.config(text=f'{percentage}% ({statistic_sick} / {total_student}) of female students have irregular periods')

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2], item[3]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E6_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected

                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with discharge/foul smell from the genito-urinary area on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E6_UTI_STI = 'yes' 
                           AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(
                            text='0% of students have pain/burning sensation while urinating')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE school_name = ? 
                               AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (school, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of students have pain/burning sensation while urinating'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E7_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selected


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with discharge/foul smell from the genito-urinary area on the selected date
                    cursor.execute(
                        """ SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E7 = 'yes' 
                           AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(
                            text='0% of students have discharge/foul smell from genito-urinary area')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE tea_garden = ? 
                              AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of students have discharge/foul smell from genito-urinary area'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)

            def statistic_E8_area(area):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format

                # Check if the school is selecte:d


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find female students with menstrual pain who have started menstruation
                    cursor.execute(
                        """SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE E8_menstrual_pain = 'yes' 
                             AND Gender = 'female' 
                             AND tea_garden = ? 
                             AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if statistic_sick == 0:
                        # Update the statistic label to show no female students with menstrual pain
                        statistic_label.config(
                            text='0% of female students that have started menstrual cycle have menstrual pain'
                        )
                    else:
                        # Query to get the total number of female students who have started menstruation
                        cursor.execute(
                            """SELECT id 
                               FROM student 
                               WHERE E4_Menarke = 'yes' 
                                 AND Gender = 'female' 
                                 AND tea_garden = ?
                                 AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        total_female_students = cursor.fetchall()  # Fetch all IDs
                        total_student = len(total_female_students)  # Count them

                        # Calculate percentage
                        percentage = round(statistic_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(
                            text=f'{percentage}% ({statistic_sick} / {total_student}) of female students that have started menstruation have menstrual pain'
                        )

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)


            def statistic_BMI_area(sickness, condition, area, problem):
                # Get the selected date from the screening_date widget
                selected_year = screening_year.get()  # Assuming this returns the date in the correct format


                # Check if a date is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Query to find students with the specified sickness and school on the selected date
                    cursor.execute(f""" SELECT id, name, school_name, tea_garden 
                                       FROM student 
                                       WHERE {sickness} = ? 
                                         AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                                   (condition, area, selected_year)
                                   )
                    result = cursor.fetchall()
                    total_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    if total_sick == 0:
                        # Update the statistic label to show no students with the issue
                        statistic_label.config(text=f'0% of students aged 5 to 18 years have {problem}')
                    else:
                        # Query to get the total number of students in the school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE age_in_month BETWEEN 61 AND 216 
                                AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )

                        total_students = cursor.fetchall()  # Fetch all IDs
                        total_student = len(total_students)  # Count them

                        # Calculate percentage
                        percentage = round(total_sick / total_student * 100, 1)

                        # Update the statistic label with the calculated percentage
                        statistic_label.config(text=f'{percentage}% ({total_sick} / {total_student}) of students aged 5 to 18 years have {problem}')

                        # Insert new data into the Treeview
                        for item in result:
                            show_record_tree.insert("", "end", values=(
                                item[0], item[1], item[2]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)
            def handle_area_record(area, sickness, problem):
                """Process and display statistics for students with a specific sickness at a given school and year."""

                selected_year = screening_year.get()  # Get the selected screening date from the combobox

                # Check if a year is selected
                if not selected_year:
                    messagebox.showerror("Error", "Please select a year.", parent=statistic_window)
                    return

                try:
                    # Execute query to find students with the specified sickness and selected date
                    cursor.execute(
                        f"""SELECT id, name, school_name, tea_garden 
                           FROM student 
                           WHERE {sickness} = 'yes' 
                           AND tea_garden = ? 
                           AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                        (area, selected_year)
                    )

                    result = cursor.fetchall()
                    statistic_sick = len(result)

                    # Clear previous entries in the Treeview
                    show_record_tree.delete(*show_record_tree.get_children())

                    # Calculate the statistic text
                    if statistic_sick == 0:
                        statistic_text = f'0% of students have {problem}'
                    else:
                        # Query to find total students in the specified school on the selected date
                        cursor.execute(
                            """SELECT oid 
                               FROM student 
                               WHERE tea_garden = ? 
                               AND '20' || SUBSTR(screen_date, 7, 2) = ?""",
                            (area, selected_year)
                        )
                        student = cursor.fetchall()
                        total_student = len(student)

                        # Check if there are no students to avoid division by zero
                        if total_student == 0:
                            statistic_text = f'No students recorded for {problem} at {school}.'
                        else:
                            # Calculate percentage
                            percentage = round(statistic_sick / total_student * 100, 1)
                            statistic_text = f'{percentage}% ({statistic_sick} / {total_student}) of students have {problem}'

                    # Update the existing label (assuming `statistic_label` is defined elsewhere)
                    statistic_label.config(text=statistic_text)

                    # Insert new data into the Treeview
                    for item in result:
                        show_record_tree.insert("", "end",
                                                values=(item[0], item[1], item[2],item[3]))  # Assuming item[2] is school_name

                except Exception as e:
                    messagebox.showerror("Database Error", f"An error occurred: {e}", parent=statistic_window)


            # Dictionary to map records to their corresponding function
            function_mapping_all_schools = {
                "Weight for age: moderately underweight": lambda: weight_age_statistic("moderately underweight"),
                "Weight for age: severely underweight": lambda: weight_age_statistic("severely underweight"),
                "Height for age: chronic malnutrition": height_age_cm_all,
                "Weight for height: moderate acute malnutrition": lambda: weight_height_statistic("moderate acute malnutrition"),
                "Weight for height: severe acute malnutrition": lambda: weight_height_statistic("severe acute malnutrition"),
                "Vision problem (objective)": vision_problem_all,
                "BMI severe underweight": lambda: statistic_bmi("severe underweight"),
                "BMI underweight": lambda: statistic_bmi("underweight"),
                "BMI overweight": lambda: statistic_bmi("overweight"),
                "Has done deworming": lambda: statistic_all(sickness="deworming", problem="been dewormed last 6 months"),
                "Has done immunization": lambda: statistic_all(sickness="vaccination",
                                                                                 problem="been in Government Childhood Vaccination Program"),
                "B1: signs of anemia": lambda: statistic_all(sickness="B1_severe_anemia", problem="signs of anemia"),
                "B2: signs of Vit. A deficiency": lambda: statistic_all(sickness="B2_Vita_A_deficiency",
                                                              problem="signs of Vit A deficiency"),
                "B3: signs of Vit D deficiency": lambda: statistic_all(sickness="B3_Vit_D_deficiency",
                                                             problem="signs of Vit D deficiency"),
                "B4: goitre": lambda: statistic_all(sickness="B4_Goitre", problem="goitre"),
                "B5: oedema": B5_Oedema_all,
                "C1: Convulsive disorder": lambda: statistic_all(sickness="C1_convulsive_dis",
                                                           problem="convulsive disorder"),
                "C2: Otitis media/ear infection": lambda: statistic_all(sickness="C2_otitis_media", problem="otitis media/ear infection"),
                "C3: Dental problem": lambda: statistic_all(sickness="C3_dental_condition",
                                                             problem="dental problem"),
                "C4: Skin problem": lambda: statistic_all(sickness="C4_skin_condition", problem="skin problem"),
                "C5: Heart murmur": lambda: statistic_all(sickness="C5_rheumatic_heart_disease",
                                                                    problem="heart murmur"),
                "C6: Respiratory problem": lambda: statistic_all(sickness="C6_others_TB_asthma", problem="respiratory problem"),
                "D1: Difficulty seeing": lambda: statistic_all(sickness="D1_difficulty_seeing",
                                                              problem="difficulty seeing"),
                "D2: Delay in walking": lambda: statistic_all(sickness="D2_delay_in_walking", problem="delay in  walking"),
                "D3: Stiffness/floppiness/reduced strength": lambda: statistic_all(sickness="D3_stiffness_floppiness",
                                                                 problem="stiffness/floppiness/reduced strength"),

                "D5: Difficulty in reading/writing/calculating": lambda: statistic_all(
                    sickness="D5_reading_writing_calculatory_difficulty",
                    problem="difficulty in reading/writing/calculating"),
                "D6: Difficulty speaking": lambda: statistic_all(sickness="D6_speaking_difficulty",
                                                                problem="difficulty speaking"),
                "D7: Difficulty hearing": lambda: statistic_all(sickness="D7_hearing_problems",
                                                             problem="difficulty hearing"),
                "D8: Difficulty in learning new things": lambda: statistic_all(sickness="D8_learning", problem="difficulty in learning new things"),
                "D9: Difficulty sustaining attention": lambda: statistic_all(sickness="D9_attention", problem="difficulty sustaining attention"),
                "E3: Signs of depression": lambda: statistic_all(sickness="E3_depression_sleep",
                                                             problem="depression or sleep problems"),
                "E4: Started period (menarche)": statistic_E4_all,
                "E5: Has regular period": statistic_E5_all,
                "E6: Has pain or burning while urinating": statistic_E6_all,
                "E7: Has discharge/ foul smell from genito-urinary area": statistic_E7_all,
                "E8: Has menstrual pain": statistic_E8_all,
                "MUAC: Have SAM based on MUAC": muac_all}
            function_mapping_school_specific = {
                "Weight for age: moderately underweight": lambda school: weight_age_mu_school(school),
                "Weight for age: severely underweight": lambda school: weight_age_su_school(school),
                "Height for age: chronic malnutrition": lambda school: height_age_cm_school(school),
                "Weight for height: moderate acute malnutrition": lambda school: weight_height_mam_school(school),
                "Weight for height: severe acute malnutrition": lambda school: weight_height_sam_school(school),
                "Vision problem (objective)": lambda school: vision_problem_school(school),
                "BMI severe underweight": lambda school: statistic_BMI('BMI_category', 'severe underweight', school, "severe underweight"),
                "BMI underweight": lambda school: statistic_BMI('BMI_category', 'underweight', school,
                                                                       "underweight"),
                "BMI overweight": lambda school: statistic_BMI('BMI_category', 'overweight', school, 'overweight'),

                "Has done deworming": lambda school: handle_school_record(school, "deworming", "been dewormed last 6 months"),
                "Has done immunization": lambda school: handle_school_record(school, "vaccination",
                                                                                               "been in Government Childhood Vaccination Program"),
                "B1: signs of anemia": lambda school: handle_school_record(school, "B1_severe_anemia", "severe anemia"),
                "B2: signs of Vit. A deficiency": lambda school: handle_school_record(school, "B2_Vita_A_deficiency",
                                                                            "signs of Vit. A deficiency"),
                "B3: signs of Vit D deficiency": lambda school: handle_school_record(school, "B3_Vit_D_deficiency",
                                                                           "signs of Vit. D deficiency"),
                "B4: goitre": lambda school: handle_school_record(school, "B4_Goitre", "goitre"),
                "B5: oedema": lambda school: B5_Oedema_school(school),
                "C1: Convulsive disorder": lambda school: handle_school_record(school, "C1_convulsive_dis",
                                                                         "convulsive disorder"),
                "C2: Otitis media/ear infection": lambda school: handle_school_record(school, "C2_otitis_media", "otitis media/ear infection"),
                "C3: Dental problem": lambda school: handle_school_record(school, "C3_dental_condition",
                                                                           "dental problem"),
                "C4: Skin problem": lambda school: handle_school_record(school, "C4_skin_condition", "skin problem"),
                "C5: Heart murmur": lambda school: handle_school_record(school, "C5_rheumatic_heart_disease",
                                                                                  "heart murmur"),
                "C6: Respiratory problem": lambda school: handle_school_record(school, "C6_others_TB_asthma",
                                                                           "respiratory problem"),
                "D1: Difficulty seeing": lambda school: handle_school_record(school, "D1_difficulty_seeing",
                                                                            "difficulty seeing"),
                "D2: Delay in walking": lambda school: handle_school_record(school, "D2_delay_in_walking",
                                                                           "delay in walking"),
                "D3: Stiffness/floppiness/reduced strength": lambda school: handle_school_record(school, "D3_stiffness_floppiness",
                                                                               "stiffness/floppiness/reduced strength"),

                "D5: Difficulty in reading/writing/calculating": lambda school: handle_school_record(school,
                                                                                                 "D5_reading_writing_calculatory_difficulty",
                                                                                                 "difficulty in reading/writing/calculationg"),
                "D6: Difficulty speaking": lambda school: handle_school_record(school, "D6_speaking_difficulty",
                                                                              "difficulty in speaking"),
                "D7: Difficulty hearing": lambda school: handle_school_record(school, "D7_hearing_problems",
                                                                           "difficulty hearing"),
                "D8: Difficulty in learning new things": lambda school: handle_school_record(school, "D8_learning", "difficulty learning new things"),
                "D9: Difficulty sustaining attention": lambda school: handle_school_record(school, "D9_attention", "difficulty sustaining attention"),
                "E3: Signs of depression": lambda school: handle_school_record(school, "E3_depression_sleep",
                                                                           "depression or sleep problems"),
                "E4: Started period (menarche)": lambda school: statistic_E4_school(school),
                "E5: Has regular period": lambda school: statistic_E5_school(school),
                "E6: Has pain or burning while urinating": lambda school: statistic_E6_school(school),
                "E7: Has discharge/ foul smell from genito-urinary area": lambda school: statistic_E7_school(school),
                "E8: Has menstrual pain": lambda school: statistic_E8_school(school),
                "MUAC: Have SAM based on MUAC": lambda school: muac_school(school)}

            function_mapping_area_specific = {
                "Weight for age: moderately underweight": lambda area: print(
                    "Moderately Underweight") or weight_age_area(area, "moderately underweight"),
                "Weight for age: severely underweight": lambda area: print("Severely Underweight") or weight_age_area(
                    area, "severely underweight"),
                "Height for age: chronic malnutrition": lambda area: height_age_cm_area(area),
                "Weight for height: moderate acute malnutrition": lambda area: weight_height_mam_area(area),
                "Weight for height: severe acute malnutrition": lambda area: weight_height_sam_area(area),
                "VISION_problem": lambda area: vision_problem_area(area),
                "BMI severe underweight": lambda area: statistic_BMI_area('BMI_category', 'severe underweight', area,
                                                                     "severe underweight"),
                "BMI underweight": lambda area: statistic_BMI_area('BMI_category', 'underweight', area, "underweight"),
                "BMI overweight": lambda area: statistic_BMI_area('BMI_category', 'overweight', area, 'overweight'),

                "Has done deworming": lambda area: handle_area_record(area, "deworming", "been dewormed last 6 months"),
                "Has done immunization": lambda area: handle_area_record(area, "vaccination",
                                                                                           "been in Government Childhood Vaccination Program"),
                "B1: signs of anemia": lambda area: handle_area_record(area, "B1_severe_anemia", "signs of anemia"),
                "B2: signs of Vit. A deficiency": lambda area: handle_area_record(area, "B2_Vita_A_deficiency",
                                                                        "Vitamin A deficiency"),
                "B3: signs of Vit D deficiency": lambda area: handle_area_record(area, "B3_Vit_D_deficiency",
                                                                       "Vitamin D deficiency"),
                "B4: goitre": lambda area: handle_area_record(area, "B4_Goitre", "Goitre"),
                "B5: oedema": lambda area: B5_Oedema_area(area),
                "C1: Convulsive disorder": lambda area: handle_area_record(area, "C1_convulsive_dis",
                                                                     "convulsive disorders/epilepsy"),
                "C2: Otitis media/ear infection": lambda area: handle_area_record(area, "C2_otitis_media", "otitis media"),
                "C3: Dental problem": lambda area: handle_area_record(area, "C3_dental_condition", "dental condition"),
                "C4: Skin problem": lambda area: handle_area_record(area, "C4_skin_condition", "skin condition"),
                "C5: Heart murmur": lambda area: handle_area_record(area, "C5_rheumatic_heart_disease",
                                                                              "heart murmur"),
                "C6: Respiratory problem": lambda area: handle_area_record(area, "C6_others_TB_asthma", "breathing difficulty"),
                "D1: Difficulty seeing": lambda area: handle_area_record(area, "D1_difficulty_seeing",
                                                                        "difficulty seeing"),
                "D2: Delay in walking": lambda area: handle_area_record(area, "D2_delay_in_walking", "delay walking"),
                "D3: Stiffness/floppiness/reduced strength": lambda area: handle_area_record(area, "D3_stiffness_floppiness",
                                                                           "stiffness or floppiness"),
                "D5: Difficulty in reading/writing/calculating": lambda area: handle_area_record(area,
                                                                                             "D5_reading_writing_calculatory_difficulty",
                                                                                             "reading/writing or calculatory difficulty"),
                "D6: Difficulty speaking": lambda area: handle_area_record(area, "D6_speaking_difficulty",
                                                                          "speaking difficulty"),
                "D7: Difficulty hearing": lambda area: handle_area_record(area, "D7_hearing_problems", "hearing problems"),
                "D8: Difficulty in learning new things": lambda area: handle_area_record(area, "D8_learning", "learning problems"),
                "D9: Difficulty sustaining attention": lambda area: handle_area_record(area, "D9_attention", "attention problems"),
                "E3: Signs of depression": lambda area: handle_area_record(area, "E3_depression_sleep",
                                                                       "depression or sleep problems"),
                "E4: Started period (menarche)": lambda area: statistic_E4_area(area),
                "E5: Has regular period": lambda area: statistic_E5_area(area),
                "E6: Has pain or burning while urinating": lambda area: statistic_E6_area(area),
                "E7: Has discharge/ foul smell from genito-urinary area": lambda area: statistic_E7_area(area),
                "E8: Has menstrual pain": lambda area: statistic_E8_area(area),
                "MUAC: Have SAM based on MUAC": lambda area: muac_area(area)}


            # General function to handle the record based on the school
            def process_record(selected_key, school_selected=None, area_selected=None):
                print(
                    f"Selection: School={school_selected}, Area={area_selected}, Key={selected_key}")  # Debugging line

                if area_selected:
                    # Map selected_key to area-specific functions
                    function_to_call = function_mapping_area_specific.get(selected_key)
                    if function_to_call:
                        function_to_call(area_selected)  # Call with area argument
                    else:
                        print(f"No function mapped for {selected_key} in area {area_selected}")
                elif school_selected == "All schools combined":
                    # Call for all schools without a specific argument
                    function_to_call = function_mapping_all_schools.get(selected_key)
                    if function_to_call:
                        function_to_call()
                    else:
                        print(f"No function mapped for {selected_key} in All schools combined")
                elif school_selected:
                    # Map selected_key to school-specific functions
                    function_to_call = function_mapping_school_specific.get(selected_key)
                    if function_to_call:
                        function_to_call(school_selected)
                    else:
                        print(f"No function mapped for {selected_key} in {school_selected}")
                else:
                    print(
                        "No valid selection for area or school.")  # Handle case where neither area nor school is selected

            # Get user selection from the Comboboxes
            selected_sickness = sickness_search.get()
            selected_school = school_options.get()  # Get selected school, if any
            selected_area = area_options.get()  # Get selected area, if any

            # Call the process_record function with the selected sickness, school, or area
            if selected_area:
                process_record(selected_sickness, area_selected=selected_area)
            elif selected_school:
                process_record(selected_sickness, school_selected=selected_school)
            else:
                print("No area or school selected, cannot process the record.")

            # SET UP WINDOW
        statistic_window = Toplevel(window)
        connection = sqlite3.connect("gracehealth.db")
        cursor = connection.cursor()

        statistic_window.geometry("5000x5000")
        statistic_window.title("Getting information from students")

        #SET UP FRAMES
        topframe = Frame(statistic_window)
        topframe.grid(row=1, rowspan=3)
        secondframe = Frame(statistic_window)
        secondframe.grid(row=4)
        from tkinter import StringVar
        from tkinter import ttk

        # Create a StringVar for storing the selected sickness
        sickness_search = StringVar()

        # List of options for the Combobox
        sickness_options = [
            "Weight for age: moderately underweight",
            "Weight for age: severely underweight",
            "Height for age: chronic malnutrition",
            "Weight for height: moderate acute malnutrition",
            "Weight for height: severe acute malnutrition",
            "Vision problem (objective)",
            "BMI severe underweight",
            "BMI underweight",
            "BMI overweight",
            "B1: signs of anemia",
            "B2: signs of Vit. A deficiency",
            "B3: signs of Vit D deficiency",
            "B4: goitre",
            "B5: oedema",
            "C1: Convulsive disorder",
            "C2: Otitis media/ear infection",
            "C3: Dental problem",
            "C4: Skin problem",
            "C5: Heart murmur",
            "C6: Respiratory problem",
            "D1: Difficulty seeing",
            "D2: Delay in walking",
            "D3: Stiffness/floppiness/reduced strength",
            "D5: Difficulty in reading/writing/calculating",
            "D6: Difficulty speaking",
            "D7: Difficulty hearing",
            "D8: Difficulty in learning new things",
            "D9: Difficulty sustaining attention",
            "E3: Signs of depression",
            "E4: Started period (menarche)",
            "E5: Has regular period",
            "E6: Has pain or burning while urinating",
            "E7: Has discharge/ foul smell from genito-urinary area",
            "E8: Has menstrual pain",
            "Has done deworming",
            "Has done immunization",
            "MUAC: Have SAM based on MUAC"
        ]

        def reset_other_combobox(selected_combobox):
            # Clear the opposite combobox based on the selected combobox
            if selected_combobox == "school":
                area_options.set("")  # Clear area combobox if school is selected
            elif selected_combobox == "area":
                school_options.set("")  # Clear school combobox if area is selected
        # Create a Combobox
        sickness_combo = ttk.Combobox(topframe, textvariable=sickness_search, values=sickness_options,width=50)
        sickness_combo.grid(row=1, column=2)

        # Optionally set a default value
        sickness_combo.current(0)  # Set the first item as default
        school_label = Label(topframe, text="SCHOOL:   ").grid(row=2, column=1)


        school_options = ttk.Combobox(topframe,values=school_database_list,width=50)
        school_options.grid(row=2, column=2)
        school_options.bind("<<ComboboxSelected>>", lambda e: reset_other_combobox("school"))

        area_label = Label(topframe, text="AREA:   ").grid(row=3, column=1)

        area_options = ttk.Combobox(topframe, values=tea_garden_database_list, width=50)
        area_options.grid(row=3, column=2)
        area_options.bind("<<ComboboxSelected>>", lambda e: reset_other_combobox("area"))


        # Function to populate the Combobox with screening dates from the database
        from datetime import datetime

        def populate_screening_years():
            try:
                # Connect to the database
                connection = sqlite3.connect("gracehealth.db")
                cursor = connection.cursor()

                # Query to extract the year from the mm/dd/yy format using SUBSTR
                cursor.execute("""
                    SELECT DISTINCT '20' || SUBSTR(screen_date, -2) as year
                    FROM student
                    WHERE screen_date LIKE '__/__/__'
                    ORDER BY year DESC
                """)

                years = cursor.fetchall()

                if not years:
                    print("No years found in the database.")
                else:
                    print("Years fetched:", years)  # Debugging

                # Extract the years from the fetched tuples and populate the list
                year_list = [year[0] for year in years]

                # Close the database connection
                connection.close()

                # Populate the combobox with the retrieved years
                screening_year['values'] = year_list
                if year_list:
                    screening_year.current(0)  # Optionally select the most recent year by default
                else:
                    screening_year['values'] = ['No data available']  # Handle the case where no years are found
            except sqlite3.Error as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Error: {e}")


        # Function to generate the summary statistics

        # Screening year label
        screening_label = Label(topframe, text="Screening Year:")
        screening_label.grid(row=0, column=1)

        # Create a Combobox for screening years
        screening_year = ttk.Combobox(topframe, width=50)
        screening_year.grid(row=0, column=2)





        # Call the process_record function with the selected sickness and school

        # Populate the screening year combobox
        populate_screening_years()

        # Run the main event loop
        search_label = Label(topframe, text="SICKNESS:   ")
        search_label.grid(row=1, column=1)
        statistic_label = Label(topframe, text="")  # Initially empty
        statistic_label.grid(row=4, column=1,columnspan=3)
        from tkinter import ttk
        # Create a Treeview widget
        show_record_tree = ttk.Treeview(secondframe, columns=("id", "name", "school", "area"), show='headings',
                                        height=10)
        show_record_tree.grid(row=5, column=1, padx=20, pady=10)
        # Define column headings
        show_record_tree.heading("id", text="ID")
        show_record_tree.heading("name", text="Name")
        show_record_tree.heading("school", text="School")
        show_record_tree.heading("area", text="Area")
        # Set column widths
        show_record_tree.column("id", width=100, anchor='center')
        show_record_tree.column("name", width=150, anchor='w')
        show_record_tree.column("school", width=350, anchor='w')
        show_record_tree.column("area", width=300, anchor='center')
        # Example: populate Treeview with data (fetch this data from your database)
        # If you want to delete previous entries and refresh the Treeview before inserting new records:
        show_button = ttk.Button(topframe, text="show record", command=show_record_function)
        show_button.grid(row=3, column=3, columnspan=2)

        connection.commit()
        connection.close()
        statistic_window.mainloop()

    from tkinter import Tk, Toplevel, Frame, Canvas, Scrollbar, Button, Label, BOTH, LEFT, RIGHT, Y, VERTICAL, W
    def create_scrollable_frame(parent):
        # Create a frame for the canvas and scrollbar
        container = Frame(parent)
        container.pack(fill=BOTH, expand=True)

        # Create a canvas
        canvas = Canvas(container)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)

        # Add a scrollbar to the canvas
        scrollbar = Scrollbar(container, orient=VERTICAL, command=canvas.yview)
        scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the canvas
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))

        # Create a frame inside the canvas to hold the widgets
        scrollable_frame = Frame(canvas)

        # Add that new frame to a window in the canvas
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

        return scrollable_frame

    # Main window setup
    import tkinter as tk
    from tkinter import ttk
    import sqlite3

    # Initialize the main window
    import tkinter as tk
    from tkinter import ttk
    import tkinter as tk
    from tkinter import ttk

    # Initialize the main window
    window = tk.Tk()
    window.title("Create new student journals")

    # Set window size to 90% of the screen dimensions for better scaling on smaller screens
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window_width = int(screen_width)
    window_height = int(screen_height * 0.9)
    x_position = (screen_width - window_width) // 2
    y_position = (screen_height - window_height) // 2
    window.geometry(f"{window_width}x{window_height}+{5}+{5}")

    # Configure the window grid
    window.grid_columnconfigure(0, weight=1)
    window.grid_rowconfigure(0, weight=1)

    # Create a Canvas and Scrollbars for a scrollable frame
    canvas = tk.Canvas(window)
    h_scrollbar = ttk.Scrollbar(window, orient="horizontal", command=canvas.xview)
    v_scrollbar = ttk.Scrollbar(window, orient="vertical", command=canvas.yview)
    scrollable_frame = ttk.Frame(canvas)

    # Configure canvas scrolling
    canvas.configure(xscrollcommand=h_scrollbar.set, yscrollcommand=v_scrollbar.set)

    # Place scrollbars and canvas in the main window
    canvas.grid(row=0, column=0, sticky="nsew")
    v_scrollbar.grid(row=0, column=1, sticky="ns")
    h_scrollbar.grid(row=1, column=0, sticky="ew")

    # Add the scrollable frame inside the canvas
    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

    # Update the scroll region whenever the scrollable frame's size changes
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    # Updated create_labeled_frame function to accept rowspan
    def create_labeled_frame(parent, text, row, col, colspan=1, rowspan=1, sticky="ew"):
        frame = ttk.LabelFrame(parent, text=text)
        frame.grid(row=row, column=col, columnspan=colspan, rowspan=rowspan, sticky=sticky, padx=10, pady=5)
        return frame

    # Fixed buttonframe (does not expand vertically)
    buttonframe = create_labeled_frame(scrollable_frame, "Button Frame", 0, 0, colspan=2, sticky="ew")

    # Expanding frames below the buttonframe
    topframe = create_labeled_frame(scrollable_frame, "Top Frame", 1, 0, colspan=2, sticky="nsew")
    secondframe = create_labeled_frame(scrollable_frame, "Second Frame", 2, 0, colspan=2, sticky="nsew")
    sicknessframe = create_labeled_frame(scrollable_frame, "Sickness Frame", 3, 0, colspan=2, sticky="nsew")

    # Journal Summary Frame on the right side, spans 4 rows
    summary_frame = create_labeled_frame(scrollable_frame, "Journal Summary", 0, 2, rowspan=4, sticky="nsew")

    # Configure the row for buttonframe to be fixed
    scrollable_frame.grid_rowconfigure(0, weight=0)

    # Configure rows below buttonframe to expand
    scrollable_frame.grid_rowconfigure(1, weight=1)
    scrollable_frame.grid_rowconfigure(2, weight=1)
    scrollable_frame.grid_rowconfigure(3, weight=1)

    # Configure columns to separate summary_frame from others
    scrollable_frame.grid_columnconfigure(0, weight=1)  # Left side expands
    scrollable_frame.grid_columnconfigure(1, weight=1)
    scrollable_frame.grid_columnconfigure(2, weight=1)  # Summary frame column expands independently

    # Text widget in summary frame
    journal_summary_text = tk.Text(summary_frame, height=10,width=40)
    journal_summary_text.grid(row=0, column=0, sticky="nsew")
    journal_summary_text.insert(tk.END, "Summary text")
    journal_summary_text.config(state=tk.DISABLED)

    # Ensure the summary frame fills remaining space independently
    summary_frame.grid_rowconfigure(0, weight=1)
    summary_frame.grid_columnconfigure(0, weight=1)



    connection = sqlite3.connect("gracehealth.db")
    cursor = connection.cursor()

    import sqlite3
    import tkinter as tk
    from tkinter import ttk, messagebox

    import sqlite3
    import tkinter as tk
    from tkinter import Toplevel, messagebox, ttk, Frame, LabelFrame

    def school_list():
        def edit_last_journal():
            selected_item = tree.selection()
            if not selected_item:
                return
            item_id = tree.item(selected_item[0], 'values')[0]
            clear_text()
            populate_for_edit(item_id)
            display_journal(item_id, summary_frame)
            school_window.destroy()

        def add_journal():
            selected_item = tree.selection()
            if not selected_item:
                return
            item_id = tree.item(selected_item[0], 'values')[0]
            clear_text()

            populate_for_new_journal(item_id)
            display_journal(item_id, summary_frame)
            school_window.destroy()

        def delete_row():
            selected_item = tree.focus()
            if selected_item:
                confirmation = messagebox.askyesno(parent=school_window,
                                                   message="Are you sure you want to delete this student?")
                if confirmation:
                    connection = sqlite3.connect("gracehealth.db")
                    cursor = connection.cursor()
                    row_id = tree.item(selected_item)['values'][0]
                    cursor.execute("DELETE FROM student WHERE id=?", (row_id,))
                    connection.commit()
                    connection.close()
                    refresh_records()  # Refresh the Treeview
                    messagebox.showinfo(parent = main_window_school_list,title="Success",message= "Row deleted successfully")
            else:
                messagebox.showwarning(parent = main_window_school_list,title="Warning",message= "Please select a row to delete")

        def flag_as_graduated():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a student to flag as graduated.")
                return
            item_id = tree.item(selected_item[0], 'values')[0]
            confirmation = messagebox.askyesno(parent=school_window,
                                               message="Are you sure you want to flag this student as 'Graduated'?")
            if confirmation:
                try:
                    connection = sqlite3.connect('gracehealth.db')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE student SET status = 'graduated' WHERE id = ?", (item_id,))
                    connection.commit()
                    connection.close()
                    refresh_records()  # Refresh the Treeview after update
                    messagebox.showinfo("Success", "Student flagged as 'Graduated'.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating status: {e}")

        def change_to_active():
            selected_item = tree.selection()
            if not selected_item:
                messagebox.showwarning("Warning", "Please select a student to change status to active.")
                return
            item_id = tree.item(selected_item[0], 'values')[0]
            confirmation = messagebox.askyesno(parent=school_window,
                                               message="Are you sure you want to change this student's status to 'Active'?")
            if confirmation:
                try:
                    connection = sqlite3.connect('gracehealth.db')
                    cursor = connection.cursor()
                    cursor.execute("UPDATE student SET status = 'active' WHERE id = ?", (item_id,))
                    connection.commit()
                    connection.close()
                    refresh_records()  # Refresh the Treeview after update
                    messagebox.showinfo("Success", "Student status changed to 'Active'.")
                except Exception as e:
                    messagebox.showerror("Error", f"Error updating status: {e}")


        def search_school(event=None):
            school_name_filter = search_school_entry.get() if search_school_entry.get() else ""
            gender_filter = gender_filter_var.get()
            student_name_filter = search_name_entry.get() if search_name_entry.get() else ""
            status_filter = status_filter_var.get().lower()  # "active" or "graduated"
            area_filter = area_filter_var.get() if area_filter_var.get() else ""
            age_filter = age_filter_var.get()  # Get the selected age range

            refresh_records(school_name_filter, gender_filter, student_name_filter, status_filter, area_filter,
                            age_filter)

        school_window = Toplevel(window)
        school_window.geometry("1300x600+10+10")

        frame = Frame(school_window)
        frame.place(x=100, y=70)
        frame2 = LabelFrame(school_window)
        frame2.place(x=100, y=20)
        frame3 = LabelFrame(school_window)
        frame3.place(x=100, y=550)

        tree = ttk.Treeview(frame, columns=("ID", "Name", "School Name", "Gender"), show="headings", height=20)
        tree.heading("ID", text="ID")
        tree.heading("Name", text="Name")
        tree.heading("School Name", text="School Name")
        tree.heading("Gender", text="Gender")
        tree.column("ID", width=100, anchor="center")
        tree.column("Name", width=200, anchor="w")
        tree.column("School Name", width=300, anchor="w")
        tree.column("Gender", width=100, anchor="center")
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(frame, command=tree.yview)
        scrollbar.grid(row=0, column=1, sticky='ns')
        tree.config(yscrollcommand=scrollbar.set)

        edit_journal_button = ttk.Button(frame3, text="Edit last screening", command=edit_last_journal)
        edit_journal_button.grid(row=0, column=0, padx=10)
        add_journal_button = ttk.Button(frame3, text="Add new screening", command=add_journal)
        add_journal_button.grid(row=0, column=1)

        flag_graduated_button = ttk.Button(frame3, text="Flag as Graduated", command=flag_as_graduated)
        flag_graduated_button.grid(row=0, column=2, padx=10)

        delete_button = ttk.Button(frame3, text="Delete", command=delete_row)
        delete_button.grid(row=0, column=3, padx=10)

        change_active_button = ttk.Button(frame3, text="Change to Active", command=change_to_active)
        change_active_button.grid(row=0, column=4, padx=10)

        search_label = tk.Label(frame2, text="Search School Name")
        search_label.grid(row=1, column=0, sticky='w')

        connection = sqlite3.connect('gracehealth.db')
        cursor = connection.cursor()
        cursor.execute("SELECT DISTINCT school_name FROM student")
        school_names = [row[0] for row in cursor.fetchall()]
        school_names.append("All students")

        cursor.execute("SELECT DISTINCT tea_garden FROM student")
        area_list = [row[0] for row in cursor.fetchall()]
        area_list.append("All areas")
        connection.close()

        # Add a new combobox for area filter in frame2
        area_filter_var = tk.StringVar(value="All areas")
        area_filter_label = tk.Label(frame2, text="Filter by Area:")
        area_filter_label.grid(row=1, column=4, sticky='w')

        area_filter_combobox = ttk.Combobox(frame2, textvariable=area_filter_var, values=area_list, width=20)
        area_filter_combobox.grid(row=2, column=4)
        area_filter_combobox.bind("<<ComboboxSelected>>", search_school)
        search_school_entry = ttk.Combobox(frame2, values=school_names, width=50)
        search_school_entry.grid(row=1, column=1)
        search_school_entry.bind("<<ComboboxSelected>>", search_school)

        gender_filter_var = tk.StringVar(value="all")
        gender_filter_label = tk.Label(frame2, text="Select Gender:")
        gender_filter_label.grid(row=1, column=2, sticky='w')

        gender_filter_combobox = ttk.Combobox(frame2, textvariable=gender_filter_var, values=["all", "male", "female"],
                                              width=20)
        gender_filter_combobox.grid(row=2, column=2)
        gender_filter_combobox.bind("<<ComboboxSelected>>", search_school)

        age_filter_var = tk.StringVar(value="All ages")
        age_filter_label = tk.Label(frame2, text="Filter by Age (Years):")
        age_filter_label.grid(row=1, column=5, sticky='w')

        age_filter_combobox = ttk.Combobox(frame2, textvariable=age_filter_var,
                                           values=["All ages"] + [str(i) for i in range(2, 19)], width=20)
        age_filter_combobox.grid(row=2, column=5)
        age_filter_combobox.bind("<<ComboboxSelected>>", search_school)

        # Add a class filter Combobox to your GUI
        class_filter_var = tk.StringVar()
        class_filter_label = tk.Label(frame2, text="Filter by Class:")
        class_filter_label.grid(row=1,column=6)
        class_combobox = ttk.Combobox(frame2, textvariable=class_filter_var)
        class_combobox['values'] = ['All Classes'] + [str(i) for i in range(1, 13)]  # Classes 1 to 12
        class_combobox.current(0)  # Default to "All Classes"
        class_combobox.grid(row=2, column=6, padx=10, pady=5)  # Adjust the grid placement as needed

        def on_class_filter_change(event):
            class_filter = class_filter_var.get()
            refresh_records(class_filter=class_filter)

        class_combobox.bind("<<ComboboxSelected>>", on_class_filter_change)

        status_filter_var = tk.StringVar(value="active")
        status_filter_label = tk.Label(frame2, text="Filter by Status:")
        status_filter_label.grid(row=1, column=3, sticky='w')

        status_filter_combobox = ttk.Combobox(frame2, textvariable=status_filter_var, values=["Active", "Graduated"],
                                              width=20)
        status_filter_combobox.grid(row=2, column=3)
        status_filter_combobox.bind("<<ComboboxSelected>>", search_school)

        name_search_label = tk.Label(frame2, text="Search Student Name")
        name_search_label.grid(row=2, column=0, sticky='w')

        search_name_entry = ttk.Entry(frame2, width=50)
        search_name_entry.grid(row=2, column=1)
        search_name_entry.bind("<Return>", search_school)
        # Add a label to show the total number of students
        total_students_var = tk.StringVar(value="Total Students: 0")
        total_students_label = tk.Label(school_window, textvariable=total_students_var, font=("Arial", 12, "bold"))
        total_students_label.place(x=100, y=520)  # Adjust the position as needed

        def refresh_records(school_name_filter="", gender_filter="", student_name_filter="", status_filter="active",
                            area_filter="", age_filter="All ages", class_filter="All Classes"):
            try:
                # Open a new database connection
                connection = sqlite3.connect('gracehealth.db')
                cursor = connection.cursor()

                # Clear the Treeview
                for item in tree.get_children():
                    tree.delete(item)

                # Build the SQL query with filters
                query = """
                           SELECT s.id, s.name, s.school_name, s.gender, s.Class_section
                           FROM student s
                           WHERE s.status = ?
                             AND '20' || SUBSTR(s.screen_date, 7, 2) || '-' || SUBSTR(s.screen_date, 1, 2) || '-' || SUBSTR(s.screen_date, 4, 2) = (
                                 SELECT MAX('20' || SUBSTR(inner_s.screen_date, 7, 2) || '-' || SUBSTR(inner_s.screen_date, 1, 2) || '-' || SUBSTR(inner_s.screen_date, 4, 2))
                                 FROM student inner_s
                                 WHERE inner_s.id = s.id)
                """
                params = [status_filter]

                # Add filters dynamically
                if school_name_filter and school_name_filter != "All students":
                    query += " AND s.school_name LIKE ?"
                    params.append('%' + school_name_filter + '%')

                if gender_filter and gender_filter != "all":
                    query += " AND s.gender = ?"
                    params.append(gender_filter)

                if student_name_filter:
                    query += " AND s.name LIKE ?"
                    params.append('%' + student_name_filter + '%')

                if area_filter and area_filter != "All areas":
                    query += " AND s.tea_garden = ?"
                    params.append(area_filter)

                if age_filter and age_filter != "All ages":
                    min_age_in_months = int(age_filter) * 12
                    max_age_in_months = (int(age_filter) + 1) * 12 - 1
                    query += " AND s.age_in_month BETWEEN ? AND ?"
                    params.extend([min_age_in_months, max_age_in_months])

                if class_filter and class_filter != "All Classes":
                    query += " AND s.Class_section = ?"
                    params.append(class_filter)

                query += " ORDER BY s.id ASC"

                # Execute the query
                cursor.execute(query, params)
                rows = cursor.fetchall()

                # Populate the Treeview
                for row in rows:
                    tree.insert("", tk.END, values=row)

                # Update the total number of students
                total_students_var.set(f"Total Students: {len(rows)}")

            except sqlite3.Error as e:
                print(f"Database error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")
            finally:
                # Ensure the connection is always closed properly
                if connection:
                    connection.close()

        age_filter_var = tk.StringVar(value="All ages")
        age_filter_label = tk.Label(frame2, text="Filter by Age (Years):")
        age_filter_label.grid(row=1, column=5, sticky='w')

        age_filter_combobox = ttk.Combobox(frame2, textvariable=age_filter_var,
                                           values=["All ages"] + [str(i) for i in range(2, 19)], width=20)
        age_filter_combobox.grid(row=2, column=5)
        age_filter_combobox.bind("<<ComboboxSelected>>", search_school)



        refresh_records()  # Load

    # Create a menu bar
    menu_bar = Menu(window)

    # Create a File menu and add items
    file_menu = Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Student list", command=school_list)
    file_menu.add_command(label="Statistics", command=statistic_search)
    #file_menu.add_command(label="clear text", command=clear_entry)
    #file_menu.add_command(label="Statistics", command=statistic_search)

    menu_bar.add_cascade(label="File", menu=file_menu)

    # Create a Help menu and add items

    # Add the menu bar to the main window
    window.config(menu=menu_bar)

    # Run the application

    #SET UP MENU
    # Create a menu bar


    def check_id():
        connection = sqlite3.connect("gracehealth.db")
        cursor = connection.cursor()
        user_id = (id_entry.get())

        cursor.execute("SELECT name from student WHERE id=?", (user_id,))
        used_name = cursor.fetchall()
        numbers = list(range(1, 1000000))
        numbers = str(numbers)

        if used_name != []:
            # check_id_confirmation.config(text=f'{used_name} already has this id!')
            messagebox.showinfo(parent=window, title="error", message=f'{used_name} already has this id!')

        elif user_id == "":
            # check_id_confirmation.config(text="Write an id number")
            messagebox.showinfo(parent=window, title="error", message="id cannot be empty!")
        elif user_id == "0":
            messagebox.showinfo(parent=window, title="error", message="id cannot be 0!")

        elif user_id not in numbers:
            messagebox.showinfo(parent=window, title="error", message="id must be a valid number")
            # check_id_confirmation.config(text='id must be a valid number!')
        else:
            messagebox.showinfo(parent=window, title="success", message="This id number is free")

        connection.commit()
        connection.close()

    def clear_entry():
        screening_date_entry.delete(0,END)
        id_entry.delete(0, END),
        name_entry.delete(0, END),
        date_of_birth_entry.delete(0, END),
        class_entry.delete(0, END),
        roll_entry.delete(0, END),
        aadhaar_entry.delete(0, END),
        father_guardian_entry.delete(0, END),
        mother_entry.delete(0, END),
        contact_no_entry.delete(0, END),
        address_entry.delete(0, END),
        email_entry.delete(0, END),
        teacher_entry.delete(0, END),
        age_entry.config(state=NORMAL),
        age_entry.delete(0, END),
        tea_garden_entry.set("")

        total_month_entry.delete(0,END),
        last_school_entry.delete(0, END),
        place_of_birth_entry.delete(0, END),
        weight_length_entry.delete(0,END),
        length_age_entry.delete(0,END),
        weight_age_entry.delete(0,END),

        known_disease_entry.delete(0, END),
        e9_entry.delete(0, END),

        weight_entry.delete(0, END),
        height_entry.delete(0, END),
        muac_entry.delete(0,END)
        muac_category_entry.delete(0,END)
        BMI_entry.delete(0, END),
        BMI_category_entry.delete(0, END),
        class_entry.delete(0, END),
        roll_entry.delete(0, END),
        aadhaar_entry.delete(0, END),
        vision_problem_entry.delete(0, END),
        both_eyesight_var.set(""),
        left_eyesight_var.set(""),
        right_eyesight_var.set(""),
        school_entry.delete(0, END),
        gender_option.set(""),
        check_id_confirmation.config(text="")

        CheckVar1.set('no')
        CheckVar2.set('no')
        CheckVar3.set('no')
        CheckVar4.set('no')
        CheckVar4.set('no')
        CheckVar5.set('no')
        CheckVar6.set('no')
        CheckVar7.set('no')
        CheckVar8.set('no')
        CheckVar9.set('no')
        CheckVar10.set('no')
        CheckVar11.set('no')
        CheckVar12.set('no')
        CheckVar13.set('no')
        CheckVar14.set('no')

        CheckVar16.set('no')
        CheckVar17.set('no')
        CheckVar18.set('no')
        CheckVar19.set('no')
        CheckVar20.set('no')
        CheckVar23.set('no')
        CheckVar24.set('no')
        CheckVar25.set('no')
        CheckVar26.set('no')
        CheckVar27.set('no')
        CheckVar28.set('no')
        CheckVar29.set('unknown')
        CheckVar30.set('unknown')


        # savebtn.config(state=ACTIVE),
        # BMI_entry.config(state=ACTIVE),

    def normal():

        id_entry.config(state=NORMAL),
        name_entry.config(state=NORMAL),

        gender_entry.config(state=ACTIVE),
        class_entry.config(state=NORMAL),
        roll_entry.config(state=NORMAL),
        aadhaar_entry.config(state=NORMAL),

        father_guardian_entry.config(state=NORMAL),
        mother_entry.config(state=NORMAL),
        contact_no_entry.config(state=NORMAL),
        address_entry.config(state=NORMAL),
        email_entry.config(state=NORMAL),
        teacher_entry.config(state=NORMAL),
        school_entry.config(state=ACTIVE),
        last_school_entry.config(state=NORMAL),
        place_of_birth_entry.config(state=NORMAL),
        known_disease_entry.config(state=NORMAL),

        weight_entry.config(state=NORMAL),
        height_entry.config(state=NORMAL),
        muac_entry.config(state=NORMAL),
        muac_category_entry.config(state=NORMAL),
        BMI_entry.config(state=NORMAL),
        vision_both_menu.config(state=ACTIVE),
        vision_left_menu.config(state=ACTIVE),
        vision_right_menu.config(state=ACTIVE),
        vision_problem_entry.config(state=NORMAL),
        b1_entry.config(state=ACTIVE),
        b2_entry.config(state=ACTIVE),
        b3_entry.config(state=ACTIVE),
        b4_entry.config(state=ACTIVE),
        b5_entry.config(state=ACTIVE),
        c1_entry.config(state=ACTIVE),
        c2_entry.config(state=ACTIVE),
        c3_entry.config(state=ACTIVE),
        c4_entry.config(state=ACTIVE),
        c5_entry.config(state=ACTIVE),
        c6_entry.config(state=ACTIVE),
        d1_entry.config(state=ACTIVE),
        d2_entry.config(state=ACTIVE),
        d3_entry.config(state=ACTIVE),
        d5_entry.config(state=ACTIVE),
        d6_entry.config(state=ACTIVE),
        d7_entry.config(state=ACTIVE),
        d8_entry.config(state=ACTIVE),
        d9_entry.config(state=ACTIVE),
        e3_entry.config(state=ACTIVE),
        e4_entry.config(state=ACTIVE),
        e5_entry.config(state=ACTIVE),
        e6_entry.config(state=ACTIVE),
        e7_entry.config(state=ACTIVE),
        e8_entry.config(state=ACTIVE),
        e9_entry.config(state=NORMAL),
        BMI_category_entry.config(state=NORMAL),
        weight_age_entry.config(state=NORMAL),
        length_age_entry.config(state=NORMAL),
        weight_length_entry.config(state=NORMAL),
        deworming_entry.config(state=ACTIVE),
        vaccination_entry.config(state=ACTIVE),


        savebtn.config(state=NORMAL),
    def reset():
        confirmation = messagebox.askyesno(parent=window, title="confirmation",
                                           message="Remember to save before creating new student! Do you want to continue?")
        if confirmation:
            for widget in summary_frame.winfo_children():
                widget.destroy()
            normal()
            clear_entry()
            populate_student_id()


    def clear_text():

        for widget in summary_frame.winfo_children():
            widget.destroy()
        normal()
        clear_entry()
        populate_student_id()


    def custom_messagebox(user_id, cursor, screening_date):
        def update_screening():
            update_last_screening(cursor, user_id, screening_date)
            custom_box.destroy()
            messagebox.showinfo(parent=window, title="success", message="The screening has been updated")


        def save_new_screening():
            save_new_entry(cursor, user_id)
            custom_box.destroy()
            messagebox.showinfo(parent=window, title="success", message="The screening has been saved")


        custom_box = Toplevel(window)
        custom_box.title("Update or New Save")
        custom_box.geometry("300x150+500+300")

        label = tk.Label(custom_box,
                         text=f"Student ID {user_id} exists.\nDo you want to update or create a new screening?")
        label.pack(pady=20)

        update_button = ttk.Button(custom_box, text="Update", command=update_screening)
        update_button.pack(side=tk.LEFT, padx=20)

        new_save_button = ttk.Button(custom_box, text="New Save", command=save_new_screening)
        new_save_button.pack(side=tk.RIGHT, padx=20)

        custom_box.grab_set()
        window.wait_window(custom_box)


    def save_or_update_entry():
        user_id = id_entry.get().strip()  # Strip whitespace from user input

        # Validate user ID
        if not user_id:
            messagebox.showinfo(parent=window, title="Error", message="ID cannot be empty!")
            return
        elif user_id == "0":
            messagebox.showinfo(parent=window, title="Error", message="ID cannot be 0!")
            return
        elif not user_id.isdigit():
            messagebox.showinfo(parent=window, title="Error", message="ID must be a valid number!")
            return

        #confirmation = messagebox.askyesno(parent=window, title="Save", message="Are you sure you want to save?")

        #if not confirmation:
         #   return  # If user cancels, exit the function

        with sqlite3.connect("gracehealth.db") as connection:
            cursor = connection.cursor()

            # Check if the ID exists in the database
            cursor.execute("SELECT COUNT(*) FROM student WHERE id=?", (user_id,))
            exists = cursor.fetchone()[0]

            if exists == 0:
                # ID does not exist, perform a new save
                confirmation = messagebox.askyesno(parent=window, title="New Save",
                                                   message=f"Student ID {user_id} not found. Do you want to save as a new entry?")
                if confirmation:
                    save_new_entry(cursor, user_id)
                    messagebox.showinfo(parent=window, title="Success", message="New student succesfully saved")

            else:
                # ID exists, use custom messagebox for Update/New Save choice
                screening_date = screening_date_entry.get()  # Retrieve the screening date value
                if not screening_date:  # Ensure screening date is provided
                    messagebox.showinfo(parent=window, title="Error", message="Screening date cannot be empty!")
                    return

                custom_messagebox(user_id, cursor, screening_date)  # Pass screening date to custom_messagebox

            # Commit changes after the operation
            connection.commit()
             # Clear input fields after successful operation

    def update_last_screening(cursor, user_id, screening_date, *args):
        # First, check if the screening_date exists for this record
        cursor.execute("SELECT screen_date FROM student WHERE id=?", (user_id,))
        existing_date = cursor.fetchone()

        # Collect the parameters to be updated in the database
        parameters = (
            name_entry.get(),
            date_of_birth_entry.get(),
            gender_option.get(),
            class_entry.get(),
            roll_entry.get(),
            aadhaar_entry.get(),
            father_guardian_entry.get(),
            mother_entry.get(),
            contact_no_entry.get(),
            address_entry.get(),
            email_entry.get(),
            teacher_entry.get(),
            school_entry.get(),
            last_school_entry.get(),
            place_of_birth_entry.get(),
            known_disease_entry.get(),
            weight_entry.get(),
            height_entry.get(),
            BMI_entry.get(),
            both_eyesight_var.get(),
            left_eyesight_var.get(),
            right_eyesight_var.get(),
            vision_problem_entry.get(),
            CheckVar1.get(),
            CheckVar2.get(),
            CheckVar3.get(),
            CheckVar4.get(),
            CheckVar5.get(),
            CheckVar6.get(),
            CheckVar7.get(),
            CheckVar8.get(),
            CheckVar9.get(),
            CheckVar10.get(),
            CheckVar11.get(),
            CheckVar12.get(),
            CheckVar13.get(),
            CheckVar14.get(),
            CheckVar16.get(),
            CheckVar17.get(),
            CheckVar18.get(),
            CheckVar19.get(),
            CheckVar20.get(),
            CheckVar23.get(),
            CheckVar24.get(),
            CheckVar25.get(),
            CheckVar26.get(),
            CheckVar27.get(),
            CheckVar28.get(),
            e9_entry.get(),
            BMI_category_entry.get(),
            weight_age_entry.get(),
            length_age_entry.get(),
            weight_length_entry.get(),
            total_month_entry.get(),
            CheckVar29.get(),
            CheckVar30.get(),
            tea_garden_entry.get(),
            muac_entry.get(),
            muac_category_entry.get(),
            screening_date_entry.get(),  # Keep this if you intend to update screen_date
            age_entry.get(),

            user_id  # Ensure this is the last item, matching the WHERE clause
        )

        # Determine if we need to add or update the screening date
        if existing_date is None or existing_date[0] is None:
            # No existing screening date, so add it in the update
            query = """
                UPDATE student 
                SET name=?,
                    date_of_birth=?,
                    Gender=?,
                    Class_section=?,
                    Roll_no=?,
                    Aadhaar_No=?,
                    Father_or_guardian_name=?,
                    mother_name=?,
                    contact_number=?,
                    Address=?,
                    email=?,
                    Name_teacher=?,
                    school_name=?,
                    last_school_name=?,
                    place_of_birth=?,
                    known_earlier_disease=?,
                    weight=?,
                    height=?,
                    BMI=?,
                    Vision_both=?,
                    VISON_left=?,
                    VISON_right=?,
                    VISION_problem=?,
                    B1_severe_anemia=?,
                    B2_Vita_A_deficiency=?,
                    B3_Vit_D_deficiency=?,
                    B4_Goitre=?,
                    B5_Oedema=?,
                    C1_convulsive_dis=?,
                    C2_otitis_media=?,
                    C3_dental_condition=?,
                    C4_skin_condition=?,
                    C5_rheumatic_heart_disease=?,
                    C6_others_TB_asthma=?,
                    D1_difficulty_seeing=?,
                    D2_delay_in_walking=?,
                    D3_stiffness_floppiness=?,
                    D5_reading_writing_calculatory_difficulty=?,
                    D6_speaking_difficulty=?,
                    D7_hearing_problems=?,
                    D8_learning=?,
                    D9_attention=?,
                    E3_depression_sleep=?,
                    E4_Menarke=?,
                    E5_regularity_period_difficulties=?,
                    E6_UTI_STI=?,
                    E7=?,
                    E8_menstrual_pain=?,
                    E9_remarks=?,
                    BMI_category=?,
                    weight_age=?,
                    length_age=?,
                    weight_height=?,
                    age_in_month=?,
                    deworming=?,
                    vaccination=?,
                    tea_garden=?,
                     muac = ?,
                     muac_sam= ?,  
                    age_screening=?,
                   screen_date=?
                WHERE id=?
            """

        else:
            # Screening date exists, so just update other fields without setting screen_date again
            parameters = parameters[:-3] + (
            age_entry.get(), user_id)  # Excludes screening_date_entry.get() when not needed

            query = """
                UPDATE student 
                SET name=?,
                    date_of_birth=?,
                    Gender=?,
                    Class_section=?,
                    Roll_no=?,
                    Aadhaar_No=?,
                    Father_or_guardian_name=?,
                    mother_name=?,
                    contact_number=?,
                    Address=?,
                    email=?,
                    Name_teacher=?,
                    school_name=?,
                    last_school_name=?,
                    place_of_birth=?,
                    known_earlier_disease=?,
                    weight=?,
                    height=?,
                    BMI=?,
                    Vision_both=?,
                    VISON_left=?,
                    VISON_right=?,
                    VISION_problem=?,
                    B1_severe_anemia=?,
                    B2_Vita_A_deficiency=?,
                    B3_Vit_D_deficiency=?,
                    B4_Goitre=?,
                    B5_Oedema=?,
                    C1_convulsive_dis=?,
                    C2_otitis_media=?,
                    C3_dental_condition=?,
                    C4_skin_condition=?,
                    C5_rheumatic_heart_disease=?,
                    C6_others_TB_asthma=?,
                    D1_difficulty_seeing=?,
                    D2_delay_in_walking=?,
                    D3_stiffness_floppiness=?,
                    D5_reading_writing_calculatory_difficulty=?,
                    D6_speaking_difficulty=?,
                    D7_hearing_problems=?,
                    D8_learning=?,
                    D9_attention=?,
                    E3_depression_sleep=?,
                    E4_Menarke=?,
                    E5_regularity_period_difficulties=?,
                    E6_UTI_STI=?,
                    E7=?,
                    E8_menstrual_pain=?,
                    E9_remarks=?,
                    BMI_category=?,
                    weight_age=?,
                    length_age=?,
                    weight_height=?,
                    age_in_month=?,
                    deworming = ?,
                    vaccination=?,
                    tea_garden=?,
                    muac = ?,
                    muac_sam = ?,
                    age_screening=?
                    
                WHERE id=?
            """

        # Execute the appropriate query
        cursor.execute(query, parameters)

    def save_new_entry(cursor, user_id):
        # Logic to save a new entry for the student
        cursor.execute("""INSERT INTO student(
            id,  -- or remove this column if it is auto-incremented
            name,
            date_of_birth,
            Gender,
            Class_section,
            Roll_no,
            Aadhaar_No,
            Father_or_guardian_name,
            mother_name,
            contact_number,
            Address,
            email,
            Name_teacher,
            school_name,
            last_school_name,
            place_of_birth,
            known_earlier_disease,
            weight,
            height,
            BMI,
            Vision_both,
            VISON_left,
            VISON_right,
            VISION_problem,
            B1_severe_anemia,
            B2_Vita_A_deficiency,
            B3_Vit_D_deficiency,
            B4_Goitre,
            B5_Oedema,
            C1_convulsive_dis,
            C2_otitis_media,
            C3_dental_condition,
            C4_skin_condition,
            C5_rheumatic_heart_disease,
            C6_others_TB_asthma,
            D1_difficulty_seeing,
            D2_delay_in_walking,
            D3_stiffness_floppiness,
            D5_reading_writing_calculatory_difficulty,
            D6_speaking_difficulty,
            D7_hearing_problems,
            D8_learning,
            D9_attention,
            E3_depression_sleep,
            E4_Menarke,
            E5_regularity_period_difficulties,
            E6_UTI_STI,
            E7,
            E8_menstrual_pain,
            E9_remarks,
            BMI_category, 
            weight_age,
            length_age,
            weight_height,
            age_in_month,
            deworming,
            vaccination,
            tea_garden,
            screen_date,
            age_screening,
            muac,
            muac_sam) 
        VALUES (?,?,
            ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                       (
                           id_entry.get(),  # Remove if id is auto-incremented
                           name_entry.get(),
                           date_of_birth_entry.get(),
                           gender_option.get(),
                           class_entry.get(),
                           roll_entry.get(),
                           aadhaar_entry.get(),
                           father_guardian_entry.get(),
                           mother_entry.get(),
                           contact_no_entry.get(),
                           address_entry.get(),
                           email_entry.get(),
                           teacher_entry.get(),
                           school_entry.get(),
                           last_school_entry.get(),
                           place_of_birth_entry.get(),
                           known_disease_entry.get(),
                           weight_entry.get(),
                           height_entry.get(),
                           BMI_entry.get(),
                           both_eyesight_var.get(),
                           left_eyesight_var.get(),
                           right_eyesight_var.get(),
                           vision_problem_entry.get(),
                           CheckVar1.get(),
                           CheckVar2.get(),
                           CheckVar3.get(),
                           CheckVar4.get(),
                           CheckVar5.get(),
                           CheckVar6.get(),
                           CheckVar7.get(),
                           CheckVar8.get(),
                           CheckVar9.get(),
                           CheckVar10.get(),
                           CheckVar11.get(),
                           CheckVar12.get(),
                           CheckVar13.get(),
                           CheckVar14.get(),
                           CheckVar16.get(),
                           CheckVar17.get(),
                           CheckVar18.get(),
                           CheckVar19.get(),
                           CheckVar20.get(),
                           CheckVar23.get(),
                           CheckVar24.get(),
                           CheckVar25.get(),
                           CheckVar26.get(),
                           CheckVar27.get(),
                           CheckVar28.get(),
                           e9_entry.get(),
                           BMI_category_entry.get(),
                           weight_age_entry.get(),
                           length_age_entry.get(),
                           weight_length_entry.get(),
                           total_month_entry.get(),
                           CheckVar29.get(),
                           CheckVar30.get(),
                           tea_garden_entry.get(),
                           screening_date_entry.get(),
                           age_entry.get(),
                           muac_entry.get(),
                           muac_category_entry.get()
                       ))

    def populate_student_id():
        last_id = get_next_student_id()
        if last_id:
            id_entry.insert(0, last_id)
        else:
            id_entry.insert(0, "1")

    import sqlite3

    def get_next_student_id():
        # Connect to the SQLite database
        conn = sqlite3.connect("gracehealth.db")
        cursor = conn.cursor()

        try:
            # Execute a query to get all IDs ordered in descending order
            cursor.execute("SELECT id FROM student ORDER BY id DESC")
            results = cursor.fetchall()

            # Loop through the results and find the first valid numeric ID
            for result in results:
                try:
                    # Attempt to convert the id to an integer
                    last_id = int(result[0])
                    return last_id + 1  # Return the next available ID
                except ValueError:
                    # If conversion fails, move to the next row (skip non-numeric IDs)
                    continue

            # If no valid numeric ID is found, start from 1
            return 1

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            return None

        finally:
            # Close the database connection
            conn.close()

    # Example usage: call the function and get the next student ID
    next_id = get_next_student_id()
    print(f"The next available student ID is: {next_id}")

    screening_label=Label(topframe,text="Date of Screening",font="bold")
    screening_label.grid(row=0,column=1)
    screening_date_entry = DateEntry(topframe, date_pattern='MM/DD/YY')
    screening_date_entry.grid(row=0,column=2)

    id_label = Label(topframe, text="Id", width=22)
    id_label.grid(column=1, row=1)
    id_entry = Entry(topframe, width=30)
    id_entry.grid(column=2, row=1)
    populate_student_id()



    name_label = Label(topframe, text="Name", width=22).grid(column=1, row=2)
    name_entry = Entry(topframe, width=30)
    name_entry.grid(column=2, row=2)

    date_of_birth = Label(topframe, text="Date of birth", width=22).grid(column=1, row=3)
    date_of_birth_var = StringVar()
    date_of_birth_entry = DateEntry(topframe, width=30, date_pattern='MM/DD/yy')
    date_of_birth_entry.delete(0, 'end')

    date_of_birth_entry.grid(column=2, row=3)


    # Python3 code to calculate age in years

    from datetime import datetime
    from tkinter import END, NORMAL

    def age_calculator():

        if screening_date_entry.get() == "":
            messagebox.showinfo(parent=window,title="error",message="Please write screening date")
            screening_date_entry.focus_set()
        else:

            age_entry.config(state=NORMAL)
            age_entry.delete(0, END)
            total_month_entry.delete(0, END)

            # Get the two dates from DateEntry widgets
            birthday = date_of_birth_entry.get()
            screening_date = screening_date_entry.get()

            # Convert string dates to datetime objects for easier calculations
            birthday = datetime.strptime(birthday, "%m/%d/%y")
            screening_date = datetime.strptime(screening_date, "%m/%d/%y")

            # Calculate the difference between screening date and birthdate
            age_years = screening_date.year - birthday.year
            age_months = screening_date.month - birthday.month

            # Adjust if the screening month is before the birth month
            if age_months < 0:
                age_years -= 1
                age_months += 12

            # Calculate total months difference
            total_months = age_years * 12 + age_months

            # Display results in the Entry widgets
            age_entry.insert(0, f"{age_years} years and {age_months} months")
            total_month_entry.insert(0, str(total_months))

    age_btn = ttk.Button(topframe, width=22, text="Age at screening", command=age_calculator)
    age_btn.grid(column=1, row=4)


    # button_hover(age_btn)
    age_entry = Entry(topframe, width=30)
    age_entry.grid(column=2, row=4)




    age_in_month_label = Label(topframe, text="Age in total months").grid(column=1, row=5)
    total_month_entry = Entry(topframe)
    total_month_entry.grid(column=2, row=5)

    gender_label = Label(topframe, text="Gender", width=22).grid(column=1, row=6)
    gender_option = StringVar()
    gender_entry = OptionMenu(topframe, gender_option, "female",
                              "male")
    gender_entry.grid(column=2, row=6)

    class_label = Label(topframe, text="Class", width=22).grid(column=3, row=1)
    class_entry = Entry(topframe, width=30)
    class_entry.grid(column=4, row=1)

    roll_no_label = Label(topframe, text="Roll number", width=22).grid(column=3, row=2)
    roll_entry = Entry(topframe, width=30)
    roll_entry.grid(column=4, row=2)

    aadhaar_label = Label(topframe, text="Aadhaar number", width=22).grid(column=3, row=3)
    aadhaar_entry = Entry(topframe, width=30)
    aadhaar_entry.grid(column=4, row=3)

    father_guardian_label = Label(topframe, text="Father or guardian", width=22).grid(column=3, row=4)
    father_guardian_entry = Entry(topframe, width=30)
    father_guardian_entry.grid(column=4, row=4)

    mother_label = Label(topframe, text="Mother", width=22).grid(column=3, row=5)
    mother_entry = Entry(topframe, width=30)
    mother_entry.grid(column=4, row=5)

    contact_no_label = Label(topframe, text="Contact number", width=22).grid(column=3, row=6)
    contact_no_entry = Entry(topframe, width=30)
    contact_no_entry.grid(column=4, row=6)

    address_label = Label(topframe, text="Address", width=22).grid(column=5, row=1)
    address_entry = Entry(topframe, width=30)
    address_entry.grid(column=6, row=1)

    email_label = Label(topframe, text="Email", width=22).grid(column=5, row=2)
    email_entry = Entry(topframe, width=30)
    email_entry.grid(column=6, row=2)
    teacher_label = Label(topframe, text="Teacher", width=22).grid(column=5, row=3)
    teacher_entry = Entry(topframe, width=30)
    teacher_entry.grid(column=6, row=3)

    main_window_school_list = [school for school in school_database_list if school not in ["All schools combined", ""]]
    school_label = Label(topframe, text="School name", width=22).grid(column=5, row=4)
    school_entry = ttk.Combobox(topframe,values=main_window_school_list,width=30)
    school_entry.grid(column=6, row=4)

    last_school_label = Label(topframe, text="Last school name", width=22).grid(column=5, row=5)
    last_school_entry = Entry(topframe, width=30)
    last_school_entry.grid(column=6, row=5)

    place_of_birth = Label(topframe, text="Place of birth", width=22).grid(column=5, row=6)
    place_of_birth_entry = Entry(topframe, width=30)
    place_of_birth_entry.grid(column=6, row=6)

    tea_garden_label=Label(topframe,text="Special area (optional):")
    tea_garden_label.grid(row=7,column=5)
    filtered_tea_garden_list = [tea_garden for tea_garden in tea_garden_database_list if tea_garden not in ["", "None"]]

    # Create the Combobox with the filtered list
    tea_garden_entry = ttk.Combobox(topframe, values=filtered_tea_garden_list)
    tea_garden_entry.grid(row=7,column=6)



    weight_label = Label(secondframe, text="Weight (kg)", width=22).grid(column=1, row=9)
    weight_entry = Entry(secondframe, width=5)
    weight_entry.grid(column=2, row=9)

    height_label = Label(secondframe, text="Height (cm)", width=22)
    height_label.grid(column=1, row=10)
    height_entry = Entry(secondframe, width=5)
    height_entry.grid(column=2, row=10)

    def muac():
        muac_category_entry.delete(0,END)
        try:
            age = int(total_month_entry.get())
            print(age)
            if 6 <= age <= 60:
                muac_category_entry.delete(0, END)
                muach_length = float(muac_entry.get())
                if muach_length >= 11.5:
                    muac_category_entry.insert(0, "normal")
                else:
                    muac_category_entry.insert(0, "severe acute malnutrition")
            else:
                # Trigger the error if age is outside the valid range

                muac_category_entry.insert(0,"N/A")

        except ValueError:
            # Handle non-integer or invalid input gracefully
            messagebox.showerror(title="Error", message="Please enter a valid number for months,and MUAC!")

    muac_label = Label(secondframe, text="MUAC (cm)", width=22)
    muac_label.grid(column=1, row=11)
    muac_entry = Entry(secondframe, width=5)
    muac_entry.grid(column=2, row=11)

    muac_category_btn = ttk.Button(secondframe, text="MUAC category", command=muac)
    muac_category_btn.grid(column=1, row=12)
    muac_category_entry = Entry(secondframe, width=25)
    muac_category_entry.grid(column=2, row=12)

    vision_list = ["3/30", "3/24", "3/19", "3/15", "3/12","3/9.5", "3/7.5", "3/6", "3/4.8", "3/3.8", "3/3", "3/2.4", "3/1.9", "3/1.5", "3/1.2"]

    both_eyesight_var = StringVar()

    vision_both_label = Label(secondframe, text="Vision both eyes", width=22).grid(column=3, row=9)
    vision_both_menu = OptionMenu(secondframe, both_eyesight_var, vision_list[0], vision_list[1],vision_list[2], vision_list[3],
                                  vision_list[4], vision_list[5], vision_list[6], vision_list[7], vision_list[8], vision_list[9],
                                  vision_list[10], vision_list[11], vision_list[12], vision_list[13], vision_list[14])
    vision_both_menu.grid(column=4, row=9)

    left_eyesight_var = StringVar()
    vision_left_label = Label(secondframe, text="Vision left eye", width=22).grid(column=3, row=10)
    vision_left_menu = OptionMenu(secondframe,
                                  left_eyesight_var, vision_list[0], vision_list[1], vision_list[2], vision_list[3],
                                  vision_list[4], vision_list[5], vision_list[6], vision_list[7],vision_list[8], vision_list[9],
                                  vision_list[10], vision_list[11], vision_list[12], vision_list[13], vision_list[14])
    vision_left_menu.grid(column=4, row=10)

    right_eyesight_var = StringVar()
    vision_right_label = Label(secondframe, text="Vision right eye", width=22).grid(column=3, row=11)
    vision_right_menu = OptionMenu(secondframe,right_eyesight_var,vision_list[0],vision_list[1],vision_list[2],vision_list[3],
                                  vision_list[4],vision_list[5],vision_list[6], vision_list[7],vision_list[8],vision_list[9],
                                  vision_list[10],vision_list[11],vision_list[12],vision_list[13],vision_list[14])
    vision_right_menu.grid(column=4, row=11)


    def vision_result():
        vision_problem_entry.delete(0,END)

        if both_eyesight_var.get() =="3/30" \
                or both_eyesight_var.get() =="3/24" \
                or both_eyesight_var.get() == "3/19" \
                or both_eyesight_var.get() == "3/15" \
                or both_eyesight_var.get() == "3/12" \
                or both_eyesight_var.get() =="3/9.5" \
                or both_eyesight_var.get() == "3/7.5" \
                or both_eyesight_var.get() == "3/6" \
                or both_eyesight_var.get() == "3/4.8" \
                or both_eyesight_var.get() == "3/3.8" \
                or left_eyesight_var.get() == "3/30" \
                or left_eyesight_var.get() == "3/24" \
                or left_eyesight_var.get() == "3/19" \
                or left_eyesight_var.get() == "3/15" \
                or left_eyesight_var.get() == "3/12" \
                or left_eyesight_var.get() =="3/9.5" \
                or left_eyesight_var.get() == "3/7.5" \
                or left_eyesight_var.get() == "3/6" \
                or left_eyesight_var.get() == "3/4.8" \
                or left_eyesight_var.get() == "3/3.8" \
                or right_eyesight_var.get() == "3/30" \
                or right_eyesight_var.get() == "3/24" \
                or right_eyesight_var.get() == "3/19" \
                or right_eyesight_var.get() == "3/15" \
                or right_eyesight_var.get() == "3/12" \
                or right_eyesight_var.get() == "3/9.5" \
                or right_eyesight_var.get() == "3/7.5" \
                or right_eyesight_var.get() == "3/6" \
                or right_eyesight_var.get() == "3/4.8" \
                or right_eyesight_var.get() == "3/3.8" \
                or vision_list.index(left_eyesight_var.get()) - vision_list.index(right_eyesight_var.get()) >= 2 \
                or vision_list.index(right_eyesight_var.get()) - vision_list.index(left_eyesight_var.get()) >= 2:
            vision_problem_entry.insert(0, "yes")
        else:
            vision_problem_entry.insert(0,"no")

    vision_problem_btn = ttk.Button(secondframe, text="Vision problem", command=vision_result, width=22)
    vision_problem_btn.grid(column=3, row=12)
    # button_hover(vision_problem_btn)
    vision_problem_entry = Entry(secondframe, width=5)
    vision_problem_entry.grid(column=4, row=12)

    def BMI_calculator():
        try:
            # Clear previous BMI result
            BMI_entry.delete(0, tk.END)

            # Get the weight and height inputs and check if they are filled
            weight = weight_entry.get().strip()
            height = height_entry.get().strip()

            if not weight or not height:
                raise ValueError("Please enter both weight and height.")

            # Convert weight and height to integers
            weight = int(weight)
            height = int(height)

            # Perform BMI calculation
            result = (weight / height ** 2) * 10000
            BMI_index = round(result, 1)

            # Insert the result into the BMI entry field
            BMI_entry.insert(0, str(float(BMI_index)))

        except ValueError as ve:
            # Show an error message if inputs are missing or invalid
            messagebox.showerror("Input Error", str(ve))
            BMI_entry.delete(0, tk.END)  # Clear BMI result if there's an error

        except Exception as e:
            # Handle any other unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            BMI_entry.delete(0, tk.END)

    BMI_btn = ttk.Button(secondframe, text="BMI value", width=22, command=BMI_calculator)
    BMI_btn.grid(column=5,row=12)
    # button_hover(BMI_btn)

    BMI_entry = Entry(secondframe, width=5)
    BMI_entry.grid(column=6, row=12)



    bmi_thresholds_female  = {
            "61": (11.8, 12.7, 18.9),
            "62": (11.8, 12.7, 18.9),
            "63": (11.8, 12.7, 18.9),
            "64": (11.8, 12.7, 18.9),
            "65": (11.7, 12.7, 19.0),
            "66": (11.7, 12.7, 19.0),
            "67": (11.7, 12.7, 19.0),
            "68": (11.7, 12.7, 19.1),
            "69": (11.7, 12.7, 19.1),
            "70": (11.7, 12.7, 19.1),
            "71": (11.7, 12.7, 19.2),
            "72": (11.7, 12.7, 19.2),
            "73": (11.7, 12.7, 19.3),  # Fill threshold values
            "74": (11.7, 12.7, 19.3),  # Fill threshold values
            "75": (11.7, 12.7, 19.3),  # Fill threshold values
            "76": (11.7, 12.7, 19.4),  # Fill threshold values
            "77": (11.7, 12.7, 19.4),  # Fill threshold values
            "78": (11.7, 12.7, 19.5),  # Fill threshold values
            "79": (11.7, 12.7, 19.5),  # Fill threshold values
            "80": (11.7, 12.7, 19.6),  # Fill threshold values
            "81": (11.7, 12.7, 19.6),  # Fill threshold values
            "82": (11.7, 12.7, 19.7),  # Fill threshold values
            "83": (11.7, 12.7, 19.7),  # Fill threshold values
            "84": (11.8, 12.7, 19.8),  # Fill threshold values
            "85": (11.8, 12.7, 19.8),  # Fill threshold values
            "86": (11.8, 12.8, 19.9),  # Fill threshold values
            "87": (11.8, 12.8, 20.0),  # Fill threshold values
            "88": (11.8, 12.8, 20.0),  # Fill threshold values
            "89": (11.8, 12.8, 20.1),  # Fill threshold values
            "90": (11.8, 12.8, 20.1),  # Fill threshold values
            "91": (11.8, 12.8, 20.2),  # Fill threshold values
            "92": (11.8, 12.8, 20.3),  # Fill threshold values
            "93": (11.8, 12.8, 20.3),  # Fill threshold values
            "94": (11.9, 12.9, 17.6),  # Fill threshold values
            "95": (11.9, 12.9, 20.5),  # Fill threshold values
            "96": (11.9, 12.9, 20.6),  # Fill threshold values
            "97": (11.9, 12.9, 20.6),  # Fill threshold values
            "98": (11.9, 12.9, 20.7),  # Fill threshold values
            "99": (11.9, 12.9, 20.8),  # Fill threshold values
            "100":(11.9, 13.0, 20.9),  # Fill threshold values
            "101": (12.0, 13.0, 20.9),  # Fill threshold values
            "102": (12.0, 13.0, 21.0),  # Fill threshold values
            "103": (12.0, 13.0, 21.1),  # Fill threshold values
            "104": (12.0, 13.0, 21.2),  # Fill threshold values
            "105": (12.0, 13.1, 21.3),  # Fill threshold values
            "106": (12.1, 13.1, 21.3),  # Fill threshold values
            "107": (12.1, 13.1, 21.4),  # Fill threshold values
            "108": (12.1, 13.1, 21.5),  # Fill threshold values
            "109": (12.1, 13.2, 21.6),  # Fill threshold values
            "110": (12.1, 13.2, 21.7),  # Fill threshold values
            "111": (12.2, 13.2, 21.8),  # Fill threshold values
            "112": (12.2, 13.2, 21.9),  # Fill threshold values
            "113": (12.2, 13.3, 21.9),  # Fill threshold values
            "114": (12.2, 13.3, 22.0),  # Fill threshold values
            "115": (12.3, 13.3, 22.1),  # Fill threshold values
            "116": (12.3, 13.4, 22.2),  # Fill threshold values
            "117": (12.3, 13.4, 22.3),  # Fill threshold values
            "118": (12.3, 13.4, 22.4),  # Fill threshold values
            "119": (12.4, 13.4, 22.5),  # Fill threshold values
            "120": (12.4, 13.5, 19.0),  # Fill threshold values
            "121": (12.4, 13.5, 22.7),  # Fill threshold values
            "122": (12.4, 13.5, 22.8),  # Fill threshold values
            "123": (12.5, 13.6, 22.8),  # Fill threshold values
            "124": (12.5, 13.6, 22.9),  # Fill threshold values
            "125": (12.5, 13.6, 23.0),  # Fill threshold values
            "126": (12.5, 13.7, 23.1),  # Fill threshold values
            "127": (12.6, 13.7, 23.2),  # Fill threshold values
            "128": (12.6, 13.7, 19.6),  # Fill threshold values
            "129": (12.6, 13.8, 23.4),  # Fill threshold values
            "130": (12.7, 13.8, 23.5),  # Fill threshold values
            "131": (12.7, 13.8, 23.6),  # Fill threshold values
            "132": (12.7, 13.9, 23.7),  # Fill threshold values
            "133": (12.8, 13.9, 23.8),  # Fill threshold values
            "134": (12.8, 14.0, 23.9),  # Fill threshold values
            "135": (12.8, 14.0, 24.0),  # Fill threshold values
            "136": (12.9, 14.0, 24.1),  # Fill threshold values
            "137": (12.9, 14.1, 24.2),  # Fill threshold values
            "138": (12.9, 14.1, 24.3),  # Fill threshold values
            "139": (13.0, 14.2, 24.4),  # Fill threshold values
            "140": (13.0, 14.2, 24.5),  # Fill threshold values
            "141": (13.0, 14.3, 24.7),  # Fill threshold values
            "142": (13.1, 14.3, 24.8),  # Fill threshold values
            "143": (13.1, 14.3, 24.9),  # Fill threshold values
            "144": (13.2, 14.4, 25.0),  # Fill threshold values
            "145": (13.2, 14.4, 25.1),  # Fill threshold values
            "146": (13.2, 14.5, 25.2),  # Fill threshold values
            "147": (13.2, 14.5, 25.3),  # Fill threshold values
            "148": (13.3, 14.6, 25.4),  # Fill threshold values
            "149": (13.3, 14.6, 25.5),  # Fill threshold values
            "150": (13.4, 14.7, 25.6),  # Fill threshold values
            "151": (13.4, 14.7, 25.7),  # Fill threshold values
            "152": (13.5, 14.8, 25.8),  # Fill threshold values
            "153": (13.5, 14.8, 25.9),  # Fill threshold values
            "154": (13.5, 14.8, 26.0),  # Fill threshold values
            "155": (13.6, 14.9, 26.1),  # Fill threshold values
            "156": (13.6, 14.9, 26.2),  # Fill threshold values
            "157": (13.6, 15.0, 26.3),  # Fill threshold values
            "158": (13.7, 15.0, 26.4),  # Fill threshold values
            "159": (13.7, 15.1, 26.5),  # Fill threshold values
            "160": (13.8, 15.1, 26.6),  # Fill threshold values
            "161": (13.8, 15.2, 26.7),  # Fill threshold values
            "162": (13.8, 15.2, 26.8),  # Fill threshold values
            "163": (13.9, 15.2, 26.9),  # Fill threshold values
            "164": (13.9, 15.3, 27.0),  # Fill threshold values
            "165": (13.9, 15.3, 27.1),  # Fill threshold values
            "166": (14.0, 15.4, 27.1),  # Fill threshold values
            "167": (14.0, 15.4, 27.2),  # Fill threshold values
            "168": (14.0, 15.4, 27.3),  # Fill threshold values
            "169": (14.1, 15.5, 27.4),  # Fill threshold values
            "170": (14.1, 15.5, 27.5),  # Fill threshold values
            "171": (14.1, 15.6, 27.6),  # Fill threshold values
            "172": (14.1, 15.6, 27.7),  # Fill threshold values
            "173": (14.2, 15.6, 27.7),  # Fill threshold values
            "174": (14.2, 15.7, 27.8),  # Fill threshold values
            "175": (14.2, 15.7, 27.9),  # Fill threshold values
            "176": (14.3, 15.7, 28.0),  # Fill threshold values
            "177": (14.3, 15.8, 28.0),  # Fill threshold values
            "178": (14.3, 15.8, 28.1),  # Fill threshold values
            "179": (14.3, 15.8, 28.2),  # Fill threshold values
            "180": (14.4, 15.9, 28.2),  # Fill threshold values
            "181": (14.4, 15.9, 28.3),  # Fill threshold values
            "182": (14.4, 15.9, 28.4),  # Fill threshold values
            "183": (14.4, 16.0, 28.4),  # Fill threshold values
            "184": (14.5, 16.0, 28.5),  # Fill threshold values
            "185": (14.5, 16.0, 28.5),  # Fill threshold values
            "186": (14.5, 16.0, 28.6),  # Fill threshold values
            "187": (14.5, 16.1, 28.6),  # Fill threshold values
            "188": (14.5, 16.1, 28.7),  # Fill threshold values
            "189": (14.5, 16.1, 28.7),  # Fill threshold values
            "190": (14.6, 16.1, 28.8),  # Fill threshold values
            "191": (14.6, 16.2, 28.8),  # Fill threshold values
            "192": (14.6, 16.2, 28.9),  # Fill threshold values
            "193": (14.6, 16.2, 28.9),  # Fill threshold values
            "194": (14.6, 16.2, 29.0),  # Fill threshold values
            "195": (14.6, 16.2, 29.0),  # Fill threshold values
            "196": (14.6, 16.2, 29.0),  # Fill threshold values
            "197": (14.6, 16.3, 29.1),  # Fill threshold values
            "198": (14.7, 16.3, 29.1),  # Fill threshold values
            "199": (14.7, 16.3, 29.1),  # Fill threshold values
            "200": (14.7, 16.3, 29.2),  # Fill threshold values
            "201": (14.7, 16.3, 29.2),  # Fill threshold values
            "202": (14.7, 16.3, 29.3),  # Fill threshold values
            "203": (14.7, 16.4, 29.3),  # Fill threshold values
            "204": (14.7, 16.4, 29.3),  # Fill threshold values
            "205": (14.7, 16.4, 29.3),  # Fill threshold values
            "206": (14.7, 16.4, 29.3),  # Fill threshold values
            "207": (14.7, 16.4, 29.4),  # Fill threshold values
            "208": (14.7, 16.4, 29.4),  # Fill threshold values
            "209": (14.7, 16.4, 29.4),  # Fill threshold values
            "210": (14.7, 16.4, 29.4),  # Fill threshold values
            "211": (14.7, 16.4, 29.4),  # Fill threshold values
            "212": (14.7, 16.4, 29.5),  # Fill threshold values
            "213": (14.7, 16.4, 29.5),  # Fill threshold values
            "214": (14.7, 16.4, 29.5),  # Fill threshold values
            "215": (14.7, 16.4, 29.5),  # Fill threshold values
            "216": (14.7, 16.4, 29.5),  # Fill threshold values
        }
    bmi_thresholds_male  = {
            "61": (12.1, 13.0, 18.3),
            "62": (12.1, 13.0, 18.3),
            "63": (12.1, 13.0, 18.3),
            "64": (12.1, 13.0, 18.3),
            "65": (12.1, 13.0, 18.3),
            "66": (12.1, 13.0, 18.4),
            "67": (12.1, 13.0, 18.4),
            "68": (12.1, 13.0, 18.4),
            "69": (12.1, 13.0, 18.4),
            "70": (12.1, 13.0, 18.5),
            "71": (12.1, 13.0, 18.5),
            "72": (12.1, 13.0, 18.5),
            "73": (12.1, 13.0, 18.6),  # Fill threshold values
            "74": (12.2, 13.1, 18.6),  # Fill threshold values
            "75": (12.2, 13.1, 18.6),  # Fill threshold values
            "76": (12.2, 13.1, 18.7),  # Fill threshold values
            "77": (12.2, 13.1, 18.7),  # Fill threshold values
            "78": (12.2, 13.1, 18.7),  # Fill threshold values
            "79": (12.2, 13.1, 18.8),  # Fill threshold values
            "80": (12.2, 13.1, 18.8),  # Fill threshold values
            "81": (12.2, 13.1, 18.9),  # Fill threshold values
            "82": (12.2, 13.1, 18.9),  # Fill threshold values
            "83": (12.2, 13.1, 19.0),  # Fill threshold values
            "84": (12.3, 13.1, 19.0),  # Fill threshold values
            "85": (12.3, 13.2, 19.1),  # Fill threshold values
            "86": (12.3, 13.2, 19.1),  # Fill threshold values
            "87": (12.3, 13.2, 19.2),  # Fill threshold values
            "88": (12.3, 13.2, 19.2),  # Fill threshold values
            "89": (12.3, 13.2, 19.3),  # Fill threshold values
            "90": (12.3, 13.2, 19.3),  # Fill threshold values
            "91": (12.3, 13.2, 19.4),  # Fill threshold values
            "92": (12.3, 13.2, 19.4),  # Fill threshold values
            "93": (12.4, 13.3, 19.5),  # Fill threshold values
            "94": (12.4, 13.3, 19.6),  # Fill threshold values
            "95": (12.4, 13.3, 19.6),  # Fill threshold values
            "96": (12.4, 13.3, 19.7),  # Fill threshold values
            "97": (12.4, 13.3, 19.7),  # Fill threshold values
            "98": (12.4, 13.3, 19.8),  # Fill threshold values
            "99": (12.4, 13.3, 19.9),  # Fill threshold values
            "100": (12.4, 13.4, 19.9),  # Fill threshold values
            "101": (12.5, 13.4, 20.0),  # Fill threshold values
            "102": (12.5, 13.4, 20.1),  # Fill threshold values
            "103": (12.5, 13.4, 20.1),  # Fill threshold values
            "104": (12.5, 13.4, 20.2),  # Fill threshold values
            "105": (12.5, 13.4, 20.3),  # Fill threshold values
            "106": (12.5, 13.5, 20.3),  # Fill threshold values
            "107": (12.5, 13.5, 20.4),  # Fill threshold values
            "108": (12.6, 13.5, 20.5),  # Fill threshold values
            "109": (12.6, 13.5, 20.5),  # Fill threshold values
            "110": (12.6, 13.5, 20.6),  # Fill threshold values
            "111": (12.6, 13.5, 20.7),  # Fill threshold values
            "112": (12.6, 13.6, 20.8),  # Fill threshold values
            "113": (12.6, 13.6, 20.8),  # Fill threshold values
            "114": (12.7, 13.6, 20.9),  # Fill threshold values
            "115": (12.7, 13.6, 21.0),  # Fill threshold values
            "116": (12.7, 13.6, 21.1),  # Fill threshold values
            "117": (12.7, 13.7, 21.2),  # Fill threshold values
            "118": (12.7, 13.7, 21.2),  # Fill threshold values
            "119": (12.8, 13.7, 21.3),  # Fill threshold values
            "120": (12.8, 13.7, 21.4),  # Fill threshold values
            "121": (12.8, 13.8, 21.5),  # Fill threshold values
            "122": (12.8, 13.8, 21.6),  # Fill threshold values
            "123": (12.8, 13.8, 21.7),  # Fill threshold values
            "124": (12.9, 13.8, 21.7),  # Fill threshold values
            "125": (12.9, 13.9, 21.8),  # Fill threshold values
            "126": (12.9, 13.9, 21.9),  # Fill threshold values
            "127": (12.9, 13.9, 22.0),  # Fill threshold values
            "128": (13.0, 13.9, 22.1),  # Fill threshold values
            "129": (13.0, 14.0, 22.2),  # Fill threshold values
            "130": (13.0, 14.0, 22.3),  # Fill threshold values
            "131": (13.0, 14.0, 22.4),  # Fill threshold values
            "132": (13.1, 14.1, 22.5),  # Fill threshold values
            "133": (13.1, 14.1, 22.5),  # Fill threshold values
            "134": (13.1, 14.1, 22.6),  # Fill threshold values
            "135": (13.1, 14.1, 22.7),  # Fill threshold values
            "136": (13.2, 14.2, 22.8),  # Fill threshold values
            "137": (13.2, 14.2, 22.9),  # Fill threshold values
            "138": (13.2, 14.2, 23.0),  # Fill threshold values
            "139": (13.2, 14.3, 23.1),  # Fill threshold values
            "140": (13.3, 14.3, 23.2),  # Fill threshold values
            "141": (13.3, 14.3, 23.3),  # Fill threshold values
            "142": (13.3, 14.4, 23.4),  # Fill threshold values
            "143": (13.4, 14.4, 23.5),  # Fill threshold values
            "144": (13.4, 14.5, 23.6),  # Fill threshold values
            "145": (13.4, 14.5, 23.7),  # Fill threshold values
            "146": (13.5, 14.5, 23.8),  # Fill threshold values
            "147": (13.5, 14.6, 23.9),  # Fill threshold values
            "148": (13.5, 14.6, 24.0),  # Fill threshold values
            "149": (13.6, 14.6, 24.1),  # Fill threshold values
            "150": (13.6, 14.7, 24.2),  # Fill threshold values
            "151": (13.6, 14.7, 24.3),  # Fill threshold values
            "152": (13.7, 14.8, 24.4),  # Fill threshold values
            "153": (13.7, 14.8, 24.5),  # Fill threshold values
            "154": (13.7, 14.8, 24.6),  # Fill threshold values
            "155": (13.8, 14.9, 24.7),  # Fill threshold values
            "156": (13.8, 14.9, 24.8),  # Fill threshold values
            "157": (13.8, 15.0, 24.9),  # Fill threshold values
            "158": (13.9, 15.0, 25.0),  # Fill threshold values
            "159": (13.9, 15.1, 25.1),  # Fill threshold values
            "160": (14.0, 15.1, 25.2),  # Fill threshold values
            "161": (14.0, 15.2, 25.2),  # Fill threshold values
            "162": (14.0, 15.2, 25.3),  # Fill threshold values
            "163": (14.1, 15.2, 25.4),  # Fill threshold values
            "164": (14.1, 15.3, 25.5),  # Fill threshold values
            "165": (14.1, 15.3, 25.6),  # Fill threshold values
            "166": (14.2, 15.4, 25.7),  # Fill threshold values
            "167": (14.2, 15.4, 25.8),  # Fill threshold values
            "168": (14.3, 15.5, 25.9),  # Fill threshold values
            "169": (14.3, 15.5, 26.0),  # Fill threshold values
            "170": (14.3, 15.6, 26.1),  # Fill threshold values
            "171": (14.4, 15.6, 26.2),  # Fill threshold values
            "172": (14.4, 15.7, 26.3),  # Fill threshold values
            "173": (14.5, 15.7, 26.4),  # Fill threshold values
            "174": (14.5, 15.7, 26.5),  # Fill threshold values
            "175": (14.5, 15.8, 26.5),  # Fill threshold values
            "176": (14.6, 15.8, 26.6),  # Fill threshold values
            "177": (14.6, 15.9, 26.7),  # Fill threshold values
            "178": (14.6, 15.9, 26.8),  # Fill threshold values
            "179": (14.7, 16.0, 26.9),  # Fill threshold values
            "180": (14.7, 16.0, 27.0),  # Fill threshold values
            "181": (14.7, 16.1, 27.1),  # Fill threshold values
            "182": (14.8, 16.1, 27.1),  # Fill threshold values
            "183": (14.8, 16.1, 27.2),  # Fill threshold values
            "184": (14.8, 16.2, 27.3),  # Fill threshold values
            "185": (14.9, 16.2, 27.4),  # Fill threshold values
            "186": (14.9, 16.3, 27.4),  # Fill threshold values
            "187": (15.0, 16.3, 27.5),  # Fill threshold values
            "188": (15.0, 16.3, 27.6),  # Fill threshold values
            "189": (15.0, 16.4, 27.7),  # Fill threshold values
            "190": (15.0, 16.4, 27.7),  # Fill threshold values
            "191": (15.1, 16.5, 27.8),  # Fill threshold values
            "192": (15.1, 16.5, 27.9),  # Fill threshold values
            "193": (15.1, 16.5, 27.9),  # Fill threshold values
            "194": (15.2, 16.6, 28.0),  # Fill threshold values
            "195": (15.2, 16.6, 28.1),  # Fill threshold values
            "196": (15.2, 16.7, 28.1),  # Fill threshold values
            "197": (15.3, 16.7, 28.2),  # Fill threshold values
            "198": (15.3, 16.7, 28.3),  # Fill threshold values
            "199": (15.3, 16.8, 28.3),  # Fill threshold values
            "200": (15.3, 16.8, 28.4),  # Fill threshold values
            "201": (15.4, 16.8, 28.5),  # Fill threshold values
            "202": (15.4, 16.9, 28.5),  # Fill threshold values
            "203": (15.4, 16.9, 28.6),  # Fill threshold values
            "204": (15.4, 16.9, 28.6),  # Fill threshold values
            "205": (15.5, 17.0, 28.7),  # Fill threshold values
            "206": (15.5, 17.0, 28.7),  # Fill threshold values
            "207": (15.5, 17.0, 28.8),  # Fill threshold values
            "208": (15.5, 17.1, 28.9),  # Fill threshold values
            "209": (15.6, 17.1, 28.9),  # Fill threshold values
            "210": (15.6, 17.1, 29.00),  # Fill threshold values
            "211": (15.6, 17.1, 29.0),  # Fill threshold values
            "212": (15.6, 17.2, 29.1),  # Fill threshold values
            "213": (15.6, 17.2, 29.1),  # Fill threshold values
            "214": (15.7, 17.2, 29.2),  # Fill threshold values
            "215": (15.7, 17.3, 29.2),  # Fill threshold values
            "216": (15.7, 17.3, 29.2),  # Fill threshold values
        }

    def bmi_category(gender, month, bmi_value):
        """
        Determine the BMI category based on gender, month, and BMI value.
        If the month is out of range, return "N/A". All error messages are displayed in messagebox.

        :param gender: str, "male" or "female"
        :param month: str, the month (as a string) like "73", "74", etc.
        :param bmi_value: float, the BMI value to categorize

        :return: str, the category (severe underweight, underweight, normal, or overweight)
        """
        try:
            # Check if gender is valid
            if gender not in ["male", "female"]:
                raise ValueError("Please select a valid gender (male or female).")

            # Select the correct BMI thresholds based on gender
            thresholds = bmi_thresholds_female if gender == "female" else bmi_thresholds_male

            # Check if the month is within the valid range
            if int(month) < 61 or int(month) > 216:
                return "N/A"

            if month not in thresholds:
                raise ValueError("BMI thresholds for the given month are not available.")

            # Fetch thresholds for the given month
            severe_underweight_threshold, normal_threshold, overweight_threshold = thresholds[month]

            # Determine the BMI category
            if bmi_value < severe_underweight_threshold:
                return "severe underweight"
            elif severe_underweight_threshold <= bmi_value < normal_threshold:
                return "underweight"
            elif normal_threshold <= bmi_value <= overweight_threshold:
                return "normal"
            else:
                return "overweight"
        except ValueError as ve:
            # Display an error message box
            messagebox.showerror("Input Error", str(ve))
            return ""
        except Exception as e:
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            return ""

    def show_bmi_category():
        try:
            # Get the BMI, month, and gender inputs
            bmi_value = BMI_entry.get().strip()  # Strip any leading/trailing spaces
            month = total_month_entry.get().strip()  # Already a string
            gender = gender_option.get().strip()  # Already a string

            # Check if the BMI value is numeric
            if not bmi_value.replace('.', '', 1).isdigit():  # Allow a single period for floats
                BMI_category_entry.delete(0, tk.END)  # Clear the previous result
                messagebox.showerror("Input Error", "Please enter a valid numeric value for BMI.")
                return

            # Convert to float
            bmi_value = float(bmi_value)

            # Get the BMI category
            category = bmi_category(gender, month, bmi_value)

            # Display the result in the BMI_category_entry field
            BMI_category_entry.delete(0, tk.END)  # Clear the previous result
            BMI_category_entry.insert(0, category)  # Insert the new category
        except Exception as e:
            # Handle unexpected errors
            BMI_category_entry.delete(0, tk.END)  # Clear previous result
            messagebox.showerror("Error", f"An unexpected error occurred: {str(e)}")
            gender_entry.focus_set()

    # Button setup in your GUI
    BMI_category_btn = ttk.Button(secondframe, text="BMI category (only for 61 to 216 months)",
                                  command=show_bmi_category)
    BMI_category_btn.grid(column=5, row=13)

    # Entry for displaying the result
    BMI_category_entry = Entry(secondframe, width=19)
    BMI_category_entry.grid(column=6, row=13)

    from tkinter import messagebox


    def weight_length_category():
        weight_length_entry.delete(0, END)
        male_height_thresholds = {
            45: (1.9, 2.0),
            46: (2.0, 2.2),
            47: (2.1, 2.3),
            48: (2.3, 2.5),
            49: (2.4, 2.6),
            50: (2.6, 2.8),
            51: (2.7, 3.0),
            52: (2.9, 3.2),
            53: (3.1, 3.4),
            54: (3.3, 3.6),
            55: (3.6, 3.8),
            56: (3.8, 4.1),
            57: (4.0, 4.3),
            58: (4.3, 4.6),
            59: (4.5, 4.8),
            60: (4.7, 5.1),
            61: (4.9, 5.3),
            62: (5.1, 5.6),
            63: (5.3, 5.8),
            64: (5.5, 6.0),
            65: (5.7, 6.2),
            66: (5.9, 6.4),
            67: (6.1, 6.6),
            68: (6.3, 6.8),
            69: (6.5, 7.0),
            70: (6.6, 7.2),
            71: (6.8, 7.4),
            72: (7.0, 7.6),
            73: (7.3, 7.7),
            74: (7.3, 7.9),
            75: (7.5, 8.1),
            76: (7.6, 8.3),
            77: (7.8, 8.4),
            78: (7.9, 8.6),
            79: (8.1, 8.7),
            80: (8.2, 8.9),
            81: (8.4, 9.1),
            82: (8.5, 9.2),
            83: (8.7, 9.4),
            84: (8.9, 9.6),
            85: (9.1, 9.8),
            86: (9.3, 10.0),
            87: (9.6, 10.4),
            88: (9.8, 10.6),
            89: (10.0, 10.8),
            90: (10.2, 11.0),
            91: (10.4, 11.2),
            92: (10.6, 11.4),
            93: (10.8, 11.6),
            94: (11.0, 11.8),
            95: (11.1, 12.0),
            96: (11.3, 12.2),
            97: (11.5, 12.4),
            98: (11.7, 12.6),
            99: (11.9, 12.9),
            100: (12.1, 13.1),
            101: (12.3, 13.3),
            102: (12.5, 13.6),
            103: (12.8, 13.8),
            104: (13.0, 14.0),
            105: (13.2, 14.3),
            106: (13.4, 14.5),
            107: (13.7, 14.8),
            108: (13.9, 15.1),
            109: (14.1, 15.3),
            110: (14.4, 15.6),
            111: (14.9, 15.9),
            112: (15.2, 16.2),
            113: (15.4, 16.5),
            114: (15.7, 16.8),
            115: (15.4, 17.1),
            116: (16.0, 17.4),
            117: (16.2, 17.7),
            118: (16.5, 18.0),
            119: (16.8, 18.3),
            120: (17.1, 18.6)}

        female_height_thresholds = {
            45: (1.9, 2.1),
            46: (2.0, 2.2),
            47: (2.2, 2.4),
            48: (2.3, 2.5),
            49: (2.4, 2.6),
            50: (2.6, 2.8),
            51: (2.8, 3.0),
            52: (2.9, 3.2),
            53: (3.1, 3.4),
            54: (3.3, 3.6),
            55: (3.5, 3.8),
            56: (3.7, 4.0),
            57: (4.0, 4.3),
            58: (4.1, 4.5),
            59: (4.3, 4.7),
            60: (4.5, 4.9),
            61: (4.7, 5.1),
            62: (4.9, 5.3),
            63: (5.1, 5.5),
            64: (5.3, 5.7),
            65: (5.5, 5.9),
            66: (5.6, 6.1),
            67: (5.8, 6.3),
            68: (6.0, 6.5),
            69: (6.1, 6.7),
            70: (6.3, 6.9),
            71: (6.5, 7.0),
            72: (6.6, 7.2),
            73: (6.8, 7.4),
            74: (6.9, 7.5),
            75: (7.1, 7.7),
            76: (7.2, 7.8),
            77: (7.4, 8.0),
            78: (7.5, 8.2),
            79: (7.7, 8.3),
            80: (7.8, 8.5),
            81: (8.0, 8.7),
            82: (8.1, 8.8),
            83: (8.3, 9.0),
            84: (8.5, 9.2),
            85: (8.7, 9.4),
            86: (8.9, 9.7),
            87: (9.2, 10.0),
            88: (9.4, 10.2),
            89: (9.6, 10.4),
            90: (9.8, 10.6),
            91: (10.0, 10.9),
            92: (10., 11.1),
            93: (10.4, 11.3),
            94: (10.6, 11.5),
            95: (10.8, 11.7),
            96: (10.9, 11.9),
            97: (11.1, 12.1),
            98: (11.3, 12.3),
            99: (11.5, 12.5),
            100: (11.7, 12.8),
            101: (12.0, 13.0),
            102: (12.2, 13.3),
            103: (12.4, 13.5),
            104: (12.6, 13.8),
            105: (12.9, 14.0),
            106: (13.1, 14.3),
            107: (13.4, 14.6),
            108: (13.7, 14.9),
            109: (13.9, 15.2),
            110: (14.2, 15.5),
            111: (14.5, 15.8),
            112: (14.8, 16.2),
            113: (15.1, 16.5),
            114: (15.4, 16.8),
            115: (15.7, 17.2),
            116: (16.0, 17.5),
            117: (16.3, 17.8),
            118: (16.6, 18.2),
            119: (16.9, 18.5),
            120: (17.3, 18.9)}

        try:
            # Get the height, weight, and age inputs
            height = int(height_entry.get())
            weight = float(weight_entry.get())
            total_months = int(total_month_entry.get())
            gender = gender_option.get()

            # Check if age is between 24 and 60 months
            if 24 <= total_months <= 60:
                if gender == "female":
                    thresholds = female_height_thresholds
                elif gender == "male":
                    thresholds = male_height_thresholds
                else:
                    messagebox.showerror("Error", "Invalid gender selection.")
                    return

                # Check if height is within the defined thresholds
                if height in thresholds:
                    lower_bound, upper_bound = thresholds[height]
                    if weight < lower_bound:
                        weight_length_entry.insert(0, "severe acute malnutrition")
                    elif lower_bound <= weight <= upper_bound:
                        weight_length_entry.insert(0,"moderate acute malnutrition" )
                    else:
                        weight_length_entry.insert(0, "normal")
                else:
                    # Height out of range
                    weight_length_entry.insert(0, "N/A")
                    messagebox.showinfo("Out of Range", "Height is out of range for classification.")
            else:
                # Age out of range
                weight_length_entry.insert(0, "N/A")


        except ValueError:
            # Handle invalid input error
            messagebox.showerror("Invalid Input", "Please enter valid values for age, gender, height and weight.")

    from tkinter import messagebox

    def weight_age_category():
        weight_age_entry.delete(0, END)
        #if int(total_month_entry.get()) == 24 and gender_option.get() == "female" and 8.1 <= float(weight_entry.get()) < 9.0:
        #    weight_age_entry.insert(0,"moderately underweight")
        #elif int(total_month_entry.get()) == 24 and gender_option.get() == "female" and float(weight_entry.get()) < 8.1:
        #    weight_age_entry.insert(0, "severely underweight")
        #elif int(total_month_entry.get()) == 24 and gender_option.get() == "female" and float(weight_entry.get()) >= 9.0:
        #    weight_age_entry.insert(0, "normal")
        # Define weight thresholds for each month between 24 and 72
        weight_female_thresholds = {
            24: (8.1, 9.0),
            25: (8.2, 9.2),
            26: (8.4, 9.4),
            27: (8.5, 9.5),
            28: (8.6, 9.7),
            29: (8.7, 9.0),
            30: (8.8, 9.8),
            31: (9.0, 10.1),
            32: (9.1, 10.3),
            33: (9.3, 10.4),
            34: (9.4, 10.5),
            35: (9.5, 10.7),
            36: (9.6, 10.8),
            37: (9.7, 10.9),
            38: (9.8, 11.1),
            39: (9.9, 11.2),
            40: (10.1, 11.3),
            41: (10.2, 11.5),
            42: (10.3, 11.6),
            43: (10.4, 11.7), # Check again for error
            44: (10.5, 11.8) , # Check for error
            45: (10.6, 12.0),
            46: (10.7, 12.1),
            47: (10.8, 12.2),
            48: (10.9, 12.3),
            49: (11.0, 12.4),
            50: (11.1, 12.6),
            51: (11.2, 12.7),
            52: (11.3, 12.8),
            53: (11.4, 12.9),
            54: (11.5, 13.0),
            55: (11.6, 13.2),
            56: (11.7, 13.3),
            57: (11.8, 13.4),
            58: (11.9, 13.5),
            59: (12.0, 13.6),
            60: (12.1, 13.7),
            61: (12.4, 14.0), #check
            62: (12.5, 14.1),
            63: (12.6, 14.2),
            64: (12.7, 14.3),
            65: (12.8, 14.4),
            66: (12.9, 14.6),
            67: (13.0, 14.7),
            68: (13.1, 14.8),
            69: (13.2, 14.9),
            70: (13.3, 15.0),
            71: (13.4, 15.2),
            72: (13.5, 15.3),
            # Add more months as needed up to 72
        }
        weight_male_thresholds = {
            24: (8.6, 9.7),
            25: (8.8, 9.8),
            26: (8.9, 10.0),
            27: (9.0, 10.1),
            28: (9.1, 10.2),
            29: (9.2, 10.4),
            30: (9.4, 10.5),
            31: (9.5, 10.7),
            32: (9.6, 10.8),
            33: (9.7, 10.9),
            34: (9.8, 11.0),
            35: (9.9, 11.2),
            36: (10.0, 11.3),
            37: (10.1, 11.4),
            38: (10.2, 11.5),
            39: (10.3, 11.6),
            40: (10.4, 11.8),
            41: (10.5, 11.9),
            42: (10.6, 12.0),
            43: (10.7, 12.1),  # Check again for error
            44: (10.8, 12.2),  # Check for error
            45: (10.9, 12.4),
            46: (11.0, 12.5),
            47: (11.1, 12.6),
            48: (11.2, 12.7),
            49: (11.3, 12.8),
            50: (11.4, 12.9),
            51: (11.5, 13.1),
            52: (11.6, 13.2),
            53: (11.7, 13.3),
            54: (11.8, 13.4),
            55: (11.9, 13.5),
            56: (12.0, 13.6),
            57: (12.1, 13.7),
            58: (12.2, 13.8),
            59: (12.3, 14.0),
            60: (12.4, 14.1),
            61: (12.7, 14.4),  # check
            62: (12.8, 14.5),
            63: (13.0, 14.6),
            64: (13.1, 14.8),
            65: (13.2, 14.9),
            66: (13.3, 15.0),
            67: (13.4, 15.2),
            68: (13.6, 15.3),
            69: (13.7, 15.4),
            70: (13.8, 15.6),
            71: (13.9, 15.7),
            72: (14.1, 15.9) }


        try:
            # Get the total months, weight, and gender
            total_months = int(total_month_entry.get())
            weight = float(weight_entry.get())
            gender = gender_option.get()

            # Check if the input months are in the valid range
            if 24 <= total_months <= 72:
                if gender == "female" and total_months in weight_female_thresholds:
                    lower_bound, upper_bound = weight_female_thresholds[total_months]
                elif gender == "male" and total_months in weight_male_thresholds:
                    lower_bound, upper_bound = weight_male_thresholds[total_months]
                else:
                    weight_age_entry.insert(0, "N/A")  # If gender is invalid or out of defined months
                    return

                # Classify weight based on thresholds
                if weight < lower_bound:
                    weight_age_entry.insert(0, "severely underweight")
                elif lower_bound <= weight < upper_bound:
                    weight_age_entry.insert(0, "moderately underweight")
                else:
                    weight_age_entry.insert(0, "normal")
            else:
                weight_age_entry.insert(0, "N/A")  # Out of range months show "N/A"

        except ValueError:
            # Show an error message if the input is invalid
            messagebox.showerror("Invalid Input", "Please enter valid values for age, gender, height and weight.")

    def length_age_category():
        length_age_entry.delete(0, END)

        # Female height thresholds
        female_thresholds = {
            24: 79.3,
            25: 80.0,
            26: 80.8,
            27: 81.5,
            28: 82.2,
            29: 82.9,
            30: 83.6,
            31: 84.3,
            32: 84.9,
            33: 85.6,
            34: 86.2,
            35: 86.8,
            36: 87.4,
            37: 88.0,
            38: 88.6,
            39: 89.2,
            40: 89.8,
            41: 90.4,
            42: 90.9,
            43: 91.5,
            44: 92.0,
            45: 92.5,
            46: 93.1,
            47: 93.6,
            48: 94.1,
            49: 94.6,
            50: 95.1,
            51: 96.1,
            52: 96.6,
            53: 97.1,
            54: 97.6,  # Corrected this entry
            55: 98.1,
            56: 98.5,
            57: 99.0,
            58: 99.5,
            59: 100.0,
            60: 100.5,
            61: 101.0,
            62: 101.4,
            63: 101.9,
            64: 102.3,
            65: 102.7,
            66: 103.2,
            67: 103.6,
            68: 104.0,
            69: 104.5,
            70: 105.0,
            71: 105.5,
            72: 106.0,
        }

        # Male height thresholds
        male_thresholds = {
            24: 81.0,
            25: 81.7,
            26: 82.5,
            27: 83.1,
            28: 83.8,
            29: 84.5,
            30: 85.1,
            31: 85.7,
            32: 86.4,
            33: 87.2,
            34: 88.1,
            35: 88.7,
            36: 89.2,
            37: 89.8,
            38: 90.3,
            39: 90.9,
            40: 91.4,
            41: 91.9,
            42: 92.4,
            43: 92.9,
            44: 93.5,
            45: 94.0,
            46: 94.5,
            47: 94.9,
            48: 95.4,
            49: 95.9,
            50: 96.4,
            51: 96.9,
            52: 97.4,
            53: 98.0,
            54: 98.5,
            55: 99.0,
            56: 99.5,
            57: 100.0,
            58: 100.5,
            59: 101.0,
            60: 101.5,
            61: 102.0,
            62: 102.5,
            63: 103.0,
            64: 103.5,
            65: 104.0,
            66: 104.5,
            67: 105.0,
            68: 105.5,
            69: 106.0,
            70: 106.5,
            71: 107.0,
            72: 107.5,
        }

        # Get user inputs
        try:
            age = int(total_month_entry.get())
            gender = gender_option.get()
            height = float(height_entry.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values for months and weight.")

            return

        # Determine which thresholds to use
        if gender == "female":
            height_thresholds = female_thresholds
        elif gender == "male":
            height_thresholds = male_thresholds
        else:
            length_age_entry.insert(0, "Invalid gender")
            return

        # Check if age is in thresholds
        if age in height_thresholds:
            threshold = height_thresholds[age]
            if height < threshold:
                length_age_entry.insert(0, "chronic malnutrition")
            else:
                length_age_entry.insert(0, "normal")
        else:
            length_age_entry.insert(0, "N/A")



    weight_age = ttk.Button(secondframe, text="Weight for age( only for 24-72 months)", command=weight_age_category)
    weight_age.grid(column=5, row=9)
    # button_hover(weight_age)
    weight_age_entry = Entry(secondframe, width=25)
    weight_age_entry.grid(column=6, row=9)

    length_age = ttk.Button(secondframe, text="Height for age (only for 24-72 months)",command=length_age_category)
    length_age.grid(column=5, row=10)
    # button_hover(length_age)
    length_age_entry = Entry(secondframe, width=25)
    length_age_entry.grid(column=6, row=10)

    weight_length = ttk.Button(secondframe, text="Weight for height (only for 24-60 months and between 45-120cm )", command=weight_length_category)
    weight_length.grid(column=5, row=11)
    # button_hover(weight_length)
    weight_length_entry = Entry(secondframe, width=25)
    weight_length_entry.grid(column=6, row=11)


    CheckVar1 = StringVar(value="no")
    b1_label = Label(sicknessframe, text="B1: Severe anemia", width=22).grid(column=1, row=14)
    b1_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar1, onvalue="yes", offvalue="no")
    b1_entry.grid(column=2, row=14)

    CheckVar2 = StringVar(value="no")
    b2_label = Label(sicknessframe, text="B2: Vitamin A deficiency", width=22).grid(column=1, row=15)
    b2_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar2, onvalue="yes", offvalue="no")
    b2_entry.grid(column=2, row=15)

    CheckVar3 = StringVar(value="no")
    b3_label = Label(sicknessframe, text="B3: Vit D deficiency", width=30).grid(column=1, row=16)
    b3_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar3, onvalue="yes", offvalue="no")
    b3_entry.grid(column=2, row=16)

    CheckVar4 = StringVar(value="no")
    b4_label = Label(sicknessframe, text="B4: Goitre", width=30).grid(column=1, row=17)
    b4_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar4, onvalue="yes", offvalue="no")
    b4_entry.grid(column=2, row=17)

    CheckVar5 = StringVar(value="no")
    b5_label = Label(sicknessframe, text="B5: Oedema / swelling of legs (2-6 years only)").grid(column=1, row=18)
    b5_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar5, onvalue="yes", offvalue="no")
    b5_entry.grid(column=2, row=18)

    CheckVar6 = StringVar(value="no")
    c1_label = Label(sicknessframe, text="C1: Convulsive disorders/epilepsy").grid(column=1, row=19)
    c1_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar6, onvalue="yes", offvalue="no")
    c1_entry.grid(column=2, row=19)

    CheckVar7 = StringVar(value="no")
    c2_label = Label(sicknessframe, text="C2: Otitis media/middle ear infection").grid(column=1, row=20)
    c2_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar7, onvalue="yes", offvalue="no")
    c2_entry.grid(column=2, row=20)

    CheckVar8 = StringVar(value="no")
    c3_label = Label(sicknessframe, text="C3: Dental condition", width=30).grid(column=1, row=21)
    c3_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar8, onvalue="yes", offvalue="no")
    c3_entry.grid(column=2, row=21)

    CheckVar9 = StringVar(value="no")
    c4_label = Label(sicknessframe, text="C4: Skin condition", width=30).grid(column=1, row=22)
    c4_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar9, onvalue="yes", offvalue="no")
    c4_entry.grid(column=2, row=22)

    CheckVar10 = StringVar(value="no")
    c5_label = Label(sicknessframe, text="C5: Rheumatic heart disease", width=30).grid(column=3, row=14)
    c5_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar10, onvalue="yes", offvalue="no")
    c5_entry.grid(column=4, row=14)

    CheckVar11 = StringVar(value="no")
    c6_label = Label(sicknessframe, text="C6: Respiratory problem (suggestive of Asthma/TB)", width=40)
    c6_label.grid(column=3, row=15)
    c6_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar11, onvalue="yes", offvalue="no")
    c6_entry.grid(column=4, row=15)

    CheckVar12 = StringVar(value="no")
    d1_label = Label(sicknessframe, text="D1: Vision problem (night vision or day vision)", width=40).grid(column=3, row=16)
    d1_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar12, onvalue="yes", offvalue="no")
    d1_entry.grid(column=4, row=16)

    CheckVar13 = StringVar(value="no")
    d2_label = Label(sicknessframe, text="D2: Delay in walking", width=30).grid(column=3, row=17)
    d2_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar13, onvalue="yes", offvalue="no")
    d2_entry.grid(column=4, row=17)

    CheckVar14 = StringVar(value="no")
    d3_label = Label(sicknessframe, text="D3: Stiffness/floppiness/reduced strength in arms/legs", width=40).grid(column=3, row=18)
    d3_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar14, onvalue="yes", offvalue="no")
    d3_entry.grid(column=4, row=18)


    CheckVar16 = StringVar(value="no")
    d5_label = Label(sicknessframe, text="D5: Reading/writing/calculatory difficulties", width=40)
    d5_label.grid(column=3, row=19)
    d5_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar16, onvalue="yes", offvalue="no")
    d5_entry.grid(column=4, row=19)

    CheckVar17 = StringVar(value="no")
    d6_label = Label(sicknessframe, text="D6: Difficulty in speaking", width=30).grid(column=3, row=20)
    d6_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar17, onvalue="yes", offvalue="no")
    d6_entry.grid(column=4, row=20)

    CheckVar18 = StringVar(value="no")
    d7_label = Label(sicknessframe, text="D7: Difficulty in hearing", width=30).grid(column=3, row=21)
    d7_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar18, onvalue="yes", offvalue="no")
    d7_entry.grid(column=4, row=21)

    CheckVar19 = StringVar(value="no")
    d8_label = Label(sicknessframe, text="D8: learning difficulties", width=30).grid(column=3, row=22)
    d8_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar19, onvalue="yes", offvalue="no")
    d8_entry.grid(column=4, row=22)

    CheckVar20 = StringVar(value="no")
    d9_label = Label(sicknessframe, text="D9: attention difficulties", width=30).grid(column=5, row=14)
    d9_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar20, onvalue="yes", offvalue="no")
    d9_entry.grid(column=6, row=14)

    #CheckVar21 = StringVar(value="no")

    #CheckVar22 = StringVar(value="no")

    CheckVar23 = StringVar(value="no")
    e3_label = Label(sicknessframe, text="E3: Feeling unduly tired/depressed (all students)").grid(column=5, row=15)
    e3_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar23, onvalue="yes", offvalue="no")
    e3_entry.grid(column=6, row=15)

    CheckVar24 = StringVar(value="no")
    e4_label = Label(sicknessframe, text="E4: Menstrual cycle started(female)?").grid(column=5, row=16)
    e4_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar24, onvalue="yes", offvalue="no")
    e4_entry.grid(column=6, row=16)

    CheckVar25 = StringVar(value="no")
    e5_label = Label(sicknessframe, text="E5: If periods started, are they regular (28 +/- 7d)?").grid(column=5, row=17)
    e5_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar25, onvalue="yes", offvalue="no")
    e5_entry.grid(column=6, row=17)

    CheckVar26 = StringVar(value="no")
    e6_label = Label(sicknessframe, text="E6:Pain/burning while urinating (all students)?").grid(column=5, row=18)
    e6_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar26, onvalue="yes", offvalue="no")
    e6_entry.grid(column=6, row=18)

    CheckVar27 = StringVar(value="no")
    e7_label = Label(sicknessframe, text="E7: Discharge/foul smell from genito-urinary area (all students)?").grid(column=5, row=19)
    e7_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar27, onvalue="yes", offvalue="no")
    e7_entry.grid(column=6, row=19)

    CheckVar28 = StringVar(value="no")
    e8_label = Label(sicknessframe, text="E8: Menstrual pain (menstruating female)?").grid(column=5, row=20)
    e8_entry = Checkbutton(sicknessframe, text="Yes", width=5, variable=CheckVar28, onvalue="yes", offvalue="no")
    e8_entry.grid(column=6, row=20)

    CheckVar29 = StringVar(value="unknown")
    deworming_label = Label(sicknessframe, text="Dewormed last 6 months").grid(column=5, row=21)
    deworming_entry = OptionMenu(sicknessframe,CheckVar29,"unknown","yes","no")
    deworming_entry.grid(column=6, row=21)

    CheckVar30 = StringVar(value="unknown")
    vaccination_label = Label(sicknessframe, text="Follows govern. Childhood vacc. (immunization)").grid(column=5, row=22)
    vaccination_entry = OptionMenu(sicknessframe,CheckVar30, "unknown","yes","no")
    vaccination_entry.grid(column=6, row=22)

    lastframe = LabelFrame(scrollable_frame)
    lastframe.grid(row=28, rowspan=3, columnspan=2, ipadx=89,sticky=W)

    e9_label = Label(sicknessframe, text="E9: remarks (free text)", width=30)
    e9_label.grid(column=1, row=28)
    e9_entry = Entry(sicknessframe,width=120)
    e9_entry.grid(column=2, row=28,columnspan=4)


    known_disease_label = Label(secondframe, text="Known earlier disease")
    known_disease_label.grid(column=1, row=13)
    known_disease_entry = Entry(secondframe)
    known_disease_entry.grid(column=2, row=13)

    # Load the image (ensure that reset.png is in the correct directory or provide the full path)
    # Load the image
    reset_image = tk.PhotoImage(file="reset.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    reset_image = reset_image.subsample(19, 19)  # Adjust the numbers to scale down (2, 2) means half size

    # Create the button with the image and command
    clearbtn = ttk.Button(buttonframe, image=reset_image, command=reset)
    cleartooltip = ToolTip(clearbtn,"New student")

    # Set the button position in the grid
    clearbtn.grid(row=0, column=2,padx=20)

    save_image = tk.PhotoImage(file="save.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    save_image = save_image.subsample(19,19)  # A
    savebtn = ttk.Button(buttonframe, text="SAVE NEW SCREENING",image=save_image, command=save_or_update_entry)
    savebtn.grid(row=0, column=3,padx=20)
    tooltip = ToolTip(savebtn,"Save screening")

    delete_image = tk.PhotoImage(file="delete.png")

    import sqlite3
    from tkinter import messagebox

    def delete_journal():
        # Retrieve the student_id and screening_date from the relevant widgets
        student_id = id_entry.get()  # Ensure id_entry is correctly initialized
        screening_date = screening_date_entry.get()  # Ensure screening_date_entry is correctly initialized

        # Ensure student_id is provided before attempting to delete
        if not student_id:
            print("Please provide a Student ID.")
            return

        # Confirm with the user before deleting
        confirm_message = f"Are you sure you want to delete the entry for Student ID {student_id}"
        if screening_date:
            confirm_message += f" on {screening_date}?"
        else:
            confirm_message += " with no screening date?"

        confirm = messagebox.askyesno("Confirm Delete", confirm_message)
        if not confirm:
            return

        # Perform the deletion in the database
        try:
            with sqlite3.connect("gracehealth.db") as conn:  # Ensure database file path is correct
                cursor = conn.cursor()

                # Case when screening_date is provided
                if screening_date:
                    cursor.execute("""
                        DELETE FROM student
                        WHERE id = ? AND screen_date = ?
                        
                        
                    """, (student_id, screening_date))
                else:
                    # Case when screening_date is empty or NULL, delete based on student_id only
                    cursor.execute("""
                        DELETE FROM student
                        WHERE id = ? 
                        AND (screen_date IS NULL OR screen_date = '')
                        
                    """, (student_id,))

                conn.commit()

                # Check if the record was deleted
                if cursor.rowcount > 0:
                    print(f"Entry for Student ID {student_id} deleted successfully.")
                    clear_text()  # Call clear_text if it’s meant to clear the entries
                else:
                    print("No matching record found to delete.")

        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    # Resize the image to fit the button (use subsample to reduce the size)
    delete_image = delete_image.subsample(19, 19)  # A
    delete_btn = ttk.Button(buttonframe, text="SAVE NEW SCREENING", image=delete_image, command=delete_journal)
    delete_btn.grid(row=0, column=9, padx=20)
    delete_tooltip=ToolTip(delete_btn,"Delete this screening")

    def populate_for_edit(user_id=None, screening_date=None):


        with sqlite3.connect("gracehealth.db") as connection:
            cursor = connection.cursor()

            # Use the screening_date and user_id to fetch the student record
            if screening_date is not None:
                cursor.execute("""
                    SELECT * FROM student WHERE id = ? AND screen_date = ?
                """, (user_id, screening_date))
            else:
                cursor.execute("""
                    SELECT * FROM student WHERE id = ? ORDER BY rowid DESC LIMIT 1
                """, (user_id,))

            student_data = cursor.fetchone()

            if student_data is None:

                return

        # Populate each entry widget with the data from the database
        if student_data:
            try:
                # Assuming student_data structure and how you populate your form goes here...
                # Example for populating tea_garden_entry
                value = student_data[60]
                if value is not None and value.strip():
                    if value in tea_garden_entry['values']:
                        tea_garden_entry.set(value)
                    else:
                        print(f"Value '{value}' not found in Combobox values. Setting it as a default.")
                        tea_garden_entry.set('')  # Set a default value or leave it empty
                else:
                    print("Empty or None value from the database. Resetting the combobox.")
                    tea_garden_entry.set('')  # Set to empty string or a default value
            except IndexError:
                print("Index error while accessing student_data.")
            id_entry.delete(0, tk.END)
            id_entry.insert(0, student_data[0])

            name_entry.delete(0, tk.END)
            name_entry.insert(0, student_data[1])

            date_of_birth_entry.delete(0, tk.END)
            date_of_birth_entry.insert(0, student_data[2])

            gender_option.set(student_data[3])

            class_entry.delete(0, tk.END)
            class_entry.insert(0, student_data[4])

            roll_entry.delete(0, tk.END)
            roll_entry.insert(0, student_data[5])

            aadhaar_entry.delete(0, tk.END)
            aadhaar_entry.insert(0, student_data[6])

            father_guardian_entry.delete(0, tk.END)
            father_guardian_entry.insert(0, student_data[7])

            mother_entry.delete(0, tk.END)
            mother_entry.insert(0, student_data[8])

            contact_no_entry.delete(0, tk.END)
            contact_no_entry.insert(0, student_data[9])

            address_entry.delete(0, tk.END)
            address_entry.insert(0, student_data[10])

            email_entry.delete(0, tk.END)
            email_entry.insert(0, student_data[11])

            teacher_entry.delete(0, tk.END)
            teacher_entry.insert(0, student_data[12])

            school_entry.delete(0, tk.END)
            school_entry.insert(0, student_data[13])

            last_school_entry.delete(0, tk.END)
            last_school_entry.insert(0, student_data[14])

            place_of_birth_entry.delete(0, tk.END)
            place_of_birth_entry.insert(0, student_data[15])

            known_disease_entry.delete(0, tk.END)
            known_disease_entry.insert(0, student_data[16])

            weight_entry.delete(0, tk.END)
            weight_entry.insert(0, student_data[19])

            height_entry.delete(0, tk.END)
            height_entry.insert(0, student_data[20])

            BMI_entry.delete(0, tk.END)
            BMI_entry.insert(0, student_data[21])

            both_eyesight_var.set(student_data[22])
            left_eyesight_var.set(student_data[23])
            right_eyesight_var.set(student_data[24])

            vision_problem_entry.delete(0, tk.END)
            vision_problem_entry.insert(0, student_data[25])

            CheckVar1.set(student_data[26])
            CheckVar2.set(student_data[27])
            CheckVar3.set(student_data[28])
            CheckVar4.set(student_data[29])
            CheckVar5.set(student_data[30])
            CheckVar6.set(student_data[31])
            CheckVar7.set(student_data[32])
            CheckVar8.set(student_data[33])
            CheckVar9.set(student_data[34])
            CheckVar10.set(student_data[35])
            CheckVar11.set(student_data[36])
            CheckVar12.set(student_data[37])
            CheckVar13.set(student_data[38])
            CheckVar14.set(student_data[39])
            CheckVar16.set(student_data[40])
            CheckVar17.set(student_data[41])
            CheckVar18.set(student_data[42])
            CheckVar19.set(student_data[43])
            CheckVar20.set(student_data[44])
            CheckVar23.set(student_data[45])
            CheckVar24.set(student_data[46])
            CheckVar25.set(student_data[47])
            CheckVar26.set(student_data[48])
            CheckVar27.set(student_data[49])
            CheckVar28.set(student_data[50])

            e9_entry.delete(0, tk.END)
            e9_entry.insert(0, student_data[51])

            BMI_category_entry.delete(0, tk.END)
            BMI_category_entry.insert(0, student_data[52])

            weight_age_entry.delete(0, tk.END)
            weight_age_entry.insert(0, student_data[53])

            length_age_entry.delete(0, tk.END)
            length_age_entry.insert(0, student_data[54])

            weight_length_entry.delete(0, tk.END)
            weight_length_entry.insert(0, student_data[55])

            total_month_entry.delete(0, tk.END)
            total_month_entry.insert(0, student_data[56])

            CheckVar29.set(student_data[57])
            CheckVar30.set(student_data[58])

            screening_date_entry.delete(0,tk.END)
            screening_date = student_data[61]


            if screening_date:  # Only insert if screening_date is not empty or None
                screening_date_entry.delete(0, 'end')  # Clear the DateEntry first
                screening_date_entry.insert(0, screening_date)
            else:
                # Handle the case where the screening_date is empty or None
                screening_date_entry.delete(0, 'end')  # Clear the DateEntry
                print("Empty or None value for screening date. Resetting the DateEntry.")
            #tea_garden_entry.delete(0, tk.END)
            #tea_garden_entry.set(student_data[60])
            age_value = student_data[62] if student_data[62] is not None else ""

            # Convert the value to string if necessary and insert it into the age_entry
            age_entry.delete(0, tk.END)  # Clear the entry before inserting
            age_entry.insert(0, str(age_value))
            #muac_entry.delete(0,END)
            #muac_entry.insert(0,student_data[64])

                # Check and insert data into the 'muac_entry' widget
            if student_data[64] is not None and student_data[64] != "":
                muac_entry.delete(0, 'end')  # Clear any existing text
                muac_entry.insert(0, str(student_data[64]))  # Ensure it's a string
            else:
                print("Empty or None value for 'muac'. Resetting the entry field.")
                muac_entry.delete(0, 'end')  # Clear the field
            if student_data[65] is not None and student_data[65] != "":
                muac_category_entry.delete(0, 'end')  # Clear any existing text
                muac_category_entry.insert(0, str(student_data[65]))  # Ensure it's a string
            else:
                print("Empty or None value for 'muac_category'. Resetting the entry field.")
                muac_category_entry.delete(0, 'end')  # Clear the field

    def populate_for_new_journal(item_id):
        connection = sqlite3.connect("gracehealth.db")
        cursor = connection.cursor()
        cursor.execute("SELECT * from student where id = ? LIMIT 1 ",(item_id,))
        student_data= cursor.fetchone()
        id_entry.delete(0, tk.END)
        id_entry.insert(0, student_data[0])

        name_entry.delete(0, tk.END)
        name_entry.insert(0, student_data[1])

        date_of_birth_entry.delete(0, tk.END)
        date_of_birth_entry.insert(0, student_data[2])

        gender_option.set(student_data[3])
        aadhaar_entry.delete(0, tk.END)
        aadhaar_entry.insert(0, student_data[6])

        father_guardian_entry.delete(0, tk.END)
        father_guardian_entry.insert(0, student_data[7])

        mother_entry.delete(0, tk.END)
        mother_entry.insert(0, student_data[8])

        contact_no_entry.delete(0, tk.END)
        contact_no_entry.insert(0, student_data[9])

        address_entry.delete(0, tk.END)
        address_entry.insert(0, student_data[10])

        email_entry.delete(0, tk.END)
        email_entry.insert(0, student_data[11])

        teacher_entry.delete(0, tk.END)
        teacher_entry.insert(0, student_data[12])

        school_entry.delete(0, tk.END)
        school_entry.insert(0, student_data[13])

        last_school_entry.delete(0, tk.END)
        last_school_entry.insert(0, student_data[14])

        place_of_birth_entry.delete(0, tk.END)
        place_of_birth_entry.insert(0, student_data[15])

        known_disease_entry.delete(0, tk.END)
        known_disease_entry.insert(0, student_data[16])

        CheckVar29.set("unknown")
        CheckVar30.set(student_data[58])


    def next_record():
        try:
            current_id = int(id_entry.get())

            with sqlite3.connect('gracehealth.db') as conn:
                cursor = conn.cursor()
                # Query to find the next available ID greater than the current ID
                cursor.execute("SELECT MIN(id) FROM student WHERE id > ?", (current_id,))
                next_id = cursor.fetchone()[0]

                if next_id:
                    # Populate with the next valid ID if found
                    populate_for_edit(next_id)
                    display_journal(next_id, summary_frame)
                else:
                    print("No more records available.")

        except ValueError:
            print("Invalid ID in id_entry.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    def previous_record():
        try:
            current_id = int(id_entry.get())

            with sqlite3.connect('gracehealth.db') as conn:
                cursor = conn.cursor()
                # Query to find the previous available ID less than the current ID
                cursor.execute("SELECT MAX(id) FROM student WHERE id < ?", (current_id,))
                previous_id = cursor.fetchone()[0]

                if previous_id:
                    # Populate with the previous valid ID if found
                    populate_for_edit(previous_id)
                    display_journal(previous_id,summary_frame)
                else:
                    print("No more records available.")

        except ValueError:
            print("Invalid ID in id_entry.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    # Define current_rowid at the top of the script, if not already done

    def student_same_previous():
        student_id = int(id_entry.get())
        current_screening_date = screening_date_entry.get()

        with sqlite3.connect('gracehealth.db') as conn:
            cursor = conn.cursor()
            # SQL query to find the previous screening date
            cursor.execute("""
                SELECT screen_date 
                FROM student 
                WHERE id = ? AND screen_date < ? 
                ORDER BY screen_date DESC 
                LIMIT 1
            """, (student_id, current_screening_date))

            previous_date = cursor.fetchone()
            if previous_date:
                # Unpack the previous_date tuple to get the actual date
                previous_date_value = previous_date[0]  # Get the first element of the tuple
                # Populate with the previous valid ID if found
                populate_for_edit(screening_date=previous_date_value, user_id=student_id)
            else:
                print("No more records available.")

    def student_same_next():
        try:
            student_id = int(id_entry.get())
            current_screening_date = screening_date_entry.get()

            with sqlite3.connect('gracehealth.db') as conn:
                cursor = conn.cursor()
                # SQL query to find the next screening date
                cursor.execute("""
                    SELECT screen_date 
                    FROM student 
                    WHERE id = ? AND screen_date > ? 
                    ORDER BY screen_date ASC 
                    LIMIT 1
                """, (student_id, current_screening_date))

                next_record = cursor.fetchone()

                if next_record:
                    next_screening_date = next_record[0]
                    # Correctly call populate_for_edit with the user ID and next screening date
                    populate_for_edit(screening_date=next_screening_date, user_id=student_id)
                    # Optionally call display_journal if needed, passing the next_screening_date
                    display_journal(next_screening_date, summary_frame)
                else:
                    print("No more records available.")

        except ValueError:
            print("Invalid Student ID or screening date.")
        except sqlite3.Error as e:
            print(f"Database error: {e}")

    next_image = tk.PhotoImage(file="next.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    next_image = next_image.subsample(19, 19)  # A

    next_btn = ttk.Button(buttonframe, image=next_image, command=next_record)
    next_btn.grid(row=0, column=6, padx=20)
    next_tooltip= ToolTip(next_btn,"Next student")

    before_image = tk.PhotoImage(file="before.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    before_image = before_image.subsample(19, 19)  # A

    before_btn = ttk.Button(buttonframe, image=before_image , command=previous_record)
    before_btn.grid(row=0, column=5, padx=20)
    before_tooltip= ToolTip(before_btn,"Previous student")

    # Hover function for styling buttons (assuming you already have this function)
    up_image = tk.PhotoImage(file="up-arrow.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    up_image = up_image.subsample(19, 19)  # A


    up_btn = ttk.Button(buttonframe, image=up_image, command=student_same_next)
    up_btn.grid(row=0, column=7, padx=20)
    up_tooltip=ToolTip(up_btn,"Newer screening of same student")

    down_image = tk.PhotoImage(file="down-arrow.png")

    # Resize the image to fit the button (use subsample to reduce the size)
    down_image = down_image.subsample(19, 19)  # A


    down_btn = ttk.Button(buttonframe, image=down_image, command=student_same_previous)
    down_btn.grid(row=0, column=8, padx=20)
    down_tooltip =  ToolTip(down_btn,"Earlier screening of same student")

    check_id_confirmation = Label(scrollable_frame)
    check_id_confirmation.grid(row=2, column=4)
    id_value=id_entry.get()
    print(f"id_value is {id_value}")

    # Fix the button command: pass the function reference, not call it
    # Button to show journal, passing the id_entry widget, not the value
    #row_id_label = Label(buttonframe, text="Screening ID: None", font=("Arial", 12), fg="blue")
    #row_id_label.grid(row=0, column=9)



    connection.commit()
    connection.close()
    window.mainloop()





# mainwindow.config(background="light pink")
# mainwindow.title(" School Health records", )


        #Set up imports

connection=sqlite3.connect("gracehealth.db")
cursor=connection.cursor()
cursor.execute("SELECT DISTINCT tea_garden FROM student")
tea_garden_names=cursor.fetchall()
tea_garden_database_list = [tea_garden_chosen[0] for tea_garden_chosen in tea_garden_names]





cursor.execute("SELECT DISTINCT school_name FROM student")
school_names = cursor.fetchall()
school_database= [school[0] for school in school_names]

school_database_list = ["All schools combined"] + school_database
connection.commit()
connection.close()


font="Arial,12"

import sqlite3
import sqlite3



def delete_column_directly(column_name):
    try:
        # Connect to the database
        conn = sqlite3.connect("gracehealth.db")
        cursor = conn.cursor()

        # Drop the column
        cursor.execute(f"ALTER TABLE student DROP COLUMN {column_name};")

        # Commit the changes
        conn.commit()
        conn.close()

        print(f"Column '{column_name}' successfully deleted from the 'student' table.")
    except sqlite3.Error as e:
        print(f"Error while deleting column: {e}")




import sqlite3

def show_table_columns_with_index(database, table_name):
    try:
        # Connect to the database
        conn = sqlite3.connect(database)
        cursor = conn.cursor()

        # Fetch table column info
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = cursor.fetchall()

        # Print column details
        if columns:
            print(f"Columns in table '{table_name}':")
            print(f"{'Index':<10}{'Column Name':<20}{'Type':<10}{'Not Null':<10}{'Default Value'}")
            print("-" * 60)
            for col in columns:
                # col: (index, name, type, notnull, default_value, primary_key)
                index, name, col_type, notnull, default_value, primary_key = col
                print(f"{index:<10}{name:<20}{col_type:<10}{notnull:<10}{default_value}")
        else:
            print(f"No columns found for table '{table_name}'.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        conn.close()

# Example usage
show_table_columns_with_index("gracehealth.db", "student")
import sqlite3

def replace_school_name(old_name, new_name):
    try:
        # Connect to the database
        conn = sqlite3.connect("gracehealth.db")
        cursor = conn.cursor()

        # Update the school_name column
        cursor.execute("""
            UPDATE student
            SET school_name = ?
            WHERE school_name = ?;
        """, (new_name, old_name))

        # Commit the changes
        conn.commit()
        updated_rows = cursor.rowcount  # Get the number of updated rows
        conn.close()

        print(f"Successfully updated {updated_rows} rows: '{old_name}' replaced with '{new_name}'.")
    except sqlite3.Error as e:
        print(f"Error while updating school names: {e}")
replace_school_name("Eden Christian English school, Makrapara", "Eden English School")

new_journal()
