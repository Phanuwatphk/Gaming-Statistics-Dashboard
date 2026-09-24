# 📚 Learning Log — Gaming Statistics Dashboard

## Final Term Project — CP352301 Script Programming

Learning Log นี้ใช้สำหรับบันทึกสิ่งที่สมาชิกในกลุ่ม
ได้เรียนรู้จากการพัฒนา Gaming Statistics Dashboard
ในแต่ละ Sprint ตั้งแต่ Sprint 1 จนถึง Sprint สุดท้าย

เนื้อหาจะถูก Update หลังจากจบแต่ละ Sprint
เพื่อบันทึกทั้ง Technical Learning, Project Management,
Teamwork, Problems และ Lessons Learned

---

# 📌 Learning Log Structure

ในแต่ละ Sprint จะบันทึกหัวข้อหลักดังนี้:

1. Sprint Overview
2. What We Did
3. What We Learned
4. Problems & Challenges
5. How We Solved Them
6. Teamwork & Process Learning
7. Technical Learning
8. Instructor / Team Feedback
9. Lessons Learned
10. How We Will Apply This Learning

---

# 🚀 Sprint 1 — Application Foundation

**Period:** 10–15 September 2026  
**Status:** ✅ Completed

## 1. Sprint Overview

Sprint 1 เป็นช่วงเริ่มต้นของการพัฒนา Project
โดยมีเป้าหมายเพื่อสร้าง Application Foundation
และทำความเข้าใจกระบวนการทำงานของทีม

ใน Sprint นี้ทีมพัฒนา Application ในรูปแบบ CLI
เพื่อทดลองโครงสร้างการทำงานของระบบ
ก่อนนำไปพัฒนาเป็น Web Application ใน Sprint ถัดไป

---

## 2. What We Did

สิ่งที่ทีมดำเนินการใน Sprint 1:

- กำหนด Sprint Goal
- กำหนด Scope และ Requirements
- แบ่ง Role ของสมาชิก
- ออกแบบ CLI Flow
- พัฒนา Main Menu
- พัฒนา Menu Navigation
- พัฒนา View Games
- พัฒนา Search Game
- พัฒนา Statistics
- พัฒนา Genre
- พัฒนา Top Rated Games
- เพิ่ม Input Validation
- เพิ่ม Exception Handling
- ทดสอบ Normal Cases
- ทดสอบ Invalid Inputs
- ทดสอบ Edge Cases
- จัดทำ Documentation
- จัดทำ GitHub Repository

---

## 3. What We Learned

### Project Planning

ทีมได้เรียนรู้ว่าการกำหนด Scope และ Requirements
ก่อนเริ่มพัฒนา ช่วยให้สมาชิกเข้าใจเป้าหมายเดียวกัน
และช่วยป้องกันการทำงานเกินขอบเขตของ Sprint

### Python Development

ทีมได้เรียนรู้การแบ่ง Program ออกเป็น Function
ตามหน้าที่ เช่น:

```text
display_main_menu()
get_menu_choice()
view_games()
search_game()
view_statistics()
````

การแยก Function ทำให้ Code อ่านง่าย
ทดสอบง่าย และสามารถแก้ไขเฉพาะส่วนได้

### Input Validation

ทีมได้เรียนรู้ว่าข้อมูลจากผู้ใช้ไม่สามารถคาดหวัง
ได้ว่าจะถูกต้องเสมอ จึงต้องมีการตรวจสอบ Input
ก่อนนำไปประมวลผล

### Exception Handling

ทีมได้เรียนรู้การใช้ `try-except`
เพื่อจัดการ Error ที่เกิดจาก Input
และป้องกันไม่ให้ Application Crash

### QA & Testing

ทีมได้เรียนรู้ว่าการทดสอบไม่ควรทดสอบเฉพาะ
กรณีที่ผู้ใช้กรอกข้อมูลถูกต้อง
แต่ควรทดสอบ Invalid Input และ Edge Cases ด้วย

---

## 4. Problems & Challenges

ปัญหาหลักที่พบใน Sprint 1:

### Problem 1 — Non-numeric Input

การรับ Input ที่เป็นข้อความ เช่น:

```text
abc
```

ในตำแหน่งที่ต้องการตัวเลข
สามารถทำให้เกิด `ValueError`

### Problem 2 — Invalid User Input

ผู้ใช้อาจกรอก:

```text
99
-1
[Blank]
```

ซึ่งอยู่นอกขอบเขตของตัวเลือกที่ระบบรองรับ

### Problem 3 — Project Scope

ในช่วงเริ่มต้นมีแนวทางที่สามารถพัฒนาได้หลายส่วน
เช่น API, Database และ Web UI
จึงต้องกำหนด Scope ของ Sprint 1
ให้ชัดเจนเพื่อไม่ให้ Development เกินขอบเขต

---

## 5. How We Solved Them

### Solution 1 — Exception Handling

ใช้ `try-except` เพื่อจัดการ `ValueError`

```python
try:
    choice = int(user_input)
