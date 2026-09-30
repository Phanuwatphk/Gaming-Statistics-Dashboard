ได้เลย ด้านล่างคือ **`Project_Pitch.md` เวอร์ชันสมบูรณ์สำหรับเอาไปวางทับไฟล์เดิมได้เลย** โดยผมปรับจาก `Project_Pitch.md` เดิมให้สอดคล้องกับพัฒนาการล่าสุดของโปรเจกต์ถึง **Sprint 3** ทั้ง Web Application, RAWG/Steam API, SQLite, Data Processing, Statistics, Visualization และ Advanced Features รวมถึงปรับสถานะ Sprint ให้ไม่ย้อนกลับไปเป็น Planned แล้ว

ข้อมูลตั้งต้นจาก `Project_Pitch.md` เดิมและเอกสาร Sprint 3 ที่มีอยู่จริงในไฟล์ของโปรเจกต์  

````markdown
# 🎮 Gaming Statistics Dashboard

## Final Term Project — CP352301 Script Programming

---

# 1. Project Overview

**Gaming Statistics Dashboard** คือ Web Application สำหรับรวบรวม จัดการ วิเคราะห์ และนำเสนอข้อมูลเกี่ยวกับวิดีโอเกมในรูปแบบ Dashboard

ระบบพัฒนาด้วย Python และ Streamlit โดยเชื่อมต่อข้อมูลเกมจาก External API ได้แก่ RAWG API และ Steam API พร้อมจัดเก็บข้อมูลผ่าน SQLite Database

ผู้ใช้สามารถเข้าถึงระบบผ่าน Web Browser เพื่อค้นหา สำรวจ กรอง เรียงลำดับ ดูรายละเอียด เปรียบเทียบ และวิเคราะห์ข้อมูลเกมได้ภายในระบบเดียว

โปรเจกต์พัฒนาด้วยแนวทาง **Incremental Development** โดยแบ่งการพัฒนาออกเป็น Sprint และเพิ่มความสามารถของระบบอย่างต่อเนื่อง ตั้งแต่ CLI Foundation ใน Sprint 1 ไปสู่ Web Application ใน Sprint 2 และ Data Analysis, Visualization และ Advanced Features ใน Sprint 3

---

# 2. Problem Statement

ข้อมูลเกี่ยวกับวิดีโอเกมมีจำนวนมากและมีข้อมูลหลายประเภท เช่น

- Game Title
- Rating
- Genre
- Platform
- Release Date
- Metacritic Score
- Steam Player Count
- Game Image
- ข้อมูลอื่น ๆ จาก External API

หากผู้ใช้ต้องการค้นหา สำรวจ หรือเปรียบเทียบข้อมูลเกมจำนวนมาก การค้นหาข้อมูลจากแหล่งข้อมูลโดยตรงอาจไม่สะดวก และผู้ใช้อาจต้องใช้หลายขั้นตอนในการค้นหาข้อมูลที่ต้องการ

นอกจากนี้ ข้อมูลเกมไม่ได้มีเพียงข้อมูลสำหรับการค้นหาเท่านั้น แต่ยังสามารถนำมาวิเคราะห์เพื่อดูแนวโน้ม การกระจายตัว ความถี่ และสถิติต่าง ๆ ได้

ดังนั้นกลุ่มจึงพัฒนา **Gaming Statistics Dashboard** เพื่อรวบรวมข้อมูลเกมจาก External API จัดการและจัดเก็บข้อมูลในระบบ และนำเสนอข้อมูลผ่าน Dashboard ที่ช่วยให้ผู้ใช้สามารถค้นหา สำรวจ วิเคราะห์ และเปรียบเทียบข้อมูลเกมได้สะดวกขึ้น

---

# 3. Project Objectives

โปรเจกต์นี้มีวัตถุประสงค์หลักดังนี้

1. พัฒนา Web Application สำหรับรวบรวมและแสดงข้อมูลเกี่ยวกับวิดีโอเกม
2. เชื่อมต่อข้อมูลเกมจาก External API
3. จัดเก็บและจัดการข้อมูลด้วย SQLite Database
4. พัฒนา Search สำหรับค้นหาเกม
5. พัฒนา Filtering และ Sorting สำหรับสำรวจข้อมูลเกม
6. แสดงรายละเอียดของเกมในรูปแบบที่เข้าใจง่าย
7. เชื่อมต่อข้อมูล Steam เพื่อแสดงข้อมูลเกี่ยวกับจำนวนผู้เล่น
8. จัดการและ Normalize ข้อมูลก่อนนำไปใช้งาน
9. คำนวณ Descriptive Statistics จากข้อมูลเกม
10. วิเคราะห์ข้อมูลด้วย Exploratory Data Analysis (EDA)
11. นำเสนอข้อมูลผ่าน Data Visualization
12. เพิ่มความสามารถในการเปรียบเทียบข้อมูลเกม
13. รองรับ Error Handling และ Empty State
14. ทดสอบการทำงานของระบบในระดับ Unit, Functional และ Integration ตามขอบเขตของแต่ละ Sprint
15. พัฒนาโปรเจกต์ตามแนวทาง Incremental Development ผ่านแต่ละ Sprint
16. ใช้ Git และ GitHub สำหรับ Version Control และการทำงานร่วมกัน

