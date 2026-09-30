# 🎮 Gaming Statistics Dashboard

> Final Term Project — CP352301 Script Programming

Gaming Statistics Dashboard เป็น Web Application สำหรับรวบรวม จัดการ วิเคราะห์ และนำเสนอข้อมูลเกี่ยวกับวิดีโอเกมผ่าน Dashboard

ระบบพัฒนาด้วย Python และ Streamlit โดยเชื่อมต่อข้อมูลจาก RAWG API และ Steam API จัดเก็บข้อมูลผ่าน SQLite Database และนำข้อมูลมาผ่าน Data Processing, Data Analysis, Statistics และ Data Visualization ก่อนนำเสนอผ่าน Web Browser

โปรเจกต์พัฒนาด้วยแนวทาง **Incremental Development** โดยเริ่มจาก CLI Application ใน Sprint 1 และต่อยอดเป็น Web Application ใน Sprint 2 จากนั้นเพิ่ม Data Analysis, Visualization และ Advanced Features ใน Sprint 3

---

## 📌 Project Overview

### Problem

ข้อมูลเกี่ยวกับวิดีโอเกมมีหลายประเภท เช่น

- Game Name
- Rating
- Genre
- Platform
- Release Date
- Metacritic Score
- Steam Player Count
- Game Image
- ข้อมูลอื่น ๆ จาก External API

ข้อมูลเหล่านี้อาจอยู่ในหลายแหล่ง ทำให้การค้นหา สำรวจ และเปรียบเทียบข้อมูลเกมจำนวนมากทำได้ไม่สะดวก

นอกจากนี้ ข้อมูลเกมยังสามารถนำมาวิเคราะห์เพื่อดู Frequency, Distribution, Statistics และแนวโน้มต่าง ๆ ได้ แต่ผู้ใช้จำเป็นต้องมีขั้นตอนในการจัดการและวิเคราะห์ข้อมูลก่อนนำเสนอ

### Proposed Solution

พัฒนา **Gaming Statistics Dashboard** ที่สามารถ:

- ดึงข้อมูลเกมจาก RAWG API
- ดึงข้อมูล Steam Player จาก Steam API
- จัดการและ Normalize ข้อมูล
- จัดเก็บข้อมูลผ่าน SQLite Database
- ค้นหาเกม
- Filter ข้อมูลเกม
- Sort ข้อมูลเกม
- Pagination
- ดูรายละเอียดเกม
- ดู Top Rated Games
- ดู Steam Live Players
- วิเคราะห์ข้อมูลด้วย EDA
- คำนวณ Descriptive Statistics
- แสดง Statistics Dashboard
- แสดง Data Visualization
- เปรียบเทียบข้อมูลเกม
- จัดการ Missing Data และ Empty State
- รองรับ API Error และ Database Error

---

## 🎯 Project Goals

เป้าหมายของ Project คือการพัฒนา Web Application ที่สามารถเชื่อมต่อ External API, Database และ Data Analysis Pipeline เข้าด้วยกัน

ระบบถูกพัฒนาเป็น Sprint ตามลำดับ:

```text
Sprint 1
Application Foundation
        ↓
CLI Application
        ↓
Sprint 2
Web UI + API + Database
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
Final QA + Integration + Documentation
````

---

## 🖥️ Application

ระบบเป็น **Web Application** ที่สามารถเปิดใช้งานผ่าน Web Browser

### Framework

* Streamlit

### Application Flow

```text
User
  ↓
Web Browser
  ↓
Streamlit Dashboard
  ↓
Game Service
  ↓
Data Processing
  ↓
RAWG API / Steam API / SQLite
  ↓
Analysis / Statistics
  ↓
Visualization
  ↓