except ValueError:
    print("Invalid input.")
```

### Solution 2 — Input Validation

เพิ่มการตรวจสอบ:

* Blank Input
* Non-numeric Input
* Negative Number
* Out-of-range Number
* Empty Search
* Unknown Game

### Solution 3 — Sprint Scope

กำหนดให้ Sprint 1 เน้น:

```text
CLI
Menu
Input
Validation
Core Features
QA
```

ส่วน Web UI, API และ Database
จะนำไปพัฒนาใน Sprint ถัดไป

---

## 6. Teamwork & Process Learning

จากการแบ่ง Role เป็น:

| Role     | Responsibility                 |
| -------- | ------------------------------ |
| Planner  | Planning และ Documentation     |
| Coder    | Development และ Implementation |
| Debugger | Testing และ QA                 |

ทีมได้เรียนรู้ว่าการแบ่งหน้าที่อย่างชัดเจน
ช่วยให้สมาชิกสามารถรับผิดชอบงานของตนเอง
และสามารถตรวจสอบงานระหว่างกันได้

นอกจากนี้ยังได้เรียนรู้ว่าการสื่อสารระหว่าง
Planner, Coder และ Debugger มีความสำคัญ
ต่อการทำให้ Requirements, Code และ QA
สอดคล้องกัน

---

## 7. Technical Learning

### Python

* Functions
* Loops
* Conditional Statements
* Exception Handling
* Input Validation
* Basic Data Processing

### Application Development

* CLI Application
* Menu Navigation
* Search
* Basic Statistics
* Error Handling

### Testing

* Test Cases
* Normal Cases
* Invalid Cases
* Edge Cases

### Git / GitHub

ทีมได้เรียนรู้ Workflow พื้นฐาน:

```text
Modify
  ↓
Git Add
  ↓
Git Commit
  ↓
Git Push
  ↓
Pull Request
  ↓
Review
  ↓