---

# 4. Target Users

ระบบถูกออกแบบสำหรับผู้ใช้ที่ต้องการสำรวจข้อมูลวิดีโอเกม เช่น

- ผู้ที่ต้องการค้นหาเกม
- ผู้ที่ต้องการดูข้อมูลพื้นฐานของเกม
- ผู้ที่ต้องการเปรียบเทียบเกม
- ผู้ที่ต้องการดู Rating และ Metacritic Score
- ผู้ที่สนใจ Genre และ Platform ของเกม
- ผู้ที่ต้องการดูข้อมูล Steam Player
- ผู้ที่ต้องการดู Statistics และ Visualization ของข้อมูลเกม

โปรเจกต์นี้เน้นการนำเสนอข้อมูลและการสำรวจข้อมูล ไม่ได้ออกแบบมาเพื่อเป็นระบบซื้อขายเกมหรือระบบจัดการบัญชีผู้ใช้

---

# 5. Target Application Format

## Web Application

ระบบพัฒนาเป็น **Web Application** โดยใช้ Streamlit และสามารถเปิดใช้งานผ่าน Web Browser

ผู้ใช้ไม่จำเป็นต้องใช้งานระบบผ่าน Command Line โดยตรง

ภาพรวมการใช้งาน:

```text
User
  │
  ↓
Web Browser
  │
  ↓
Gaming Statistics Dashboard
  │
  ├── Game Library
  ├── Search
  ├── Filter
  ├── Sort
  ├── Game Detail
  ├── Top Rated
  ├── Live Players
  ├── Statistics
  ├── Visualization
  └── Game Comparison
````

---

# 6. Project Evolution

โปรเจกต์ถูกพัฒนาตามลำดับจากระบบพื้นฐานไปสู่ Web Application ที่มีความสามารถด้าน Data Analysis

```text
Sprint 1
CLI Foundation
      ↓
Local Sample Dataset
      ↓
Sprint 2
Streamlit Web Application
      ↓
RAWG API + Steam API
      ↓
SQLite Database
      ↓
Game Service
      ↓
Sprint 3
Data Processing
      ↓
EDA / Statistics
      ↓
Data Visualization
      ↓
Advanced Filtering / Sorting
      ↓
Game Comparison
      ↓
Integrated Dashboard
      ↓
