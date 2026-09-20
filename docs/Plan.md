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

| Sprint           | ช่วงเวลา | เป้าหมายหลัก                                     | Status      |
| ---------------- | -------- | ------------------------------------------------ | ----------- |
| **Sprint 1**     | Week 12  | Application Foundation และ CLI                   | ✅ Completed |
| **Sprint 2**     | Week 13  | Web UI + RAWG API + SQLite                       | ⏳ Planned   |
| **Sprint 3**     | Week 14  | System Integration และ Core Features             | ⏳ Planned   |
| **Final Sprint** | Week 15  | Testing, CI/CD, AI Integration และ Final Project | ⏳ Planned   |

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

### API Integration

เชื่อมต่อ **RAWG Video Games Database API**
เพื่อดึงข้อมูลเกมมาใช้งานจริง

### Database

เพิ่ม **SQLite Database**
สำหรับจัดเก็บและจัดการข้อมูลเกม

## Main Deliverable

Web Dashboard ที่สามารถ:

* เปิดใช้งานผ่าน Web Browser
* แสดงข้อมูลเกม
* ดึงข้อมูลจาก RAWG API
* เชื่อมต่อ SQLite
* แสดงข้อมูลจาก Database บน Dashboard

## Status

**⏳ Planned**

รายละเอียดการดำเนินงานของ Sprint 2:

`Sprint2/Sprint_2.md`

---

# 6. Sprint 3 — System Integration & Core Features

## Objective

เชื่อมต่อส่วนต่าง ๆ ของระบบให้ทำงานร่วมกันอย่างสมบูรณ์
และพัฒนา Core Features ของ Dashboard

## Main Scope

* Front-End / Back-End Integration
* API และ Database Integration
* Search
* Filter
* Sort
* Statistics
* Data Processing
* Data Consistency
* Error Handling
* Edge Case Handling
* Integration Testing

## Main Deliverable

ระบบ Gaming Statistics Dashboard ที่สามารถทำงานร่วมกันระหว่าง

```text
Web UI
   ↓
Application Logic
   ↓
Data Processing
   ↓
SQLite
   ↑
RAWG API
```

## Status

**⏳ Planned**

รายละเอียดการดำเนินงานของ Sprint 3:

`Sprint3/Sprint_3.md`

---

# 7. Final Sprint — Testing, CI/CD & AI Integration

## Objective

เตรียม Project ให้พร้อมสำหรับ Final Project
และการส่งมอบระบบ

## Main Scope

* Automated Testing
* pytest
* GitHub Actions
* CI/CD
* AI Integration
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

`Sprint4/` หรือเอกสาร Sprint ตามโครงสร้างที่จะกำหนดภายหลัง

---

# 8. Project Technology Roadmap

| Technology         | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
| ------------------ | -------- | -------- | -------- | ------------ |
| Python             | ✅        | ✅        | ✅        | ✅            |
| CLI                | ✅        | -        | -        | -            |
| Streamlit          | -        | ✅        | ✅        | ✅            |
| RAWG API           | -        | ✅        | ✅        | ✅            |
| Pandas             | -        | ✅        | ✅        | ✅            |
| SQLite             | -        | ✅        | ✅        | ✅            |
| Data Visualization | -        | ✅        | ✅        | ✅            |
| pytest             | -        | -        | Planned  | ✅            |
| GitHub Actions     | -        | -        | -        | ✅            |
| AI Integration     | -        | -        | -        | ✅            |

> เครื่องมือที่ยังไม่ถึง Sprint ของตัวเองจะยังไม่ถือว่าเป็นงานที่ดำเนินการเสร็จแล้ว

---

# 9. Project Deliverables Roadmap

| Deliverable                | Sprint       |
| -------------------------- | ------------ |
| Project Pitch              | Sprint 1     |
| Project Plan               | Sprint 1     |
| CLI Foundation             | Sprint 1     |
| Sprint 1 Documentation     | Sprint 1     |
| Web Dashboard              | Sprint 2     |
| RAWG API Integration       | Sprint 2     |
| SQLite Database            | Sprint 2     |
| Search / Filter / Sort     | Sprint 3     |
| Statistics & Visualization | Sprint 3     |
| Integration Testing        | Sprint 3     |
| Automated Testing          | Final Sprint |
| GitHub Actions / CI/CD     | Final Sprint |
| AI Integration             | Final Sprint |
| Final Documentation        | Final Sprint |
| Final Presentation         | Final Sprint |

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
│   ├── Change_Log.md
│   └── Learning_Log.md
│
├── src/
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
└── ...
```

### Documentation Responsibilities

| File / Folder           | Purpose                                               |
| ----------------------- | ----------------------------------------------------- |
| `README.md`             | ภาพรวมของ Project และ Current Status                  |
| `docs/Project_Pitch.md` | แนวคิด Problem, Solution, Technology และ Architecture |
| `docs/Plan.md`          | แผนการพัฒนาโดยรวมของ Project และทุก Sprint            |
| `docs/Change_Log.md`    | บันทึกการเปลี่ยนแปลงของ Project                       |
| `docs/Learning_Log.md`  | บันทึกสิ่งที่ทีมเรียนรู้ระหว่างการพัฒนา               |
| `Sprint1/Sprint_1.md`   | รายละเอียดการดำเนินงานและผลลัพธ์ของ Sprint 1          |
| `Sprint2/Sprint_2.md`   | รายละเอียดการดำเนินงานของ Sprint 2                    |
| `Sprint3/`              | รายละเอียดการดำเนินงานของ Sprint 3                    |
| `src/`                  | Source Code ของ Application                           |

---

# 11. Team Planning

ทีมมีสมาชิก 3 คน และใช้ Role หลักในการแบ่งความรับผิดชอบ

| Member    | Primary Role | Main Responsibility                        |
| --------- | ------------ | ------------------------------------------ |
| **คิม**   | Planner      | Planning, Requirements และ Documentation   |
| **ฟลุ๊ค** | Coder        | Application Development และ Implementation |
| **ออม**   | Debugger     | Testing, QA และ Bug Verification           |

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
```

---

# 12. Sprint Status

## Current Project Status

| Sprint       | Status      |
| ------------ | ----------- |
| Sprint 1     | ✅ Completed |
| Sprint 2     | ⏳ Planned   |
| Sprint 3     | ⏳ Planned   |
| Final Sprint | ⏳ Planned   |

### Current Stage

**Sprint 1 Completed → Preparing for Sprint 2**

Sprint 1 ได้พัฒนา Application Foundation และ CLI เรียบร้อยแล้ว

ขั้นตอนถัดไปของ Project คือการนำ Foundation จาก Sprint 1
ไปพัฒนาเป็น Web Application ใน Sprint 2

---

# 13. Plan Maintenance

`Plan.md` เป็นเอกสารระดับ Project และจะถูกปรับปรุงเมื่อ Project มีการเปลี่ยนแปลงที่สำคัญ เช่น

* เปลี่ยน Scope ของ Project
* เปลี่ยน Technology
* เปลี่ยน Sprint Timeline
* เปลี่ยนเป้าหมายของ Sprint
* ได้รับ Feedback ที่ส่งผลต่อ Project Direction
* เพิ่มหรือลด Major Feature

รายละเอียดการเปลี่ยนแปลงแต่ละครั้งจะถูกบันทึกเพิ่มเติมใน:

`docs/Change_Log.md`

ส่วนสิ่งที่ทีมเรียนรู้จากการพัฒนา
จะถูกบันทึกใน:

`docs/Learning_Log.md`

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

```
