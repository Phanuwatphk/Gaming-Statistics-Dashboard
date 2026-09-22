# 🎮 Gaming Statistics Dashboard

> Final Term Project — CP352301 Script Programming

**Gaming Statistics Dashboard** เป็น Python Application สำหรับค้นหา สำรวจ
และวิเคราะห์ข้อมูลเกี่ยวกับวิดีโอเกม โดยโปรเจกต์ถูกพัฒนาแบบ Incremental Development
ผ่านหลาย Sprint ตั้งแต่ CLI Foundation ไปจนถึงการเชื่อมต่อข้อมูลจริง
การวิเคราะห์ข้อมูล และ User Interface สำหรับ Final Project

---

## 📌 Project Overview

ข้อมูลเกี่ยวกับวิดีโอเกม เช่น Rating, Genre, Platform และ Release Date
มีอยู่เป็นจำนวนมาก ทำให้การค้นหา สำรวจ และเปรียบเทียบข้อมูลเกม
จากข้อมูลจำนวนมากทำได้ไม่สะดวก

Gaming Statistics Dashboard จึงถูกพัฒนาขึ้นเพื่อช่วยให้ผู้ใช้งานสามารถ:

- 🎮 ดูข้อมูลเกม
- 🔎 ค้นหาเกม
- 🗂️ สำรวจ Genre และ Platform
- ⭐ ดู Rating และเกมที่มี Rating สูง
- ↕️ Filter และ Sort ข้อมูล
- 📊 วิเคราะห์ข้อมูลทางสถิติ
- 📈 ดูข้อมูลผ่าน Data Visualization
- 🖥️ ใช้งานผ่าน User Interface ที่เข้าใจง่าย

---

## 🎯 Project Goal

เป้าหมายของโปรเจกต์คือการพัฒนา Application ที่สามารถนำข้อมูลวิดีโอเกม
มาจัดการ ประมวลผล วิเคราะห์ และนำเสนอในรูปแบบที่ผู้ใช้งานสามารถสำรวจได้ง่าย

โปรเจกต์จะถูกพัฒนาทีละส่วนในแต่ละ Sprint
โดยเริ่มจาก CLI Foundation ก่อน แล้วจึงเพิ่ม Data Processing,
External API, Data Persistence, Visualization และ User Interface ตามลำดับ

---

## 🌐 Planned Data Source

โปรเจกต์มีแผนที่จะใช้ **RAWG Video Games Database API**
เป็นแหล่งข้อมูลเกมภายนอกหลัก

ข้อมูลที่วางแผนจะนำมาใช้ เช่น:

- Game Title
- Rating
- Release Date
- Genre
- Platform
- Metacritic Score
- Game Images
- Related Game Information

**RAWG Website:**  
https://rawg.io/

**RAWG API:**  
https://api.rawg.io/

> **Current Status:** Sprint 1 ยังใช้ Local Sample Dataset
> และยังไม่ได้เชื่อมต่อ RAWG API จริง

---

## 🏗️ Planned Final Architecture

```text
RAWG API
    ↓
Data Collection
    ↓
Data Processing
    ↓
SQLite Database
    ↓
Statistics & Analysis
    ↓
User Interface
```

> Architecture นี้เป็นเป้าหมายสำหรับ Final Project
> และจะถูกพัฒนาทีละส่วนตาม Scope ของแต่ละ Sprint

---

## 🛠️ Technology Stack

### Current

เทคโนโลยีที่ใช้งานแล้ว:

- Python
- Google Colab / Jupyter Notebook
- Git
- GitHub

### Planned

เทคโนโลยีที่วางแผนจะเพิ่มใน Sprint ถัดไป:

- RAWG API
- Pandas
- SQLite
- Data Visualization
- Streamlit
- pytest
- GitHub Actions

---

# 🚀 Development Roadmap

โปรเจกต์แบ่งการพัฒนาออกเป็น 4 ช่วงหลัก:

```text
Sprint 1
CLI Foundation
      ↓
Sprint 2
Data & Core Logic
      ↓
Sprint 3
Integration & Application Development
      ↓
Sprint Final
Testing, UI & Final Integration
      ↓
🎮 Gaming Statistics Dashboard
```