Final Sprint
Final QA + Documentation + Final Delivery
```

---

# 7. Main Features

## 7.1 Game Library

ระบบสามารถแสดงรายการเกมจากข้อมูลที่จัดเก็บและประมวลผลในระบบ

ข้อมูลที่เกี่ยวข้อง เช่น

* Game Title
* Rating
* Genre
* Platform
* Release Date
* Metacritic Score
* Game Image
* Steam Player Data เมื่อมีข้อมูล

---

## 7.2 Search

ผู้ใช้สามารถค้นหาเกมจากชื่อเกม

ตัวอย่าง:

```text
Search: Minecraft
```

ระบบจะแสดงเกมที่ตรงกับคำค้นหาตามข้อมูลที่มีอยู่

---

## 7.3 Filtering

ระบบรองรับการกรองข้อมูลเกมตามเงื่อนไข เช่น

* Genre
* Platform
* Minimum Rating
* Release Year

สามารถใช้หลายเงื่อนไขร่วมกันเพื่อจำกัดชุดข้อมูลที่ต้องการสำรวจ

---

## 7.4 Sorting

ระบบรองรับการเรียงข้อมูลตามข้อมูลสำคัญ เช่น

* Rating
* Release Date
* Game Name

และสามารถเรียงได้ทั้ง

```text
Ascending
Descending
```

---

## 7.5 Pagination

เมื่อมีข้อมูลเกมจำนวนมาก ระบบรองรับการแบ่งข้อมูลออกเป็นหลายหน้าเพื่อช่วยให้การแสดงผลและการสำรวจข้อมูลทำได้ง่ายขึ้น

---

## 7.6 Game Detail

ผู้ใช้สามารถเลือกเกมเพื่อดูรายละเอียดเพิ่มเติม เช่น

* Game Name
* Rating
* Genre
* Platform
* Release Date
* Metacritic Score
* Game Image
* Steam Player Information เมื่อมีข้อมูล

---

## 7.7 Top Rated Games

ระบบสามารถแสดงเกมที่มี Rating สูง เพื่อให้ผู้ใช้สามารถสำรวจเกมที่มีคะแนนสูงได้ง่ายขึ้น

---

## 7.8 Steam Live Players

ระบบเชื่อมต่อ Steam API เพื่อดึงข้อมูลจำนวนผู้เล่นปัจจุบันของเกมที่มี Steam App ID ที่สามารถจับคู่ได้

ข้อมูล Steam สามารถนำมาใช้สำหรับ

* Current Player Count
* Top Live Players
* Player Snapshot
* Data Analysis

---

## 7.9 Statistics Dashboard

ระบบมีส่วนสำหรับสรุป Statistics ของข้อมูลเกม เช่น

* Total Games
* Average Rating
* Highest Rating
* Lowest Rating
* Genre Frequency
* Platform Frequency
* Release Year Frequency
* Metacritic Statistics เมื่อมีข้อมูล
* Steam Player Statistics เมื่อมีข้อมูล

---

## 7.10 Data Visualization

ระบบนำข้อมูลมาแสดงในรูปแบบ Visualization เพื่อช่วยให้ผู้ใช้เข้าใจข้อมูลได้ง่ายขึ้น

ตัวอย่างการนำเสนอ:

* Genre Distribution
* Platform Distribution
* Rating Analysis
* Rating by Genre
* Release Year Distribution
* Metacritic Score Distribution
* Steam Player Data

ชนิดของ Chart จะเลือกตามประเภทและความเหมาะสมของข้อมูล

---

## 7.11 Game Comparison

ระบบรองรับการเปรียบเทียบเกม โดยสามารถเลือก Game A และ Game B แล้วเปรียบเทียบข้อมูลสำคัญ เช่น

* Rating
* Metacritic Score
* Steam Players

การเปรียบเทียบช่วยให้ผู้ใช้สามารถดูความแตกต่างของเกมที่สนใจในรูปแบบเดียวกัน

---

## 7.12 Empty State & Error Handling

ระบบมีการจัดการกรณีข้อมูลไม่พร้อมใช้งาน เช่น

* API Error
* Invalid API Response
* Missing Data
* Empty Dataset
* ไม่มีข้อมูลหลังจาก Filter
* ข้อมูลไม่เพียงพอสำหรับ Visualization

ระบบควรแสดงข้อความที่เหมาะสมแทนการทำให้ Application Crash

---

# 8. Data Sources

## 8.1 RAWG API

RAWG Video Games Database API เป็นแหล่งข้อมูลหลักสำหรับข้อมูลเกม

ข้อมูลที่ใช้ในระบบอาจประกอบด้วย

* Game Title
* Rating
* Genre
* Platform
* Release Date
* Metacritic Score
* Game Image
* Game ID
* ข้อมูลอื่น ๆ ที่ API ส่งกลับมา

RAWG Website:

[https://rawg.io/](https://rawg.io/)

RAWG API:

[https://api.rawg.io/](https://api.rawg.io/)

---

## 8.2 Steam API

Steam API ใช้สำหรับข้อมูลที่เกี่ยวข้องกับ Steam และจำนวนผู้เล่นของเกมที่สามารถจับคู่กับ Steam App ID ได้

ข้อมูลที่เกี่ยวข้อง เช่น

* Steam App ID
* Current Players
* Top Live Players
* Player Snapshot

---

# 9. Data Processing

ข้อมูลจาก External API ไม่สามารถนำไปใช้โดยตรงทั้งหมด จึงต้องผ่าน Data Processing ก่อนนำไปจัดเก็บ วิเคราะห์ หรือแสดงผล

กระบวนการหลักประกอบด้วย

```text
External API
    ↓
Raw Data
    ↓
Data Processing
    ↓
Data Normalization
    ↓
Data Validation
    ↓
SQLite Database / Analysis
    ↓
Dashboard
```

การจัดการข้อมูลอาจประกอบด้วย

* Normalize Nested Data
* ตรวจสอบ Data Type
* จัดการ Missing Values
* แปลง Numeric Values
* จัดการ Release Date
* Extract Release Year
* Normalize Genre
* Normalize Platform
* ตรวจสอบข้อมูลก่อนนำไปวิเคราะห์

---

# 10. Data Quality Principles

ระบบให้ความสำคัญกับคุณภาพของข้อมูลก่อนนำไปวิเคราะห์

หลักการสำคัญ ได้แก่

* ตรวจสอบ Missing Values
* ตรวจสอบ Data Type
* ตรวจสอบข้อมูลที่มีรูปแบบไม่ถูกต้อง
* ตรวจสอบข้อมูลซ้ำตามเกณฑ์ที่เหมาะสม
* ไม่กำหนด Missing Value เป็นศูนย์โดยอัตโนมัติ
* ไม่สร้างข้อมูลขึ้นมาแทนโดยไม่มีหลักเกณฑ์
* ตรวจสอบจำนวนข้อมูลก่อนและหลัง Data Processing
* ใช้ข้อมูลที่มีอยู่จริงในการคำนวณ Statistics
* ตรวจสอบความสอดคล้องระหว่างข้อมูล Database, Service และ Dashboard

---

# 11. Data Analysis

Sprint 3 เพิ่มส่วน Data Analysis เพื่อเปลี่ยนข้อมูลเกมที่จัดเก็บอยู่ในระบบให้สามารถนำมาวิเคราะห์ได้

กระบวนการโดยรวม:

```text
SQLite Database
       ↓
