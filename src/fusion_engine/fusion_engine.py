# src/fusion_engine/fusion_engine.py

from src.mbti_model.mbti_model import MBTIPredictor
from src.enneagram_model.enneagram_model import EnneagramPredictor
from src.body_language.body_language import BodyLanguageAnalyzer

class FusionEngine:
    def __init__(self):
        self.mbti_model = MBTIPredictor()
        self.enneagram_model = EnneagramPredictor()
        self.body_language_model = BodyLanguageAnalyzer()

    def analyze(self, features: dict) -> dict:
        """
        ادغام خروجی مدل‌های شخصیتی و رفتاری برای برچسب‌گذاری مشتری

        Parameters:
        ----------
        features : dict => ترکیب ورودی همه ماژول‌ها

        Returns:
        -------
        dict:
            {
                'mbti': 'INFP',
                'enneagram': (6, 'The Loyalist'),
                'confidence': 0.35,
                'suspicion': 0.78,
                'restlessness': 0.65,
                'final_label': 'thief',
                'recommendation': '⚠️ مشتری مشکوک - اطلاع به نیرو'
            }
        """

        # مدل‌ها
        mbti = self.mbti_model.predict(features)
        enneagram_type, enneagram_desc = self.enneagram_model.predict(features)
        body = self.body_language_model.analyze(features)

        # تصمیم نهایی
        suspicion = body['suspicion_score']
        restlessness = body['restlessness_score']
        confidence = body['confidence_score']

        if suspicion > 0.7:
            label = "thief"
            rec = "⚠️ مشتری مشکوک - اطلاع به نیرو"
        elif confidence > 0.8:
            label = "buyer"
            rec = "✅ مشتری مطمئن - احتمال خرید بالا"
        elif restlessness > 0.5:
            label = "browser"
            rec = "🟡 مشتری در حال بررسی یا مردد"
        else:
            label = "unknown"
            rec = "⚪ اطلاعات کافی نیست"

        return {
            'mbti': mbti,
            'enneagram': (enneagram_type, enneagram_desc),
            'confidence': confidence,
            'suspicion': suspicion,
            'restlessness': restlessness,
            'final_label': label,
            'recommendation': rec
        }
