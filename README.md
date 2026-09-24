# 🎮 Gaming Statistics Dashboard

> Final Term Project — CP352301 Script Programming

Gaming Statistics Dashboard เป็น Web Application สำหรับรวบรวมและแสดงข้อมูลเกม
โดยใช้ข้อมูลจริงจาก RAWG API และจัดเก็บข้อมูลผ่าน SQLite Database

โปรเจกต์นี้พัฒนาจาก CLI Application ใน Sprint 1
ไปสู่ Web Application ใน Sprint 2
เพื่อให้ผู้ใช้สามารถค้นหา ดูข้อมูล และสำรวจข้อมูลเกมผ่าน Web Browser ได้ง่ายขึ้น

---

## 📌 Project Overview

### Problem

ข้อมูลเกี่ยวกับเกม เช่น Rating, Genre, Platform, Release Date และ Metacritic Score
กระจายอยู่ในแหล่งข้อมูลต่าง ๆ ทำให้การค้นหาและเปรียบเทียบข้อมูลเกมทำได้ไม่สะดวก

### Proposed Solution

พัฒนา Gaming Statistics Dashboard ที่สามารถ:

- ดึงข้อมูลเกมจริงจาก RAWG API
- จัดการและ Normalize ข้อมูลจาก API
- จัดเก็บข้อมูลผ่าน SQLite Database
- ค้นหาและดูข้อมูลเกมผ่าน Web Browser
- แสดงข้อมูลเกมในรูปแบบ Dashboard
- แสดงข้อมูล Steam Player และ Live Players
- รองรับการ Filter และ Pagination
- จัดการกรณี API Error และข้อมูลไม่พร้อมใช้งาน

---

## 🎯 Project Goals

เป้าหมายของ Project คือการพัฒนา Python Application
ที่สามารถเชื่อมต่อ External API และ Database
พร้อมแสดงข้อมูลผ่าน Web Application

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
Data Processing + Analysis + Visualization
        ↓
Final Sprint
Testing + Final Integration + Presentation
````

---

## 🖥️ Application

ระบบเป็น **Web Application** ที่สามารถเปิดใช้งานผ่าน Web Browser

Framework หลัก:

* Streamlit

Application Flow:

```text
User
  ↓
Web Dashboard
  ↓
Search / Filter / View Games
  ↓
Game Service
  ↓
Data Processing
  ↓
API / SQLite Database
```

---

## ✨ Current Features

### 🎮 Game Library

แสดงรายการเกมจากข้อมูลที่ระบบจัดการไว้
พร้อมรองรับ Pagination เพื่อช่วยจัดการข้อมูลจำนวนมาก

### 🔎 Game Search

ค้นหาเกมจากชื่อเกมผ่าน Web Application

### ⭐ Top Rated Games

แสดงเกมที่มี Rating สูง

### 🎭 Genres

แสดงและจัดการข้อมูลเกมตาม Genre

### 🎯 Filters

รองรับการ Filter ข้อมูลเกมตาม:

* Genre
* Platform
* Minimum Rating

### 📊 Game Detail

แสดงรายละเอียดของเกม เช่น:

* Game Name
* Rating
* Release Date
* Genres
* Platforms
* Metacritic Score
* Ratings Count
* Image

### 👥 Live Players

เชื่อมต่อ Steam API เพื่อแสดงข้อมูลเกี่ยวกับ:

* Current Player Count
* Steam Top 100 / Live Players

ข้อมูล Steam Player อาจไม่มีสำหรับเกมบางรายการ
หากเกมนั้นไม่มีข้อมูลที่ระบบสามารถเชื่อมต่อได้

### 🔄 Refresh / Snapshot

มีระบบ Refresh และ Snapshot สำหรับข้อมูล Steam Player
เพื่อช่วยลดการเรียก API ซ้ำและจัดการข้อมูลที่มีการเปลี่ยนแปลงตลอดเวลา

### ⚠️ Error & Empty State

ระบบรองรับกรณี:

* API Error
* Database Error
* Missing Data
* Empty Search Result
* ข้อมูลบางส่วนไม่พร้อมใช้งาน

---

## 🛠️ Technologies

| Technology    | Purpose                 |
| ------------- | ----------------------- |
| Python        | Application Development |
| Streamlit     | Web Application / UI    |
| RAWG API      | Game Data               |
| Steam API     | Steam Player Data       |
| SQLite        | Data Persistence        |
| Pandas        | Data Processing         |
| pytest        | Automated Testing       |
| Git / GitHub  | Version Control         |
| python-dotenv | Environment Variables   |

---

## 🌐 APIs

### RAWG Video Games Database API

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

### Steam API

ใช้สำหรับข้อมูลที่เกี่ยวข้องกับ Steam
โดยเฉพาะข้อมูล Player Count และ Steam Top 100 / Live Players

---

## 🗄️ Database

Project ใช้ **SQLite** เป็น Database สำหรับจัดเก็บข้อมูล

Database File:

```text
data/gaming_statistics.db
```

Database ทำหน้าที่เป็นส่วนหนึ่งของ Data Flow:

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite Database
    ↓
Game Service
    ↓
Streamlit Web UI
```

---

## 🏗️ Project Structure

```text
Gaming-Statistics-Dashboard/
│
├── README.md
├── requirements.txt
├── .gitignore
├── .env
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
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── app.py
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── rawg_api.py
│   │   └── steam_api.py
│   │
│   ├── components/
│   │   ├── __init__.py
│   │   ├── dashboard.py
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
    ├── test_steam_api.py
    └── test_time_utils.py