Retrieve Game Data
       ↓
Data Cleaning
       ↓
Data Preparation
       ↓
EDA
       ↓
Statistical Analysis
       ↓
Visualization
       ↓
Dashboard
```

---

# 12. Exploratory Data Analysis (EDA)

การวิเคราะห์ข้อมูลเบื้องต้นประกอบด้วย

## 12.1 Dataset Overview

วิเคราะห์ภาพรวมของ Dataset เช่น

* จำนวนเกมทั้งหมด
* จำนวนข้อมูลที่พร้อมใช้
* Missing Values
* จำนวน Genre
* จำนวน Platform
* ช่วงของ Rating
* ข้อมูล Release Year

---

## 12.2 Rating Analysis

วิเคราะห์ Rating เช่น

* Mean
* Median
* Minimum
* Maximum
* Standard Deviation
* Rating Distribution

---

## 12.3 Genre Analysis

วิเคราะห์ Genre เช่น

* จำนวนเกมในแต่ละ Genre
* Frequency
* Proportion
* Average Rating ตาม Genre เมื่อข้อมูลเพียงพอ

---

## 12.4 Platform Analysis

วิเคราะห์ Platform เช่น

* จำนวนเกมในแต่ละ Platform
* Frequency
* Proportion
* Rating Summary ตาม Platform เมื่อข้อมูลเพียงพอ

---

## 12.5 Release Year Analysis

หากข้อมูล Release Date มีความพร้อม สามารถนำมา Extract เป็น Release Year เพื่อวิเคราะห์จำนวนเกมในแต่ละปีได้

---

## 12.6 Metacritic Analysis

หากมี Metacritic Score สามารถนำมาวิเคราะห์ เช่น

* จำนวนข้อมูลที่มีคะแนน
* Mean
* Median
* Minimum
* Maximum
* Distribution

---

## 12.7 Steam Player Analysis

หากมีข้อมูล Steam Player Count สามารถนำมาวิเคราะห์จำนวนผู้เล่นของเกมที่มีข้อมูล Steam ได้

---

# 13. Statistical Analysis

ระบบใช้ Descriptive Statistics เป็นหลักสำหรับสรุปลักษณะของ Dataset

Statistics ที่ใช้ ได้แก่

| Statistic          | Description          |
| ------------------ | -------------------- |
| Count              | จำนวนข้อมูล          |
| Mean               | ค่าเฉลี่ย            |
| Median             | ค่ามัธยฐาน           |
| Minimum            | ค่าต่ำสุด            |
| Maximum            | ค่าสูงสุด            |
| Standard Deviation | ส่วนเบี่ยงเบนมาตรฐาน |
| Frequency          | ความถี่              |
| Proportion         | สัดส่วน              |

การเลือกใช้ Statistics ต้องพิจารณาตามชนิดของข้อมูลและจำนวนข้อมูลที่มีจริง

ระบบไม่ได้มีเป้าหมายหลักในการทำ Inferential Statistics หรือ Machine Learning

---

# 14. Dashboard Statistics & Visualization

Dashboard ของ Sprint 3 เพิ่มส่วนสำหรับนำเสนอผลการวิเคราะห์

ตัวอย่างองค์ประกอบ:

```text
┌──────────────────────────────────────────┐
│           Statistics Dashboard           │
├────────────┬────────────┬───────────────┤
│ Total Game │ Avg Rating │ Max Rating    │
├────────────┴────────────┴───────────────┤
│ Genre Distribution                       │
├──────────────────────────────────────────┤
│ Platform Distribution                    │
├──────────────────────────────────────────┤
│ Rating / Genre Analysis                  │
├──────────────────────────────────────────┤
│ Release / Metacritic / Steam Analysis    │
└──────────────────────────────────────────┘
```

Visualization ถูกออกแบบให้สัมพันธ์กับประเภทของข้อมูล เช่น

| Visualization      | Purpose                             |
| ------------------ | ----------------------------------- |
| Bar Chart          | เปรียบเทียบจำนวนหรือค่าระหว่างกลุ่ม |
| Distribution Chart | แสดงการกระจายของข้อมูล              |
| Category Chart     | แสดง Frequency ของ Genre / Platform |
| Comparison Chart   | เปรียบเทียบค่าระหว่างเกมหรือกลุ่ม   |

---

# 15. System Architecture

Architecture ของระบบหลังจาก Sprint 3 สามารถสรุปได้ดังนี้

```text
                         ┌─────────────────────┐
                         │     Web Browser     │
                         │        User         │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │   Streamlit Web UI  │
                         │      Dashboard      │
                         └──────────┬──────────┘
                                    │
                                    ↓
                         ┌─────────────────────┐
                         │    Game Service     │
                         │ Application Logic   │
                         └──────┬────────┬─────┘
                                │        │
                    ┌───────────┘        └───────────┐
                    ↓                                ↓
             ┌─────────────┐                  ┌─────────────┐
             │  RAWG API   │                  │  Steam API  │
             └──────┬──────┘                  └──────┬──────┘
                    │                                │
                    └────────────┬───────────────────┘
                                 ↓
                       ┌──────────────────┐
                       │ Data Processing  │
                       │   Normalization  │
                       └────────┬─────────┘
                                │
                                ↓
                       ┌──────────────────┐
                       │ SQLite Database  │
                       └────────┬─────────┘
                                │
                                ↓
                       ┌──────────────────┐
                       │ Data Analysis    │
                       │   Statistics     │
                       └────────┬─────────┘
                                │
                                ↓
                       ┌──────────────────┐
                       │ Visualization    │
                       └────────┬─────────┘
                                │
                                ↓
                       ┌──────────────────┐
                       │ Streamlit        │
                       │ Dashboard        │
                       └──────────────────┘