Merge
```

---

## 8. Instructor / Team Feedback

หลังจากนำเสนอ Sprint 1
ทีมได้รับ Feedback ให้ปรับปรุง:

* Project Pitch
* Project Plan
* Project Timeline
* Task Allocation
* Change Log
* Learning Log
* Contribution Metrics

ทีมจึงนำ Feedback ดังกล่าวมาใช้ปรับปรุง
Project Documentation และ Repository Structure

---

## 9. Lessons Learned

สิ่งสำคัญที่ทีมได้เรียนรู้จาก Sprint 1:

1. ควรกำหนด Scope ก่อนเริ่ม Development
2. ควรแบ่งงานตามหน้าที่อย่างชัดเจน
3. Code ควรแบ่งเป็น Function ตาม Responsibility
4. User Input ต้องได้รับการ Validation
5. ควรทดสอบ Invalid Input และ Edge Cases
6. Documentation ควร Update ไปพร้อมกับ Development
7. Git/GitHub ควรใช้เป็นส่วนหนึ่งของ Development Workflow
8. Feedback จากการ Review สามารถนำมาใช้ปรับปรุง Project ได้

---

## 10. How We Will Apply This Learning

สิ่งที่เรียนรู้จาก Sprint 1
จะถูกนำไปใช้ใน Sprint ถัดไป โดยเฉพาะ:

* ใช้ Modular Design ในการพัฒนา Web Application
* ใช้ Input Validation กับ Web UI
* ใช้ Error Handling กับ API และ Database
* ใช้ Git/GitHub Workflow ต่อเนื่อง
* ทำ QA ระหว่าง Development
* Update Documentation อย่างต่อเนื่อง
* ใช้ Task Allocation เพื่อติดตามงานของสมาชิก

---

## 11. Sprint 1 Learning Summary

| Learning Area      | Status    |
| ------------------ | --------- |
| Project Planning   | ✅ Learned |
| Python Functions   | ✅ Learned |
| CLI Development    | ✅ Learned |
| Input Validation   | ✅ Learned |
| Exception Handling | ✅ Learned |
| Search Logic       | ✅ Learned |
| Basic Statistics   | ✅ Learned |
| QA / Testing       | ✅ Learned |
| Edge Case Testing  | ✅ Learned |
| Git / GitHub       | ✅ Learned |
| Teamwork           | ✅ Learned |
| Documentation      | ✅ Learned |
| Feedback Handling  | ✅ Learned |

---

# 🚀 Sprint 2 — Web UI, API & Database

**Period:** 20–24 September 2026
**Status:** ✅ Completed

> Sprint 2 เป็นช่วงที่ทีมพัฒนาระบบจาก CLI ใน Sprint 1
> ให้เป็น Web Application และเชื่อมต่อข้อมูลจริงจาก API
> พร้อมจัดเก็บข้อมูลผ่าน SQLite Database

## 1. Sprint Overview

**Sprint Goal:**

พัฒนา Gaming Statistics Dashboard ให้สามารถใช้งานผ่าน Web Browser
โดยเชื่อมต่อข้อมูลเกมจริงจาก RAWG API และจัดเก็บข้อมูลผ่าน SQLite Database
พร้อมพัฒนา Backend / Data Flow ให้สามารถนำข้อมูลไปแสดงผลบน Web UI ได้

**Main Focus:**

* Web UI
* Dashboard Layout
* RAWG API
* SQLite Database
* Backend / Data Flow

---

## 2. What We Did

> Update หลังจบ Sprint 2

* [x] Web UI
* [x] Dashboard
* [x] RAWG API Integration
* [x] API Data Retrieval
* [x] SQLite Database
* [x] Data Flow
* [x] Testing

**Update:**

ทีมพัฒนา Streamlit Web Application สำหรับ Gaming Statistics Dashboard
โดยเปลี่ยนจาก CLI ใน Sprint 1 มาเป็น Web Application ที่สามารถใช้งานผ่าน Web Browser

มีการเชื่อมต่อ RAWG API เพื่อดึงข้อมูลเกมจริง เช่น Game Name, Rating,
Released Date, Genres, Platforms, Metacritic Score และ Image

นอกจากนี้ยังเพิ่ม Steam API สำหรับข้อมูลจำนวนผู้เล่นออนไลน์
และ Steam Top 100 / Live Players

ทีมพัฒนา SQLite Database สำหรับจัดเก็บข้อมูลเกม
และสร้าง Game Service เพื่อจัดการ Application Logic
รวมถึงเพิ่ม Data Processing และ Data Normalization
ก่อนนำข้อมูลไปใช้งานใน Web Application

ในส่วนของ Web UI มีการพัฒนา Game Library, Search,
Genres, Top Rated, Live Players และ Game Detail
รวมถึงเพิ่ม Filter, Pagination, Error Handling และ Empty State

มีการจัดทำ Automated Tests สำหรับ API, Database,
Service และ Data Processing modules

---

## 3. What We Learned

> Update หลังจบ Sprint 2

### Web Development

ทีมได้เรียนรู้การพัฒนา Web Application ด้วย Streamlit
และการออกแบบ Dashboard สำหรับแสดงข้อมูลเกมในรูปแบบที่ผู้ใช้สามารถค้นหา
กรอง และดูรายละเอียดข้อมูลได้

นอกจากนี้ยังได้เรียนรู้การจัดการ Page Navigation,
Pagination, Error State และ Empty State บน Web UI

### API Integration

ทีมได้เรียนรู้การเชื่อมต่อ REST API และการทำงานกับ JSON Response
โดยใช้ RAWG API เป็นแหล่งข้อมูลหลักของเกม

ทีมยังได้เรียนรู้การจัดการ API Key ผ่าน Environment Variable
รวมถึงการตรวจสอบ API Response, API Error และข้อมูลที่อาจไม่ครบถ้วน

นอกจากนี้ยังได้เรียนรู้การเชื่อมต่อ Steam API
เพื่อดึงข้อมูลเกี่ยวกับจำนวนผู้เล่นและ Steam Top 100

### Database

ทีมได้เรียนรู้การใช้ SQLite Database
สำหรับจัดเก็บและจัดการข้อมูลเกมภายในระบบ

รวมถึงการออกแบบการเชื่อมต่อระหว่าง Application
กับ Database และการใช้ Database Layer แยกออกจากส่วนอื่นของระบบ

### Data Management

ทีมได้เรียนรู้การทำ Data Processing และ Data Normalization
เพื่อแปลงข้อมูลจาก API ให้อยู่ในรูปแบบที่เหมาะสมกับการนำไปใช้งาน

นอกจากนี้ยังได้เรียนรู้การจัดการข้อมูลที่มี Missing Values
และข้อมูลที่อาจมีรูปแบบแตกต่างกันจาก API

---

## 4. Problems & Challenges

> Update หลังจบ Sprint 2

| Problem | Impact | Solution | Result |
| ------- | ------ | -------- | ------ |
| API Response มีข้อมูลซ้อนกันหลายระดับ | นำข้อมูลไปใช้งานโดยตรงได้ยาก | สร้าง Data Processing และ Data Normalization | ข้อมูลอยู่ในรูปแบบที่ระบบนำไปใช้งานต่อได้ |
| RAWG และ Steam ใช้ข้อมูลระบุตัวเกมต่างกัน | ไม่สามารถเชื่อมข้อมูลเกมจากทั้งสอง API ได้โดยตรง | จัดการ Steam App ID Mapping | สามารถเชื่อมข้อมูลเกมกับ Steam ได้ในส่วนที่รองรับ |
| API อาจตอบกลับช้าหรือเกิด Error | Web Application อาจแสดงผลผิดพลาดหรือไม่สามารถโหลดข้อมูลได้ | เพิ่ม Error Handling และ Empty State | ระบบสามารถจัดการกรณี API ใช้งานไม่ได้หรือไม่มีข้อมูล |
| จำนวนข้อมูลเกมมีมาก | แสดงข้อมูลทั้งหมดในหน้าเดียวได้ยาก | เพิ่ม Pagination | ผู้ใช้สามารถดูข้อมูลเป็นหน้าได้ |
| ข้อมูล Steam Player มีการเปลี่ยนแปลงตลอดเวลา | ต้องเรียก API ซ้ำบ่อยเพื่อให้ข้อมูลเป็นปัจจุบัน | ใช้ระบบ Refresh และ Snapshot | ลดการเรียก API ซ้ำและสามารถจัดเก็บข้อมูลล่าสุดไว้ใช้งาน |
| การพัฒนาหลายส่วนพร้อมกัน | อาจทำให้ Code และ Module เชื่อมต่อกันผิดพลาด | แบ่ง API, Database, Service, Processing และ UI ออกจากกัน | สามารถพัฒนาและตรวจสอบแต่ละส่วนได้ง่ายขึ้น |

---

## 5. How We Solved Them

> Update หลังจบ Sprint 2

ทีมแก้ไขปัญหาโดยแบ่งระบบออกเป็นหลาย Layer
เพื่อให้แต่ละส่วนมีหน้าที่ชัดเจน ได้แก่

```text
Web UI
   ↓