---

## 📊 Project Status

| Sprint | Main Focus | Status |
|---|---|---|
| **Sprint 1** | CLI Foundation & Input Validation | ✅ Completed |
| **Sprint 2** | Data & Core Logic | ⏳ Planned |
| **Sprint 3** | API, Persistence & Integration | ⏳ Planned |
| **Sprint Final** | UI, Testing & Final Integration | ⏳ Planned |

### Current Progress

```text
Sprint 1      ██████████  Completed
Sprint 2      ░░░░░░░░░░  Planned
Sprint 3      ░░░░░░░░░░  Planned
Sprint Final  ░░░░░░░░░░  Planned
```

**Current Sprint Status:** Sprint 1 Completed ✅

---

# ✅ Sprint 1 — CLI Foundation

Sprint 1 มุ่งเน้นการสร้างพื้นฐาน Front-End CLI
ของ Gaming Statistics Dashboard

### Implemented Features

- ✅ Welcome Screen
- ✅ Main Menu
- ✅ Menu Navigation
- ✅ View Games
- ✅ Search Game
- ✅ View Statistics
- ✅ View Genres
- ✅ View Top Rated Games
- ✅ Input Validation
- ✅ Exception Handling
- ✅ Case-insensitive Search
- ✅ Safe Exit
- ✅ QA & Edge-case Testing

### Sprint 1 Menu

```text
1. View Games
2. Search Game
3. View Statistics
4. View Genres
5. View Top Rated Games
0. Exit
```

Sprint 1 ใช้ **Local Sample Dataset จำนวน 8 เกม**
เพื่อพัฒนาและทดสอบ CLI ก่อนการเชื่อมต่อข้อมูลจริงใน Sprint ถัดไป

### QA Result

```text
Total Test Cases : 14
Passed           : 14
Failed           : 0
Critical Defects : 0
```

**Sprint 1 Result: ✅ PASS**

---

# 🚧 Sprint 2 — Web UI + API + Database

**Status: In progress**

Sprint 2 เพิ่ม Web Dashboard ตาม `docs/Plan.md` แล้ว:

- Streamlit dashboard สำหรับแสดง/ค้นหาข้อมูลเกม โดยค้นหา RAWG เพื่อเพิ่มเกมที่ยังไม่มีในคลังได้
- RAWG API client ที่อ่าน key จาก `RAWG_API_KEY`
- SQLite สำหรับเก็บข้อมูลเกมที่ดึงจาก API และแสดงข้อมูลที่เก็บไว้ได้ในครั้งถัดไป
- จำนวนผู้เล่นปัจจุบันบน Steam สำหรับเกมที่จับคู่ Steam ได้ พร้อมเวลาอัปเดตล่าสุด

## Run Sprint 2

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
# ใส่ RAWG API key ของคุณใน .env
streamlit run src/app.py
```

ฐานข้อมูลเริ่มต้นอยู่ที่ `data/gaming_statistics.db` และจะไม่ถูก commit. สามารถเปลี่ยนตำแหน่งได้ด้วยตัวแปร `GAMING_DASHBOARD_DB`.

เมื่อผู้ใช้เปิด Dashboard ระบบจะตรวจและอัปเดต Top 50 เกมที่มีผู้เล่นสูงสุดจาก Steam ลงฐานข้อมูลกลาง โดยค่าเริ่มต้นจะใช้ข้อมูลร่วมกันไม่เกิน 15 นาที (`PLAYER_REFRESH_MINUTES=15`) เพื่อไม่เรียก API ซ้ำเมื่อมีผู้ใช้หลายคนเข้าพร้อมกัน. เกมที่ผู้ใช้ค้นหาจะถูกเพิ่มเข้า SQLite แยกต่างหากเพื่อใช้งานในภายหลัง.

รัน automated tests ได้ด้วย `python -m pytest -q` หลังจาก activate virtual environment.

---

# ⏳ Sprint 3 — Integration & Application Development

**Status: Planned**

แผนเบื้องต้น:

- RAWG API Integration
- Data Processing
- Data Cleaning
- SQLite Persistence
- Application Integration
- Integration Error Handling

รายละเอียดของ Scope สามารถปรับเปลี่ยนได้เมื่อเริ่ม Sprint 3

---

# ⏳ Sprint Final — Final Integration & Delivery

**Status: Planned**

แผนเบื้องต้น:

- Streamlit User Interface
- Data Visualization
- Final Integration
- Automated Testing with pytest
- GitHub Actions
- Final QA
- Final Documentation
- Final Demo

---

# 📂 Repository Structure

```text
Gaming-Statistics-Dashboard/
│
├── README.md
│
├── docs/
│   ├── PROJECT_PITCH.md
│   ├── PLAN.md
│   └── SPRINT_1.md
│
└── Sprint1/
    ├── Sprint1.ipynb
    └── main.py