Dashboard
```

---

# ✨ Current Features

## 🎮 Game Library

แสดงรายการเกมจากข้อมูลที่ระบบจัดการไว้

รองรับข้อมูล เช่น:

* Game Name
* Rating
* Genres
* Platforms
* Release Date
* Metacritic Score
* Image
* Steam Player Data เมื่อมีข้อมูล

ระบบรองรับ Pagination เพื่อช่วยจัดการข้อมูลจำนวนมาก

---

## 🔎 Game Search

ค้นหาเกมจากชื่อเกมผ่าน Web Application

ตัวอย่าง:

```text
Search: Minecraft
```

ระบบจะค้นหาเกมที่ตรงกับคำค้นหาจากข้อมูลที่มีอยู่

---

## 🎯 Game Filters

ระบบรองรับการ Filter ข้อมูลเกมตาม:

* Genre
* Platform
* Minimum Rating
* Release Year

สามารถใช้หลายเงื่อนไขร่วมกันเพื่อจำกัดชุดข้อมูลที่ต้องการสำรวจ

---

## ↕️ Game Sorting

ระบบรองรับการเรียงข้อมูลเกมตามข้อมูลสำคัญ เช่น:

* Rating
* Release Date
* Game Name

รองรับ:

* Ascending
* Descending

---

## 📄 Pagination

เมื่อ Dataset มีข้อมูลจำนวนมาก ระบบแบ่งข้อมูลออกเป็นหลายหน้าเพื่อให้ผู้ใช้สามารถสำรวจข้อมูลได้ง่ายขึ้น

---

## ⭐ Top Rated Games

แสดงเกมที่มี Rating สูง เพื่อให้ผู้ใช้สามารถสำรวจเกมที่มีคะแนนสูงได้สะดวก

---

## 🎭 Genres

แสดงและจัดการข้อมูลเกมตาม Genre

ข้อมูล Genre สามารถนำไปใช้ทั้งใน:

* Filtering
* Statistics
* Visualization
* Data Analysis

---

## 🎯 Platforms

แสดงและจัดการข้อมูล Platform ของเกม

ข้อมูล Platform สามารถนำไปใช้ใน:

* Filtering
* Frequency Analysis
* Proportion Analysis
* Visualization

---

## 📊 Game Detail

แสดงรายละเอียดของเกม เช่น:

* Game Name
* Rating
* Release Date
* Genres
* Platforms
* Metacritic Score
* Ratings Count
* Image
* Steam Player Information เมื่อมีข้อมูล

---

## 👥 Steam Live Players

ระบบเชื่อมต่อ Steam API เพื่อแสดงข้อมูลเกี่ยวกับ Steam Player

ข้อมูลที่เกี่ยวข้อง:

* Steam App ID
* Current Player Count
* Top Live Players
* Player Snapshot

ข้อมูล Steam Player อาจไม่มีสำหรับเกมบางรายการ หากเกมนั้นไม่มี Steam App ID หรือไม่สามารถจับคู่ข้อมูลได้

---

## 🔄 Refresh & Snapshot

ระบบมีการจัดการข้อมูล Steam Player ที่มีการเปลี่ยนแปลงตามเวลา

มีแนวคิดในการใช้ Snapshot และ Refresh เพื่อช่วย:

* ลดการเรียก API ซ้ำ
* เก็บข้อมูล Player Count
* จัดการข้อมูลที่เปลี่ยนแปลงตามเวลา
* นำข้อมูลไปใช้ในการวิเคราะห์

---

# 📈 Data Processing

ข้อมูลจาก External API จะถูกนำมาผ่าน Data Processing ก่อนนำไปจัดเก็บหรือวิเคราะห์

ภาพรวม:

```text
RAWG API / Steam API
        ↓
Raw Data
        ↓
Data Processing
        ↓
Normalization
        ↓
Validation
        ↓
SQLite Database
        ↓
Game Service
        ↓
