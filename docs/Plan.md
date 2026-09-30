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

Project ใช้แนวทางการพัฒนาแบบ **Incremental Development**

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

แนวทางนี้ช่วยให้ทีมสามารถพัฒนา Project ทีละส่วน
และสามารถตรวจสอบผลลัพธ์ของแต่ละช่วงก่อนขยาย Scope
ไปยัง Sprint ถัดไป

---

# 3. Project Timeline

| Sprint           | ช่วงเวลา             | เป้าหมายหลัก                                       | Status      |
| ---------------- | -------------------- | -------------------------------------------------- | ----------- |
| **Sprint 1**     | 10–15 September 2026 | Application Foundation และ CLI                     | ✅ Completed |
| **Sprint 2**     | 20–24 September 2026 | Web UI + API + SQLite + Backend Foundation         | ✅ Completed |
| **Sprint 3**     | 25–29 September 2026 | Data Analysis, Visualization และ Advanced Features | ✅ Completed |
| **Final Sprint** | Planned              | Final Integration, Final QA และ Final Project      | ⏳ Planned   |


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

# 6. Sprint 3 — Data Analysis, Visualization & Advanced Features

## Objective

นำข้อมูลเกมที่ได้จาก Sprint 2
มาพัฒนาเป็นส่วนของ Data Analysis และ Data Visualization
เพื่อเพิ่มความสามารถในการวิเคราะห์และนำเสนอข้อมูลบน Dashboard

พร้อมเพิ่มความสามารถในการสำรวจข้อมูลผ่าน:

* Advanced Filtering
* Advanced Sorting
* Game Comparison
* Data Consistency
* Integration Testing

## Main Scope

### Data Preparation

* Data Cleaning
* Data Processing เพิ่มเติม
* Data Normalization
* Data Validation
* การจัดการ Missing / Optional Values

### Data Analysis

* Exploratory Data Analysis (EDA)
* Descriptive Statistics
* Summary Statistics
* Genre Analysis
* Platform Analysis
* Rating Analysis
* Release Year Analysis
* Metacritic Analysis
* Steam Live Player Analysis

### Statistics

รองรับสถิติเชิงพรรณนา เช่น:

* Count
* Mean
* Median
* Minimum
* Maximum
* Standard Deviation

### Data Visualization

เพิ่ม Visualization สำหรับ:

* Genre Distribution
* Platform Distribution
* Rating by Genre
* Release Year Distribution
* Metacritic Score Distribution
* Top Live Steam Players

### Advanced Filtering

รองรับการ Filter เพิ่มเติมตาม:

* Genre
* Platform
* Minimum Rating
* Release Year

### Advanced Sorting

รองรับการ Sort ตาม:

* Rating
* Release Date
* Game Name

พร้อมรองรับ:

* Ascending
* Descending

และการจัดการ Missing Values ที่เกี่ยวข้องกับการ Sort

### Game Comparison

เพิ่มความสามารถในการเปรียบเทียบข้อมูลของเกม
โดยใช้ข้อมูลที่ระบบรองรับ เช่น:

* Rating
* Metacritic Score
* Steam Players

### Dashboard Integration

เชื่อม Analysis และ Visualization
เข้ากับ Dashboard เพื่อให้ข้อมูลที่ผู้ใช้เห็น
สอดคล้องกับข้อมูลที่ผ่าน Data Processing

### Empty State

รองรับกรณีที่ Filter แล้วไม่มีข้อมูลที่ตรงกับเงื่อนไข
เพื่อไม่ให้ Dashboard แสดงผลผิดพลาด

### Testing

ทดสอบ:

* Data Processing
* Statistical Analysis
* Visualization
* Filtering
* Sorting
* Game Comparison
* Dashboard Integration
* Empty State
* Regression Cases

## Main Deliverable

ระบบ Gaming Statistics Dashboard
ที่สามารถนำข้อมูลเกมมาวิเคราะห์และแสดงผลในรูปแบบ Statistics
และ Visualization พร้อมความสามารถในการ Filter, Sort
และเปรียบเทียบข้อมูลเกม

ตัวอย่าง Data Flow:

```text
API / SQLite
      ↓
Data Processing
      ↓
Data Preparation
      ↓
Statistics / Analysis
      ↓
Visualization
      ↓
Dashboard
```

## Sprint 3 Timeline

Sprint 3 ดำเนินงานเป็นระยะเวลา 5 วัน:

