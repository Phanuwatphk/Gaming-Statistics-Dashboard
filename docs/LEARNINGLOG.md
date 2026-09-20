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

**Period:** TBD
**Status:** ⏳ Planned

> Section นี้จะถูก Update หลังจากดำเนินงาน Sprint 2
> และจะบันทึกสิ่งที่ทีมเรียนรู้จากการพัฒนา Web UI,
> การเชื่อมต่อ API และ Database

## 1. Sprint Overview

**Sprint Goal:**

TBD

**Main Focus:**

* Web UI
* Dashboard Layout
* RAWG API
* SQLite Database
* Backend / Data Flow

---

## 2. What We Did

> Update หลังจบ Sprint 2

* [ ] Web UI
* [ ] Dashboard
* [ ] RAWG API Integration
* [ ] API Data Retrieval
* [ ] SQLite Database
* [ ] Data Flow
* [ ] Testing

**Update:**

> TBD

---

## 3. What We Learned

> Update หลังจบ Sprint 2

### Web Development

> TBD

### API Integration

> TBD

### Database

> TBD

### Data Management

> TBD

---

## 4. Problems & Challenges

> Update หลังจบ Sprint 2

| Problem | Impact | Solution | Result |
| ------- | ------ | -------- | ------ |
| TBD     | TBD    | TBD      | TBD    |

---

## 5. How We Solved Them

> Update หลังจบ Sprint 2

TBD

---

## 6. Teamwork & Process Learning

> Update หลังจบ Sprint 2

TBD

---

## 7. Technical Learning

> Update หลังจบ Sprint 2

* Web UI: TBD
* API: TBD
* SQLite: TBD
* Data Processing: TBD
* Git / GitHub: TBD

---

## 8. Instructor / Team Feedback

> Update หลังจบ Sprint 2

TBD

---

## 9. Lessons Learned

> Update หลังจบ Sprint 2

1. TBD
2. TBD
3. TBD

---

## 10. How We Will Apply This Learning

> Update หลังจบ Sprint 2

TBD

---

## 11. Sprint 2 Learning Summary

| Learning Area   | Status |
| --------------- | ------ |
| Web UI          | ⏳ TBD  |
| Dashboard       | ⏳ TBD  |
| API Integration | ⏳ TBD  |
| SQLite          | ⏳ TBD  |
| Data Processing | ⏳ TBD  |
| Testing         | ⏳ TBD  |
| Teamwork        | ⏳ TBD  |

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

# 🚀 Sprint 4 — Integration, Testing & Finalization

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

> Update หลังจบ Sprint 4

TBD

---

## 3. What We Learned

> Update หลังจบ Sprint 4

TBD

---

## 4. Problems & Challenges

> Update หลังจบ Sprint 4

| Problem | Impact | Solution | Result |
| ------- | ------ | -------- | ------ |
| TBD     | TBD    | TBD      | TBD    |

---

## 5. How We Solved Them

> Update หลังจบ Sprint 4

TBD

---

## 6. Teamwork & Process Learning

> Update หลังจบ Sprint 4

TBD

---

## 7. Technical Learning

> Update หลังจบ Sprint 4

TBD

---

## 8. Instructor / Team Feedback

> Update หลังจบ Sprint 4

TBD

---

## 9. Lessons Learned

> Update หลังจบ Sprint 4

TBD

---

## 10. How We Will Apply This Learning

เนื่องจาก Sprint 4 เป็น Sprint สุดท้าย
หัวข้อนี้สามารถใช้สรุปว่า
ความรู้ทั้งหมดที่ได้จาก Project
สามารถนำไปต่อยอดกับ Project อื่นหรือการพัฒนาทักษะของสมาชิกได้อย่างไร

TBD

---

## 11. Sprint 4 Learning Summary

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

| Area               | Sprint 1 | Sprint 2 | Sprint 3 | Sprint 4 |
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