Game Service
   ↓
Data Processing
   ↓
API / Database
````

สำหรับข้อมูลจาก API ทีมสร้าง Data Processing Layer
เพื่อจัดรูปแบบและ Normalize ข้อมูลก่อนนำไปใช้งาน

สำหรับปัญหาการเชื่อมต่อข้อมูลจาก RAWG และ Steam
ทีมใช้ข้อมูลที่เกี่ยวข้องกับ Steam App ID เพื่อเชื่อมข้อมูลเกม
ในส่วนที่สามารถรองรับได้

สำหรับ API Error และข้อมูลที่ไม่มี
ทีมเพิ่ม Error Handling และ Empty State
เพื่อให้ Application สามารถทำงานต่อได้โดยไม่ Crash

สำหรับข้อมูลจำนวนมาก ทีมเพิ่ม Pagination
เพื่อช่วยลดปริมาณข้อมูลที่แสดงในแต่ละหน้า

สำหรับ Steam Player Data ทีมเพิ่มระบบ Refresh และ Snapshot
เพื่อจัดการข้อมูลที่เปลี่ยนแปลงตลอดเวลาและลดการเรียก API ซ้ำ

---

## 6. Teamwork & Process Learning

> Update หลังจบ Sprint 2

ใน Sprint 2 ทีมมีการหมุนเวียน Role ตามที่กำหนด โดยแบ่งเป็น:

