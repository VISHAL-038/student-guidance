# 📘 Dataset Inventory — Student Guidance System

## 1️⃣ Main Dataset — Student Performance Prediction
**Source:** [Kaggle – Student Performance Dataset (Math, Portuguese, Science)](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams)  
**Path:** `data/raw/students_performance.csv`  

**Description:**  
This dataset contains demographic, social, and academic information for students.

**Key Fields:**  
- `gender` — Male/Female  
- `race/ethnicity` — Student’s background group  
- `parental level of education` — Highest education level of parents  
- `test preparation course` — Whether test prep course completed  
- `math score`, `reading score`, `writing score` — Exam performance  

**Usage in Project:**  
Used for building the initial **performance prediction model** (to predict overall CGPA or academic success based on background and preparation factors).

---

## 2️⃣ Secondary Dataset — Resume Skill Mapping
**Source:** [Kaggle – Resume Dataset (Skills, Category)](https://www.kaggle.com/datasets/gauravduttakiit/resume-dataset)  
**Path:** `data/raw/resume_dataset.csv`  

**Description:**  
Contains text from real resumes categorized by domain and skills.

**Key Fields:**  
- `Category` — Job domain (e.g., Data Science, HR, Web Developer, etc.)  
- `Resume_str` — Resume text content  

**Usage in Project:**  
Used to train a simple NLP model to recommend **career paths or skills** based on a student’s resume upload.

---

## 3️⃣ Future Data Augmentations (Optional)

| Planned Dataset | Purpose |
|------------------|----------|
| Online Courses API (Coursera/edX) | Recommend skill-based learning paths |
| College Internal Dataset | Map semester scores and subject performance |
| Job Role Skills Dataset | Connect academic profile to industry demand |

---

## 📂 Folder Structure
data/
├── raw/
│ ├── students_performance.csv
│ └── resume_dataset.csv
docs/
└── datasets.md


---

## 🧠 Notes
- Cleaned datasets will be stored under `data/processed/` (in future).  
- All datasets are open-source and for educational use only.
