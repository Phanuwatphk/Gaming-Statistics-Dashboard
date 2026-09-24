# 📋 Gaming Statistics Dashboard — Project Plan

## Final Term Project — CP352301 Script Programming

---

# 1. Project Plan Overview

**Gaming Statistics Dashboard** เป็น Web Application สำหรับรวบรวม จัดการ วิเคราะห์ และนำเสนอข้อมูลเกี่ยวกับวิดีโอเกมผ่าน Dashboard โดยผู้ใช้สามารถเข้าถึงระบบผ่าน Web Browser

Project นี้พัฒนาโดยใช้แนวทาง **Incremental Development** โดยแบ่งการพัฒนาออกเป็นหลาย Sprint และเพิ่มความสามารถของระบบทีละส่วน

การวางแผนระดับ Project นี้ใช้สำหรับกำหนด:

- เป้าหมายของแต่ละ Sprint
- ขอบเขตงานในภาพรวม
- ลำดับการพัฒนา
- Deliverables หลัก
- กำหนดเวลา
- สถานะของแต่ละ Sprint

รายละเอียดการดำเนินงานของแต่ละ Sprint จะถูกจัดเก็บแยกไว้ในไฟล์ของ Sprint นั้น ๆ

---

# 2. Project Development Approach

Project ใช้แนวทางการพัฒนาแบบ Incremental Development

