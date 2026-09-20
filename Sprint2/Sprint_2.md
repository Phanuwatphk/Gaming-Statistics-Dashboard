# Sprint 2 — Web UI, RAWG API & SQLite

## 1. Sprint Overview

Sprint 2 เป็นการพัฒนาต่อยอดจาก Sprint 1 โดยเปลี่ยนระบบจาก CLI Application ให้เป็น Web Application ที่สามารถใช้งานผ่าน Web Browser ได้

ใน Sprint นี้จะเน้นการเชื่อมต่อระบบ 3 ส่วนหลัก ได้แก่

1. Web UI
2. RAWG API
3. SQLite Database

โดยมีเป้าหมายให้ระบบสามารถรับข้อมูลเกมจริงจาก RAWG API จัดการข้อมูล และจัดเก็บข้อมูลลง SQLite ก่อนนำข้อมูลมาแสดงบน Web Dashboard

---

## 2. Sprint Goal

พัฒนาจาก CLI Foundation ใน Sprint 1 ให้เป็น Web Application ที่สามารถ:

- เปิดใช้งานผ่าน Web Browser
- แสดง Gaming Statistics Dashboard
- เชื่อมต่อ RAWG API
- ดึงข้อมูลเกมจริงจาก API
- จัดการข้อมูลจาก API
- บันทึกข้อมูลลง SQLite
- อ่านข้อมูลจาก SQLite มาแสดงบน Web UI
- เชื่อมต่อ Web UI, Application Logic, API และ Database เข้าด้วยกัน

---

## 3. Sprint Scope

### 3.1 Web UI Development

พัฒนา User Interface สำหรับ Gaming Statistics Dashboard โดยใช้ Streamlit

สิ่งที่จะทำ:

- สร้างหน้า Web Application
- สร้าง Dashboard Layout
- แสดงชื่อโปรเจกต์และข้อมูลหลัก
- แสดงรายการเกม
- แสดงข้อมูลสำคัญของเกม
- เพิ่มช่อง Search สำหรับค้นหาเกม
- เตรียมพื้นที่สำหรับ Features ที่จะพัฒนาต่อใน Sprint 3
- ปรับ Features จาก CLI ใน Sprint 1 ให้สามารถใช้งานผ่าน Web UI

---

### 3.2 RAWG API Integration

เชื่อมต่อ RAWG Video Games Database API เพื่อใช้ข้อมูลเกมจริงแทน Local Sample Dataset จาก Sprint 1

สิ่งที่จะทำ:

- ตั้งค่า RAWG API
- จัดการ API Key ผ่าน Environment Variable
- สร้าง Module สำหรับเรียก RAWG API
- ส่ง Request ไปยัง API
- รับ API Response
- ตรวจสอบ Response และ Error
- ดึงข้อมูลเกมที่จำเป็น
- เตรียมข้อมูลให้อยู่ในรูปแบบที่ระบบสามารถนำไปใช้ต่อได้

ข้อมูลที่สนใจ เช่น:

- Game ID
- Game Name
- Rating
- Released Date
- Genres
- Platforms
- Metacritic Score
- Ratings Count
- Image

---

### 3.3 SQLite Database

สร้าง Database สำหรับจัดเก็บข้อมูลเกมที่ได้รับจาก RAWG API

สิ่งที่จะทำ:

- สร้าง SQLite Database
- สร้าง Table สำหรับข้อมูลเกม
- กำหนด Fields ที่จำเป็น
- สร้างระบบ Insert Data
- สร้างระบบ Read Data
- ตรวจสอบข้อมูลก่อนบันทึก
- ป้องกันข้อมูลซ้ำที่ไม่จำเป็น
- เตรียม Database สำหรับการวิเคราะห์ใน Sprint 3

ตัวอย่างข้อมูลหลัก:

| Field | Description |
|---|---|
| game_id | ID ของเกมจาก RAWG |
| name | ชื่อเกม |
| rating | คะแนน Rating |
| released | วันที่วางจำหน่าย |
| genres | ประเภทเกม |
| platforms | Platform ที่รองรับ |
| metacritic | คะแนน Metacritic |
| ratings_count | จำนวน Rating |
| image | URL รูปภาพเกม |

---

## 4. Data Flow

ระบบใน Sprint 2 จะมี Data Flow ดังนี้:

User
↓
Web UI
↓
Game Service
↓
RAWG API
↓
Data Processing
↓
SQLite Database
↓
Game Service
↓
Web Dashboard