```

---

# 16. Application Data Flow

```text
RAWG API
   ↓
Fetch Game Data
   ↓
Data Processing
   ↓
Normalize Data
   ↓
SQLite Database
   ↓
Game Service
   ↓
Analysis / Statistics
   ↓
Visualization
   ↓
Streamlit Dashboard
   ↓
Web Browser
```

สำหรับ Steam:

```text
Steam API
   ↓
Steam Player Data
   ↓
Data Processing
   ↓
SQLite / Snapshot
   ↓
Game Service
   ↓
Dashboard / Analysis
```

---

# 17. Technology Stack

| Technology | Purpose                      |
| ---------- | ---------------------------- |
| Python     | Programming Language         |
| Streamlit  | Web Application / Dashboard  |
| Pandas     | Data Processing และ Analysis |
| SQLite     | Database                     |
| RAWG API   | Game Data Source             |
| Steam API  | Steam Player Data            |
| pytest     | Automated Testing            |
| Git        | Version Control              |
| GitHub     | Repository / Collaboration   |

---

# 18. Project Structure

โครงสร้างโปรเจกต์หลังการพัฒนาประกอบด้วยส่วนหลักดังนี้

```text
Gaming-Statistics-Dashboard/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env.example
│
├── data/
│   └── gaming_statistics.db
│
├── docs/
│   ├── Project_Pitch.md
│   ├── Plan.md
│   ├── CHANGELOG.md
│   └── LEARNINGLOG.md
│
├── src/
│   ├── app.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   ├── api/
│   │   ├── rawg_api.py
│   │   └── steam_api.py
│   │
│   ├── components/
│   │   ├── dashboard.py
│   │   ├── statistics_page.py
│   │   └── styles.py
│   │
│   ├── database/
│   │   └── database.py
│   │
│   ├── services/
│   │   └── game_service.py
│   │
│   └── utils/
│       ├── data_processing.py
│       └── time_utils.py
│
├── tests/
│   ├── test_dashboard.py
│   ├── test_data_processing.py
│   ├── test_database.py
│   ├── test_game_service.py
│   ├── test_rawg_api.py
│   ├── test_statistics.py
│   ├── test_steam_api.py
│   └── test_time_utils.py
│
├── Sprint1/
│   └── Sprint_1.md
│
├── Sprint2/
│   └── Sprint_2.md
│
├── Sprint3/
│   └── Sprint_3.md
│
└── Sprint4/
    └── ...
```

### Directory Responsibilities

| Directory / File  | Responsibility                        |
| ----------------- | ------------------------------------- |
| `src/app.py`      | Entry Point ของ Streamlit Application |
| `src/analysis/`   | Data Analysis และ Statistics          |
| `src/api/`        | External API Integration              |
| `src/components/` | Dashboard และ UI Components           |
| `src/database/`   | SQLite Database                       |
| `src/services/`   | Application / Business Logic          |
| `src/utils/`      | Data Processing และ Utility Functions |
| `tests/`          | Automated Tests                       |
| `docs/`           | Project Documentation                 |
| `Sprint1/`        | Sprint 1 Documentation                |
| `Sprint2/`        | Sprint 2 Documentation                |
| `Sprint3/`        | Sprint 3 Documentation                |

---

# 19. Development Methodology

โปรเจกต์ใช้แนวทาง **Incremental Development**

แต่ละ Sprint มี Goal และ Scope ของตัวเอง โดยนำผลลัพธ์จาก Sprint ก่อนหน้าไปต่อยอดใน Sprint ถัดไป

```text
Plan
  ↓
Develop
  ↓
Test
  ↓
