# 🎮 Gaming Statistics Dashboard — Sprint 3 Report

## Final Term Project — CP352301 Script Programming

**Sprint:** Sprint 3 — Data Analysis, Visualization & Advanced Features  
**Period:** 25–29 September 2026  
**Duration:** 5 Days  
**Status:** ⏳ Planned / In Progress

**Repository:** https://github.com/Phanuwatphk/Gaming-Statistics-Dashboard

---

# 1. Sprint Overview

Sprint 3 เป็นการพัฒนาต่อยอดจาก Sprint 2 ซึ่งทีมได้พัฒนา Web Application ด้วย Streamlit พร้อมเชื่อมต่อ RAWG API, Steam API และ SQLite Database

เป้าหมายของ Sprint นี้คือการนำข้อมูลเกมที่มีอยู่ในระบบมาจัดการ เตรียมข้อมูล วิเคราะห์ และนำเสนอผ่าน Dashboard ในรูปแบบ Statistics และ Data Visualization รวมถึงปรับปรุงความสามารถในการสำรวจและเปรียบเทียบข้อมูลเกม

งานใน Sprint 3 จะเน้น Data Cleaning, Exploratory Data Analysis (EDA), Statistical Analysis, Data Visualization, Dashboard Statistics และ Advanced Features โดยยังคงใช้โครงสร้าง Web UI, Game Service, Data Processing และ SQLite ที่พัฒนาจาก Sprint 2

---

# 2. Sprint Goal

> พัฒนา Gaming Statistics Dashboard ให้สามารถนำข้อมูลเกมจากระบบมาวิเคราะห์และนำเสนอในรูปแบบ Statistics และ Data Visualization พร้อมเพิ่มความสามารถในการสำรวจ เปรียบเทียบ และกรองข้อมูลเกมได้สะดวกขึ้น

เมื่อจบ Sprint 3 ระบบควรสามารถ:

- ตรวจสอบและเตรียมข้อมูลเกมก่อนนำไปวิเคราะห์
- ทำ Data Cleaning และ Data Validation ตามความเหมาะสมของข้อมูล
- วิเคราะห์ข้อมูลเกมด้วย Exploratory Data Analysis (EDA)
- คำนวณ Descriptive Statistics ที่เกี่ยวข้อง
- แสดง Statistics บน Dashboard
- แสดงข้อมูลผ่าน Chart และ Visualization
- เปรียบเทียบข้อมูลเกมตามกลุ่มหรือเงื่อนไขที่กำหนด
- ปรับปรุง Advanced Filtering และ Advanced Sorting
- รักษาความสอดคล้องของข้อมูลระหว่าง UI, Service และ Database
- ทดสอบการทำงานร่วมกันของฟีเจอร์ที่พัฒนาใน Sprint นี้

---

# 3. Team Members & Roles

| สมาชิก | Role | หน้าที่หลัก |
|---|---|---|
| **คิม** | Coder | พัฒนา Data Processing, Analysis, Statistics, Visualization และฟีเจอร์ที่อยู่ใน Scope ของ Sprint 3 |
| **ฟลุ๊ค** | Debugger | ออกแบบและดำเนินการทดสอบ ตรวจสอบผลลัพธ์ วิเคราะห์ปัญหา และยืนยันการแก้ไข Bug |
| **ออม** | Planner | กำหนด Sprint Goal, Scope, Requirements, Definition of Done, แบ่งงาน ติดตามความคืบหน้า และจัดทำ Documentation |

> Role ดังกล่าวเป็น Role ที่ใช้ในการทำงานของ Sprint 3 โดยสมาชิกสามารถหมุนเวียน Role ใน Sprint ถัดไปได้

---

# 4. Sprint 3 Scope

## In Scope

สิ่งที่วางแผนพัฒนาใน Sprint 3:

### Data Cleaning & Data Preparation

- ตรวจสอบความครบถ้วนของข้อมูลเกม
- ตรวจสอบ Missing Values และข้อมูลที่มีรูปแบบไม่ถูกต้อง
- ตรวจสอบข้อมูลซ้ำตามเกณฑ์ที่เหมาะสม
- ปรับรูปแบบชนิดข้อมูลที่จำเป็นต่อการวิเคราะห์
- เตรียมข้อมูลสำหรับ Statistics และ Visualization
- ตรวจสอบความสอดคล้องระหว่างข้อมูลจาก Database และข้อมูลที่นำไปแสดงผล

### Exploratory Data Analysis (EDA)

- วิเคราะห์ภาพรวมของชุดข้อมูลเกม
- วิเคราะห์การกระจายตัวของ Rating
- วิเคราะห์จำนวนเกมในแต่ละ Genre
- วิเคราะห์จำนวนเกมในแต่ละ Platform
- สำรวจข้อมูล Release Year หากข้อมูลเพียงพอ
- สำรวจข้อมูล Metacritic Score หากข้อมูลเพียงพอ
- สำรวจข้อมูล Steam Player Count หากข้อมูลมีความพร้อม
- สรุปข้อค้นพบจากข้อมูลโดยอ้างอิงผลการวิเคราะห์จริง