Analysis / Dashboard
```

### Data Processing ที่เกี่ยวข้อง

* Normalize API Response
* ตรวจสอบ Data Type
* จัดการ Missing Values
* แปลง Numeric Data
* จัดการ Release Date
* Extract Release Year
* Normalize Genre
* Normalize Platform
* ตรวจสอบข้อมูลก่อน Analysis

---

# 🧹 Data Quality

ระบบให้ความสำคัญกับ Data Quality ก่อนนำข้อมูลไปใช้

หลักการสำคัญ:

* ตรวจสอบ Missing Values
* ตรวจสอบ Data Type
* ตรวจสอบข้อมูลที่ไม่ถูกต้อง
* ตรวจสอบข้อมูลซ้ำตามเกณฑ์ที่เหมาะสม
* ตรวจสอบข้อมูลที่อยู่นอกช่วงที่เหมาะสม
* ไม่กำหนด Missing Value เป็นศูนย์โดยอัตโนมัติ
* ไม่สร้างข้อมูลแทนโดยไม่มีหลักเกณฑ์
* ตรวจสอบจำนวนข้อมูลก่อนและหลัง Processing
* ใช้ข้อมูลจริงในการคำนวณ Statistics

---

# 📊 Data Analysis

Sprint 3 เพิ่ม Data Analysis Layer เพื่อเปลี่ยนข้อมูลเกมที่จัดเก็บอยู่ในระบบให้สามารถวิเคราะห์และนำเสนอเป็น Statistics ได้

ภาพรวม:

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

# 🔍 Exploratory Data Analysis (EDA)

## Dataset Overview

วิเคราะห์ภาพรวมของ Dataset เช่น:

* Total Games
* จำนวนข้อมูลที่พร้อมใช้
* Missing Values
* จำนวน Genre
* จำนวน Platform
* Rating Range
* Release Year
* Metacritic Data Availability
* Steam Player Data Availability

---

## ⭐ Rating Analysis

วิเคราะห์ Rating เช่น:

* Count
* Mean
* Median
* Minimum
* Maximum
* Standard Deviation
* Rating Distribution

---

## 🎭 Genre Analysis

วิเคราะห์ Genre เช่น:

* จำนวนเกมในแต่ละ Genre
* Frequency
* Proportion
* Average Rating ตาม Genre เมื่อข้อมูลเพียงพอ

---

## 🎯 Platform Analysis

วิเคราะห์ Platform เช่น:

* จำนวนเกมในแต่ละ Platform
* Frequency
* Proportion
* Rating Summary ตาม Platform เมื่อข้อมูลเพียงพอ

---

## 📅 Release Year Analysis

นำ Release Date มา Extract เป็น Release Year เพื่อวิเคราะห์จำนวนเกมในแต่ละปี เมื่อข้อมูลมีความพร้อม

---

## 🏆 Metacritic Analysis

หากมี Metacritic Score สามารถวิเคราะห์:

* Count
* Mean
* Median
* Minimum
* Maximum
* Distribution

---

## 👥 Steam Player Analysis

หากมี Steam Player Count สามารถวิเคราะห์:

* Current Player Count
* Top Live Players
* Player Distribution
* Player Comparison

---

# 📐 Statistical Analysis

ระบบใช้ **Descriptive Statistics** เป็นหลักในการสรุปลักษณะของข้อมูล

Statistics ที่ใช้ ได้แก่:

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

การเลือกใช้ Statistics จะพิจารณาตามประเภทของข้อมูลและข้อมูลที่มีจริง

โปรเจกต์ไม่ได้มีเป้าหมายหลักในการทำ Inferential Statistics หรือ Machine Learning

---

# 📊 Statistics Dashboard

ระบบมีส่วนสำหรับสรุป Statistics ในรูปแบบ Dashboard

ตัวอย่างข้อมูลที่สามารถแสดง:

* Total Games
* Average Rating
* Highest Rating
* Lowest Rating
* Number of Genres
* Number of Platforms
* Release Year Statistics
* Metacritic Statistics
* Steam Player Statistics

ตัวอย่างโครงสร้าง:

```text
┌──────────────────────────────────────────┐
│          Statistics Dashboard            │
├────────────┬────────────┬───────────────┤
│ Total Game │ Avg Rating │ Max Rating    │
├────────────┴────────────┴───────────────┤
│ Genre Distribution                       │
├──────────────────────────────────────────┤
│ Platform Distribution                    │
├──────────────────────────────────────────┤
│ Rating Analysis                          │
├──────────────────────────────────────────┤
│ Release / Metacritic / Steam Analysis    │
└──────────────────────────────────────────┘
```

---

# 📉 Data Visualization

ระบบนำข้อมูลมาแสดงในรูปแบบ Visualization เพื่อช่วยให้ผู้ใช้เข้าใจข้อมูลได้ง่ายขึ้น

Visualization ที่เกี่ยวข้อง:

* Genre Distribution
* Platform Distribution
* Rating Analysis
* Rating by Genre
* Release Year Distribution
* Metacritic Score Distribution
* Steam Player Visualization

ชนิด Chart จะเลือกให้เหมาะสมกับประเภทของข้อมูล

ตัวอย่าง:

| Visualization      | Purpose                              |
| ------------------ | ------------------------------------ |
| Bar Chart          | เปรียบเทียบจำนวนหรือค่า              |
| Distribution Chart | แสดงการกระจายข้อมูล                  |
| Category Chart     | แสดง Frequency ของ Category          |
| Comparison Chart   | เปรียบเทียบข้อมูลระหว่างกลุ่มหรือเกม |

---

# ⚖️ Game Comparison

ระบบรองรับการเปรียบเทียบเกม 2 เกม

ตัวอย่างข้อมูล:

```text
Game A              Game B
--------------------------------
Rating
Metacritic
Steam Players
```

ผู้ใช้สามารถเลือกเกมที่ต้องการเปรียบเทียบและดูข้อมูลสำคัญในรูปแบบเดียวกัน

---

# ⚠️ Error Handling & Empty State

ระบบรองรับกรณีที่ข้อมูลไม่พร้อมใช้งาน เช่น:

* API Error
* Invalid API Response
* Database Error
* Missing Data
* Empty Search Result
* Empty Dataset
* ไม่มีข้อมูลหลัง Filter
* ข้อมูลไม่เพียงพอสำหรับ Visualization

ระบบควรแสดงข้อความที่เหมาะสมแทนการทำให้ Application Crash

---

# 🛠️ Technologies

| Technology    | Purpose                     |
| ------------- | --------------------------- |
| Python        | Application Development     |
| Streamlit     | Web Application / Dashboard |
| Pandas        | Data Processing / Analysis  |
| RAWG API      | Game Data                   |
| Steam API     | Steam Player Data           |
| SQLite        | Data Persistence            |
| pytest        | Automated Testing           |
| Git           | Version Control             |
| GitHub        | Repository / Collaboration  |
| python-dotenv | Environment Variables       |

---

# 🌐 APIs

## RAWG Video Games Database API

ใช้เป็นแหล่งข้อมูลหลักของเกม

ข้อมูลที่ระบบสนใจ เช่น:

* Game ID
* Game Name
* Rating
* Released Date
* Genres
* Platforms
* Metacritic Score
* Ratings Count
* Image

Website:

[https://rawg.io/](https://rawg.io/)

API:

[https://api.rawg.io/](https://api.rawg.io/)

---

## Steam API

ใช้สำหรับข้อมูลที่เกี่ยวข้องกับ Steam

โดยเฉพาะ:

* Steam App ID
* Current Player Count
* Top Live Players
* Player Snapshot

ข้อมูล Steam อาจไม่มีสำหรับเกมบางรายการ

---

# 🗄️ Database

Project ใช้ **SQLite** เป็น Database สำหรับจัดเก็บข้อมูล

Database File:

```text
data/gaming_statistics.db
```

Data Flow:

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite Database
    ↓
Game Service
    ↓
Analysis
    ↓
Streamlit Web UI
```