| วันที่            | Focus                            |
| ----------------- | -------------------------------- |
| 25 September 2026 | Planning & Technical Preparation |
| 26 September 2026 | Data Processing & Analysis       |
| 27 September 2026 | Statistics & Visualization       |
| 28 September 2026 | Advanced Features & Integration  |
| 29 September 2026 | Final QA & Documentation         |

## Status

**✅ Completed**

รายละเอียดการดำเนินงานของ Sprint 3:

`Sprint3/Sprint_3.md`

---

# 7. Final Sprint

## Objective

เตรียม Project ให้พร้อมสำหรับ Final Project
และการส่งมอบระบบ

## Main Scope

* Final Integration
* Final QA
* Regression Testing
* Bug Fixing
* Performance / Reliability Checking
* Automated Testing
* pytest
* GitHub Actions
* CI/CD
* Final Documentation
* Final Presentation

> งานใน Final Sprint จะเริ่มดำเนินการตาม Scope
> เมื่อเข้าสู่ Sprint สุดท้ายของ Project

## Main Deliverable

Gaming Statistics Dashboard เวอร์ชัน Final
ที่ผ่านการทดสอบและเตรียมพร้อมสำหรับการนำเสนอและส่งมอบ

## Status

**⏳ Planned**

รายละเอียดการดำเนินงานของ Final Sprint:

`Final Sprint/`

---

# 8. Project Technology Roadmap

| Technology          | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
| ------------------- | -------- | -------- | -------- | ------------ |
| Python              | ✅        | ✅        | ✅        | ✅            |
| CLI                 | ✅        | -        | -        | -            |
| Streamlit           | -        | ✅        | ✅        | ✅            |
| RAWG API            | -        | ✅        | ✅        | ✅            |
| Steam API           | -        | ✅        | ✅        | ✅            |
| Pandas              | -        | ✅        | ✅        | ✅            |
| SQLite              | -        | ✅        | ✅        | ✅            |
| Data Processing     | -        | ✅        | ✅        | ✅            |
| Data Analysis / EDA | -        | -        | ✅        | ✅            |
| Statistics          | -        | -        | ✅        | ✅            |
| Data Visualization  | -        | -        | ✅        | ✅            |
| Advanced Filtering  | -        | -        | ✅        | ✅            |
| Advanced Sorting    | -        | -        | ✅        | ✅            |
| Game Comparison     | -        | -        | ✅        | ✅            |
| pytest              | -        | ✅        | ✅        | ✅            |
| GitHub Actions      | -        | -        | -        | Planned      |
| CI/CD               | -        | -        | -        | Planned      |
| AI Integration      | -        | -        | -        | Planned      |

> เครื่องมือหรือ Features ที่ยังไม่ถึง Sprint ของตัวเอง
> จะยังไม่ถือว่าเป็นงานที่ดำเนินการเสร็จแล้ว

---

# 9. Project Deliverables Roadmap

| Deliverable                            | Sprint       |
| -------------------------------------- | ------------ |
| Project Pitch                          | Sprint 1     |
| Project Plan                           | Sprint 1     |
| CLI Foundation                         | Sprint 1     |
| Sprint 1 Documentation                 | Sprint 1     |
| Web Dashboard                          | Sprint 2     |
| RAWG API Integration                   | Sprint 2     |
| Steam API Integration                  | Sprint 2     |
| SQLite Database                        | Sprint 2     |
| Game Service                           | Sprint 2     |
| Data Processing / Normalization        | Sprint 2     |
| Search / Filter / Pagination           | Sprint 2     |
| Game Detail / Top Rated / Live Players | Sprint 2     |
| Automated Tests — Initial Test Suite   | Sprint 2     |
| Data Analysis / EDA                    | Sprint 3     |
| Statistics                             | Sprint 3     |
| Data Visualization                     | Sprint 3     |
| Advanced Filtering                     | Sprint 3     |
| Advanced Sorting                       | Sprint 3     |
| Game Comparison                        | Sprint 3     |
| Integration Testing                    | Sprint 3     |
| Final Integration                      | Final Sprint |
| Final QA                               | Final Sprint |
| Regression Testing                     | Final Sprint |
| GitHub Actions / CI/CD                 | Final Sprint |
| AI Integration                         | Final Sprint |
| Final Documentation                    | Final Sprint |
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
│   └── Sprint_3.md
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
| `Sprint3/Sprint_3.md`   | รายละเอียดการดำเนินงานและผลลัพธ์ของ Sprint 3          |
| `Final Sprint/`         | รายละเอียดการดำเนินงานของ Final Sprint                |
| `src/`                  | Source Code ของ Application                           |
| `tests/`                | Automated Tests ของ Project                           |

