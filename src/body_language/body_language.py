# src/body_language/body_language.py

class BodyLanguageAnalyzer:
    def __init__(self):
        pass

    def analyze(self, features: dict) -> dict:
        """
        تحلیل زبان بدن مشتری

        Parameters:
        ----------
        features : dict
            {
                'face_touch_count': int,
                'hand_to_pocket_count': int,
                'fidgeting_score': float,           # [0.0 - 1.0]
                'eye_contact_count': int,
                'is_sitting': bool,
                'head_turn_frequency': int          # how often head moves side-to-side
            }

        Returns:
        -------
        dict:
            {
                'confidence_score': float,
                'suspicion_score': float,
                'restlessness_score': float,
                'description': str
            }
        """

        face_touch = features.get('face_touch_count', 0)
        pocket_touch = features.get('hand_to_pocket_count', 0)
        fidget = features.get('fidgeting_score', 0.0)
        eye_contact = features.get('eye_contact_count', 0)
        is_sitting = features.get('is_sitting', False)
        head_turns = features.get('head_turn_frequency', 0)

        # محاسبه نمره‌ها:
        confidence_score = max(0.0, min(1.0, (eye_contact + (0.5 if is_sitting else 0)) / 5))
        suspicion_score = max(0.0, min(1.0, (pocket_touch + face_touch + head_turns) / 10))
        restlessness_score = max(0.0, min(1.0, fidget + (head_turns / 10)))

        # توضیح کلی
        if suspicion_score > 0.7:
            description = "High suspicion due to frequent face/pocket touches and head movement."
        elif restlessness_score > 0.6:
            description = "Customer appears restless and unfocused."
        elif confidence_score > 0.8:
            description = "Customer shows calm and confident behavior."
        else:
            description = "Neutral or mixed body language."

        return {
            'confidence_score': round(confidence_score, 2),
            'suspicion_score': round(suspicion_score, 2),
            'restlessness_score': round(restlessness_score, 2),
            'description': description
        }