SQLite ช่วยให้ระบบสามารถจัดเก็บข้อมูลเกมและข้อมูลที่เกี่ยวข้องไว้ใน Local Database และนำกลับมาใช้งานโดยไม่ต้องเรียก External API ทุกครั้ง

---

# 🏗️ Project Structure

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
│   ├── CHANGELOG.md
│   ├── LEARNINGLOG.md
│   ├── Plan.md
│   └── Project_Pitch.md
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
├── src/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── analysis/
│   │   ├── __init__.py
│   │   └── statistics.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── rawg_api.py
│   │   └── steam_api.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── dashboard.py
│   │   ├── statistics_page.py
│   │   └── styles.py
│   │
│   ├── database/
│   │   ├── __init__.py
│   │   └── database.py
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   └── game_service.py
│   │
│   └── utils/
│       ├── __init__.py
│       ├── data_processing.py
│       └── time_utils.py
│
└── tests/
    ├── test_dashboard.py
    ├── test_data_processing.py
    ├── test_database.py
    ├── test_game_service.py
    ├── test_rawg_api.py
    ├── test_statistics.py
    ├── test_steam_api.py
    └── test_time_utils.py
```

---

# 🧩 Architecture

Project แบ่งระบบออกเป็น Module ตามหน้าที่ เพื่อให้สามารถพัฒนา ทดสอบ และดูแลได้ง่ายขึ้น

## API Layer

รับผิดชอบการเชื่อมต่อ External API

```text
src/api/
├── rawg_api.py
└── steam_api.py
```

---

## Data Processing Layer

รับผิดชอบการจัดรูปแบบ Normalize และเตรียมข้อมูล

```text
src/utils/data_processing.py
```

---

## Database Layer

รับผิดชอบ SQLite Database

```text
src/database/database.py
```

---

## Service Layer

รับผิดชอบ Application Logic และเป็นตัวกลางระหว่าง UI, API, Data Processing และ Database

```text
src/services/game_service.py
```

---

## Analysis Layer

รับผิดชอบ Statistics และ Data Analysis

```text
src/analysis/statistics.py
```

---

## UI / Components Layer

รับผิดชอบ Web Application, Dashboard และ Statistics Page

```text
src/app.py
src/components/
```

---

# 🔄 System Architecture

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
                         │  Application Logic  │
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

# ⚙️ Installation

## 1. Clone Repository

```bash
git clone <repository-url>
cd Gaming-Statistics-Dashboard
```

---

## 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

สร้างไฟล์ `.env` จาก `.env.example`

ตัวอย่าง:

```env
RAWG_API_KEY=your_rawg_api_key
```

API Key ไม่ควรถูกเขียนไว้โดยตรงใน Source Code และไม่ควร Commit ลง Public Repository

ไฟล์ `.env` ควรอยู่ใน `.gitignore`

---

# ▶️ Run Application

รัน Streamlit Application:

```bash
streamlit run src/app.py
```

จากนั้นเปิด URL ที่ Streamlit แสดงใน Terminal ผ่าน Web Browser

โดยทั่วไป:

```text
http://localhost:8501
```

---

# 🧪 Testing

Project ใช้ `pytest` สำหรับ Automated Testing

รัน Test Suite:

```bash
pytest
```

Test Modules:

```text
tests/
├── test_dashboard.py
├── test_data_processing.py
├── test_database.py
├── test_game_service.py
├── test_rawg_api.py
├── test_statistics.py
├── test_steam_api.py
└── test_time_utils.py
```

การทดสอบครอบคลุมส่วนสำคัญ เช่น:

* Dashboard
* Data Processing
* Database
* Game Service
* RAWG API
* Statistics
* Steam API
* Time Utilities

> หมายเหตุ: ผลการทดสอบบางส่วนขึ้นอยู่กับ Environment และ Dependencies ที่ติดตั้งในเครื่อง

---

# 🔐 API Key Security

API Key ถูกจัดการผ่าน Environment Variable

```text
.env
  ↓
