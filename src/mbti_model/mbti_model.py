# src/mbti_model/mbti_model.py

class MBTIPredictor:
    def __init__(self):
        self.dimensions = {
            "I/E": None,
            "N/S": None,
            "T/F": None,
            "P/J": None,
        }

    def predict(self, features: dict) -> str:
        """
        Predict MBTI type from behavior features.

        Parameters:
        ----------
        features : dict
            {
                'pause_duration': float,             # seconds
                'product_touch_count': int,          # how many items touched
                'product_return_count': int,         # how many items picked and put back
                'help_seeking_attempt': bool,        # did they look for help or not
                'eye_contact_count': int,            # number of eye contacts with staff
                'wandering_ratio': float             # path_efficiency = straight / total path
            }

        Returns:
        -------
        str : MBTI type (e.g., 'INTJ', 'ESFP', etc.)
        """

        # I/E - Introvert vs. Extrovert
        if features.get('eye_contact_count', 0) < 2 and not features.get('help_seeking_attempt', False):
            self.dimensions["I/E"] = 'I'
        else:
            self.dimensions["I/E"] = 'E'

        # N/S - Intuitive vs. Sensing
        if features.get('pause_duration', 0) > 30:
            self.dimensions["N/S"] = 'N'
        else:
            self.dimensions["N/S"] = 'S'

        # T/F - Thinking vs. Feeling
        if features.get('product_touch_count', 0) > 4:
            self.dimensions["T/F"] = 'F'
        else:
            self.dimensions["T/F"] = 'T'

        # P/J - Perceiving vs. Judging
        if features.get('wandering_ratio', 0.0) > 0.5:
            self.dimensions["P/J"] = 'P'
        else:
            self.dimensions["P/J"] = 'J'

        return ''.join([
            self.dimensions["I/E"],
            self.dimensions["N/S"],
            self.dimensions["T/F"],
            self.dimensions["P/J"],
        ])