### Statistical Analysis

- จำนวนข้อมูลที่ใช้ในการวิเคราะห์
- Mean
- Median
- Minimum / Maximum
- Standard Deviation
- Frequency และ Proportion
- การเปรียบเทียบค่าสถิติระหว่างกลุ่มที่เหมาะสม
- การตรวจสอบความเหมาะสมของข้อมูลก่อนเลือกใช้สถิติ

### Dashboard Statistics

- จำนวนเกมทั้งหมดในชุดข้อมูลที่นำมาวิเคราะห์
- Average Rating
- Highest Rating
- Lowest Rating
- จำนวนเกมตาม Genre
- จำนวนเกมตาม Platform
- Summary Cards หรือองค์ประกอบสรุปข้อมูลที่เหมาะสม
- Statistics อื่น ๆ ที่สามารถคำนวณจากข้อมูลที่มีจริง

### Data Visualization

- Rating Distribution
- Genre Distribution
- Platform Distribution
- Rating Comparison ตาม Genre หรือ Platform
- Release Year Distribution หากข้อมูลเพียงพอ
- Metacritic Score Visualization หากข้อมูลเพียงพอ
- Steam Player Count Visualization หากข้อมูลเพียงพอ
- เลือกชนิด Chart ให้เหมาะสมกับประเภทและความหมายของข้อมูล

### Advanced Features

- Advanced Filtering
- Advanced Sorting
- Data Comparison
- ปรับปรุงการสำรวจข้อมูลจากผลการวิเคราะห์
- ปรับปรุงการแสดงผลเมื่อไม่พบข้อมูลหลังใช้ Filter
- ปรับปรุงการเชื่อมต่อระหว่าง Dashboard, Game Service และ Data Processing

### Testing & Quality

- Unit Testing สำหรับฟังก์ชัน Data Processing และ Analysis
- Functional Testing สำหรับ Statistics และ Visualization
- Integration Testing ระหว่าง UI, Service และ Database
- Edge Case Testing
- ตรวจสอบความถูกต้องของค่าทางสถิติและผลลัพธ์จาก Chart
- ตรวจสอบการจัดการ Missing Values และ Empty Dataset

## Out of Scope

งานที่ยังไม่ใช่เป้าหมายหลักของ Sprint 3:

- การสร้าง Web Application ใหม่ตั้งแต่ต้น
- การเปลี่ยนจาก Streamlit ไปใช้ Framework อื่น
- การเปลี่ยน External API หลักของระบบ
- การสร้างระบบ Authentication / User Account
- GitHub Actions และ CI/CD แบบสมบูรณ์
- Final Presentation และ Final Documentation
- AI Integration เว้นแต่มีการปรับ Scope อย่างเป็นทางการ

---

# 5. System Architecture

Sprint 3 จะต่อยอดจาก Architecture ที่พัฒนาใน Sprint 2 โดยเพิ่มส่วน Analysis และ Visualization เข้าไปในกระบวนการนำเสนอข้อมูล

```text
RAWG API ───────┐
                ↓
          Data Processing
                ↓
           SQLite Database
                ↓
           Game Service
                ↓
       Data Analysis / Statistics
                ↓
          Data Visualization
                ↓
        Streamlit Dashboard
                ↓
            Web Browser

Steam API
    ↓
Player Data Processing
    ↓
SQLite Database
    ↓
Game Service / Analysis
```

### Sprint 3 Data Flow

```text
SQLite Database
       ↓
Retrieve Game Data
       ↓
Data Cleaning / Validation
       ↓
Data Preparation
       ↓
EDA / Statistical Analysis
       ↓
Statistics / Visualization
       ↓
Dashboard
       ↓
User
```

> Architecture นี้เป็นภาพรวมที่วางแผนไว้ รายละเอียดการเชื่อมต่อจริงให้ปรับตามโครงสร้าง Source Code และผลการพัฒนาใน Sprint 3

---

# 6. Project Structure

Sprint 3 จะพัฒนาต่อยอดจากโครงสร้างโปรเจกต์เดิม โดยเพิ่มหรือปรับไฟล์เท่าที่จำเป็นสำหรับ Data Analysis และ Visualization

```text
Gaming-Statistics-Dashboard/
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
│   ├── api/
│   ├── components/
│   ├── database/
│   ├── services/
│   └── utils/
│       ├── data_processing.py
│       └── ...
│
├── tests/
│   ├── ...
│   └── ...
│
├── Sprint1/
│   └── Sprint_1.md
├── Sprint2/
│   └── Sprint_2.md
├── Sprint3/
│   └── Sprint_3.md
└── Sprint4/
    └── ...
```

> โครงสร้างข้างต้นเป็นแนวทางเบื้องต้น ไม่ได้หมายความว่ามีการสร้างหรือแก้ไขไฟล์เหล่านี้แล้ว รายละเอียดจริงให้ยืนยันหลัง Implementation