---

# 11. Team Planning

ทีมมีสมาชิก 3 คน และใช้ **Role Rotation**
ในการแบ่งความรับผิดชอบในแต่ละ Sprint

## Team Members

| Member               | Nickname |
| -------------------- | -------- |
| นายชิษณุพงศ์ ซู      | คิม      |
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค    |
| นายเดโชชิต โตวินัส   | ออม      |

---

## Sprint 1 Roles

| Member    | Role          | Main Responsibility                        |
| --------- | ------------- | ------------------------------------------ |
| **คิม**   | Planner       | Planning, Requirements และ Documentation   |
| **ฟลุ๊ค** | Coder         | Application Development และ Implementation |
| **ออม**   | Debugger / QA | Testing, QA และ Bug Verification           |

---

## Sprint 2 Roles

| Member    | Role          | Main Responsibility                                    |
| --------- | ------------- | ------------------------------------------------------ |
| **ฟลุ๊ค** | Planner       | Planning, Requirements, Architecture และ Documentation |
| **ออม**   | Coder         | Web UI, API, Database, Service และ Data Processing     |
| **คิม**   | Debugger / QA | Testing, QA, Error Handling และ Edge Cases             |

---

## Sprint 3 Roles

| Member    | Role     | Main Responsibility                                                          |
| --------- | -------- | ---------------------------------------------------------------------------- |
| **ออม**   | Planner  | Planning, Requirements, Task Allocation และ Documentation                    |
| **คิม**   | Coder    | Data Processing, Analysis, Statistics, Visualization และ Feature Development |
| **ฟลุ๊ค** | Debugger | Testing, QA, Data Validation และ Bug Verification                            |

---

## Final Sprint Roles

**TBD**

Role ของ Final Sprint จะกำหนดเมื่อเริ่ม Final Sprint
และจะบันทึกไว้ในเอกสารของ Final Sprint

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

| Sprint       | Status      |
| ------------ | ----------- |
| Sprint 1     | ✅ Completed |
| Sprint 2     | ✅ Completed |
| Sprint 3     | ✅ Completed |
| Final Sprint | ⏳ Planned   |

### Current Stage

**Sprint 1 Completed → Sprint 2 Completed → Sprint 3 Completed → Preparing for Final Sprint**

Sprint 1 ได้พัฒนา Application Foundation และ CLI เรียบร้อยแล้ว

Sprint 2 ได้พัฒนา Web Application
พร้อม RAWG API, Steam API, SQLite Database,
Data Processing, Game Service และ Web Dashboard Features

Sprint 3 ได้พัฒนาต่อยอดระบบด้าน Data Analysis,
Statistics และ Data Visualization
พร้อม Advanced Features ได้แก่ Filtering, Sorting
และ Game Comparison ตามขอบเขตของ Sprint

ขั้นตอนถัดไปของ Project คือ Final Sprint
ซึ่งมุ่งเน้นการรวมระบบ การทดสอบขั้นสุดท้าย
การแก้ไขปัญหา และการเตรียมส่งมอบ Final Project

---

# 13. Plan Maintenance

`Plan.md` เป็นเอกสารระดับ Project
และจะถูกปรับปรุงเมื่อ Project มีการเปลี่ยนแปลงที่สำคัญ เช่น:

* เปลี่ยน Scope ของ Project
* เปลี่ยน Technology
* เปลี่ยน Sprint Timeline
* เปลี่ยนเป้าหมายของ Sprint
* ได้รับ Feedback ที่ส่งผลต่อ Project Direction
* เพิ่มหรือลด Major Feature
* เปลี่ยนแปลงจากผลการพัฒนาใน Sprint ก่อนหน้า
* เปลี่ยนแปลงสถานะของ Sprint

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

---

# 15. Sprint 3 Daily Work Plan

Sprint 3 ดำเนินงานเป็นระยะเวลา 5 วัน
ตั้งแต่วันที่ **25–29 September 2026**