Application
  ↓
API Client
  ↓
External API
```

ไม่ควรเผยแพร่ `.env` หรือ API Key ลงใน Public Repository

---

# 📚 Documentation

Project Documentation อยู่ภายใน `docs/`

```text
docs/
├── Project_Pitch.md
├── Plan.md
├── CHANGELOG.md
└── LEARNINGLOG.md
```

และ Sprint Documentation:

```text
Sprint1/
└── Sprint_1.md

Sprint2/
└── Sprint_2.md

Sprint3/
└── Sprint_3.md
```

### Project Pitch

อธิบาย:

* Project Overview
* Problem
* Proposed Solution
* Objectives
* Features
* Architecture
* Technology
* Project Scope
* Project Direction

### Plan

ใช้สำหรับ:

* Project Roadmap
* Sprint Planning
* Timeline
* Deliverables
* Team Planning
* Completion Criteria

### CHANGELOG

บันทึกการเปลี่ยนแปลงของ Project ในแต่ละ Version และ Sprint

### LEARNINGLOG

บันทึก:

* Technical Learning
* Problems
* Solutions
* Teamwork
* Lessons Learned
* Development Process

### Sprint Documentation

แต่ละ Sprint มีรายละเอียด เช่น:

* Sprint Goal
* Scope
* Tasks
* Team Roles
* Development
* Testing
* QA
* Review
* Documentation

---

# 👥 Team

| Member               | Nickname | Role                       |
| -------------------- | -------- | -------------------------- |
| นายชิษณุพงศ์ ซู      | คิม      | Planner / Coder / Debugger |
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค    | Coder / Planner / Debugger |
| นายเดโชชิต โตวินัส   | ออม      | Debugger / Coder / Planner |

Role มีการหมุนเวียนตาม Sprint เพื่อให้สมาชิกได้เรียนรู้ทั้ง:

* Planning
* Development
* Debugging
* QA
* Documentation

---

# 🔁 Sprint Roles

## Sprint 1

| Member | Role     |
| ------ | -------- |
| คิม    | Planner  |
| ฟลุ๊ค  | Coder    |
| ออม    | Debugger |

---

## Sprint 2

| Member | Role          |
| ------ | ------------- |
| ฟลุ๊ค  | Planner       |
| ออม    | Coder         |
| คิม    | Debugger / QA |

---

## Sprint 3

| Member | Role     |
| ------ | -------- |
| ออม    | Planner  |
| คิม    | Coder    |
| ฟลุ๊ค  | Debugger |

---

# 🚀 Sprint Progress

| Sprint       | Period         | Main Focus                                                     | Status      |
| ------------ | -------------- | -------------------------------------------------------------- | ----------- |
| Sprint 1     | 10–15 Sep 2026 | Application Foundation / CLI                                   | ✅ Completed |
| Sprint 2     | 20–24 Sep 2026 | Web UI / API / Database                                        | ✅ Completed |
| Sprint 3     | 25–29 Sep 2026 | Data Processing / Analysis / Visualization / Advanced Features | ✅ Completed |
| Final Sprint | หลัง Sprint 3  | Final QA / Integration / Documentation / Submission            | ⏳ Planned   |

---

# 🏁 Sprint 1 — Application Foundation

Sprint 1 เป็นช่วงสร้าง Foundation ของระบบ

### Main Features

* CLI Application
* Menu Navigation
* Game Listing
* Search
* Statistics
* Genre
* Top Rated
* Input Validation
* Exception Handling
* Local Sample Dataset
* QA Testing

### Status

**✅ Completed**

---

# 🌐 Sprint 2 — Web Application, API & Database

Sprint 2 เป็นการเปลี่ยนจาก CLI ไปสู่ Web Application

### Main Features

* Streamlit Web Application
* Dashboard
* RAWG API
* Steam API
* SQLite Database
* Game Service
* Data Processing
* Search
* Pagination
* Genre
* Top Rated
* Live Players
* Game Detail
* Error Handling
* Empty State
* Steam Player Snapshot

### Architecture

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

### Status

**✅ Completed**

---

# 📊 Sprint 3 — Data Analysis, Visualization & Advanced Features

Sprint 3 เป็นการนำข้อมูลจากระบบมาวิเคราะห์และนำเสนอในรูปแบบ Statistics และ Visualization

### Main Features

#### Data Processing

* Data Cleaning
* Data Preparation
* Data Validation
* Data Normalization
* Missing Data Handling

#### Data Analysis

* EDA
* Rating Analysis
* Genre Analysis
* Platform Analysis
* Release Year Analysis
* Metacritic Analysis
* Steam Player Analysis

#### Statistics

* Count
* Mean
* Median
* Minimum
* Maximum
* Standard Deviation
* Frequency
* Proportion

#### Visualization

* Genre Distribution
* Platform Distribution
* Rating Analysis
* Rating by Genre
* Release Year Distribution
* Metacritic Visualization
* Steam Player Visualization

#### Advanced Features

* Advanced Filtering
* Advanced Sorting
* Game Comparison
* Dashboard Integration
* Empty State Handling

### Status

**✅ Completed**

---

# 🏁 Final Sprint

Final Sprint มีเป้าหมายเพื่อเตรียม Project สำหรับ Final Submission และ Presentation

### Planned Tasks

* Final Integration
* Final QA
* Regression Testing
* Bug Fixing
* Source Code Cleanup
* Documentation Review
* README Review
* Project Pitch Review
* Project Plan Review
* CHANGELOG Review
* LEARNINGLOG Review
* Final Presentation
* Final Submission

งานที่ยังไม่ได้ตรวจสอบจากผลการทำงานจริงจะไม่ถือว่าเสร็จสมบูรณ์จนกว่าจะผ่านการตรวจสอบ

### Status

**⏳ Planned**

---

# 📈 Project Development Roadmap

```text
                    Gaming Statistics Dashboard
                              │
                              ↓
                       Sprint 1
                    CLI Foundation
                              │
                              ↓
                       Sprint 2
                 Web + API + Database
                              │
                              ↓
                       Sprint 3
             Data Processing + Analysis
                              │
                    ┌─────────┴─────────┐
                    ↓                   ↓
               Statistics         Visualization
                    │                   │
                    └─────────┬─────────┘
                              ↓
                     Advanced Features
                              │
                              ↓
                       Final Sprint
                              │
                ┌─────────────┴─────────────┐
                ↓                           ↓
            Final QA                  Documentation
                │                           │
                └─────────────┬─────────────┘
                              ↓
                       Final Project