Review
  ↓
Document
  ↓
Next Sprint
```

แนวทางนี้ช่วยให้ทีมสามารถแบ่งงานออกเป็นส่วนย่อย ตรวจสอบผลลัพธ์เป็นระยะ และลดความเสี่ยงจากการพัฒนาระบบทั้งหมดพร้อมกัน

---

# 20. Sprint 1 — CLI Foundation

## Period

**10–15 September 2026**

## Goal

สร้าง Foundation ของ Application และทดสอบโครงสร้างการทำงานหลักก่อนเชื่อมต่อ External API

## Main Features

* CLI Application
* Main Menu
* Menu Navigation
* View Games
* Search Game
* View Statistics
* View Genres
* View Top Rated Games
* Input Validation
* Exception Handling
* Local Sample Dataset
* QA / Edge Case Testing

## Data Source

Sprint 1 ใช้ **Local Sample Dataset**

ยังไม่ได้เชื่อมต่อ RAWG API จริง

## Status

**✅ Completed**

---

# 21. Sprint 2 — Web Application, API & Database

## Period

**20–24 September 2026**

## Goal

เปลี่ยนจาก CLI Foundation ไปสู่ Web Application พร้อม External API และ Database

## Main Features

* Streamlit Web Application
* Dashboard Navigation
* RAWG API Integration
* RAWG Search
* Pagination
* Steam API Integration
* Current Player Count
* Steam Top 100 / Live Players
* SQLite Database
* Game Service
* Data Processing
* Game Library
* Genre Filter
* Platform Filter
* Rating Filter
* Top Rated Games
* Game Detail
* Error Handling
* Empty State
* Steam Player Snapshot
* Automated Tests

## Architecture

```text
Web Browser
     ↓
Streamlit UI
     ↓
Game Service
     ↓
RAWG / Steam API
     ↓
Data Processing
     ↓
SQLite
```

## Status

**✅ Completed**

---

# 22. Sprint 3 — Data Analysis, Visualization & Advanced Features

## Period

**25–29 September 2026**

## Goal

นำข้อมูลจากระบบมาวิเคราะห์และนำเสนอในรูปแบบ Statistics และ Visualization พร้อมเพิ่มความสามารถในการสำรวจและเปรียบเทียบข้อมูลเกม

## Main Areas

### Data Processing

* Data Cleaning
* Data Preparation
* Data Validation
* Data Normalization
* Missing Data Handling

### Analysis

* EDA
* Descriptive Statistics
* Rating Analysis
* Genre Analysis
* Platform Analysis
* Release Year Analysis
* Metacritic Analysis
* Steam Player Analysis

### Dashboard

* Statistics Summary
* Data Visualization
* Chart Integration
* Empty State

### Advanced Features

* Advanced Filtering
* Advanced Sorting
* Game Comparison
* Dashboard Integration

### Testing

* Data Processing Testing
* Statistics Testing
* Visualization Testing
* Filter Testing
* Sorting Testing
* Comparison Testing
* Integration Testing
* Edge Case Testing

## Team Roles

| สมาชิก | Role     |
| ------ | -------- |
| ออม    | Planner  |
| คิม    | Coder    |
| ฟลุ๊ค  | Debugger |

## Status

**✅ Completed**

---

# 23. Final Sprint

Final Sprint มีเป้าหมายเพื่อเตรียม Project สำหรับการส่งมอบและ Final Presentation

ขอบเขตงานที่สามารถดำเนินการต่อ ได้แก่

* Final Integration
* Final QA
* Regression Testing
* Documentation Review
* README Review
* Project Pitch Review
* Project Plan Review
* Change Log Review
* Learning Log Review
* Source Code Cleanup
* Final Presentation Preparation
* Final Project Submission

งานที่ยังไม่ได้ดำเนินการไม่ควรถูกระบุว่าเสร็จจนกว่าจะมีการตรวจสอบผลจริง

## Status

**⏳ Planned**

---

# 24. Project Timeline

| Sprint       | Period         | Main Focus                                   | Status      |
| ------------ | -------------- | -------------------------------------------- | ----------- |
| Sprint 1     | 10–15 Sep 2026 | CLI Foundation                               | ✅ Completed |
| Sprint 2     | 20–24 Sep 2026 | Web UI + API + SQLite                        | ✅ Completed |
| Sprint 3     | 25–29 Sep 2026 | Analysis + Visualization + Advanced Features | ✅ Completed |
| Final Sprint | หลัง Sprint 3  | Final QA + Documentation + Submission        | ⏳ Planned   |

---

# 25. Team Roles

Role ของทีมถูกหมุนเวียนระหว่าง Sprint เพื่อให้สมาชิกได้มีประสบการณ์ในหลายหน้าที่

## Sprint 1

| สมาชิก | Role     |
| ------ | -------- |
| คิม    | Planner  |
| ฟลุ๊ค  | Coder    |
| ออม    | Debugger |

## Sprint 2

| สมาชิก | Role          |
| ------ | ------------- |
| ฟลุ๊ค  | Planner       |
| ออม    | Coder         |
| คิม    | Debugger / QA |

## Sprint 3

| สมาชิก | Role     |
| ------ | -------- |
| ออม    | Planner  |
| คิม    | Coder    |
| ฟลุ๊ค  | Debugger |

---

# 26. Testing Strategy

ระบบมีการทดสอบหลายระดับตามขอบเขตของแต่ละ Sprint

## Unit Testing

ทดสอบ Function หรือ Module แต่ละส่วน เช่น

* Data Processing
* Statistics
* Database
* API
* Service

## Functional Testing

ตรวจสอบว่า Feature ทำงานตาม Requirements เช่น

* Search
* Filter
* Sort
* Statistics
* Visualization
* Game Comparison

## Integration Testing

ตรวจสอบการทำงานร่วมกันของ

```text
UI
 ↓
