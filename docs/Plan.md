# 🎮 Gaming Statistics Dashboard

# Project Development Plan

## 1. Project Information

**Project:** Gaming Statistics Dashboard  
**Course:** CP352301 Script Programming  
**Semester:** 1/2569  
**Domain:** Data Analysis & Management

---

# 2. Project Goal

เป้าหมายของโปรเจกต์ **Gaming Statistics Dashboard** คือการพัฒนา Python Application
สำหรับค้นหา สำรวจ และวิเคราะห์ข้อมูลวิดีโอเกม

ระบบจะถูกพัฒนาแบบ Incremental Development โดยแบ่งการพัฒนาออกเป็นหลาย Sprint
เริ่มจากการสร้างพื้นฐานของ Application ก่อน แล้วค่อยเพิ่ม Data Processing,
External API, Data Persistence, User Interface และ Testing ตามลำดับ

เป้าหมายสุดท้ายคือ Application ที่สามารถดึงข้อมูลเกมจากแหล่งข้อมูลภายนอก
นำข้อมูลมาประมวลผลและจัดเก็บ วิเคราะห์ข้อมูลทางสถิติ
และนำเสนอข้อมูลให้ผู้ใช้งานสามารถสำรวจได้อย่างสะดวก

---

# 3. Project Vision

Gaming Statistics Dashboard มีเป้าหมายให้ผู้ใช้งานสามารถ:

- ดูข้อมูลเกม
- ค้นหาเกม
- กรองและเรียงข้อมูลเกม
- สำรวจ Genre และ Platform
- ดูเกมที่มี Rating สูง
- วิเคราะห์ข้อมูลทางสถิติ
- ดูข้อมูลในรูปแบบ Visualization
- ใช้งานระบบผ่าน User Interface ที่เข้าใจง่าย

---

# 4. Planned Data Source

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

### RAWG

Website:  
https://rawg.io/

API:  
https://api.rawg.io/

---

# 5. Planned Final Architecture

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

Architecture นี้เป็นเป้าหมายของ Final Project
และจะถูกพัฒนาทีละส่วนตาม Scope ของแต่ละ Sprint

---

# 6. Planned Technology Stack

| Technology | Planned Usage |
|---|---|
| Python | Core Application |
| RAWG API | External Game Data |
| Pandas | Data Processing & Analysis |
| SQLite | Data Persistence |
| Matplotlib / Visualization Tools | Data Visualization |
| Streamlit | Final User Interface |
| pytest | Automated Testing |
| GitHub | Version Control & Collaboration |
| GitHub Actions | CI/CD & Automated Testing |

> Technology Stack สามารถปรับเปลี่ยนได้ตามผลการพัฒนาและข้อกำหนดของ Sprint ในอนาคต

---

