# 🎮 Gaming Statistics Dashboard

## Project Pitch

### Project Title
**Gaming Statistics Dashboard**

---

## 1. Problem

ปัจจุบันข้อมูลเกี่ยวกับวิดีโอเกม เช่น Rating, Genre, Platform และ Release Date มีอยู่เป็นจำนวนมาก ทำให้ผู้ใช้งานอาจค้นหา สำรวจ และเปรียบเทียบข้อมูลเกมจากข้อมูลจำนวนมากได้ไม่สะดวก

ข้อมูลเกมที่มีหลายประเภทและมาจากชุดข้อมูลขนาดใหญ่ยังทำให้การมองเห็นภาพรวม เช่น เกมที่มี Rating สูง ประเภทเกมที่พบ หรือข้อมูลทางสถิติของเกม ทำได้ยากขึ้น

---

## 2. Solution

**Gaming Statistics Dashboard** เป็น Python Application ที่มีเป้าหมายเพื่อช่วยให้ผู้ใช้งานสามารถค้นหา สำรวจ และวิเคราะห์ข้อมูลเกี่ยวกับวิดีโอเกมได้ง่ายขึ้น

ระบบมีแผนที่จะรองรับความสามารถ เช่น:

- ดูข้อมูลเกม
- ค้นหาเกม
- ดู Rating ของเกม
- สำรวจ Genre
- สำรวจ Platform
- ดูเกมที่มี Rating สูง
- วิเคราะห์ข้อมูลทางสถิติ
- แสดงผลข้อมูลในรูปแบบที่เข้าใจง่าย

---

## 3. Domain

**Data Analysis & Management**

โปรเจกต์มุ่งเน้นการนำข้อมูลวิดีโอเกมมาจัดการ ประมวลผล วิเคราะห์ และนำเสนอให้ผู้ใช้งานสามารถสำรวจข้อมูลได้สะดวก

---

## 4. Planned Data Source

โปรเจกต์มีแผนที่จะใช้ **RAWG Video Games Database API** เป็นแหล่งข้อมูลเกมภายนอก

ข้อมูลที่สามารถนำมาใช้กับโปรเจกต์ เช่น:

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

## 5. Planned Final Project Architecture

```text
RAWG API
    ↓
Data Processing
    ↓
SQLite
    ↓
Statistics & Analysis
    ↓
User Interface
```

Architecture นี้เป็นทิศทางสำหรับ **Final Project** และไม่ได้หมายความว่าองค์ประกอบทั้งหมดถูกพัฒนาแล้วใน Sprint 1

---

## 6. Planned Technologies

เทคโนโลยีที่วางแผนจะนำมาใช้ตลอดการพัฒนาโปรเจกต์ ได้แก่:

- Python
- RAWG API
- Pandas
- SQLite
- Data Visualization
- Streamlit
- pytest
- GitHub Actions

เทคโนโลยีเหล่านี้จะถูกเพิ่มเข้ามาตาม Scope ของแต่ละ Sprint

---

## 7. Sprint Development Strategy

โปรเจกต์จะถูกพัฒนาแบบ Incremental Development โดยแบ่งการพัฒนาออกเป็นหลาย Sprint

```text
Sprint 1
CLI Foundation
Menu Navigation
Input Validation
QA
        ↓
Future Sprints
Data Processing
API Integration
Persistence
Advanced Features
        ↓
Final Project
Complete Gaming Statistics Dashboard
```

Sprint 1 จะเริ่มจากการสร้าง Foundation ของ Application ก่อน จากนั้นจึงค่อยเพิ่ม Data Processing, External API, Persistence และ User Interface ที่ซับซ้อนขึ้นใน Sprint ถัดไป

---

## 8. Project Vision

เป้าหมายสุดท้ายของ **Gaming Statistics Dashboard** คือการสร้าง Python Application ที่ช่วยให้ผู้ใช้งานสามารถสำรวจ ค้นหา และวิเคราะห์ข้อมูลวิดีโอเกมได้อย่างสะดวก โดยมีโครงสร้างโปรแกรมที่สามารถพัฒนาต่อยอดและเพิ่มความสามารถใน Sprint ต่อ ๆ ไปได้