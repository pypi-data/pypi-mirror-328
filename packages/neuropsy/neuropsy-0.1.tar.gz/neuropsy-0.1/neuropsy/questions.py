import sys  # Import sys for PySide6 application exit
from PySide6.QtWidgets import (QApplication, QWidget, QLabel, QRadioButton,
                             QVBoxLayout, QGroupBox, QCheckBox, QPushButton,
                             QMessageBox, QLineEdit, QSizePolicy, QScrollArea,
                             QHBoxLayout, QFileDialog)  # Import necessary widgets
from PySide6.QtCore import Qt  # Import Qt for alignment
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from functools import partial
import json
from .pdf_generator import NeuropsyPDFGenerator
import os
from .score_cal import ScoreCalculator





class Question:
    def __init__(self, question_text, description=""):
        self.question_text = question_text
        self.description = description
        self.answer = None
        self.comments = ""

    def create_description_label(self):
        if self.description:
            desc_label = QLabel(self.description)
            desc_label.setWordWrap(True)
            desc_label.setStyleSheet("color: gray; font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif; font-size: 14pt;")
            return desc_label
        return None

    def create_comments_box(self):
        comments_label = QLabel("Additional Comments:")
        comments_label.setStyleSheet("font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif; font-size: 14pt;")
        comments_box = QLineEdit()
        comments_box.setPlaceholderText("Enter any additional comments here...")
        comments_box.setStyleSheet("font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif; font-size: 14pt;")
        comments_box.textChanged.connect(lambda text: setattr(self, 'comments', text))
        comments_box.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        return comments_label, comments_box

    def display(self, layout):
        raise NotImplementedError("This method should be overridden in subclasses.")

    def get_answer(self):
        return {
            'answer': self.answer,
            'description': self.description,
            'comments': self.comments
        }

class Heading(Question):
    def __init__(self, heading_text):
        super().__init__(heading_text)

    def display(self, layout):
        label = QLabel(self.question_text)
        label.setStyleSheet("font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif; font-size: 26pt;")
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)
        
    def get_answer(self):
        return None  # Headings don't have answers

class YesNoQuestion(Question):
    def __init__(self, question_text, description=""):
        super().__init__(question_text, description)
        self.var = ""

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)
        
        # Add description if provided
        desc_label = self.create_description_label()
        if desc_label:
            layout.addWidget(desc_label)
            
        yes_button = QRadioButton("Yes")
        no_button = QRadioButton("No")
        yes_button.toggled.connect(lambda: setattr(self, 'var', 'Yes') if yes_button.isChecked() else None)
        no_button.toggled.connect(lambda: setattr(self, 'var', 'No') if no_button.isChecked() else None)
        hbox = QVBoxLayout()
        hbox.addWidget(yes_button)
        hbox.addWidget(no_button)
        layout.addLayout(hbox)
        
        # Add comments box
        comments_label, comments_box = self.create_comments_box()
        layout.addWidget(comments_label)
        layout.addWidget(comments_box)

    def get_answer(self):
        return {
            'answer': self.var,
            'description': self.description,
            'comments': self.comments
        }

class RatingQuestion(Question):
    def __init__(self, question_text, description=""):
        super().__init__(question_text, description)
        self.var = 0

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)
        
        # Add description if provided
        desc_label = self.create_description_label()
        if desc_label:
            layout.addWidget(desc_label)
            
        for i in range(1, 6):
            rb = QRadioButton(str(i))
            rb.toggled.connect(lambda checked, i=i: setattr(self, 'var', i) if checked else None)
            layout.addWidget(rb)
            
        # Add comments box
        comments_label, comments_box = self.create_comments_box()
        layout.addWidget(comments_label)
        layout.addWidget(comments_box)

    def get_answer(self):
        return {
            'answer': self.var,
            'description': self.description,
            'comments': self.comments
        }