| Role     | Member | Responsibility                                         |
| -------- | ------ | ------------------------------------------------------ |
| Planner  | ฟลุ๊ค  | Planning, Requirements, Architecture และ Documentation |
| Coder    | ออม    | Web UI, API, Database, Service และ Data Processing     |
| Debugger | คิม    | Testing, QA, Error Handling และ Edge Cases             |

ทีมได้เรียนรู้ว่าการแบ่งงานตาม Role
ช่วยให้แต่ละคนมีความรับผิดชอบที่ชัดเจนมากขึ้น

Planner ต้องทำความเข้าใจ Scope และ Requirements
ก่อนส่งต่อให้ Coder

Coder ต้องพัฒนา Code ให้สอดคล้องกับ Requirements
และแบ่ง Module ให้สามารถทำงานร่วมกับส่วนอื่นได้

Debugger ต้องตรวจสอบทั้ง Normal Cases,
Invalid Cases และ Error Cases

การทำงานร่วมกันทำให้ทีมเห็นความสำคัญของการสื่อสาร
ระหว่าง Planning, Development และ Testing
เพื่อให้แต่ละส่วนของระบบสามารถทำงานร่วมกันได้

---

## 7. Technical Learning

> Update หลังจบ Sprint 2

* Web UI: เรียนรู้การพัฒนา Web Application และ Dashboard ด้วย Streamlit รวมถึง Navigation, Pagination, Filter และ Empty State
* API: เรียนรู้ REST API, JSON Response, RAWG API, Steam API, API Key และ API Error Handling
* SQLite: เรียนรู้การสร้าง Database, การจัดเก็บข้อมูล และการเชื่อมต่อ Application กับ SQLite
* Data Processing: เรียนรู้ Data Cleaning, Data Normalization และการจัดรูปแบบข้อมูลจาก API ก่อนนำไปใช้งาน
* Git / GitHub: เรียนรู้การทำงานร่วมกันผ่าน Git/GitHub และการแบ่งงานระหว่างสมาชิกตาม Role

---

## 8. Instructor / Team Feedback

> Update หลังจบ Sprint 2

ใน Sprint 2 ยังไม่มี Instructor Feedback เพิ่มเติม
เนื่องจากเป็นส่วนที่ทีมพัฒนาต่อจาก Feedback ของ Sprint 1

ทีมจึงนำ Feedback จาก Sprint 1
เกี่ยวกับ Project Pitch, Project Plan, Timeline,
Task Allocation, Change Log, Learning Log และ Contribution Metrics
มาใช้ในการทำงานและปรับปรุง Documentation ของ Project

---

## 9. Lessons Learned