---

# 7. Tools & Technologies

| Technology | Purpose |
|---|---|
| Python | Programming Language |
| Streamlit | Web Application / Dashboard |
| Pandas | Data Processing, Cleaning และ Analysis |
| SQLite | Data Storage |
| RAWG API | Game Data Source |
| Steam API | Player Data Source |
| Data Visualization Library | สร้าง Chart และ Visualization ตาม Library ที่ใช้จริงในโปรเจกต์ |
| pytest | Automated Testing |
| Git + GitHub | Version Control, Collaboration และ Pull Request |

> ให้ตรวจสอบ Dependencies ใน `requirements.txt` ก่อนระบุชื่อ Library สำหรับ Visualization เพิ่มเติม

---

# 8. Data Cleaning & Preparation

## 8.1 Data Quality Checks

ตรวจสอบคุณภาพข้อมูลก่อนนำไปวิเคราะห์ เช่น:

- Missing Values
- Duplicate Records
- Data Type Consistency
- Invalid หรือ Out-of-Range Values
- ความพร้อมของ Rating, Genre, Platform และ Release Date
- ความพร้อมของ Metacritic Score และ Player Count

## 8.2 Data Preparation

เตรียมข้อมูลให้เหมาะสมกับการคำนวณและการสร้าง Visualization เช่น:

- เลือก Columns ที่จำเป็นต่อการวิเคราะห์
- แปลงชนิดข้อมูลตามความเหมาะสม
- จัดการ Missing Values โดยไม่สร้างข้อมูลขึ้นมาแทนโดยไม่มีหลักเกณฑ์
- กำหนดวิธีจัดการข้อมูลที่ไม่สมบูรณ์ให้ชัดเจน
- แยกข้อมูลที่ใช้วิเคราะห์ตาม Feature

## 8.3 Data Quality Principles

- ไม่เปลี่ยนแปลงข้อมูลต้นฉบับโดยไม่มีเหตุผล
- ระบุวิธีจัดการ Missing Values ให้ตรวจสอบย้อนกลับได้
- ไม่ใช้ค่า Missing เป็นศูนย์โดยอัตโนมัติ
- ตรวจสอบจำนวนข้อมูลก่อนและหลัง Cleaning
- ใช้ข้อมูลที่มีอยู่จริงในการคำนวณ Statistics

---

# 9. Exploratory Data Analysis (EDA)

## 9.1 Dataset Overview

วิเคราะห์ภาพรวมของข้อมูล เช่น:

- จำนวนเกมทั้งหมด
- จำนวนข้อมูลที่พร้อมใช้ในแต่ละตัวแปร
- จำนวน Missing Values
- จำนวน Genre และ Platform ที่พบ
- ช่วงของ Rating และคะแนนที่เกี่ยวข้อง

## 9.2 Rating Analysis

วิเคราะห์ข้อมูล Rating เช่น:

- Mean และ Median
- Minimum และ Maximum
- Standard Deviation
- Rating Distribution
- จำนวนเกมในแต่ละช่วง Rating ตามเกณฑ์ที่กำหนด

## 9.3 Genre Analysis

วิเคราะห์ข้อมูล Genre เช่น:

- จำนวนเกมในแต่ละ Genre
- สัดส่วนของเกมแต่ละ Genre
- Rating Summary แยกตาม Genre เมื่อข้อมูลเพียงพอ

## 9.4 Platform Analysis

วิเคราะห์ข้อมูล Platform เช่น:

- จำนวนเกมในแต่ละ Platform
- สัดส่วนของเกมแต่ละ Platform
- Rating Summary แยกตาม Platform เมื่อข้อมูลเพียงพอ

## 9.5 Additional Analysis

อาจวิเคราะห์ Release Year, Metacritic Score หรือ Steam Player Count เพิ่มเติม หากข้อมูลมีความครบถ้วนและเหมาะสมต่อการวิเคราะห์

---

# 10. Statistical Analysis

## 10.1 Descriptive Statistics

คำนวณค่าสถิติเชิงพรรณนาที่เหมาะสมกับข้อมูล เช่น:

| Statistic | Description |
|---|---|
| Count | จำนวนข้อมูลที่ใช้คำนวณ |
| Mean | ค่าเฉลี่ย |
| Median | ค่ามัธยฐาน |
| Minimum | ค่าต่ำสุด |
| Maximum | ค่าสูงสุด |
| Standard Deviation | ส่วนเบี่ยงเบนมาตรฐาน |
| Frequency | ความถี่ของข้อมูลแต่ละกลุ่ม |
| Proportion | สัดส่วนของข้อมูลแต่ละกลุ่ม |

## 10.2 Group Comparison

เปรียบเทียบข้อมูลระหว่างกลุ่ม เช่น Rating ตาม Genre หรือ Platform โดยเลือกวิธีสรุปผลให้เหมาะสมกับลักษณะข้อมูลและจำนวนตัวอย่าง

