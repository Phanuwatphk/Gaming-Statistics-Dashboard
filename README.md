# Gaming Statistics Dashboard

> **Final Term Project — CP352301 Script Programming**

เว็บแอปพลิเคชันสำหรับรวบรวม จัดการ วิเคราะห์ และนำเสนอข้อมูลวิดีโอเกมผ่าน Dashboard โดยเชื่อมต่อ **RAWG API** และ **Steam API** พร้อมจัดเก็บข้อมูลด้วย **SQLite**

## 👥 Team Members & Sprint Roles

ทีมใช้แนวทาง **Role Rotation** โดยสมาชิกทั้ง 3 คนหมุนเวียนบทบาท **Planner, Coder และ Debugger** ในแต่ละ Sprint เพื่อให้ทุกคนมีประสบการณ์ทั้งด้านการวางแผน การพัฒนา และการทดสอบระบบ

| Member | Sprint 1<br>10–15 Sep | Sprint 2<br>20–24 Sep | Sprint 3<br>25–29 Sep | Final Sprint<br>2–6 Oct |
|:--|:--|:--|:--|:--|
| **คิม** | Planner | Debugger | Coder | Planner |
| **ฟลุ๊ค** | Coder | Planner | Debugger | Coder |
| **ออม** | Debugger | Coder | Planner | Debugger |

### Role Responsibilities

| Role | Responsibilities |
|:--|:--|
| **Planner** | กำหนด Sprint Goal / Scope, วางแผนงาน, แบ่ง Task, ติดตาม Progress และดูแล Sprint Documentation |
| **Coder** | พัฒนา Feature, แก้ไข Source Code, Integration และ Implement งานตาม Sprint Scope |
| **Debugger** | จัดทำ Test Cases, ทดสอบระบบ, ตรวจสอบ Bug, Regression Testing และ QA |

## 📌 Project Overview

### Problem

ข้อมูลเกม เช่น Rating, Genre, Platform, Release Date, Metacritic Score และ Steam Players กระจายอยู่หลายแหล่ง ทำให้การค้นหา สำรวจ วิเคราะห์ และเปรียบเทียบทำได้ไม่สะดวก

### Proposed Solution

**Gaming Statistics Dashboard** รวมข้อมูลเกมไว้ในระบบเดียวผ่าน Web Browser และรองรับการ **Search, Filter, Sort, Statistics, Visualization** และ **Game Comparison**

## 🎯 Project Goals

- พัฒนา Web Application ด้วย Python และ Streamlit
- เชื่อมต่อ External APIs
- Normalize และจัดการข้อมูล
- จัดเก็บข้อมูลด้วย SQLite
- สร้าง Statistics และ Data Visualization
- เพิ่ม Filtering, Sorting และ Game Comparison
- ทดสอบและเตรียมระบบสำหรับ Final Delivery
- จัดทำ Documentation ให้ตรงกับระบบจริง

## 🛠️ Technology Stack

| Technology | Purpose |
|:--|:--|
| **Python** | Programming Language |
| **Streamlit** | Web Application / Dashboard |
| **RAWG API** | Game Information |
| **Steam API** | Steam Player Information |
| **SQLite** | Local Database |
| **Pandas** | Data Processing & Analysis |
| **pytest** | Automated Testing |
| **python-dotenv** | Environment / API Configuration |
| **Git / GitHub** | Version Control |

## 🏗️ System Architecture

```text
User / Web Browser
        ↓
Streamlit UI / Dashboard
        ↓
Game Service
   ↙          ↘
RAWG API    Steam API
   ↘          ↙
Data Processing / Normalize
        ↓
SQLite Database
        ↓
Analysis / Statistics / Visualization
        ↓
Statistics Page
```

## ✨ Main Features

### Game Library

- Game Search
- Game Detail
- Genre View
- Top Rated Games
- Pagination
- Rating / Genre / Platform / Release Date
- Metacritic Score

### Data Exploration

- Genre Filter
- Platform Filter
- Minimum Rating
- Release Year
- Sort by Rating, Release Date, Name
- Ascending / Descending
- Missing-value handling

### Statistics & Analysis

- Count, Mean, Median, Minimum, Maximum, Standard Deviation
- Genre Frequency / Proportion
- Platform Frequency / Proportion
- Average Rating by Genre
- Release Year Distribution
- Metacritic Analysis
- Steam Current Players / Top Players
- Game Comparison

### Data Visualization

1. Genre Distribution
2. Platform Distribution
3. Rating by Genre
4. Release Year Distribution
5. Metacritic Score Distribution
6. Top Live Steam Players

### Game Comparison

เปรียบเทียบเกม 2 เกมในด้าน **Rating, Metacritic และ Steam Players**

## 🔄 Project Development Journey

```text
Sprint 1
Application Foundation / CLI
        ↓
Review / Feedback
        ↓
Sprint 2
Web UI + API + SQLite
        ↓
Sprint 3
Data Processing + Analysis
+ Visualization + Advanced Features
        ↓
Final Sprint
Final Integration + QA
+ Bug Fixing + Documentation
        ↓
Final Project
```

