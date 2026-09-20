# 🎮 Gaming Statistics Dashboard

## Final Term Project — CP352301 Script Programming

---

# 1. Project Overview

**Gaming Statistics Dashboard** คือ Web Application สำหรับรวบรวม จัดการ วิเคราะห์ และนำเสนอข้อมูลเกี่ยวกับวิดีโอเกมในรูปแบบ Dashboard

ผู้ใช้สามารถเข้าถึงระบบผ่าน **Web Browser** โดยไม่จำเป็นต้องใช้งานผ่าน Command Line โดยตรง

ระบบมีเป้าหมายเพื่อช่วยให้ผู้ใช้สามารถสำรวจข้อมูลเกมได้สะดวกขึ้น เช่น การค้นหาเกม การดู Rating การสำรวจ Genre และ Platform รวมถึงการดู Statistics และข้อมูลในรูปแบบ Visualization

โปรเจกต์พัฒนาด้วยแนวทาง **Incremental Development** โดยแบ่งการพัฒนาออกเป็นหลาย Sprint และเพิ่มความสามารถของระบบอย่างต่อเนื่องจาก Foundation ไปสู่ Web Application ที่สามารถใช้งานได้จริง

---

# 2. Problem Statement

ข้อมูลเกี่ยวกับวิดีโอเกมมีจำนวนมากและมีข้อมูลหลายประเภท เช่น ชื่อเกม Rating, Genre, Platform, Release Date และข้อมูลอื่น ๆ

หากผู้ใช้ต้องการค้นหาและเปรียบเทียบข้อมูลเกมจำนวนมาก การค้นหาข้อมูลจากแหล่งข้อมูลโดยตรงอาจไม่สะดวก และผู้ใช้อาจต้องใช้หลายขั้นตอนในการค้นหาข้อมูลที่ต้องการ

ดังนั้นกลุ่มจึงต้องการพัฒนา Web Application ที่รวบรวมข้อมูลเกมและนำเสนอข้อมูลผ่าน Dashboard เพื่อให้ผู้ใช้สามารถค้นหา สำรวจ และดูข้อมูลเกมได้ง่ายขึ้น

---

# 3. Project Objective

โปรเจกต์นี้มีวัตถุประสงค์หลักดังนี้

1. พัฒนา Web Application สำหรับแสดงข้อมูลเกี่ยวกับวิดีโอเกม
2. เชื่อมต่อข้อมูลเกมจาก External API
3. จัดเก็บและจัดการข้อมูลด้วย Database
4. พัฒนาระบบ Search, Filter และ Sort สำหรับข้อมูลเกม
5. คำนวณและแสดง Statistics ที่สำคัญของข้อมูลเกม
6. นำเสนอข้อมูลในรูปแบบ Dashboard และ Data Visualization
7. พัฒนาระบบตามแนวทาง Incremental Development ผ่านแต่ละ Sprint
8. ใช้ Git และ GitHub สำหรับ Version Control และการส่งมอบงาน

---

# 4. Target Application Format

## Web Application

Final Project จะพัฒนาเป็น **Web Application** ที่สามารถเปิดใช้งานผ่าน Web Browser

ผู้ใช้จะเข้าถึงระบบผ่านหน้า Dashboard และสามารถโต้ตอบกับข้อมูลเกมผ่าน User Interface โดยไม่จำเป็นต้องใช้ Command Line ในการใช้งานระบบจริง

ตัวอย่างการใช้งาน:

```text
User
  │
  │ เปิด Web Browser
  ↓
Gaming Statistics Dashboard
  │
  ├── View Games
  ├── Search Game
  ├── Filter
  ├── Sort
  ├── View Statistics
  ├── Explore Genres
  └── Explore Platforms
````

# 5. Final Project User Flow

การทำงานของระบบในภาพรวมมีลำดับดังนี้

```text
User
  ↓
Web Browser
  ↓
Web Dashboard
  ↓
Application Logic
  ↓
Data Processing
  ↓
SQLite Database
  ↑
  │