Game Service
 ↓
Data Processing
 ↓
Database / API
```

## Edge Case Testing

ตรวจสอบกรณี เช่น

* Empty Dataset
* Missing Values
* Invalid API Response
* API Error
* ไม่มีข้อมูลหลัง Filter
* ข้อมูลไม่เพียงพอสำหรับ Chart

---

# 27. Error Handling

ระบบออกแบบให้รองรับข้อผิดพลาดที่อาจเกิดขึ้นจาก External API และข้อมูลภายในระบบ

ตัวอย่าง:

```text
API Error
    ↓
Error Handling
    ↓
User-friendly Message
```

กรณีที่ข้อมูลไม่พร้อมใช้งาน ระบบควรแสดงข้อความหรือ Empty State ที่เหมาะสมแทนการทำให้ Application Crash

---

# 28. Project Scope

## In Scope

* Web Application
* Game Data
* RAWG API
* Steam API
* SQLite
* Data Processing
* Search
* Filtering
* Sorting
* Pagination
* Game Detail
* Top Rated
* Live Players
* EDA
* Descriptive Statistics
* Data Visualization
* Game Comparison
* Automated Testing
* Documentation

## Out of Scope

งานต่อไปนี้ไม่ใช่เป้าหมายหลักของ Project ในขอบเขตปัจจุบัน

* User Authentication
* User Account System
* Online Game Purchasing
* Payment System
* Social Network
* Machine Learning Model
* Recommendation Model
* Full-scale Production Deployment
* ระบบ AI ที่อยู่นอก Scope ของรายวิชา

---

# 29. Project Limitations

แม้ว่าระบบจะสามารถรวบรวมและวิเคราะห์ข้อมูลเกมได้ แต่ยังมีข้อจำกัดบางประการ

### 1. External API Dependency

ข้อมูลขึ้นอยู่กับ External API หาก API ไม่พร้อมใช้งาน ระบบอาจไม่สามารถดึงข้อมูลใหม่ได้

### 2. Data Completeness

เกมบางเกมอาจไม่มีข้อมูลบางประเภท เช่น

* Metacritic Score
* Steam App ID
* Steam Player Count
* Release Date

ดังนั้น Statistics และ Visualization บางประเภทอาจใช้ข้อมูลเฉพาะ Records ที่มีข้อมูลพร้อม

### 3. Data Freshness

ข้อมูลจาก External API และ Steam Player Count อาจมีการเปลี่ยนแปลงตามเวลา

### 4. Analysis Scope

การวิเคราะห์เน้น Descriptive Statistics และ EDA ไม่ได้มีเป้าหมายเพื่อสรุปเหตุและผล หรือสร้าง Predictive Model

---

# 30. Expected Benefits

ระบบช่วยให้ผู้ใช้สามารถ

* ค้นหาเกมได้ง่ายขึ้น
* สำรวจข้อมูลเกมในระบบเดียว
* ใช้ Filter และ Sort เพื่อค้นหาข้อมูลที่ต้องการ
* ดูรายละเอียดเกมได้สะดวก
* ดูข้อมูล Rating และ Metacritic
* ดู Steam Player Data
* เปรียบเทียบเกม
* ดู Statistics
* เข้าใจข้อมูลผ่าน Visualization

ในมุมมองด้านการเรียนรู้ โปรเจกต์ยังช่วยให้สมาชิกได้ฝึก

* Python Programming
* Web Application Development
* API Integration
* Database Management
* Data Processing
* Data Analysis
* Data Visualization
* Software Testing
* Git / GitHub
* Team Collaboration
* Incremental Development

---

# 31. Project Goal

เป้าหมายสุดท้ายของโปรเจกต์คือการพัฒนา **Gaming Statistics Dashboard** ให้เป็น Web Application ที่สามารถรวบรวมข้อมูลเกมจาก External API จัดการข้อมูลผ่าน Database วิเคราะห์ข้อมูล และนำเสนอข้อมูลผ่าน Dashboard ในระบบเดียว

ภาพรวม:

```text
                     USER
                      ↓
                WEB BROWSER
                      ↓
          GAMING STATISTICS DASHBOARD
                      ↓
              ┌───────┴────────┐
              ↓                ↓
           SEARCH          STATISTICS
              ↓                ↓
           FILTER          VISUALIZATION
              ↓                ↓
            SORT           COMPARISON
              └───────┬────────┘
                      ↓
                 GAME SERVICE
                      ↓
              ┌───────┴────────┐
              ↓                ↓
          RAWG API         STEAM API
              ↓                ↓
              └───────┬────────┘
                      ↓
               DATA PROCESSING
                      ↓
                 SQLITE DB