## 10.3 Statistical Validation

- ตรวจสอบจำนวนข้อมูลที่ใช้คำนวณ
- ตรวจสอบ Missing Values
- ตรวจสอบผลลัพธ์ด้วยตัวอย่างคำนวณหรือ Unit Tests
- ระบุข้อจำกัดของข้อมูลเมื่อแปลผล
- หลีกเลี่ยงการสรุปความสัมพันธ์เชิงเหตุและผลจากข้อมูลเชิงพรรณนา

---

# 11. Dashboard Statistics & Data Visualization

## 11.1 Dashboard Statistics

พัฒนา Summary Cards หรือส่วนแสดงค่าสถิติ เช่น:

- Total Games
- Average Rating
- Highest Rating
- Lowest Rating
- Number of Genres
- Number of Platforms

ค่าที่แสดงต้องคำนวณจากข้อมูลที่ผ่านการเตรียมข้อมูลแล้ว และควรระบุให้ชัดเจนว่าคำนวณจากข้อมูลชุดใด

## 11.2 Visualization

| Visualization | Purpose |
|---|---|
| Bar Chart | เปรียบเทียบจำนวนเกมหรือค่าสถิติระหว่างกลุ่ม |
| Pie / Donut Chart | แสดงสัดส่วนของข้อมูลที่มีจำนวนกลุ่มเหมาะสม |
| Histogram | แสดงการกระจายตัวของ Rating หรือค่าตัวเลข |
| Box Plot | สำรวจการกระจายและค่าผิดปกติของข้อมูลตัวเลข |
| Comparison Chart | เปรียบเทียบค่าสถิติระหว่าง Genre หรือ Platform |

> เลือกใช้ Chart ตามความเหมาะสมของข้อมูลและ Library ที่มีอยู่จริง ไม่จำเป็นต้องสร้างทุกประเภท

## 11.3 Visualization Requirements

- Chart ต้องมีชื่อและคำอธิบายที่เข้าใจได้
- แกนและหน่วยต้องชัดเจนเมื่อเกี่ยวข้อง
- การแสดงผลต้องสอดคล้องกับข้อมูลที่ใช้คำนวณ
- ต้องจัดการกรณี Dataset ว่างหรือข้อมูลไม่เพียงพอ
- Filter ที่ผู้ใช้เลือกควรสัมพันธ์กับข้อมูลที่นำไปแสดงผล

---

# 12. Advanced Features

## 12.1 Advanced Filtering

ปรับปรุงความสามารถในการกรองข้อมูลตาม Feature ที่มีอยู่ เช่น:

- Genre
- Platform
- Rating
- Release Year หากข้อมูลพร้อม
- เงื่อนไขหลายตัวกรองร่วมกัน

## 12.2 Advanced Sorting

ปรับปรุงการเรียงลำดับข้อมูล เช่น:

- Rating สูง → ต่ำ
- Rating ต่ำ → สูง
- Release Date ใหม่ → เก่า
- Release Date เก่า → ใหม่
- Sort ตามตัวแปรที่รองรับและมีข้อมูลเพียงพอ

## 12.3 Data Comparison

เพิ่มความสามารถในการเปรียบเทียบข้อมูลระหว่างกลุ่ม เช่น:

- Rating ตาม Genre
- Rating ตาม Platform
- จำนวนเกมระหว่างกลุ่ม
- สถิติอื่น ๆ ที่เหมาะสมกับข้อมูล

---

# 13. Development Tasks

## Task 1 — Sprint Planning & Requirements

### Planner — ออม

- กำหนด Sprint Goal และ Scope
- ระบุ Features ที่ต้องพัฒนา
- กำหนด Requirements และ Definition of Done
- แบ่งงานและจัดทำ Daily Task Allocation
- ติดตามความคืบหน้า
- จัดทำและปรับปรุง Sprint Documentation

### Coder — คิม

- ตรวจสอบโครงสร้าง Source Code ปัจจุบัน
- ประเมินจุดที่ต้องเพิ่มหรือปรับปรุงสำหรับ Analysis และ Visualization
- ให้ข้อมูลด้าน Implementation และ Technical Constraints

### Debugger — ฟลุ๊ค

- วางแนวทาง Test Cases
- ระบุ Edge Cases ที่เกี่ยวข้องกับข้อมูลและการคำนวณ
- กำหนดแนวทางตรวจสอบความถูกต้องของ Statistics

---

## Task 2 — Data Cleaning & Preparation

### Planner — ออม

- กำหนดขอบเขต Data Cleaning
- ระบุข้อมูลและตัวแปรที่จะใช้วิเคราะห์
- กำหนดเกณฑ์ตรวจสอบ Data Quality

### Coder — คิม

- พัฒนา Data Cleaning และ Data Preparation
- จัดการ Missing Values และ Data Types ตามเกณฑ์ที่กำหนด
- เพิ่มหรือปรับปรุงฟังก์ชัน Data Processing ตามความจำเป็น