RAWG Video Games API
```

เมื่อผู้ใช้เปิด Web Application:

1. ระบบแสดงหน้า Gaming Statistics Dashboard
2. ระบบแสดงข้อมูลเกมที่มีอยู่ในระบบ
3. ผู้ใช้สามารถค้นหาเกมที่ต้องการ
4. ผู้ใช้สามารถ Filter หรือ Sort ข้อมูล
5. ผู้ใช้สามารถดูข้อมูลรายละเอียดของเกม
6. ระบบสามารถคำนวณ Statistics จากข้อมูล
7. ระบบแสดงผลข้อมูลในรูปแบบ Table, Summary และ Visualization

---

# 6. Main Features

Final Project มีเป้าหมายที่จะพัฒนา Features หลักดังนี้

## 6.1 Game Data

แสดงข้อมูลสำคัญของเกม เช่น

* Game Title
* Rating
* Genre
* Platform
* Release Date
* Metacritic Score
* Game Image
* ข้อมูลอื่น ๆ ที่ได้จาก API

---

## 6.2 Search

ผู้ใช้สามารถค้นหาเกมจากชื่อเกม

ตัวอย่าง:

```text
Search: Minecraft
```

ระบบจะแสดงเกมที่ตรงกับคำค้นหา

---

## 6.3 Filter

ผู้ใช้สามารถกรองข้อมูลเกมตามเงื่อนไขต่าง ๆ เช่น

* Genre
* Platform
* Rating
* Release Year

---

## 6.4 Sort

ผู้ใช้สามารถเรียงข้อมูล เช่น

* Rating สูง → ต่ำ
* Rating ต่ำ → สูง
* Release Date ใหม่ → เก่า
* Release Date เก่า → ใหม่

---

## 6.5 Statistics

ระบบสามารถคำนวณ Statistics จากข้อมูลเกม เช่น

* จำนวนเกมทั้งหมด
* Average Rating
* Highest Rating
* Lowest Rating
* จำนวนเกมในแต่ละ Genre
* จำนวนเกมในแต่ละ Platform

---

## 6.6 Data Visualization

นำข้อมูลมาแสดงในรูปแบบ Visualization เพื่อช่วยให้ผู้ใช้เข้าใจข้อมูลได้ง่ายขึ้น เช่น

* Bar Chart
* Pie / Donut Chart
* Rating Distribution
* Genre Distribution
* Platform Distribution

---

# 7. Technology Stack

## Programming Language

**Python**

ใช้เป็นภาษาหลักในการพัฒนา Application การจัดการข้อมูล และ Business Logic

---

## Web Application / Dashboard

**Streamlit**

ใช้สำหรับพัฒนา Web Interface และ Dashboard เพื่อให้ผู้ใช้สามารถเข้าถึงระบบผ่าน Web Browser

---

## Data Source

**RAWG Video Games Database API**

ใช้เป็นแหล่งข้อมูลหลักเกี่ยวกับวิดีโอเกม

ข้อมูลที่สามารถนำมาใช้ในระบบ เช่น

* Game Title
* Rating
* Release Date
* Genre
* Platform
* Metacritic Score
* Game Images

Website:

[https://rawg.io/](https://rawg.io/)

API:

[https://api.rawg.io/](https://api.rawg.io/)

> หมายเหตุ: การเชื่อมต่อ RAWG API จริงจะเริ่มดำเนินการใน Sprint 2

---

## Data Processing

**Pandas**

ใช้สำหรับจัดการและประมวลผลข้อมูลก่อนนำไปแสดงผลหรือวิเคราะห์ใน Dashboard

ตัวอย่างการใช้งาน:

* Data Cleaning
* Data Transformation
* Filtering
* Sorting
* Aggregation
* Statistical Calculation

---

## Database

**SQLite**

ใช้สำหรับจัดเก็บข้อมูลเกมภายในระบบ

Database จะทำหน้าที่เป็นส่วนจัดเก็บข้อมูลระหว่าง Application และข้อมูลที่ได้รับจาก API

> หมายเหตุ: SQLite Database จะเริ่มดำเนินการใน Sprint 2

---

## Version Control

**Git + GitHub**

ใช้สำหรับ:

* Version Control
* Branch Management
* Pull Request
* Code Review
* Project Collaboration
* Project History

---

## Testing

**pytest**

มีแผนใช้สำหรับ Automated Testing ใน Sprint ที่เกี่ยวข้องกับการทดสอบระบบ

นอกจากนี้จะมีการทำ:

* Manual Testing
* Functional Testing
* Edge Case Testing
* Integration Testing

---

## CI/CD

**GitHub Actions**

มีแผนใช้สำหรับ Automated Testing และ CI/CD ในช่วง Final Project

---

# 8. System Architecture

Architecture ของ Final Project แบ่งออกเป็นส่วนหลักดังนี้

```text
                    ┌─────────────────────┐
                    │      Web Browser    │
                    │       (User)        │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │  Streamlit Web UI   │
                    │     Dashboard       │
                    └──────────┬──────────┘
                               │
                               ↓
                    ┌─────────────────────┐
                    │   Application Logic │
                    │ Search / Filter /   │
                    │ Sort / Statistics   │
                    └──────┬─────────┬────┘
                           │         │
                           ↓         ↓
                ┌──────────────┐  ┌──────────────┐
                │    Pandas    │  │    SQLite    │
                │     Data     │  │   Database   │
                │  Processing  │  │              │
                └───────┬──────┘  └──────▲───────┘
                        │                │
                        ↓                │
                ┌────────────────────────┘
                │
        ┌───────▼────────┐
        │    RAWG API    │
        │ Video Games DB │
        └────────────────┘
```

### Data Flow

```text
RAWG API
   ↓
Fetch Game Data
   ↓
Data Processing
   ↓
SQLite Database
   ↓
Application Logic
   ↓
Streamlit Dashboard
   ↓
Web Browser
```

---

# 9. Project Development Strategy

โปรเจกต์จะพัฒนาแบบ **Incremental Development** โดยแบ่งการทำงานออกเป็น Sprint

แต่ละ Sprint จะมีขอบเขตและเป้าหมายของตัวเอง จากนั้นจึงนำผลลัพธ์และ Feedback จาก Sprint ก่อนหน้าไปใช้พัฒนา Sprint ถัดไป

ภาพรวม:

```text
Sprint 1
Foundation
    ↓