```

---

# 32. Current Project Status

ณ สิ้นสุด Sprint 3 ระบบได้พัฒนาจาก CLI Application ไปสู่ Web Application และต่อยอดไปสู่ระบบที่มี Data Processing, Statistics, Visualization และ Advanced Features

## Completed

* CLI Foundation
* Streamlit Web Application
* RAWG API Integration
* Steam API Integration
* SQLite Database
* Game Service
* Data Processing
* Game Library
* Search
* Filter
* Sort
* Pagination
* Top Rated
* Game Detail
* Live Players
* Statistics
* Data Visualization
* Advanced Features
* Game Comparison
* Automated Testing ในส่วนที่อยู่ใน Scope
* Project Documentation สำหรับ Sprint 1–3

## Remaining / Final Sprint

* Final QA
* Final Regression Testing
* Final Documentation Review
* Source Code Cleanup
* Final Integration Review
* Final Presentation
* Final Submission

---

# 33. Definition of Project Completion

โปรเจกต์จะถือว่าเสร็จสมบูรณ์เมื่อ

### Application

* [ ] Web Application สามารถเปิดใช้งานได้
* [ ] Navigation ทำงานได้
* [ ] Game Library ทำงานได้
* [ ] Search ทำงานได้
* [ ] Filter ทำงานได้
* [ ] Sort ทำงานได้
* [ ] Game Detail ทำงานได้
* [ ] Statistics แสดงผลได้
* [ ] Visualization แสดงผลได้
* [ ] Game Comparison ทำงานได้
* [ ] Error Handling และ Empty State ทำงานได้

### Data

* [ ] RAWG API ทำงานตาม Scope
* [ ] Steam API ทำงานตาม Scope
* [ ] Data Processing ทำงานถูกต้อง
* [ ] SQLite Database ทำงานถูกต้อง
* [ ] Statistics ใช้ข้อมูลที่ผ่านการเตรียมแล้ว

### Testing

* [ ] Unit Tests ทำงาน
* [ ] Functional Tests ทำงาน
* [ ] Integration Tests ทำงานตาม Scope
* [ ] Edge Cases ได้รับการตรวจสอบ
* [ ] Known Issues ถูกบันทึกอย่างชัดเจน

### Documentation

* [ ] README อัปเดต
* [ ] Project Pitch อัปเดต
* [ ] Project Plan อัปเดต
* [ ] Change Log อัปเดต
* [ ] Learning Log อัปเดต
* [ ] Sprint Reports อัปเดต

### Submission

* [ ] Source Code พร้อมส่ง
* [ ] Documentation พร้อมส่ง
* [ ] Final QA เสร็จ
* [ ] Final Presentation พร้อม
* [ ] Repository อยู่ในสถานะพร้อมส่งมอบ

---

# 34. Conclusion

**Gaming Statistics Dashboard** เริ่มต้นจาก CLI Application ใน Sprint 1 และพัฒนาอย่างต่อเนื่องจนกลายเป็น Web Application ที่สามารถเชื่อมต่อข้อมูลจริงจาก RAWG API และ Steam API จัดเก็บข้อมูลผ่าน SQLite และนำข้อมูลมาประมวลผล วิเคราะห์ และนำเสนอผ่าน Dashboard

การพัฒนาแบ่งออกเป็นลำดับดังนี้

```text
Sprint 1
CLI Foundation
      ↓
Sprint 2
Web Application
      ↓
RAWG + Steam + SQLite
      ↓
Sprint 3
Data Processing
      ↓
EDA + Statistics
      ↓
Visualization
      ↓
Advanced Features
      ↓
Final Sprint
Final QA + Documentation + Submission
```

เป้าหมายของโปรเจกต์ไม่ได้มีเพียงการสร้าง Application ที่สามารถแสดงข้อมูลเกมเท่านั้น แต่ยังเป็นการประยุกต์ใช้ความรู้ด้าน **Python Programming, Web Application, API Integration, Database, Data Processing, Data Analysis, Visualization และ Software Testing** เข้าด้วยกันภายใน Project เดียว

> **Gaming Statistics Dashboard — From Game Data to Interactive Insights.**