### Debugger — ฟลุ๊ค

- ทดสอบข้อมูลที่ครบถ้วนและไม่ครบถ้วน
- ตรวจสอบ Duplicate และ Data Type
- ตรวจสอบจำนวนข้อมูลก่อนและหลัง Cleaning
- ตรวจสอบว่าไม่เกิดการเปลี่ยนแปลงข้อมูลโดยไม่ตั้งใจ

---

## Task 3 — EDA & Statistical Analysis

### Planner — ออม

- กำหนดคำถามและขอบเขตการวิเคราะห์
- ระบุตัวแปรและ Statistics ที่ต้องการ
- ตรวจสอบว่าแผนการวิเคราะห์สอดคล้องกับข้อมูลจริง

### Coder — คิม

- พัฒนา EDA และฟังก์ชันคำนวณ Statistics
- คำนวณ Descriptive Statistics
- วิเคราะห์ Rating, Genre และ Platform
- เตรียมผลลัพธ์สำหรับนำไปแสดงบน Dashboard

### Debugger — ฟลุ๊ค

- ตรวจสอบผลการคำนวณ
- ทดสอบ Dataset ว่างและ Missing Values
- เปรียบเทียบผลลัพธ์กับตัวอย่างคำนวณ
- ตรวจสอบความถูกต้องของ Group Comparison

---

## Task 4 — Dashboard Statistics & Visualization

### Planner — ออม

- กำหนดรูปแบบและตำแหน่งการแสดงผลบน Dashboard
- กำหนดข้อมูลที่ต้องแสดงใน Summary Cards และ Charts
- ตรวจสอบความสอดคล้องระหว่าง Requirements กับ UI

### Coder — คิม

- พัฒนา Statistics Components
- เพิ่ม Chart และ Visualization ที่อยู่ใน Scope
- เชื่อมผล Analysis เข้ากับ Dashboard
- ปรับปรุง Empty State และการแสดงผลเมื่อไม่มีข้อมูล

### Debugger — ฟลุ๊ค

- ตรวจสอบค่าที่แสดงใน Summary Cards
- ตรวจสอบ Chart และ Label
- ทดสอบการเปลี่ยนแปลงผลลัพธ์เมื่อใช้ Filter
- ตรวจสอบการแสดงผลในกรณีข้อมูลไม่เพียงพอ

---

## Task 5 — Advanced Features & Integration

### Planner — ออม

- กำหนด Advanced Filter / Sort และ Data Comparison
- ติดตามการเชื่อมต่อระหว่าง UI, Service และ Database
- ตรวจสอบ Scope และ Definition of Done

### Coder — คิม

- พัฒนา Advanced Filtering และ Sorting ตาม Scope
- พัฒนา Data Comparison
- เชื่อม Analysis และ Visualization เข้ากับระบบเดิม
- ปรับปรุงการจัดการข้อมูลและ Error Handling ตามความจำเป็น

### Debugger — ฟลุ๊ค

- ทดสอบการทำงานร่วมกันของ Features
- ทดสอบ Filter และ Sort หลายเงื่อนไข
- ตรวจสอบ Data Consistency
- บันทึก Bug และตรวจสอบผลหลังแก้ไข

---

# 14. Sprint 3 Daily Task Allocation & Update

ระยะเวลาการทำงาน Sprint 3 คือ **25–29 September 2026 (5 Days)**

| Date | Planner — ออม | Coder — คิม | Debugger — ฟลุ๊ค | Daily Deliverable |
|---|---|---|---|---|
| **25 Sep 2026 (Day 1)** | กำหนด Scope, Requirements, DoD และแบ่งงาน | ตรวจสอบโครงสร้างเดิมและเริ่ม Data Cleaning / Preparation | ออกแบบ Test Cases และตรวจสอบคุณภาพข้อมูลเบื้องต้น | Sprint Plan, Data Quality Checklist และโครงสร้างงาน |
| **26 Sep 2026 (Day 2)** | ติดตามงานและยืนยันตัวแปรสำหรับ EDA | พัฒนา Data Cleaning, EDA และ Descriptive Statistics | ทดสอบ Data Processing และตรวจสอบค่าทางสถิติ | Data Preparation และผล EDA / Statistics เบื้องต้น |
| **27 Sep 2026 (Day 3)** | กำหนด Dashboard Statistics และรูปแบบ Visualization | พัฒนา Summary Statistics และ Charts | ตรวจสอบค่าที่แสดงและทดสอบ Empty / Missing Data | Dashboard Statistics และ Visualization เบื้องต้น |
| **28 Sep 2026 (Day 4)** | ตรวจสอบ Advanced Features และติดตาม Integration | พัฒนา Advanced Filter / Sort, Data Comparison และเชื่อม Dashboard | ทดสอบ Feature Integration, Filter / Sort และ Data Consistency | Advanced Features และ Integrated Dashboard |
| **29 Sep 2026 (Day 5)** | ตรวจสอบ DoD, สรุปผล และจัดทำ Sprint Report | แก้ไข Bug และเตรียม Source Code สำหรับส่งมอบ | ทำ Final QA, Regression / Edge Case Testing และสรุปผลทดสอบ | Sprint 3 Deliverable, QA Result และ Documentation |