# 7. Development Roadmap

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
Gaming Statistics Dashboard
```

---

# 8. Sprint 1 — CLI Foundation

## Sprint Goal

สร้างพื้นฐาน Command Line Interface (CLI)
สำหรับ Gaming Statistics Dashboard
ให้ผู้ใช้งานสามารถใช้งาน Feature พื้นฐาน
และระบบสามารถจัดการ Invalid Input ได้อย่างปลอดภัย

## Scope

### CLI Foundation
- Welcome Screen
- Main Menu
- Menu Navigation
- Main Application Loop
- Safe Exit

### Basic Features
- View Games
- Search Game
- View Statistics
- View Genres
- View Top Rated Games

### Input Validation
- Blank Input
- Non-numeric Input
- Invalid Menu Range
- Negative Input
- Empty Search
- Unknown Game
- Case-insensitive Search

### Data
ใช้ **Local Sample Dataset** จำนวน 8 เกม
เพื่อพัฒนาและทดสอบ Front-End CLI

### QA
ทดสอบทั้ง:

- Normal Cases
- Invalid Input
- Edge Cases
- Menu Navigation
- Search
- Safe Exit

---

## Sprint 1 Functional Requirements

### FR-01 — Welcome Screen
ระบบต้องแสดงชื่อ Gaming Statistics Dashboard เมื่อเริ่มต้นโปรแกรม

### FR-02 — Main Menu

```text
1. View Games
2. Search Game
3. View Statistics
4. View Genres
5. View Top Rated Games
0. Exit
```

### FR-03 — Menu Input
ผู้ใช้งานต้องสามารถเลือก Menu Option ตั้งแต่ `0–5`

### FR-04 — Input Validation
Invalid Input ต้องไม่ทำให้ Application Crash

### FR-05 — Search Game
ระบบต้องรองรับ:

- Partial Search
- Case-insensitive Search
- Empty Search Validation
- Unknown Game Handling

### FR-06 — Menu Navigation
เมื่อ Feature ทำงานเสร็จ ระบบต้องกลับ Main Menu ได้

### FR-07 — Safe Exit
เมื่อเลือก `0` โปรแกรมต้องจบการทำงานอย่างถูกต้อง

---

## Sprint 1 Definition of Done

- [x] CLI สามารถเริ่มทำงานได้
- [x] Welcome Screen ทำงานได้
- [x] Main Menu ทำงานได้
- [x] Menu Navigation ทำงานได้
- [x] View Games ทำงานได้
- [x] Search Game ทำงานได้
- [x] View Statistics ทำงานได้
- [x] View Genres ทำงานได้
- [x] View Top Rated Games ทำงานได้
- [x] Input Validation ทำงานได้
- [x] Invalid Input ไม่ทำให้โปรแกรม Crash
- [x] Search Validation ทำงานได้
- [x] Safe Exit ทำงานได้
- [x] Functions มีหน้าที่ชัดเจน
- [x] Functions สำคัญมี Docstring
- [x] QA Test Cases ถูกจัดทำ
- [x] Sprint Retrospective ถูกจัดทำ
- [x] Code พร้อมสำหรับ GitHub Submission

---

# 9. Sprint 2 — Data & Core Logic

## Sprint Goal

พัฒนาระบบจัดการข้อมูลและ Business Logic
ให้ Application สามารถทำงานกับข้อมูลเกมที่มีโครงสร้างมากขึ้น
และเพิ่มความสามารถในการค้นหา กรอง และเรียงข้อมูล

## Planned Scope

### Data Management
- กำหนด Data Structure สำหรับข้อมูลเกม
- เตรียมข้อมูลสำหรับการประมวลผล
- เพิ่ม File I/O
- Load / Save Data

### Search
พัฒนาระบบค้นหาให้รองรับข้อมูลและเงื่อนไขมากขึ้น

### Filter
วางแผนรองรับการกรอง เช่น:

- Genre
- Platform
- Rating

### Sort
วางแผนรองรับการเรียง เช่น:

- Rating
- Game Title
- Release Date

### Statistics
พัฒนา Statistics จาก Sprint 1 ให้รองรับข้อมูลจริงมากขึ้น เช่น:

- Total Games
- Average Rating
- Highest Rating
- Lowest Rating
- Genre Distribution
- Platform Distribution

---

## Sprint 2 Planned Definition of Done

- [ ] Data Structure ถูกกำหนดอย่างชัดเจน
- [ ] Application สามารถ Load Data ได้
- [ ] Application สามารถ Save Data ได้ตาม Scope
- [ ] Search ทำงานกับข้อมูลได้ถูกต้อง
- [ ] Filter ทำงานได้
- [ ] Sort ทำงานได้
- [ ] Statistics ทำงานกับข้อมูลที่พัฒนาใหม่ได้
- [ ] Error Handling ครอบคลุม File/Data Errors
- [ ] QA Test Cases ถูกจัดทำ
- [ ] Sprint Retrospective ถูกจัดทำ
- [ ] Code ถูกส่งผ่าน GitHub Workflow

---

# 10. Sprint 3 — Integration & Application Development

## Sprint Goal

เชื่อมส่วนประกอบหลักของ Gaming Statistics Dashboard
เข้าด้วยกัน และพัฒนา Application ให้ใกล้เคียง Final Architecture มากขึ้น

## Planned Scope

### RAWG API Integration
วางแผนเชื่อมต่อ RAWG API เพื่อดึงข้อมูลเกมจริง เช่น:

- Game Title
- Rating
- Genre
- Platform
- Release Date

### Data Processing
นำข้อมูลจาก API มาทำ:

- Data Cleaning
- Data Transformation
- Missing-value Handling
- Data Preparation

### Data Persistence
วางแผนใช้ SQLite สำหรับจัดเก็บข้อมูลเกม

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite
```

### Application Integration

เชื่อม:

```text
User Input
    ↓
Application Logic
    ↓
Processed Game Data
    ↓
Database
    ↓
Statistics
```

### Error Handling

รองรับกรณี เช่น:

- API Connection Error
- Invalid API Response
- Missing Data
- Database Error
- Empty Result
- Invalid User Input

---

## Sprint 3 Planned Definition of Done