| วันที่          | Planner — ออม                                     | Coder — คิม                                                                  | Debugger — ฟลุ๊ค                                | ผลการดำเนินงาน                   |
| --------------- | ------------------------------------------------- | ---------------------------------------------------------------------------- | ----------------------------------------------- | -------------------------------- |
| **25 Sep 2569** | กำหนด Sprint Goal, Scope, Requirements และแบ่งงาน | ตรวจสอบ Source Code เดิมและงานที่ต่อเนื่องจาก Sprint 2                       | เตรียม Test Cases และจุดตรวจสอบ                 | Planning & Technical Preparation |
| **26 Sep 2569** | ติดตามความคืบหน้าและควบคุม Scope                  | พัฒนา Data Processing, Data Normalization และ Analysis Layer                 | ทดสอบ Data Processing, Type และ Missing Data    | Data Processing & Analysis       |
| **27 Sep 2569** | ติดตาม Requirements ของ Statistics Dashboard      | พัฒนา Statistics Page, Summary Statistics และ Visualization                  | ทดสอบ Statistics และ Charts                     | Statistics & Visualization       |
| **28 Sep 2569** | ติดตาม Advanced Features และ Integration          | พัฒนา Advanced Filtering, Sorting, Game Comparison และ Dashboard Integration | ทดสอบ Filter, Sort, Comparison และ Integration  | Advanced Features & Integration  |
| **29 Sep 2569** | ตรวจสอบ Definition of Done และจัดทำ Documentation | แก้ไข Bugs และเตรียม Source สำหรับ Final QA                                  | Final QA, Regression Test และตรวจสอบ Test Cases | Final QA & Documentation         |

---

# 16. Project Completion Criteria

Project จะถือว่าเข้าสู่ Final Stage
เมื่อ Features หลักจาก Sprint 1–3
สามารถทำงานร่วมกันได้ตาม Scope ที่กำหนด

เกณฑ์หลักประกอบด้วย:

### Application

* Web Application สามารถเปิดใช้งานได้
* Dashboard สามารถแสดงข้อมูลเกมได้
* Navigation ทำงานได้
* Search และ Filtering ทำงานได้
* Game Detail ทำงานได้

### Data

* RAWG API สามารถเชื่อมต่อได้
* Steam API สามารถเชื่อมต่อได้ในส่วนที่ระบบรองรับ
* SQLite สามารถจัดเก็บข้อมูลได้
* Data Processing สามารถเตรียมข้อมูลสำหรับ Application ได้

### Analysis

* Statistics สามารถคำนวณจากข้อมูลที่เตรียมแล้ว
* Data Visualization สามารถแสดงข้อมูลได้
* Advanced Filtering ทำงานได้
* Advanced Sorting ทำงานได้
* Game Comparison ทำงานได้

### Reliability

* API Error มีการจัดการ
* Empty State มีการจัดการ
* Missing / Optional Data มีการจัดการ
* Application ไม่ควร Crash จาก Input หรือ Data ที่ไม่เป็นไปตามปกติ

### Testing

* Features หลักได้รับการทดสอบ
* Integration ระหว่าง Module ได้รับการตรวจสอบ
* Final Regression Testing จะดำเนินการใน Final Sprint

### Documentation

* README อัปเดต
* Project Plan อัปเดต
* Change Log อัปเดต
* Learning Log อัปเดต
* Sprint Documentation อัปเดต

---

# 17. Future / Final Sprint Scope

Features ต่อไปนี้ยังถือเป็นงานของ Final Sprint
และยังไม่ถือว่า Completed ณ จุดสิ้นสุดของ Sprint 3:

* Final Integration
* Final QA
* Regression Testing
* Performance / Reliability Checking
* GitHub Actions
* CI/CD
* AI Integration
* Final Documentation
* Final Presentation

รายละเอียดจริงของ Final Sprint จะถูกบันทึก
หลังจากทีมเริ่มดำเนินงานใน Sprint ดังกล่าว

---

# 18. Project Planning Summary

```text
SPRINT 1
Application Foundation
CLI + Core Logic + QA
        │
        ▼
SPRINT 2
Web Application Foundation
Streamlit + RAWG + Steam + SQLite
        │
        ▼
SPRINT 3
Data Analysis & Advanced Features
Statistics + Visualization + Filter + Sort + Comparison
        │
        ▼
FINAL SPRINT
Integration + Final QA + Documentation
        │
        ▼
FINAL PROJECT
```

**Current Status:**

```text
Sprint 1       ✅ Completed
Sprint 2       ✅ Completed
Sprint 3       ✅ Completed
Final Sprint   ⏳ Planned
```