> ตารางนี้เป็นแผนงานล่วงหน้า ให้ปรับสถานะและผลลัพธ์ตามการทำงานจริงในแต่ละวัน

---

# 15. Sprint Progress

| Task | Status | Notes |
|---|---|---|
| Sprint Planning & Requirements | ⏳ Planned | กำหนด Scope และ DoD |
| Data Cleaning & Preparation | ⏳ Planned | ตรวจสอบและเตรียมข้อมูล |
| Exploratory Data Analysis | ⏳ Planned | วิเคราะห์ภาพรวมข้อมูล |
| Statistical Analysis | ⏳ Planned | คำนวณและตรวจสอบ Statistics |
| Dashboard Statistics | ⏳ Planned | เพิ่ม Summary Statistics |
| Data Visualization | ⏳ Planned | เพิ่ม Chart ตามข้อมูลที่พร้อม |
| Advanced Filtering / Sorting | ⏳ Planned | ปรับปรุงการสำรวจข้อมูล |
| Data Comparison | ⏳ Planned | เปรียบเทียบข้อมูลระหว่างกลุ่ม |
| Integration Testing | ⏳ Planned | ตรวจสอบการทำงานร่วมกัน |
| Final QA | ⏳ Planned | ตรวจสอบก่อนส่งมอบ |
| Documentation | ⏳ Planned | อัปเดตเอกสาร Sprint |

---

# 16. QA Test Cases

Test Cases ต่อไปนี้เป็นรายการที่วางแผนไว้สำหรับ Sprint 3

| Test ID | Test Case | Expected Result |
|---|---|---|
| S3-TC-01 | ตรวจสอบ Dataset ที่มีข้อมูลครบถ้วน | Data Processing ทำงานได้ถูกต้อง |
| S3-TC-02 | ตรวจสอบ Missing Values | ระบบจัดการ Missing Values ตามเกณฑ์ที่กำหนด |
| S3-TC-03 | ตรวจสอบข้อมูลซ้ำ | ตรวจพบหรือจัดการข้อมูลซ้ำตามเกณฑ์ |
| S3-TC-04 | ตรวจสอบ Data Type | ตัวแปรมีชนิดข้อมูลเหมาะสมต่อการวิเคราะห์ |
| S3-TC-05 | ตรวจสอบ Mean / Median | ผลคำนวณตรงกับค่าที่ตรวจสอบด้วยตัวอย่าง |
| S3-TC-06 | ตรวจสอบ Min / Max / Standard Deviation | ผลคำนวณถูกต้องตามข้อมูลที่ใช้ |
| S3-TC-07 | ตรวจสอบ Genre / Platform Frequency | จำนวนและสัดส่วนถูกต้อง |
| S3-TC-08 | ตรวจสอบ Dataset ว่าง | ระบบไม่ Crash และแสดง Empty State |
| S3-TC-09 | ตรวจสอบ Rating Visualization | Chart สอดคล้องกับข้อมูลต้นทาง |
| S3-TC-10 | ตรวจสอบ Filter ร่วมกันหลายเงื่อนไข | ผลลัพธ์ตรงตามเงื่อนไข |
| S3-TC-11 | ตรวจสอบ Sorting | ข้อมูลเรียงลำดับตามเงื่อนไขที่เลือก |
| S3-TC-12 | ตรวจสอบ Data Comparison | ค่าที่เปรียบเทียบตรงกับข้อมูลที่ใช้ |
| S3-TC-13 | ตรวจสอบ Dashboard Integration | UI แสดงผลจาก Service / Analysis ได้ถูกต้อง |
| S3-TC-14 | ตรวจสอบข้อมูลไม่เพียงพอสำหรับ Chart | ระบบแสดงข้อความหรือ Empty State ที่เหมาะสม |

---

# 17. QA Result

ส่วนนี้จะบันทึกผลการทดสอบหลังจากดำเนินงานจริง

| Test ID | Result | Issue / Notes |
|---|---|---|
| S3-TC-01 | ⏳ Not Tested | |
| S3-TC-02 | ⏳ Not Tested | |
| S3-TC-03 | ⏳ Not Tested | |
| S3-TC-04 | ⏳ Not Tested | |
| S3-TC-05 | ⏳ Not Tested | |
| S3-TC-06 | ⏳ Not Tested | |
| S3-TC-07 | ⏳ Not Tested | |
| S3-TC-08 | ⏳ Not Tested | |
| S3-TC-09 | ⏳ Not Tested | |
| S3-TC-10 | ⏳ Not Tested | |
| S3-TC-11 | ⏳ Not Tested | |
| S3-TC-12 | ⏳ Not Tested | |
| S3-TC-13 | ⏳ Not Tested | |
| S3-TC-14 | ⏳ Not Tested | |