- [ ] RAWG API สามารถเชื่อมต่อได้
- [ ] สามารถดึงข้อมูลเกมได้
- [ ] API Data ถูก Process ก่อนใช้งาน
- [ ] ข้อมูลสามารถจัดเก็บใน SQLite ได้
- [ ] Application Logic เชื่อมกับ Data Layer ได้
- [ ] Search / Filter / Sort ทำงานกับข้อมูลที่เชื่อมต่อแล้ว
- [ ] Statistics ทำงานกับข้อมูลที่เชื่อมต่อแล้ว
- [ ] Error Handling ครอบคลุม Integration Errors
- [ ] QA Test Cases ถูกจัดทำ
- [ ] Sprint Retrospective ถูกจัดทำ
- [ ] Code ถูกส่งผ่าน GitHub Workflow

---

# 11. Sprint Final — Final Integration & Delivery

## Sprint Goal

รวมระบบทั้งหมดให้เป็น Gaming Statistics Dashboard
เวอร์ชันสมบูรณ์ พร้อม User Interface, Visualization,
Testing และ Final Documentation

## Planned Scope

### User Interface

วางแผนพัฒนา User Interface ด้วย **Streamlit**

ตัวอย่าง Features:

- Game Dashboard
- Search
- Filter
- Sort
- Statistics
- Genre Analysis
- Platform Analysis
- Top Rated Games

### Data Visualization

วางแผนเพิ่ม Visualization เช่น:

- Rating Distribution
- Genre Distribution
- Platform Distribution
- Top Rated Games
- Statistical Summary

### Automated Testing

ใช้ `pytest` สำหรับทดสอบ Core Functions เช่น:

- Search
- Filter
- Sort
- Statistics
- Data Processing

### CI/CD

ใช้ GitHub Actions สำหรับ:

- Automated Tests
- Code Validation
- Continuous Integration

### Final Integration

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite
    ↓
Statistics & Analysis
    ↓
Streamlit Dashboard
```

---

## Sprint Final Planned Definition of Done

- [ ] Core Features ทำงานครบตาม Final Requirements
- [ ] RAWG API Integration ทำงานได้
- [ ] Data Processing ทำงานได้
- [ ] SQLite Persistence ทำงานได้
- [ ] Search / Filter / Sort ทำงานได้
- [ ] Statistics & Analysis ทำงานได้
- [ ] Visualization แสดงผลได้
- [ ] User Interface ทำงานได้
- [ ] Exception Handling ครอบคลุม Critical Cases
- [ ] Automated Tests ผ่าน
- [ ] GitHub Actions ทำงานได้
- [ ] Final Documentation เสร็จสมบูรณ์
- [ ] Final QA เสร็จสมบูรณ์
- [ ] Application พร้อมสำหรับ Final Demo

---

# 12. Sprint Summary

| Sprint | Main Focus | Status |
|---|---|---|
| Sprint 1 | CLI Foundation & Input Validation | Completed |
| Sprint 2 | Data & Core Logic | Planned |
| Sprint 3 | API, Persistence & Integration | Planned |
| Sprint Final | UI, Testing & Final Integration | Planned |

---

# 13. Team Roles

ทีมใช้แนวทาง Rotating Roles ในแต่ละ Sprint:

- **Planner**
- **Coder**
- **Debugger**

บทบาทสามารถสลับกันใน Sprint ถัดไปเพื่อให้สมาชิกแต่ละคนได้เรียนรู้กระบวนการพัฒนาซอฟต์แวร์ในหลายหน้าที่

### Sprint 1

| Role | Member |
|---|---|
| Planner | คิม |
| Coder | ฟลุ๊ค |
| Debugger | ออม |

บทบาทของ Sprint ถัดไปจะถูกกำหนดเมื่อเริ่ม Sprint นั้น

---

# 14. GitHub Workflow

แต่ละ Sprint จะใช้ GitHub สำหรับ Version Control และการส่งมอบงาน

Planned Workflow:

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

ตัวอย่าง Branch:

```text
main
├── sprint-1
├── sprint-2
├── sprint-3
└── sprint-final
```

---

# 15. Project Repository Structure

โครงสร้าง Repository ที่วางแผนไว้:

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
│   ├── Sprint1.ipynb
│   └── main.py
│
├── Sprint2/
│
├── Sprint3/
│
└── SprintFinal/
```

Folder และ Sprint Report ของ Sprint ถัดไปจะถูกเพิ่มเมื่อเริ่มพัฒนา Sprint นั้นจริง

---

# 16. Project Status

**Current Sprint: Sprint 1**

```text
Sprint 1      ██████████  Completed
Sprint 2      ░░░░░░░░░░  Planned
Sprint 3      ░░░░░░░░░░  Planned
Sprint Final  ░░░░░░░░░░  Planned
```

โปรเจกต์จะถูกพัฒนาต่อแบบ Incremental Development
โดย Scope ของ Sprint ในอนาคตสามารถปรับเปลี่ยนได้ตามผลการพัฒนา
Feedback และ Requirements ที่ได้รับในแต่ละ Sprint