## 🗓️ Sprint Overview

| Sprint | Period | Main Focus | Status |
|:--|:--|:--|:--|
| **Sprint 1** | 10–15 Sep 2026 | Application Foundation / CLI | ✅ Completed |
| **Sprint 2** | 20–24 Sep 2026 | Web UI / API / Database | ✅ Completed |
| **Sprint 3** | 25–29 Sep 2026 | Data Processing / Analysis / Visualization / Advanced Features | ✅ Completed |
| **Final Sprint** | 2–6 Oct 2026 | Integration / Testing / QA / Finalization | ⏳ Planned |

### Sprint 1 — Application Foundation

สร้างพื้นฐานระบบในรูปแบบ CLI: Project Planning, Main Menu, Navigation, Game Search, Statistics, Genres, Top Rated Games, Input Validation, Exception Handling และ Initial Testing

### Sprint 2 — Web Application

เปลี่ยนจาก CLI สู่ Web Application และเพิ่ม Streamlit, RAWG API, Steam API, SQLite, Game Service, Data Processing, Search, Pagination, Game Detail และ Live Players

### Sprint 3 — Data Analysis & Advanced Features

เพิ่ม Data Cleaning / Preparation, Data Normalization, EDA, Descriptive Statistics, Statistics Page, Data Visualization, Advanced Filtering, Sorting, Game Comparison และ Empty State Handling

### 🚀 Final Sprint — Final Integration & Delivery

เน้น Final Integration, Bug Fixing, Full Regression Testing, Final QA, Data/API/Database Verification, UI/UX Verification, Documentation และ Final Delivery

> Final Sprint เน้น **Stabilization และ Finalization** มากกว่าการเพิ่ม Feature ขนาดใหญ่ใหม่

## 🧪 Testing & Quality Assurance

```text
Feature Development
       ↓
Functional Testing
       ↓
Edge Case Testing
       ↓
Integration Testing
       ↓
Regression Testing
       ↓
Final QA
       ↓
Final Release
```

เครื่องมือหลัก: **pytest**

การทดสอบครอบคลุม Application Flow, API, Database, Data Processing, Statistics, Visualization, Search, Filter, Sort, Comparison, Error Handling, Empty State และ Regression

> ผล Pass / Fail ของ Final QA จะสรุปตามผลการทดสอบจริงหลังจบ Final Sprint

## 📁 Project Structure

```text
Gaming-Statistics-Dashboard/
├── README.md
├── docs/
│   ├── Project_Pitch.md
│   ├── Plan.md
│   ├── CHANGELOG.md
│   └── LEARNINGLOG.md
├── Sprint1/Sprint_1.md
├── Sprint2/Sprint_2.md
├── Sprint3/Sprint_3.md
├── Final Sprint/Final_Sprint.md
├── src/
│   ├── analysis/
│   ├── api/
│   ├── components/
│   ├── database/
│   ├── services/
│   ├── utils/
│   └── app.py
├── tests/
├── requirements.txt
└── .env
```

## 📚 Documentation

| File | Purpose |
|:--|:--|
| `README.md` | ภาพรวม Project |
| `docs/Project_Pitch.md` | Problem, Solution และ Project Direction |
| `docs/Plan.md` | แผนการพัฒนาและ Sprint |
| `docs/CHANGELOG.md` | บันทึกการเปลี่ยนแปลง |
| `docs/LEARNINGLOG.md` | สิ่งที่ทีมเรียนรู้ |
| `Sprint1/Sprint_1.md` | รายละเอียด Sprint 1 |
| `Sprint2/Sprint_2.md` | รายละเอียด Sprint 2 |
| `Sprint3/Sprint_3.md` | รายละเอียด Sprint 3 |
| `Final Sprint/Final_Sprint.md` | รายละเอียด Final Sprint |

## 📌 Current Project Status

**Project:** Gaming Statistics Dashboard  
**Course:** CP352301 Script Programming

| Sprint | Status |
|:--|:--|
| Sprint 1 | ✅ Completed |
| Sprint 2 | ✅ Completed |
| Sprint 3 | ✅ Completed |
| Final Sprint | ⏳ Planned |

ปัจจุบันระบบมี Web Application ที่เชื่อมต่อ RAWG API, Steam API และ SQLite Database พร้อม Game Library, Data Processing, Statistics, Visualization, Filtering, Sorting และ Game Comparison

## 🚀 Final Sprint

**Period:** 2–6 October 2026  
**Duration:** 5 Days

| Role | Member |
|:--|:--|
| Planner | **คิม** |
| Coder | **ฟลุ๊ค** |
| Debugger | **ออม** |

> Final Sprint จะสรุปผลจริงจากการทดสอบและการดำเนินงาน โดยไม่ระบุ Pass/Fail หรือ Performance ที่ยังไม่มีหลักฐาน

## 🔗 Repository

**GitHub:** https://github.com/Phanuwatphk/Gaming-Statistics-Dashboard

**CP352301 Script Programming — Final Term Project**

*From Game Data to Gaming Statistics Dashboard*
