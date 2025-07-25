# src/enneagram_model/enneagram_model.py

class EnneagramPredictor:
    def __init__(self):
        self.types = {
            1: "The Reformer (Perfectionist)",
            2: "The Helper",
            3: "The Achiever",
            4: "The Individualist",
            5: "The Investigator",
            6: "The Loyalist",
            7: "The Enthusiast",
            8: "The Challenger",
            9: "The Peacemaker"
        }

    def predict(self, features: dict) -> tuple[int, str]:
        """
        Predict Enneagram type from behavior features.

        Parameters:
        ----------
        features : dict
            {
                'hesitation_count': int,
                'product_return_rate': float,
                'interaction_span': float,        # total seconds spent on single product
                'confidence_score': float,       # from body language module [0 to 1]
                'seeking_help': bool
            }

        Returns:
        -------
        tuple[int, str] : (type_number, description)
        """

        hesitation = features.get('hesitation_count', 0)
        return_rate = features.get('product_return_rate', 0.0)
        duration = features.get('interaction_span', 0.0)
        confidence = features.get('confidence_score', 0.5)
        help_needed = features.get('seeking_help', False)

        # Rule-based heuristic (تا ساخت مدل ML کامل بشه)
        if hesitation > 5 and return_rate > 0.5:
            return (6, self.types[6])  # Loyalist (مردد، مراقب، ریسک‌گریز)

        if confidence < 0.3 and help_needed:
            return (2, self.types[2])  # Helper (نیاز به تعامل)

        if duration > 100 and hesitation == 0:
            return (5, self.types[5])  # Investigator (عمیق، تحلیل‌گر)

        if hesitation == 0 and confidence > 0.7:
            return (3, self.types[3])  # Achiever (قاطع و نتیجه‌گرا)

        if hesitation < 2 and return_rate < 0.1:
            return (9, self.types[9])  # Peacemaker (آرام، بدون تنش)

        if duration < 20 and confidence > 0.8:
            return (7, self.types[7])  # Enthusiast (بی‌قرار، سریع، لذت‌جو)

        return (4, self.types[4])  # fallback: Individualist