---

# 18. Contribution Matrix — Member Performance

ส่วนนี้ใช้สำหรับประเมินการทำงานของสมาชิกแต่ละคนหลังจบ Sprint 3

**เกณฑ์คะแนน:** งานแต่ละส่วนเต็ม 10 คะแนน

- 10 = ทำครบตามหน้าที่และส่งมอบงานเรียบร้อย
- 8–9 = ทำได้เกือบครบ มีการแก้ไขหรือปรับปรุงเล็กน้อย
- 6–7 = ทำได้บางส่วน แต่ยังต้องมีการช่วยเหลือหรือแก้ไขเพิ่มเติม
- 1–5 = ทำงานไม่ครบตามหน้าที่
- 0 = ไม่ได้ดำเนินงานในส่วนดังกล่าว

> คะแนนในตารางนี้ยังไม่กำหนดล่วงหน้า ให้ประเมินจากผลงานจริงเมื่อสิ้นสุด Sprint

## 18.1 Planner — ออม

| งานที่รับผิดชอบ | รายละเอียด | คะแนน |
|---|---|---:|
| Sprint Planning | กำหนด Goal, Scope และ Sprint Direction | — / 10 |
| Requirements & DoD | กำหนด Requirements และ Definition of Done | — / 10 |
| Task Allocation | แบ่งงานและติดตามความคืบหน้า | — / 10 |
| Integration Tracking | ติดตามการเชื่อมต่อ Features | — / 10 |
| Documentation | จัดทำและปรับปรุง Sprint Documentation | — / 10 |
| **Total** | | **— / 50** |

### Planner Contribution

บันทึกหน้าที่และผลงานของ Planner หลังจบ Sprint 3

---

## 18.2 Coder — คิม

| งานที่รับผิดชอบ | รายละเอียด | คะแนน |
|---|---|---:|
| Data Cleaning & Preparation | พัฒนา Data Cleaning และเตรียมข้อมูล | — / 10 |
| EDA & Statistics | พัฒนา EDA และคำนวณ Statistics | — / 10 |
| Dashboard Statistics | พัฒนา Summary Statistics | — / 10 |
| Visualization | พัฒนา Charts และเชื่อมต่อ Dashboard | — / 10 |
| Advanced Features | พัฒนา Filter / Sort / Comparison และ Integration | — / 10 |
| **Total** | | **— / 50** |

### Coder Contribution

บันทึกหน้าที่และผลงานของ Coder หลังจบ Sprint 3

---

## 18.3 Debugger — ฟลุ๊ค

| งานที่รับผิดชอบ | รายละเอียด | คะแนน |
|---|---|---:|
| Test Case Design | ออกแบบ Test Cases สำหรับ Sprint 3 | — / 10 |
| Data Quality Testing | ตรวจสอบ Data Cleaning และ Data Quality | — / 10 |
| Statistics Verification | ตรวจสอบผลการคำนวณ Statistics | — / 10 |
| Integration Testing | ตรวจสอบการทำงานร่วมกันของระบบ | — / 10 |
| Bug Verification | ตรวจสอบ Error และผลหลังแก้ไข | — / 10 |
| **Total** | | **— / 50** |

### Debugger Contribution

บันทึกหน้าที่และผลงานของ Debugger หลังจบ Sprint 3

---

# 19. Contribution Summary

| สมาชิก | Role | คะแนนที่ได้รับ | คะแนนเต็ม | Completion |
|---|---|---:|---:|---:|
| **ออม** | Planner | — | 50 | — |
| **คิม** | Coder | — | 50 | — |
| **ฟลุ๊ค** | Debugger | — | 50 | — |
| **Total** | | **—** | **150** | **—** |

> กรอกคะแนนและ Completion หลังประเมินผลงานจริงเท่านั้น

---

# 20. Definition of Done

Sprint 3 จะถือว่าเสร็จเมื่อ:

### Data Processing & Analysis

- [ ] มีการตรวจสอบและเตรียมข้อมูลสำหรับการวิเคราะห์
- [ ] มีการจัดการ Missing Values ตามเกณฑ์ที่กำหนด
- [ ] มีผล EDA สำหรับข้อมูลที่อยู่ใน Scope
- [ ] มีการคำนวณ Descriptive Statistics ที่กำหนด
- [ ] ตรวจสอบความถูกต้องของผลคำนวณแล้ว

### Dashboard & Visualization

- [ ] Dashboard แสดง Statistics ตาม Scope
- [ ] มี Visualization ตาม Feature ที่กำหนด
- [ ] Chart แสดงผลสอดคล้องกับข้อมูลที่ใช้คำนวณ
- [ ] มีการจัดการ Empty Dataset และข้อมูลไม่เพียงพอ
- [ ] Statistics และ Visualization เชื่อมต่อกับข้อมูลในระบบได้

