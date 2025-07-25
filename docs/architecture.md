# 🧩 معماری سیستم تحلیل رفتار مشتری بدون وابستگی به پلان فروشگاه

در این نسخه از معماری، تحلیل رفتار مشتری بر پایه‌ی «رفتار و تعامل مستقیم» انجام می‌شود، بدون نیاز به نقشه چیدمان، مختصات قفسه یا تقسیم فیزیکی فروشگاه. این معماری مناسب محیط‌هایی است که چیدمان موقت، فصلی یا دائماً در حال تغییر دارند.

---

## 📐 ساختار کلی سیستم (Context-Agnostic)

```text
[Input: CCTV Video]
        ↓
[1. Frame Extractor]
        ↓
[2. Feature Extractor]
        ↓
[3. Object & Interaction Detection]
        ├── کالا (خودکار، کتاب، دفتر...)
        ├── قفسه / میز
        └── تعامل (لمس، برداشتن، نشستن، خواندن)
        ↓
[4. Behavior Classification Modules]
        ├── Enneagram Estimator
        ├── MBTI Estimator
        ├── Body Language Interpreter
        ↓
[5. Behavior Fusion Engine]
        ↓
[6. Customer Type Classifier]
        └── Output: buyer | browser | thief
        ↓
[7. LLM Explainer (optional)]
        ↓
[8. Feedback & Reward Engine]

🧱 اجزای سیستم
1. 📥 Frame Extractor
استخراج فریم از ویدیو با نرخ 1 تا 5 fps

2. 🧠 Feature Extractor
استخراج داده‌های حرکتی، رفتاری، زمانی

3. 🔍 Object & Interaction Detector

| عملکرد      | ابزار                       | توضیح                                  |
| ----------- | --------------------------- | -------------------------------------- |
| تشخیص اجسام | YOLOv8 / SSD                | تشخیص خودکار کالا، قفسه، کیف، دست      |
| تشخیص تعامل | Heuristic / Temporal Vision | لمس کالا، بازگشت، نشستن، خواندن طولانی |

این مرحله جایگزین کامل Spatial Mapping بر اساس مختصات است.


4. Behavior Classifier Modules

| ماژول                     | وظیفه                                     |
| ------------------------- | ----------------------------------------- |
| Enneagram Estimator       | تخمین تیپ شخصیتی از رفتار                 |
| MBTI Estimator            | تحلیل شخصیت براساس ۴ بعد اصلی             |
| Body Language Interpreter | تشخیص استرس، تردید، هدف‌مندی، نیاز به کمک |

5. 🔀 Behavior Fusion Engine
ترکیب خروجی ماژول‌ها

محاسبه امتیازات نهایی: suspicion_score, intent_to_buy, confusion_score


6. 🧭 Customer Type Classifier
دسته‌بندی نهایی به یکی از سه حالت:

buyer

browser

thief

7. 🗣️ LLM Explainer (اختیاری)
تولید توضیح قابل فهم برای رفتار تحلیل‌شده

بر پایه ترکیب خروجی مدل + prompt


8. 🧪 Feedback & Reward Engine
مقایسه با برچسب‌های واقعی

اصلاح وزن تصمیم‌گیری

ثبت یادگیری تدریجی


🗃️ ساختار داده‌ها

| نوع             | مسیر پیشنهادی               | توضیح                       |
| --------------- | --------------------------- | --------------------------- |
| ویدیو خام       | `data/raw_videos/`          | ورودی اصلی                  |
| فریم‌ها         | `data/extracted_frames/`    | خروجی فاز ۱                 |
| ویژگی‌ها        | `data/features/`            | خروجی فاز ۲                 |
| برچسب‌ها        | `data/labels/`              | برای یادگیری مدل یا فیدبک   |
| تعامل با اجسام  | `data/detections/`          | bounding boxها و کلاس اشیاء |
| گزارشات و نتایج | `experiments/test_outputs/` | خروجی تحلیلی و لاگ‌ها       |

🧩 مزایای این معماری:
مناسب محیط‌های متغیر، بدون نیاز به نقشه

عملکرد در شرایط واقعی فروشگاه‌های کوچک و فصلی

متمرکز بر رفتار واقعی مشتری، نه موقعیت جغرافیایی در تصویر

کاهش خطای ناشی از mismatch بین layout و تصویر دوربین



