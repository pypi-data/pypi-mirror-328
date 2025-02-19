from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.units import mm
from datetime import datetime

class NeuropsyPDFGenerator:
    def __init__(self, filename="survey_responses.pdf"):
        self.doc = SimpleDocTemplate(
            filename,
            pagesize=A4,
            rightMargin=20*mm,
            leftMargin=20*mm,
            topMargin=20*mm,
            bottomMargin=20*mm
        )
        self.styles = getSampleStyleSheet()
        self._create_custom_styles()

    def _create_custom_styles(self):
        # Category heading style
        self.styles.add(ParagraphStyle(
            'CategoryHeading',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=colors.HexColor('#2C3E50'),
            spaceAfter=10,
            spaceBefore=20
        ))
        
        # Question style
        self.styles.add(ParagraphStyle(
            'Question',
            parent=self.styles['Normal'],
            fontSize=11,
            textColor=colors.HexColor('#34495E'),
            leftIndent=20,
            spaceAfter=5
        ))
        
        # Answer style
        self.styles.add(ParagraphStyle(
            'Answer',
            parent=self.styles['Normal'],
            fontSize=10,
            textColor=colors.HexColor('#2980B9'),
            leftIndent=40,
            spaceAfter=8
        ))
        
        # Comments style
        self.styles.add(ParagraphStyle(
            'Comments',
            parent=self.styles['Italic'],
            fontSize=9,
            textColor=colors.HexColor('#7F8C8D'),
            leftIndent=40,
            spaceAfter=10
        ))

    def generate(self, answers):
        story = []
        
        # Add title and date
        title = Paragraph(
            f"Remote Neuropsychological Test Battery Record Form<br/><font size=10>{datetime.now().strftime('%B %d, %Y')}</font>", 
            self.styles['Title']
        )
        story.append(title)
        story.append(Spacer(1, 20))

        for category_name, category_answers in answers.items():
            # Add category heading
            story.append(Paragraph(category_name, self.styles['CategoryHeading']))
            
            for question_text, answer_data in category_answers.items():
                # Skip headings which don't have answer data
                if not isinstance(answer_data, dict):
                    continue

                # Add question
                story.append(Paragraph(f"<b>{question_text}</b>", self.styles['Question']))
                
                # Add answer
                answer = answer_data['answer']
                if isinstance(answer, list):
                    answer = ", ".join(str(item) for item in answer)
                story.append(Paragraph(f"<i>Answer:</i> {answer}", self.styles['Answer']))
                
                # Add description if present
                if answer_data['description']:
                    story.append(Paragraph(
                        f"<i>Description:</i> {answer_data['description']}", 
                        self.styles['Answer']
                    ))
                
                # Add comments if present
                if answer_data['comments']:
                    story.append(Paragraph(
                        f"<i>Comments:</i> {answer_data['comments']}", 
                        self.styles['Comments']
                    ))

            story.append(Spacer(1, 10))

        # Build the PDF
        self.doc.build(story) 