class CheckboxQuestion(Question):
    def __init__(self, question_text, options, description=""):
        super().__init__(question_text, description)
        self.options = options
        self.vars = {opt: False for opt in options}  # Initialize to False (bool)

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)

        # Add description if provided
        desc_label = self.create_description_label()
        if desc_label:
            layout.addWidget(desc_label)
            
        for opt in self.options:
            cb = QCheckBox(opt)
            # Correct connection using a partial function
            cb.stateChanged.connect(partial(self.set_check_state, opt))  # Fixed!
            layout.addWidget(cb)

        # Add comments box
        comments_label, comments_box = self.create_comments_box()
        layout.addWidget(comments_label)
        layout.addWidget(comments_box)

    def set_check_state(self, opt, state):
        # Compare state to Qt.Checked (which is an integer)
        self.vars[opt] = state != Qt.Checked  # Store boolean value



    def get_answer(self):
        return {
            'answer': [opt for opt, checked in self.vars.items() if checked],
            'description': self.description,
            'comments': self.comments
        }
    
class TextQuestion(Question):
    def __init__(self, question_text):
        super().__init__(question_text)
        self.var = ""

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)
        text_input = QLineEdit() 
        text_input.textChanged.connect(lambda text: setattr(self, 'var', text))
        layout.addWidget(text_input)

    def get_answer(self):
        return {
            'answer': self.var,
            'description': self.description,
            'comments': self.comments
        }

class HorizontalCheckboxQuestion(Question):
    def __init__(self, question_text, options, description=""):
        super().__init__(question_text, description)
        self.options = options
        self.vars = {opt: False for opt in options}  # Initialize to False (bool)

    def display(self, layout):
        label = QLabel(self.question_text)
        layout.addWidget(label)

        # Add description if provided
        desc_label = self.create_description_label()
        if desc_label:
            layout.addWidget(desc_label)
            
        # Create horizontal layout for checkboxes
        checkbox_layout = QHBoxLayout()
        for opt in self.options:
            cb = QCheckBox(opt)
            cb.stateChanged.connect(partial(self.set_check_state, opt))
            checkbox_layout.addWidget(cb)
        layout.addLayout(checkbox_layout)

        # Add comments box
        comments_label, comments_box = self.create_comments_box()
        layout.addWidget(comments_label)
        layout.addWidget(comments_box)

    def set_check_state(self, opt, state):
        self.vars[opt] = state != Qt.Checked

    def get_answer(self):
        return {
            'answer': [opt for opt, checked in self.vars.items() if checked],
            'description': self.description,
            'comments': self.comments
        }

class Category:
    # Define a list of light, semi-transparent background colors
    COLORS = [
        "QGroupBox { background-color: rgba(255, 230, 230, 0.3); border: 1px solid gray; margin-top: 6px; } QGroupBox::title { subcontrol-origin: margin; left: 7px; padding: 0px 5px 0px 5px; }",  # Light red
        "QGroupBox { background-color: rgba(230, 255, 230, 0.3); border: 1px solid gray; margin-top: 6px; } QGroupBox::title { subcontrol-origin: margin; left: 7px; padding: 0px 5px 0px 5px; }",  # Light green
        "QGroupBox { background-color: rgba(230, 230, 255, 0.3); border: 1px solid gray; margin-top: 6px; } QGroupBox::title { subcontrol-origin: margin; left: 7px; padding: 0px 5px 0px 5px; }",  # Light blue
        "QGroupBox { background-color: rgba(255, 255, 230, 0.3); border: 1px solid gray; margin-top: 6px; } QGroupBox::title { subcontrol-origin: margin; left: 7px; padding: 0px 5px 0px 5px; }",  # Light yellow
        "QGroupBox { background-color: rgba(255, 230, 255, 0.3); border: 1px solid gray; margin-top: 6px; } QGroupBox::title { subcontrol-origin: margin; left: 7px; padding: 0px 5px 0px 5px; }",  # Light purple
    ]
    _color_index = 0  # Class variable to track color index

    def __init__(self, name, questions):
        self.name = name
        self.questions = questions
        # Get next color and increment index
        self.color = self.COLORS[Category._color_index]
        Category._color_index = (Category._color_index + 1) % len(self.COLORS)

    def display(self, layout):
        # Create a group box for the category
        category_group = QGroupBox(self.name)
        category_group.setStyleSheet(self.color)  # Apply the background color
        category_layout = QVBoxLayout()
        
        # Display all questions in this category
        for question in self.questions:
            question_group = QGroupBox()
            question_group.setStyleSheet("QGroupBox { border: none; background-color: transparent; }")  # Make inner groups transparent
            question_layout = QVBoxLayout()
            question.display(question_layout)
            question_group.setLayout(question_layout)
            category_layout.addWidget(question_group)
            
        category_group.setLayout(category_layout)
        layout.addWidget(category_group)

    def get_answers(self):
        return {q.question_text: q.get_answer() for q in self.questions}