```text
Project Planning
      ↓
Sprint 1
      ↓
Review / Feedback
      ↓
Sprint 2
      ↓
Review / Feedback
      ↓
Sprint 3
      ↓
Review / Feedback
      ↓
Final Sprint
      ↓
Final Project
````

ในแต่ละ Sprint ทีมจะ:

1. กำหนดเป้าหมายของ Sprint
2. กำหนดขอบเขตงาน
3. พัฒนาและทดสอบระบบ
4. Review ผลลัพธ์
5. รับ Feedback
6. ปรับปรุงระบบและ Documentation
7. นำผลลัพธ์ไปใช้เป็นพื้นฐานของ Sprint ถัดไป

---

# 3. Project Timeline

| Sprint                      | ช่วงเวลา             | เป้าหมายหลัก                                       | Status      |
| --------------------------- | -------------------- | -------------------------------------------------- | ----------- |
| **Sprint 1**                | 10–15 September 2026 | Application Foundation และ CLI                     | ✅ Completed |
| **Sprint 2**                | 20–24 September 2026 | Web UI + API + SQLite + Backend Foundation         | ✅ Completed |
| **Sprint 3**                | Planned              | Data Analysis, Visualization และ Advanced Features | ⏳ Planned   |
| **Final Sprint** | Planned              | Testing, Integration, Final QA และ Final Project   | ⏳ Planned   |

> กำหนดการของแต่ละ Sprint อ้างอิงตามแนวทางและกำหนดการของรายวิชา

---

# 4. Sprint 1 — Application Foundation

## Objective

สร้าง Foundation ของ Gaming Statistics Dashboard
เพื่อเตรียมโครงสร้างพื้นฐานสำหรับพัฒนาเป็น Web Application ใน Sprint ถัดไป

## Main Scope

* Command Line Interface (CLI)
* Main Menu
* Menu Navigation
* User Input
* Input Validation
* Exception Handling
* Game Data Presentation
* Search
* Basic Statistics
* QA และ Edge Case Testing

## Main Deliverable

ระบบ CLI ที่สามารถทำงานได้และรองรับการใช้งานพื้นฐานของ Gaming Statistics Dashboard

## Data Source

ใช้ **Local Sample Dataset**

ยังไม่มีการเชื่อมต่อ RAWG API และ SQLite ใน Sprint นี้

## Status

**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 1:

`Sprint1/Sprint_1.md`

---

# 5. Sprint 2 — Web UI + API + Database

## Objective

พัฒนา Foundation จาก Sprint 1 ให้กลายเป็น Web Application
ที่สามารถใช้งานผ่าน Web Browser และสามารถแสดงข้อมูลจากแหล่งข้อมูลจริงได้

## Main Scope

### Web UI

พัฒนา Dashboard Interface ด้วย **Streamlit**

รองรับ:

* Web Dashboard
* Navigation
* Game Library
* Search
* Game Detail
* Top Rated Games
* Genres
* Live Players
* Pagination
* Empty State

### API Integration

เชื่อมต่อ **RAWG Video Games Database API**
เพื่อดึงข้อมูลเกมมาใช้งานจริง

ข้อมูลที่นำมาใช้ เช่น:

* Game Name
* Rating
* Released Date
* Genres
* Platforms
* Metacritic Score
* Ratings Count
* Image

นอกจากนี้ยังเชื่อมต่อ **Steam API**
สำหรับข้อมูลเกี่ยวกับ Current Player Count และ Steam Top 100 / Live Players

### Data Processing

เพิ่ม Data Processing และ Data Normalization
เพื่อจัดรูปแบบข้อมูลจาก API ก่อนนำไปใช้งานใน Application

### Database

เพิ่ม **SQLite Database**
สำหรับจัดเก็บและจัดการข้อมูลเกม

### Service Layer

เพิ่ม **Game Service**
เพื่อจัดการ Application Logic และเป็นตัวกลางระหว่าง UI,
Data Processing, API และ Database

### Filtering

รองรับการ Filter ข้อมูลเกมตาม:

* Genre
* Platform
* Minimum Rating

### Live Player Data

แสดงจำนวนผู้เล่นปัจจุบันจาก Steam
สำหรับเกมที่สามารถจับคู่ Steam App ID ได้

มีการจัดเก็บข้อมูลและเวลาอัปเดตไว้ใน SQLite
พร้อมระบบ Refresh และ Snapshot เพื่อลดการเรียก API ซ้ำ

### Testing

เพิ่ม Automated Tests สำหรับส่วนสำคัญของระบบ เช่น:

* API
* Database
* Game Service
* Data Processing
* Time Utilities
* Dashboard

## Main Deliverable

Web Dashboard ที่สามารถ:

* เปิดใช้งานผ่าน Web Browser
* แสดงข้อมูลเกมจริง
* ดึงข้อมูลจาก RAWG API
* เชื่อมต่อ Steam API
* เชื่อมต่อ SQLite
* ประมวลผลและ Normalize ข้อมูล
* ค้นหาเกม
* Filter เกม
* แสดงรายละเอียดเกม
* แสดง Top Rated Games
* แสดง Steam Live Players
* รองรับ Pagination
* จัดการ API Error และ Empty State

## Status

**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 2:

`Sprint2/Sprint_2.md`

---

# 6. Sprint 3 — Data Analysis & Visualization

## Objective

นำข้อมูลเกมที่ได้จาก Sprint 2
มาพัฒนาเป็นส่วนของ Data Analysis และ Data Visualization
เพื่อเพิ่มความสามารถในการวิเคราะห์และนำเสนอข้อมูลบน Dashboard

## Main Scope

* Data Cleaning
* Data Processing เพิ่มเติม
* Exploratory Data Analysis (EDA)
* Statistical Analysis
* Data Visualization
* Dashboard Statistics
* Data Comparison
* Advanced Filtering
* Advanced Sorting
* Data Consistency
* Integration Testing

## Main Deliverable

ระบบ Gaming Statistics Dashboard
ที่สามารถนำข้อมูลเกมมาวิเคราะห์และแสดงผลในรูปแบบ Visualization
เพื่อช่วยให้ผู้ใช้สามารถสำรวจและทำความเข้าใจข้อมูลได้ง่ายขึ้น

ตัวอย่าง Data Flow:

```text
Web UI
   ↓
Game Service
   ↓
Data Processing
   ↓
Statistics / Analysis
   ↓
Visualization
   ↓