```

---

# 📌 Current Project Status

## Sprint 1

**✅ Completed**

CLI Foundation และ Basic Features ได้รับการพัฒนาเป็นพื้นฐานของระบบ

---

## Sprint 2

**✅ Completed**

ระบบได้รับการพัฒนาเป็น Web Application พร้อม:

* Streamlit
* RAWG API
* Steam API
* SQLite
* Game Service
* Data Processing
* Search
* Filter
* Pagination
* Game Detail
* Top Rated
* Live Players

---

## Sprint 3

**✅ Completed**

ระบบได้รับการต่อยอดด้าน:

* Data Cleaning
* Data Preparation
* EDA
* Descriptive Statistics
* Dashboard Statistics
* Data Visualization
* Advanced Filtering
* Advanced Sorting
* Game Comparison
* Integration

---

## Final Sprint

**⏳ Planned**

งานหลักที่เหลือ:

* Final QA
* Regression Testing
* Final Integration
* Documentation Review
* Final Presentation
* Final Submission

---

# ⚠️ Project Limitations

## 1. External API Dependency

ข้อมูลขึ้นอยู่กับ RAWG API และ Steam API

หาก External API ไม่พร้อมใช้งาน ระบบอาจไม่สามารถดึงข้อมูลใหม่ได้

---

## 2. Data Completeness

เกมบางรายการอาจไม่มีข้อมูลบางประเภท เช่น:

* Metacritic Score
* Steam App ID
* Steam Player Count
* Release Date

ดังนั้น Statistics และ Visualization บางประเภทอาจใช้เฉพาะข้อมูลที่มีความพร้อม

---

## 3. Data Freshness

ข้อมูล Steam Player มีการเปลี่ยนแปลงตามเวลา

ข้อมูลที่แสดงจึงขึ้นอยู่กับเวลาที่มีการดึงหรือ Refresh ข้อมูล

---

## 4. Analysis Scope

การวิเคราะห์เน้น:

* Data Processing
* EDA
* Descriptive Statistics
* Visualization

ไม่ได้มีเป้าหมายหลักในการ:

* Inferential Statistics
* Machine Learning
* Predictive Modeling
* Recommendation System

---

# 🎓 Learning Outcomes

จากการพัฒนา Project ทีมได้ประยุกต์ใช้ความรู้ด้าน:

* Python Programming
* Streamlit Web Development
* REST API Integration
* SQLite Database
* Data Processing
* Data Cleaning
* Data Analysis
* Descriptive Statistics
* Data Visualization
* Software Testing
* Error Handling
* Git / GitHub
* Team Collaboration
* Incremental Development

---

# 📄 Project Information

| Item            | Information                 |
| --------------- | --------------------------- |
| Project         | Gaming Statistics Dashboard |
| Course          | CP352301 Script Programming |
| Project Type    | Final Term Project          |
| Language        | Python                      |
| Web Framework   | Streamlit                   |
| Database        | SQLite                      |
| Game API        | RAWG API                    |
| Steam Data      | Steam API                   |
| Data Processing | Pandas / Python             |
| Testing         | pytest                      |
| Version Control | Git / GitHub                |
| Current Sprint  | Sprint 3                    |
| Current Status  | ✅ Sprint 3 Completed        |

---

# 🎯 Project Completion Criteria

Project จะถือว่าเสร็จสมบูรณ์เมื่อ:

### Application

* [ ] Web Application เปิดใช้งานได้
* [ ] Navigation ทำงานได้
* [ ] Game Library ทำงานได้
* [ ] Search ทำงานได้
* [ ] Filter ทำงานได้
* [ ] Sort ทำงานได้
* [ ] Pagination ทำงานได้
* [ ] Game Detail ทำงานได้
* [ ] Statistics ทำงานได้
* [ ] Visualization ทำงานได้
* [ ] Game Comparison ทำงานได้
* [ ] Error Handling ทำงานได้
* [ ] Empty State ทำงานได้

### Data

* [ ] RAWG API ทำงานตาม Scope
* [ ] Steam API ทำงานตาม Scope
* [ ] Data Processing ทำงาน
* [ ] SQLite Database ทำงาน
* [ ] Analysis ใช้ข้อมูลที่ผ่านการเตรียมแล้ว
* [ ] Statistics ผ่านการตรวจสอบ

### Testing

* [ ] Unit Testing
* [ ] Functional Testing
* [ ] Integration Testing
* [ ] Edge Case Testing
* [ ] Regression Testing
* [ ] Final QA

### Documentation

* [ ] README
* [ ] Project Pitch
* [ ] Project Plan
* [ ] CHANGELOG
* [ ] LEARNINGLOG
* [ ] Sprint Documentation

### Submission

* [ ] Source Code พร้อมส่ง
* [ ] Documentation พร้อมส่ง
* [ ] Final QA เสร็จ
* [ ] Final Presentation พร้อม
* [ ] Repository พร้อมส่งมอบ

---

# 🔗 Documentation Map

```text
README.md
│
├── Project Overview
├── Installation
├── Usage
├── Features
├── Architecture
├── Testing
└── Project Status
        │
        ├── docs/Project_Pitch.md
        │       └── Project Concept & Scope
        │
        ├── docs/Plan.md
        │       └── Project Roadmap & Planning
        │
        ├── docs/CHANGELOG.md
        │       └── Version History
        │
        ├── docs/LEARNINGLOG.md
        │       └── Learning & Lessons Learned
        │
        ├── Sprint1/Sprint_1.md
        │       └── Sprint 1
        │
        ├── Sprint2/Sprint_2.md
        │       └── Sprint 2
        │
        └── Sprint3/Sprint_3.md
                └── Sprint 3
```

---

# 🎮 Final Project Vision

Gaming Statistics Dashboard มีเป้าหมายในการรวมกระบวนการตั้งแต่

```text
Game Data
    ↓
External APIs
    ↓
Data Processing
    ↓
Database
    ↓
Data Analysis
    ↓
Statistics
    ↓
Visualization
    ↓
Interactive Dashboard
```

ไว้ภายในระบบเดียว

โปรเจกต์จึงไม่ได้เป็นเพียง Web Application สำหรับแสดงข้อมูลเกม แต่เป็นการประยุกต์ใช้กระบวนการด้าน **Software Development + Data Processing + Data Analysis + Data Visualization** เข้าด้วยกัน

> **Gaming Statistics Dashboard — From Game Data to Interactive Insights.**