โดยระบบควรสามารถนำข้อมูลจาก Database กลับมาแสดงบน Web UI ได้

---

## 5. Project Structure

โครงสร้าง Source Code ที่ใช้ใน Sprint 2:

```text
src/
│
├── app.py
│
├── api/
│   ├── __init__.py
│   └── rawg_api.py
│
├── database/
│   ├── __init__.py
│   └── database.py
│
├── services/
│   ├── __init__.py
│   └── game_service.py
│
├── utils/
│   ├── __init__.py
│   └── data_processing.py
│
└── components/
    ├── __init__.py
    └── dashboard.py
````

---

## 6. File Responsibilities

### `src/app.py`

เป็น Entry Point ของ Web Application

หน้าที่:

* เริ่มต้น Streamlit Application
* ตั้งค่า Page Configuration
* เรียก Dashboard
* ควบคุม Main Application Flow

---

### `src/api/rawg_api.py`

รับผิดชอบการเชื่อมต่อ RAWG API

หน้าที่:

* โหลด API Key
* ส่ง HTTP Request
* รับ API Response
* ตรวจสอบ API Error
* ส่งข้อมูลกลับไปยัง Service Layer

---

### `src/database/database.py`

รับผิดชอบ SQLite Database

หน้าที่:

* สร้าง Database Connection
* สร้าง Table
* Insert Game Data
* Read Game Data
* ตรวจสอบข้อมูลที่มีอยู่
* ปิด Connection อย่างเหมาะสม

---

### `src/services/game_service.py`

เป็นตัวกลางระหว่าง API, Database และ Web UI

หน้าที่:

* เรียกข้อมูลจาก RAWG API
* จัดการข้อมูลเกม
* บันทึกข้อมูลลง Database
* อ่านข้อมูลจาก Database
* จัดการ Search Game
* ส่งข้อมูลที่พร้อมใช้งานให้ Dashboard

---

### `src/utils/data_processing.py`

รับผิดชอบการเตรียมข้อมูล

หน้าที่:

* แปลงข้อมูลจาก API
* จัดการ Nested Data
* จัดรูปแบบ Genres
* จัดรูปแบบ Platforms
* จัดการ Missing Values
* เตรียมข้อมูลก่อนบันทึก Database

---

### `src/components/dashboard.py`

รับผิดชอบส่วนประกอบของ Web Dashboard

หน้าที่:

* แสดง Game List
* แสดง Game Information
* Search Interface
* แสดงข้อมูลจาก Database
* จัด Layout ของ Dashboard

---

## 7. Tools & Technologies

| Tool / Technology | Purpose                      |
| ----------------- | ---------------------------- |
| Python            | พัฒนาระบบหลัก                |
| Streamlit         | พัฒนา Web UI และ Dashboard   |
| RAWG API          | แหล่งข้อมูลเกม               |
| Requests          | ส่ง HTTP Request ไปยัง API   |
| SQLite            | จัดเก็บข้อมูลเกม             |
| Pandas            | จัดการและเตรียมข้อมูล        |
| Git               | Version Control              |
| GitHub            | Repository และ Collaboration |
| VS Code           | Development Environment      |
| `.env`            | จัดเก็บ API Key อย่างปลอดภัย |

---

## 8. Development Tasks

### Task 1 — Prepare Web Application

* สร้าง Streamlit Application
* สร้างหน้า Dashboard เบื้องต้น
* ตรวจสอบการเปิด Web Application ผ่าน Browser
* เชื่อมโครงสร้าง Web UI เข้ากับ Source Code

### Task 2 — Connect RAWG API

* ตั้งค่า API Key
* สร้าง `rawg_api.py`
* ทดสอบ API Request
* ตรวจสอบ API Response
* จัดการ API Error
* ดึงข้อมูลเกมจริง

### Task 3 — Prepare Data

* ตรวจสอบข้อมูลจาก RAWG API
* เลือก Fields ที่ต้องใช้
* Normalize ข้อมูลที่เป็น Nested Data
* จัดการ Missing Values
* เตรียมข้อมูลสำหรับ SQLite

### Task 4 — Create SQLite Database

* สร้าง Database
* สร้าง Games Table
* กำหนด Schema
* สร้าง Insert Function
* สร้าง Read Function
* ทดสอบ Database

### Task 5 — Connect API & Database

* ดึงข้อมูลจาก RAWG API
* Process ข้อมูล
* บันทึกข้อมูลลง SQLite
* อ่านข้อมูลจาก SQLite
* ตรวจสอบความถูกต้องของ Data Flow

### Task 6 — Connect Database & Web UI

* ดึงข้อมูลจาก SQLite
* แสดงข้อมูลบน Dashboard
* เพิ่ม Search
* ตรวจสอบการแสดงผล
* ตรวจสอบกรณีไม่มีข้อมูล

### Task 7 — Testing & Debugging

ทดสอบระบบในกรณีต่าง ๆ เช่น:

* API เชื่อมต่อสำเร็จ
* API เชื่อมต่อไม่ได้
* API Response ไม่สมบูรณ์
* API Key ไม่ถูกต้อง
* Database สามารถสร้างได้
* สามารถ Insert Data ได้
* สามารถ Read Data ได้
* Search พบข้อมูล
* Search ไม่พบข้อมูล
* Database ไม่มีข้อมูล
* Web Application สามารถเปิดได้
* Web UI แสดงข้อมูลได้ถูกต้อง

---

## 9. Team Roles

### Planner — คิม

Responsibilities:

* กำหนด Sprint Goal และ Scope
* วางแผนการพัฒนา Sprint 2
* กำหนดโครงสร้างระบบ
* วางแผน Web UI, API และ Database
* ติดตามความคืบหน้าของทีม
* จัดทำและอัปเดต Sprint Documentation

### Coder — ฟลุ๊ค

Responsibilities:

* พัฒนา Web Application
* พัฒนา Streamlit Dashboard
* พัฒนา RAWG API Integration
* พัฒนา SQLite Database
* พัฒนา Service Layer
* เชื่อมต่อ API, Database และ Web UI

### Debugger / QA — ออม

Responsibilities:

* ทดสอบ Web Application
* ทดสอบ API Connection
* ทดสอบ Database Operations
* ตรวจสอบ Input และ Search
* ตรวจสอบ Error Handling
* ตรวจสอบ Data Flow
* บันทึกและติดตาม Bugs

---

## 10. Definition of Done

Sprint 2 จะถือว่าเสร็จเมื่อ:

* [ ] Web Application สามารถเปิดผ่าน Web Browser ได้
* [ ] มี Web Dashboard เบื้องต้น
* [ ] Dashboard สามารถแสดงข้อมูลเกมได้
* [ ] ระบบสามารถเชื่อมต่อ RAWG API ได้
* [ ] ระบบสามารถดึงข้อมูลเกมจริงได้
* [ ] ระบบสามารถจัดการ API Error ได้
* [ ] SQLite Database ถูกสร้างและใช้งานได้
* [ ] สามารถบันทึกข้อมูลเกมลง SQLite ได้
* [ ] สามารถอ่านข้อมูลเกมจาก SQLite ได้
* [ ] Web UI สามารถแสดงข้อมูลจาก Database ได้
* [ ] Search Game สามารถทำงานได้
* [ ] API, Database และ Web UI สามารถทำงานร่วมกันได้
* [ ] มีการทดสอบ Core Features ของ Sprint 2
* [ ] มีการแก้ไข Bugs ที่พบจากการทดสอบ
* [ ] Source Code ถูกจัดเก็บใน GitHub
* [ ] Documentation ของ Sprint 2 ถูกอัปเดต

---

## 11. Expected Result

เมื่อจบ Sprint 2 ระบบ Gaming Statistics Dashboard จะเปลี่ยนจาก CLI Application ใน Sprint 1 เป็น Web Application ที่สามารถใช้งานผ่าน Web Browser

ระบบจะสามารถ:

```text
User
  ↓
Web Dashboard
  ↓
Search / View Games
  ↓
Game Service
  ↓
SQLite Database
  ↕
RAWG API
```

โดย Sprint 2 จะเน้นการสร้างระบบพื้นฐานสำหรับ Web, API และ Database ก่อน ส่วนการวิเคราะห์ข้อมูลเชิงสถิติ การสร้าง Visualization และ Features การวิเคราะห์เพิ่มเติมจะพัฒนาต่อใน Sprint ถัดไป

---

## 12. Sprint 2 Deliverables

สิ่งที่ต้องส่งมอบเมื่อจบ Sprint 2:

* Web Application
* Streamlit Dashboard
* RAWG API Integration
* SQLite Database
* API Module
* Database Module
* Game Service
* Data Processing Module
* Dashboard Components
* Test Cases / QA Result
* Updated Sprint 2 Documentation
* Updated Change Log
* Updated Learning Log
* GitHub Commit / Pull Request สำหรับ Sprint 2