> Update หลังจบ Sprint 2

1. Web Application ที่ใช้ External API จำเป็นต้องมี Error Handling และ Empty State เพื่อรองรับกรณี API ไม่สามารถใช้งานได้หรือไม่มีข้อมูล
2. การแยกระบบออกเป็น API, Database, Service, Data Processing และ UI ช่วยให้ Code มีโครงสร้างชัดเจนและสามารถพัฒนาแต่ละส่วนได้ง่ายขึ้น
3. การใช้ Database ช่วยให้ Application สามารถจัดเก็บและจัดการข้อมูลได้อย่างเป็นระบบ
4. API Data อาจมีโครงสร้างและข้อมูลที่ไม่สมบูรณ์ จึงต้องมี Data Processing และ Data Normalization ก่อนนำไปใช้งาน
5. ข้อมูลที่เปลี่ยนแปลงตลอดเวลา เช่น Steam Player Data ต้องมีการจัดการ Refresh และการจัดเก็บ Snapshot
6. Pagination มีความสำคัญเมื่อ Application ต้องแสดงข้อมูลจำนวนมากบน Web UI
7. การทดสอบควรทำควบคู่กับการพัฒนา เพื่อช่วยค้นหา Error และปัญหาจากการเชื่อมต่อระหว่างแต่ละ Module

---

## 10. How We Will Apply This Learning

> Update หลังจบ Sprint 2

สิ่งที่เรียนรู้จาก Sprint 2
จะถูกนำไปใช้ในการพัฒนา Sprint ถัดไป โดยเฉพาะ:

* ใช้ Modular Architecture ต่อในการพัฒนา Features ใหม่
* ใช้ Data Processing และ Data Normalization กับข้อมูลที่จะนำมาวิเคราะห์
* ใช้ SQLite และ Service Layer เป็นส่วนหนึ่งของ Data Flow
* ใช้ Error Handling กับ External API และ Database อย่างต่อเนื่อง
* ใช้ Pagination และ Filtering เพื่อปรับปรุง User Experience
* ทำ Automated Testing ควบคู่กับการพัฒนา Features
* ใช้ Git/GitHub Workflow และการแบ่ง Role ต่อเนื่อง
* Update Documentation ให้สอดคล้องกับการพัฒนาในแต่ละ Sprint

---

## 11. Sprint 2 Learning Summary

| Learning Area   | Status    |
| --------------- | --------- |
| Web UI          | ✅ Learned |
| Dashboard       | ✅ Learned |
| API Integration | ✅ Learned |
| SQLite          | ✅ Learned |
| Data Processing | ✅ Learned |
| Testing         | ✅ Learned |
| Teamwork        | ✅ Learned |

---

# 🚀 Sprint 3 — Data Processing & Dashboard Development

**Period:** TBD
**Status:** ⏳ Planned

## 1. Sprint Overview

**Sprint Goal:**

TBD

**Main Focus:**

* Data Processing
* Data Cleaning
* Statistics
* Dashboard Features
* Search / Filter / Sort
* Data Visualization

---

## 2. What We Did

> Update หลังจบ Sprint 3

TBD

---

## 3. What We Learned

> Update หลังจบ Sprint 3

TBD

---

## 4. Problems & Challenges

> Update หลังจบ Sprint 3

| Problem | Impact | Solution | Result |
| ------- | ------ | -------- | ------ |
| TBD     | TBD    | TBD      | TBD    |

---

## 5. How We Solved Them

> Update หลังจบ Sprint 3

TBD

---

## 6. Teamwork & Process Learning

> Update หลังจบ Sprint 3

TBD

---

## 7. Technical Learning

> Update หลังจบ Sprint 3

TBD

---

## 8. Instructor / Team Feedback

> Update หลังจบ Sprint 3

TBD

---

## 9. Lessons Learned

> Update หลังจบ Sprint 3

TBD

---

## 10. How We Will Apply This Learning

> Update หลังจบ Sprint 3

TBD

---

## 11. Sprint 3 Learning Summary