```

Folder และ Sprint Report ของ Sprint ถัดไปจะถูกเพิ่มเมื่อเริ่มพัฒนา Sprint นั้นจริง

ตัวอย่างในอนาคต:

```text
Gaming-Statistics-Dashboard/
│
├── README.md
│
├── docs/
│   ├── PROJECT_PITCH.md
│   ├── PLAN.md
│   ├── SPRINT_1.md
│   ├── SPRINT_2.md
│   ├── SPRINT_3.md
│   └── SPRINT_FINAL.md
│
├── Sprint1/
├── Sprint2/
├── Sprint3/
└── SprintFinal/
```

---

# 📖 Documentation

เอกสารหลักของโปรเจกต์อยู่ใน `docs/`

| Document | Description |
|---|---|
| `PROJECT_PITCH.md` | Problem, Solution, Data Source และ Project Vision |
| `PLAN.md` | Development Plan ตั้งแต่ Sprint 1 จนถึง Sprint Final |
| `SPRINT_1.md` | Sprint 1 Implementation, QA Result และ Retrospective |

เอกสารของ Sprint ถัดไปจะถูกเพิ่มเมื่อ Sprint นั้นเริ่มพัฒนา

---

# ▶️ How to Run Sprint 1

## Option 1 — Jupyter Notebook / Google Colab

เปิดไฟล์:

```text
Sprint1/Sprint1.ipynb
```

Run Code Cells ตามลำดับ และรัน:

```python
main()
```

## Option 2 — Python

Clone Repository:

```bash
git clone https://github.com/Phanuwatphk/Gaming-Statistics-Dashboard.git
```

เข้าไปยัง Project Directory:

```bash
cd Gaming-Statistics-Dashboard
```

Run Sprint 1:

```bash
python Sprint1/main.py
```

> ต้องติดตั้ง Python 3 ก่อนใช้งาน

---

# 👥 Team

| Role — Sprint 1 | Member |
|---|---|
| Planner | คิม |
| Coder | ฟลุ๊ค |
| Debugger | ออม |

โปรเจกต์ใช้แนวทาง **Rotating Roles**
โดยสมาชิกสามารถสลับบทบาท Planner, Coder และ Debugger
ใน Sprint ถัดไป

---

# 🔄 Development Workflow

```text
Planning
    ↓
Create Sprint Branch
    ↓
Development
    ↓
Testing & Debugging
    ↓
Push to GitHub
    ↓
Pull Request
    ↓
Review
    ↓
Merge
```

แต่ละ Sprint จะถูกพัฒนาและตรวจสอบแยกกัน
ก่อน Merge เข้าสู่ Main Branch

---

# 📝 Current Project Status

> **Current Stage: Sprint 1 Completed ✅**

CLI Foundation ของ Gaming Statistics Dashboard
ได้รับการพัฒนาและทดสอบเรียบร้อยแล้ว

ขั้นตอนถัดไปของโปรเจกต์คือ **Sprint 2 — Data & Core Logic**
ซึ่งจะต่อยอดจาก CLI Foundation ที่สร้างไว้ใน Sprint 1

---

## 📚 Course Information

**Course:** CP352301 Script Programming  
**Semester:** 1/2569  
**Project:** Gaming Statistics Dashboard