### Advanced Features

- [ ] Advanced Filtering ทำงานตาม Requirements
- [ ] Advanced Sorting ทำงานตาม Requirements
- [ ] Data Comparison ทำงานตาม Scope ที่กำหนด
- [ ] การใช้ Filter และ Sort ไม่ทำให้ข้อมูลแสดงผลผิดพลาด

### Testing

- [ ] Unit Tests สำหรับส่วนที่พัฒนาใน Sprint 3
- [ ] ตรวจสอบผลคำนวณ Statistics
- [ ] ทดสอบ Data Cleaning และ Missing Values
- [ ] ทดสอบ Dashboard Integration
- [ ] ทดสอบ Edge Cases
- [ ] บันทึก QA Result ตามผลการทดสอบจริง
- [ ] แก้ไขหรือบันทึก Known Issues ที่ยังเหลือ

### Documentation

- [ ] Sprint 3 Report ได้รับการอัปเดต
- [ ] Project Plan ได้รับการอัปเดตตามผลจริง
- [ ] Change Log ได้รับการอัปเดต
- [ ] Learning Log ได้รับการอัปเดต
- [ ] README ได้รับการอัปเดตหากมีการเปลี่ยนแปลงการใช้งาน

### GitHub

- [ ] Sprint 3 Branch ได้รับการจัดการตาม Workflow ของทีม
- [ ] Commit History สะท้อนการทำงาน
- [ ] Code Review / Pull Request ตาม Workflow ของทีม
- [ ] ส่งมอบ Source Code และ Documentation ที่เกี่ยวข้อง

---

# 21. Wow! — สิ่งที่ทำได้ดี

ส่วนนี้จะบันทึกสิ่งที่ทีมทำได้ดีหลังจบ Sprint 3 โดยอ้างอิงจากผลการดำเนินงานจริง

### 1. Data Analysis

บันทึกสิ่งที่ทำได้ดีเกี่ยวกับ Data Cleaning, EDA และ Statistical Analysis

### 2. Dashboard Statistics

บันทึกการพัฒนา Statistics และการนำเสนอข้อมูลบน Dashboard

### 3. Data Visualization

บันทึกผลการสร้าง Chart และการเชื่อมต่อกับข้อมูลจริง

### 4. Advanced Features

บันทึกการพัฒนา Filter, Sort และ Data Comparison

### 5. Testing & Integration

บันทึกผลการทดสอบและการทำงานร่วมกันของระบบ

---

# 22. Whoops! — ปัญหาและการแก้ไข

ส่วนนี้จะบันทึกปัญหาที่พบจริงใน Sprint 3 พร้อมสาเหตุและแนวทางแก้ไข

## Problem 1 — Data Quality

**Problem:** บันทึกปัญหาคุณภาพข้อมูลที่พบจริง

### Solution

บันทึกวิธีแก้ไขและผลหลังแก้ไข

---

## Problem 2 — Statistical Calculation

**Problem:** บันทึกปัญหาที่พบในการคำนวณหรือการตรวจสอบ Statistics

### Solution

บันทึกวิธีแก้ไขและผลหลังแก้ไข

---

## Problem 3 — Visualization

**Problem:** บันทึกปัญหาที่พบในการสร้างหรือแสดงผล Chart

### Solution

บันทึกวิธีแก้ไขและผลหลังแก้ไข

---

## Problem 4 — Integration / Advanced Features

**Problem:** บันทึกปัญหาที่พบในการเชื่อมต่อ Dashboard, Service, Filter หรือ Sort

### Solution

บันทึกวิธีแก้ไขและผลหลังแก้ไข

---

# 23. Sprint 3 Review

ส่วนนี้จะสรุปผลหลังจบ Sprint 3

### Sprint Goal

บันทึกว่า Sprint 3 บรรลุเป้าหมายด้าน Data Analysis, Statistics, Visualization และ Advanced Features ได้มากน้อยเพียงใด โดยอ้างอิงจากผลการทดสอบจริง

### Result

- **Completed Features:** บันทึก Features ที่ทำเสร็จ
- **Partially Completed:** บันทึก Features ที่ทำได้บางส่วน
- **Not Completed:** บันทึก Features ที่ยังไม่เสร็จ
- **Known Issues:** บันทึกปัญหาที่คงเหลือ
- **Next Sprint Considerations:** บันทึกงานที่ควรส่งต่อไป Sprint 4

---

# 24. Sprint 3 Final Status

## Data Processing & Analysis

**⏳ Planned**

## Dashboard Statistics & Visualization

**⏳ Planned**

## Advanced Features

**⏳ Planned**

## Testing & Integration

**⏳ Planned**

## Documentation

**⏳ Planned**

---

**Current Sprint Status:** ⏳ Planned

> เปลี่ยนสถานะเป็น In Progress หรือ Completed ตามความคืบหน้าและผลการตรวจสอบจริง