Dashboard
```

## Status

**⏳ Planned**

รายละเอียดการดำเนินงานของ Sprint 3:

`Sprint3/Sprint_3.md`

---

# 7. Final Sprint

## Objective

เตรียม Project ให้พร้อมสำหรับ Final Project
และการส่งมอบระบบ

## Main Scope

* Automated Testing
* pytest
* GitHub Actions
* CI/CD
* Final Integration
* Final QA
* Bug Fixing
* Performance / Reliability Checking
* Final Documentation
* Final Presentation

## Main Deliverable

Gaming Statistics Dashboard เวอร์ชัน Final
ที่ผ่านการทดสอบและเตรียมพร้อมสำหรับการนำเสนอและส่งมอบ

## Status

**⏳ Planned**

รายละเอียดการดำเนินงานของ Final Sprint:

`Final Sprint/`

---

# 8. Project Technology Roadmap

| Technology         | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
| ------------------ | -------- | -------- | -------- | -------- |
| Python             | ✅        | ✅        | ✅        | ✅        |
| CLI                | ✅        | -        | -        | -        |
| Streamlit          | -        | ✅        | ✅        | ✅        |
| RAWG API           | -        | ✅        | ✅        | ✅        |
| Steam API          | -        | ✅        | ✅        | ✅        |
| Pandas             | -        | ✅        | ✅        | ✅        |
| SQLite             | -        | ✅        | ✅        | ✅        |
| Data Processing    | -        | ✅        | ✅        | ✅        |
| Data Visualization | -        | -        | Planned  | ✅        |
| pytest             | -        | ✅        | ✅        | ✅        |
| GitHub Actions     | -        | -        | -        | Planned  |
| CI/CD              | -        | -        | -        | Planned  |
| AI Integration     | -        | -        | -        | Planned  |

> เครื่องมือที่ยังไม่ถึง Sprint ของตัวเองจะยังไม่ถือว่าเป็นงานที่ดำเนินการเสร็จแล้ว

---

# 9. Project Deliverables Roadmap

| Deliverable                            | Sprint   |
| -------------------------------------- | -------- |
| Project Pitch                          | Sprint 1 |
| Project Plan                           | Sprint 1 |
| CLI Foundation                         | Sprint 1 |
| Sprint 1 Documentation                 | Sprint 1 |
| Web Dashboard                          | Sprint 2 |
| RAWG API Integration                   | Sprint 2 |
| Steam API Integration                  | Sprint 2 |
| SQLite Database                        | Sprint 2 |
| Game Service                           | Sprint 2 |
| Data Processing / Normalization        | Sprint 2 |
| Search / Filter / Pagination           | Sprint 2 |
| Game Detail / Top Rated / Live Players | Sprint 2 |
| Automated Tests — Initial Test Suite   | Sprint 2 |
| Data Analysis / EDA                    | Sprint 3 |
| Statistics & Visualization             | Sprint 3 |
| Advanced Filtering / Sorting           | Sprint 3 |
| Integration Testing                    | Sprint 3 |
| Final QA                               | Final Sprint |
| GitHub Actions / CI/CD                 | Final Sprint |
| AI Integration                         | Final Sprint |
| Final Documentation                    | Fianl Sprint |
| Final Presentation                     | Final Sprint |

---

# 10. Project Documentation Structure

Documentation ของ Project จะแยกตามระดับของข้อมูล

```text
Gaming-Statistics-Dashboard/
│
├── README.md
│
├── docs/
│   ├── Project_Pitch.md
│   ├── Plan.md
│   ├── CHANGELOG.md
│   └── LEARNINGLOG.md
│
├── src/
│   ├── ...
│   └── ...
│
├── tests/
│   ├── ...
│   └── ...
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
└── Final Sprint/
    └── ...