class Neuropsy(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Remote Neuropsychological Test Battery Record Form")
        
        # Update title label style
        title_label = QLabel("Remote Neuropsychological Test Battery Record Form")
        title_label.setStyleSheet("""
            font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
            font-size: 30pt;
            color: #333;
            padding: 10px;
        """)
        title_label.setAlignment(Qt.AlignCenter)

        # Set global style for the entire application
        self.setStyleSheet("""
            QLabel {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 20pt;
            }
            QRadioButton {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 20pt;
            }
            QCheckBox {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 20pt;
            }
            QLineEdit {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 20pt;
            }
            QPushButton {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 20pt;
                padding: 5px 15px;
            }
            QGroupBox {
                font-family: 'Segoe UI Light', 'Helvetica Neue Light', sans-serif;
                font-size: 22pt;
            }
        """)

        # 1. Create the Scroll Area
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        # 2. Create a Widget to hold the content
        self.content_widget = QWidget()
        self.content_layout = QVBoxLayout()
        self.content_layout.addWidget(title_label)  # Add title to the layout
        self.content_widget.setLayout(self.content_layout)

        # 3. Set the content widget as the scroll area's widget
        scroll_area.setWidget(self.content_widget)

        # 4. Set the main layout of the SurveyApp
        main_layout = QVBoxLayout()
        main_layout.addWidget(scroll_area)

        # Organize questions into categories
        self.categories = [
            Category("Rater's Data", [
                Heading("Rater's Data"),
                TextQuestion("Name of the Rater:"),
                TextQuestion("Email of the Rater:"),
                TextQuestion("Date of Testing"),
            ]),
            Category("Participant Demographics", [
                Heading("Participant Demographics"),
                TextQuestion("Subject ID:"),
                TextQuestion("Session Number:"),
                TextQuestion("First and Last Name:"),
                TextQuestion("Date of Birth (DD/MM/YYYY):"),
                TextQuestion("Age:"),
                TextQuestion("Sex:"),
                TextQuestion("Years of Education:"),
                CheckboxQuestion("Handedness:", ["Right", "Left", "Ambidextrous"]),
                TextQuestion("Participant Contact Information:"),
                TextQuestion("Other Contact Information (i.e., spouse, partner, friend, relative of participant):"),
                YesNoQuestion("Consent for Audio and Video Recording:"),
            ]),
            Category("Participant Hearing and Vision", [
                Heading("Participant Hearing and Vision"),
                YesNoQuestion("Reported adequate hearing?", "Description of hearing test"),
                YesNoQuestion("Repeated sentence accurately?", "Description of sentence repetition"),
                YesNoQuestion("Reported adequate vision?", "Description of vision test"),
                YesNoQuestion("Can read text presented on screen?", "Description of text reading"),
                YesNoQuestion("Proceeded with testing:", "Yes (i.e., responses for items 1 through 4 = Yes \n No (i.e., responses for items 1 through 4 suggested sensory impairment would severely bias their cognitive testing)"),

            ]),
            Category("Testing Environment", [
                Heading("Testing Environment"),
                YesNoQuestion("Appropriate testing location (i.e., participant is alone and located in a quiet location free from distraction)?"),
                YesNoQuestion("Stable internet connection?"),
                YesNoQuestion("Using appropriate device (i.e., a laptop or desktop computer)?"),
                YesNoQuestion("Can read text presented on screen?", "Description of text reading"),
                CheckboxQuestion("Due to responding No to items 1 through 3, the participant could not proceed and testing was:", ["Rescheduled", "Terminated"]),

            ]),
            Category("Montreal Cognitive Assessment (MoCA)", [
                Heading("Montreal Cognitive Assessment (MoCA)"),
                CheckboxQuestion("Memory (Trial 1):", ["Face", "Velvet", "Church", "Daisy", "Red"], "Read list of words, subject must repeat them. Do 2 trials, even if 1st trial is successful. Do a recall after 5 minutes."),
                CheckboxQuestion("Memory (Trial 2):", ["Face", "Velvet", "Church", "Daisy", "Red"]),
                CheckboxQuestion("Attention (Part 1):", ["(Forward Order) 2 1 8 5 4", " (Backward Order) 7 4 2"], "Read list of digits (1 digit/ sec.)."),
                HorizontalCheckboxQuestion("Attention (Part 2):", ["F", "B", "A", "C", "M", "N", "A", "A", "J", "K", "L", "B", "A", "F", "A", "K", "D", "E", "A", "A", "A", "J", "A", "M", "O", "F", "A", "A", "B"], "Read list of letters. The subject must raise their hand at each letter A. No points if >= 2 errors."),
                CheckboxQuestion("Seria 7 subtraction starting at 100", ["93", "86", "79", "72", "65"], "4 or 5 correct subtractions: 3 pts, 2 or 3 correct: 2 pts, 1 correct: 1 pt, 0 correct: 0 pt"),
                CheckboxQuestion("Language (Part 1: Repeatsentence):", ["I only know that John is the one to help today.", "The cat always hid under the couch when dogs were in the room"], "Repeat the sentence."),
                CheckboxQuestion("Language (Part 2: Fluency):", ["Name maximum number of words in one minute that begin with the letter F."], "N >= 11 words."),
                CheckboxQuestion("Abstraction", ["train - bicycle", "watch - ruler"], "Similarity between the two wrods. E.g., orange - banana = fruit."),
                CheckboxQuestion("Memory (Delayed Recall):", ["Face", "Velvet", "Church", "Daisy", "Red"]),
                HorizontalCheckboxQuestion("Orientation", ["Date", "Month", "Year", "Day", "Place", "City"]),
            ]),
            Category("Preferences", [
                Heading("Personal Preferences"),
                CheckboxQuestion("Select your favorite fruits:", ["Apples", "Bananas", "Cherries", "Dates"]),
                RatingQuestion("Rate your satisfaction with the survey (1-5):", "Description of survey experience"),
            ])
        ]

        self.display_categories(self.content_layout)

        submit_button = QPushButton("Submit")
        submit_button.clicked.connect(self.submit)
        main_layout.addWidget(submit_button)

        self.setLayout(main_layout)

    def display_categories(self, layout):
        for category in self.categories:
            category.display(layout)

    def submit(self):
        self.answers = {
            category.name: category.get_answers()
            for category in self.categories
        }

        # Get the subject ID and session number from the answers
        subject_id = ""
        session_num = ""
        demographics = self.answers.get("Participant Demographics", {})
        for question_text, answer_data in demographics.items():
            if question_text == "Subject ID:":
                subject_id = answer_data.get('answer', '')
            elif question_text == "Session Number:":
                session_num = answer_data.get('answer', '')

        # Use subject ID and session in filenames, with defaults if empty
        if not subject_id:
            subject_id = "noid"
        if not session_num:
            session_num = "01"
        else:
            session_num = f"{session_num}"

        # Calculate and save sensory scores
        calculator = ScoreCalculator()
        sensory_scores = calculator.calculate_sensory_scores(self.answers, subject_id, session_num)

        # Open folder selection dialog
        save_dir = QFileDialog.getExistingDirectory(
            self,
            "Select Directory to Save Results",
            "",  # Default directory, empty string means current directory
            QFileDialog.ShowDirsOnly
        )
        
        if save_dir:  # User selected a directory
            # Create directory with new naming format
            result_dir = os.path.join(save_dir, f"sub-{subject_id}_ses-{session_num}")
            os.makedirs(result_dir, exist_ok=True)
            
            # Calculate sensory scores
            calculator = ScoreCalculator()
            sensory_scores = calculator.calculate_sensory_scores(self.answers, subject_id, session_num)
            
            # Save all files with consistent naming convention
            json_path = os.path.join(result_dir, f"sub-{subject_id}_ses-{session_num}_questionnaire.json")
            with open(json_path, 'w') as f:
                json.dump(self.answers, f)
                
            pdf_path = os.path.join(result_dir, f"sub-{subject_id}_ses-{session_num}_questionnaire.pdf")
            self.generate_pdf(self.answers, pdf_path)
            
            # Save sensory scores CSV
            calculator.save_sensory_scores(sensory_scores, result_dir)
            
            QMessageBox.information(self, "Success", "Your responses have been saved!")

    def generate_pdf(self, answers, filename):
        pdf_generator = NeuropsyPDFGenerator(filename)
        pdf_generator.generate(answers)

def main():
    app = QApplication(sys.argv)
    neuropsy_app = Neuropsy()
    neuropsy_app.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()

