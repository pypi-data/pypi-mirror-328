import json
import pandas as pd
from datetime import datetime
from pathlib import Path

class ScoreCalculator:
    def __init__(self):
        self.results = {}
    
    def calculate_test_score(self, test_name, test_data, patient_info):
        """
        Calculate scores based on the specific test type
        """
        if test_name == "digit_span":
            score = self._calculate_digit_span(test_data)
        elif test_name == "trail_making":
            score = self._calculate_trail_making(test_data)
        else:
            raise ValueError(f"Unknown test type: {test_name}")
            
        # Store results
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        result = {
            "patient_info": patient_info,
            "test_name": test_name,
            "score": score,
            "timestamp": timestamp,
            "raw_data": test_data
        }
        
        self.results[timestamp] = result
        return score
    
    def _calculate_digit_span(self, data):
        """
        Calculate Digit Span test score
        To be implemented based on specific scoring rules
        """
        pass
    
    def _calculate_trail_making(self, data):
        """
        Calculate Trail Making test score
        To be implemented based on specific scoring rules
        """
        pass

    def calculate_sensory_scores(self, answers, subject_id, session_num):
        """Calculate hearing and vision scores from questionnaire data"""
        hearing_vision_data = answers.get("Participant Hearing and Vision", {})
        
        # Calculate hearing score (0-2)
        hearing_score = 0
        if hearing_vision_data.get("Reported adequate hearing?", {}).get('answer') == 'Yes':
            hearing_score += 1
        if hearing_vision_data.get("Repeated sentence accurately?", {}).get('answer') == 'Yes':
            hearing_score += 1
            
        # Calculate vision score (0-2)
        vision_score = 0
        if hearing_vision_data.get("Reported adequate vision?", {}).get('answer') == 'Yes':
            vision_score += 1
        if hearing_vision_data.get("Can read text presented on screen?", {}).get('answer') == 'Yes':
            vision_score += 1
        
        # Prepare results
        results = {
            'subject_id': subject_id,
            'session': session_num,
            'hearing_score': hearing_score,
            'vision_score': vision_score,
            'total_sensory_score': hearing_score + vision_score,
            'timestamp': datetime.now().strftime("%Y%m%d_%H%M%S")
        }
        
        return results
    
    def save_sensory_scores(self, results, save_dir):
        """Save sensory scores to CSV in the specified directory"""
        # Create DataFrame
        df = pd.DataFrame([results])
        
        # Create filename using the naming convention
        filename = f"sub-{results['subject_id']}_ses-{results['session']}_sensory_scores.csv"
        csv_path = Path(save_dir) / filename
        
        # Save to CSV
        df.to_csv(csv_path, index=False)

# Usage example:
"""
calculator = ScoreCalculator()

# Example patient info
patient_info = {
    "patient_id": "P001",
    "name": "John Doe",
    "age": 45,
    "gender": "M"
}

# Example test data
digit_span_data = {
    "forward_span": [7, 6, 8],
    "backward_span": [4, 5, 3]
}

score = calculator.calculate_test_score("digit_span", digit_span_data, patient_info)
""" 