```

### Documentation Responsibilities

| File / Folder           | Purpose                                               |
| ----------------------- | ----------------------------------------------------- |
| `README.md`             | ภาพรวมของ Project และ Current Status                  |
| `docs/Project_Pitch.md` | แนวคิด Problem, Solution, Technology และ Architecture |
| `docs/Plan.md`          | แผนการพัฒนาโดยรวมของ Project และทุก Sprint            |
| `docs/CHANGELOG.md`     | บันทึกการเปลี่ยนแปลงของ Project                       |
| `docs/LEARNINGLOG.md`   | บันทึกสิ่งที่ทีมเรียนรู้ระหว่างการพัฒนา               |
| `Sprint1/Sprint_1.md`   | รายละเอียดการดำเนินงานและผลลัพธ์ของ Sprint 1          |
| `Sprint2/Sprint_2.md`   | รายละเอียดการดำเนินงานและผลลัพธ์ของ Sprint 2          |
| `Sprint3/`              | รายละเอียดการดำเนินงานของ Sprint 3                    |
| `Final Sprint/`              | รายละเอียดการดำเนินงานของ Final Sprint                    |
| `src/`                  | Source Code ของ Application                           |
| `tests/`                | Automated Tests ของ Project                           |

---

# 11. Team Planning

ทีมมีสมาชิก 3 คน และใช้ Role Rotation
ในการแบ่งความรับผิดชอบในแต่ละ Sprint

## Team Members

| Member               | Nickname |
| -------------------- | -------- |
| นายชิษณุพงศ์ ซู      | คิม      |
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค    |
| นายเดโชชิต โตวินัส   | ออม      |

## Sprint 1 Roles

| Member    | Role          | Main Responsibility                        |
| --------- | ------------- | ------------------------------------------ |
| **คิม**   | Planner       | Planning, Requirements และ Documentation   |
| **ฟลุ๊ค** | Coder         | Application Development และ Implementation |
| **ออม**   | Debugger / QA | Testing, QA และ Bug Verification           |

## Sprint 2 Roles

| Member    | Role          | Main Responsibility                                    |
| --------- | ------------- | ------------------------------------------------------ |
| **ฟลุ๊ค** | Planner       | Planning, Requirements, Architecture และ Documentation |
| **ออม**   | Coder         | Web UI, API, Database, Service และ Data Processing     |
| **คิม**   | Debugger / QA | Testing, QA, Error Handling และ Edge Cases             |

การแบ่งงานแบบละเอียดของแต่ละ Sprint
จะถูกระบุในไฟล์ Sprint ของ Sprint นั้น ๆ

ตัวอย่าง:

```text
Sprint1/Sprint_1.md
        ↓
Sprint 1 Team Tasks

Sprint2/Sprint_2.md
        ↓
Sprint 2 Team Tasks

Sprint3/Sprint_3.md
        ↓
Sprint 3 Team Tasks

Final Sprint/
        ↓
Final Sprint Team Tasks
```

---

# 12. Sprint Status

## Current Project Status

| Sprint   | Status      |
| -------- | ----------- |
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ⏳ Planned   |
| Final Sprint | ⏳ Planned   |

### Current Stage

**Sprint 1 Completed → Sprint 2 Completed → Preparing for Sprint 3**

Sprint 1 ได้พัฒนา Application Foundation และ CLI เรียบร้อยแล้ว

Sprint 2 ได้พัฒนา Web Application
พร้อม RAWG API, Steam API, SQLite Database,
Data Processing, Game Service และ Web Dashboard Features

ขั้นตอนถัดไปของ Project คือการนำข้อมูลและระบบจาก Sprint 2
ไปพัฒนา Data Analysis, Statistics และ Data Visualization ใน Sprint 3

---

# 13. Plan Maintenance

`Plan.md` เป็นเอกสารระดับ Project และจะถูกปรับปรุงเมื่อ Project มีการเปลี่ยนแปลงที่สำคัญ เช่น

* เปลี่ยน Scope ของ Project
* เปลี่ยน Technology
* เปลี่ยน Sprint Timeline
* เปลี่ยนเป้าหมายของ Sprint
* ได้รับ Feedback ที่ส่งผลต่อ Project Direction
* เพิ่มหรือลด Major Feature
* เปลี่ยนแปลงจากผลการพัฒนาใน Sprint ก่อนหน้า

รายละเอียดการเปลี่ยนแปลงแต่ละครั้งจะถูกบันทึกเพิ่มเติมใน:

`docs/CHANGELOG.md`

ส่วนสิ่งที่ทีมเรียนรู้จากการพัฒนา
จะถูกบันทึกใน:

`docs/LEARNINGLOG.md`

---

# 14. Planning Principle

Project จะไม่ถือว่างานของ Sprint ถัดไปเป็นงานที่เสร็จแล้ว
จนกว่าจะมีการพัฒนาและตรวจสอบจริงใน Sprint นั้น

ดังนั้น Status จะใช้หลัก:

* **✅ Completed** — พัฒนาและตรวจสอบแล้ว
* **🔄 In Progress** — อยู่ระหว่างการพัฒนา
* **⏳ Planned** — วางแผนไว้แต่ยังไม่ได้เริ่ม
* **❌ Cancelled** — ยกเลิกจาก Project Scope

การวางแผนจะถูกปรับตามผลการดำเนินงานและ Feedback
ที่ได้รับในแต่ละ Sprint