```

---

## 🧩 Architecture

Project แบ่งระบบออกเป็น Module ตามหน้าที่
เพื่อให้ Code สามารถพัฒนา ทดสอบ และดูแลได้ง่ายขึ้น

### API Layer

รับผิดชอบการเชื่อมต่อ External API

```text
src/api/
├── rawg_api.py
└── steam_api.py
```

### Data Processing Layer

รับผิดชอบการจัดรูปแบบและ Normalize ข้อมูล

```text
src/utils/data_processing.py
```

### Database Layer

รับผิดชอบ SQLite Database

```text
src/database/database.py
```

### Service Layer

รับผิดชอบ Application Logic
และเป็นตัวกลางระหว่าง UI กับ API / Database

```text
src/services/game_service.py
```

### UI Layer

รับผิดชอบ Web Application และ Dashboard

```text
src/app.py
src/components/
```

---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd Gaming-Statistics-Dashboard
```

### 2. Create Virtual Environment

Windows:

```bash
python -m venv .venv
```

Activate:

```bash
.venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

สร้างไฟล์ `.env` จาก `.env.example`

ตัวอย่าง:

```env
RAWG_API_KEY=your_rawg_api_key
```

API Key ไม่ควรถูก Commit ลง GitHub

ไฟล์ `.env` ควรอยู่ใน `.gitignore`

---

## ▶️ Run Application

รัน Streamlit Application ด้วย:

```bash
streamlit run src/app.py
```

จากนั้นเปิด URL ที่ Streamlit แสดงใน Terminal
ผ่าน Web Browser

โดยทั่วไปจะเป็น:

```text
http://localhost:8501
```

---

## 🧪 Testing

Project ใช้ `pytest` สำหรับ Automated Testing

สามารถรัน Test Suite ด้วย:

```bash
pytest
```

Test ครอบคลุมส่วนสำคัญของระบบ เช่น:

* API
* Database
* Game Service
* Data Processing
* Time Utilities
* Dashboard

> หมายเหตุ: การทดสอบบางส่วนอาจขึ้นอยู่กับ Environment และ Dependencies
> ที่ติดตั้งในเครื่อง

---

## 🔐 API Key Security

API Key ถูกจัดการผ่าน Environment Variable
แทนการเขียน API Key ไว้โดยตรงใน Source Code

```text
.env
  ↓
Application
  ↓
API Request
```

ไม่ควรเผยแพร่ `.env` หรือ API Key ลงใน Public Repository

---

## 📚 Project Documentation

เอกสารของ Project อยู่ภายใน `docs/` และแต่ละ Sprint

```text
docs/
├── Project_Pitch.md
├── Plan.md
├── CHANGELOG.md
└── LEARNINGLOG.md

Sprint1/
└── Sprint_1.md

Sprint2/
└── Sprint_2.md
```

### Project Pitch

อธิบาย:

* Problem
* Proposed Solution
* Domain
* API
* Database
* Features
* Project Direction

### Plan

ใช้สำหรับ Project Roadmap และ Planning

### Change Log

บันทึกการเปลี่ยนแปลงของ Project ในแต่ละ Version / Sprint

### Learning Log

บันทึกสิ่งที่ทีมเรียนรู้:

* Technical Learning
* Problems
* Teamwork
* Lessons Learned
* Development Process

### Sprint Documentation

แต่ละ Sprint มีเอกสารอธิบาย:

* Sprint Goal
* Scope
* Tasks
* Development
* Testing
* Result
* Review

---

## 👥 Team

| Member               | Nickname | Role               |
| -------------------- | -------- | ------------------ |
| นายชิษณุพงศ์ ซู      | คิม      | Planner / Debugger |
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค    | Coder / Planner    |
| นายเดโชชิต โตวินัส   | ออม      | Debugger / Coder   |

Role มีการหมุนเวียนตาม Sprint
เพื่อให้สมาชิกได้เรียนรู้ทั้ง Planning, Development และ QA

### Sprint 1

| Member | Role          |
| ------ | ------------- |
| คิม    | Planner       |
| ฟลุ๊ค  | Coder         |
| ออม    | Debugger / QA |

### Sprint 2

| Member | Role          |
| ------ | ------------- |
| ฟลุ๊ค  | Planner       |
| ออม    | Coder         |
| คิม    | Debugger / QA |

---

## 🚀 Sprint Progress

| Sprint   | Focus                                      | Status      |
| -------- | ------------------------------------------ | ----------- |
| Sprint 1 | Application Foundation / CLI               | ✅ Completed |
| Sprint 2 | Web UI / API / Database                    | ✅ Completed |
| Sprint 3 | Data Processing / Analysis / Visualization | ⏳ Planned   |
| Final Sprint | Testing / Integration / Finalization       | ⏳ Planned   |

---

## 📈 Future Development

Features ต่อไปจะพัฒนาตาม Sprint ที่เหลือ เช่น:

* Data Cleaning
* Data Analysis
* Statistical Analysis
* Data Visualization
* Advanced Dashboard Features
* Additional Search / Filter / Sort
* Final Testing
* Final Integration
* Project Finalization

> Features ในส่วนนี้เป็นแผนสำหรับ Sprint ถัดไป
> และยังไม่ถือว่าเป็น Features ที่เสร็จสมบูรณ์ใน Version ปัจจุบัน

---

## 📄 Project Status

**Current Version:** Sprint 2

**Current Status:** ✅ Completed

ปัจจุบันระบบสามารถทำงานเป็น Web Application
เชื่อมต่อ RAWG API, Steam API และ SQLite Database
พร้อมมี Search, Filter, Pagination, Game Detail,
Top Rated, Genres และ Live Players

การพัฒนา Data Analysis และ Data Visualization
จะดำเนินการต่อใน Sprint ถัดไป

---

## 🎓 Course

**Course:** CP352301 Script Programming

**Project:** Gaming Statistics Dashboard

**Project Type:** Final Term Project

**Development Approach:**

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

---