Sprint 2
Web UI + API + SQLite
    ↓
Sprint 3
Integration + Core Features
    ↓
Final Sprint
Testing + CI/CD + AI Integration
    ↓
Final Web Application
```

---

# 10. Sprint 1 — Foundation

Sprint 1 เป็นช่วงเริ่มต้นของการพัฒนา โดยเน้นการสร้าง Foundation ของ Application

เนื่องจาก Sprint 1 มีเป้าหมายด้าน Front-End App Development กลุ่มจึงเริ่มต้นด้วย CLI เพื่อพัฒนาและทดสอบโครงสร้างการทำงานของ Application ก่อน

## Sprint 1 Features

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

## Sprint 1 Data

ใน Sprint 1 ยังไม่ได้เชื่อมต่อ RAWG API จริง

ระบบใช้ **Local Sample Dataset** เพื่อให้สามารถพัฒนาและทดสอบ Application Foundation ได้โดยไม่ขึ้นอยู่กับ External API

## Sprint 1 Status

**✅ Completed**

---

# 11. Sprint 2 — Web UI + API + Database

Sprint 2 จะเป็นการเปลี่ยนจาก Foundation ของ Sprint 1 ไปสู่ระบบ Web Application ที่สามารถใช้งานผ่าน Web Browser

เป้าหมายหลักของ Sprint 2 ได้แก่

## Web UI

พัฒนา Dashboard Interface ด้วย Streamlit

```text
Web Browser
     ↓
Streamlit Dashboard
```

## API Integration

เชื่อมต่อ RAWG API จริง

```text
RAWG API
    ↓
Fetch Game Data
    ↓
Application
```

## Database

เพิ่ม SQLite Database

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite
    ↓
Dashboard
```

## Sprint 2 Status

**⏳ Planned**

---

# 12. Sprint 3 — Integration

Sprint 3 มีเป้าหมายเพื่อเชื่อมต่อส่วนต่าง ๆ ของระบบให้ทำงานร่วมกันอย่างสมบูรณ์

Planned Tasks:

* API Integration
* Database Integration
* Dashboard Integration
* Search
* Filter
* Sort
* Statistics
* Data Consistency
* Error Handling
* Edge Case Handling
* Integration Testing

## Sprint 3 Status

**⏳ Planned**

---

# 13. Final Sprint

Final Sprint มีเป้าหมายเพื่อเตรียมระบบสำหรับ Final Project และการส่งมอบ

Planned Tasks:

* Automated Testing
* pytest
* GitHub Actions
* CI/CD
* AI Integration
* Final QA
* Final Documentation
* Final Integration
* Final Presentation

## Final Sprint Status

**⏳ Planned**

---

# 14. Repository Structure

Project Repository จะจัดโครงสร้างโดยแยก Documentation ออกจาก Source Code และแยก Source Code ตามส่วนของ Project

โครงสร้างที่วางไว้:

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

### Directory Responsibilities

| Directory   | Purpose                      |
| ----------- | ---------------------------- |
| `docs/`     | Project Documentation        |
| `src/`      | Main Application Source Code |
| `Sprint1/`  | Sprint 1 Development Files   |
| `Sprint2/`  | Sprint 2 Development Files   |
| `Sprint3/`  | Sprint 3 Development Files   |
| `README.md` | Project Overview             |

---

# 15. Current Project Status

## Sprint 1

**✅ Completed**

CLI Foundation, Menu Navigation, Basic Features, Input Validation และ QA ได้รับการพัฒนาและทดสอบแล้ว

## Sprint 2

**⏳ Planned**

จะพัฒนา:

* Web Dashboard UI
* RAWG API Integration
* SQLite Database
* การแสดงข้อมูลจริงบน Dashboard

## Sprint 3

**⏳ Planned**

จะพัฒนา:

* System Integration
* Search / Filter / Sort
* Statistics
* Integration Testing

## Final Sprint

**⏳ Planned**

จะพัฒนา:

* Automated Testing
* CI/CD
* AI Integration
* Final Integration
* Final QA

---

# 16. Project Goal

เป้าหมายสุดท้ายของโปรเจกต์คือการพัฒนา **Gaming Statistics Dashboard** ให้เป็น Web Application ที่ผู้ใช้สามารถเปิดผ่าน Web Browser และสามารถค้นหา สำรวจ วิเคราะห์ และดูข้อมูลเกี่ยวกับวิดีโอเกมผ่าน Dashboard ได้ในระบบเดียว

```text
        User
         ↓
   Web Browser
         ↓
Gaming Statistics Dashboard
         ↓
 ┌───────┼────────┐
 ↓       ↓        ↓
Search  Filter  Statistics
         ↓
      Game Data
         ↓
 RAWG API + SQLite
```

โดยระบบจะพัฒนาทีละ Sprint และนำ Feedback จากแต่ละ Sprint มาใช้ปรับปรุง Project อย่างต่อเนื่อง

```
```