| Learning Area      | Status |
| ------------------ | ------ |
| Data Processing    | ⏳ TBD  |
| Data Cleaning      | ⏳ TBD  |
| Statistics         | ⏳ TBD  |
| Data Visualization | ⏳ TBD  |
| Dashboard          | ⏳ TBD  |
| Testing            | ⏳ TBD  |
| Teamwork           | ⏳ TBD  |

---

# 🚀 Final Sprint — Integration, Testing & Finalization

**Period:** TBD
**Status:** ⏳ Planned

## 1. Sprint Overview

**Sprint Goal:**

TBD

**Main Focus:**

* System Integration
* Final Dashboard
* Testing
* Bug Fixing
* Performance Improvement
* Documentation
* Final Presentation

---

## 2. What We Did

> Update หลังจบ Final Sprint

TBD

---

## 3. What We Learned

> Update หลังจบ Final Sprint

TBD

---

## 4. Problems & Challenges

> Update หลังจบ Final Sprint

| Problem | Impact | Solution | Result |
| ------- | ------ | -------- | ------ |
| TBD     | TBD    | TBD      | TBD    |

---

## 5. How We Solved Them

> Update หลังจบ Final Sprint

TBD

---

## 6. Teamwork & Process Learning

> Update หลังจบ Fianl Sprint

TBD

---

## 7. Technical Learning

> Update หลังจบ Fianl Sprint

TBD

---

## 8. Instructor / Team Feedback

> Update หลังจบ Final Sprint

TBD

---

## 9. Lessons Learned

> Update หลังจบ Final Sprint

TBD

---

## 10. How We Will Apply This Learning

เนื่องจาก Fianl Sprint เป็น Sprint สุดท้าย
หัวข้อนี้สามารถใช้สรุปว่า
ความรู้ทั้งหมดที่ได้จาก Project
สามารถนำไปต่อยอดกับ Project อื่นหรือการพัฒนาทักษะของสมาชิกได้อย่างไร

TBD

---

## 11. Final Sprint Learning Summary

| Learning Area      | Status |
| ------------------ | ------ |
| System Integration | ⏳ TBD  |
| Testing            | ⏳ TBD  |
| Bug Fixing         | ⏳ TBD  |
| Performance        | ⏳ TBD  |
| Documentation      | ⏳ TBD  |
| Presentation       | ⏳ TBD  |
| Teamwork           | ⏳ TBD  |

---

# 📊 Overall Project Learning Summary

Section นี้จะ Update เมื่อ Project ใกล้เสร็จ
เพื่อสรุปสิ่งที่ทีมเรียนรู้ตลอดทั้ง Project

| Area               | Sprint 1 | Sprint 2 | Sprint 3 | Final Sprint |
| ------------------ | -------- | -------- | -------- | -------- |
| Planning           | ✅        | ⏳        | ⏳        | ⏳        |
| Python             | ✅        | ⏳        | ⏳        | ⏳        |
| Web Development    | ⏳        | ⏳        | ⏳        | ⏳        |
| API                | ⏳        | ⏳        | ⏳        | ⏳        |
| Database           | ⏳        | ⏳        | ⏳        | ⏳        |
| Data Processing    | ⏳        | ⏳        | ⏳        | ⏳        |
| Data Visualization | ⏳        | ⏳        | ⏳        | ⏳        |
| Testing            | ✅        | ⏳        | ⏳        | ⏳        |
| Git / GitHub       | ✅        | ⏳        | ⏳        | ⏳        |
| Teamwork           | ✅        | ⏳        | ⏳        | ⏳        |
| Documentation      | ✅        | ⏳        | ⏳        | ⏳        |

---

# 🧠 Final Project Reflection

> Section นี้จะเขียนเมื่อ Project เสร็จสมบูรณ์

ตลอดการพัฒนา Gaming Statistics Dashboard
ทีมจะรวบรวมสิ่งที่เรียนรู้จากทุก Sprint
ทั้งในด้าน Technical Skills, Project Management,
Teamwork, Problem Solving และ Software Development Process

**Final Reflection:**

> TBD

````
