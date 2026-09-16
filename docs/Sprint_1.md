# 🎮 Gaming Statistics Dashboard

# Sprint 1 — Result Report

## 1. Sprint Information

**Project:** Gaming Statistics Dashboard  
**Sprint:** Sprint 1 — Front-End CLI Development

### Team Roles

- **Planner:** คิม
- **Coder:** ฟลุ๊ค
- **Debugger:** ออม

---

# 2. Sprint Progress Summary

Sprint 1 มุ่งเน้นการสร้าง CLI Foundation ของ Gaming Statistics Dashboard

ผลการพัฒนา:

- [x] กำหนด Sprint Goal
- [x] กำหนด Sprint Scope
- [x] กำหนด Functional Requirements
- [x] กำหนด Definition of Done
- [x] พัฒนา Welcome Screen
- [x] พัฒนา Main Menu
- [x] พัฒนา Menu Navigation
- [x] พัฒนา View Games
- [x] พัฒนา Search Game
- [x] พัฒนา View Statistics
- [x] พัฒนา View Genres
- [x] พัฒนา View Top Rated Games
- [x] พัฒนา Input Validation
- [x] พัฒนา Search Validation
- [x] Invalid Input ไม่ทำให้โปรแกรม Crash
- [x] ทดสอบ QA Test Cases
- [x] Review Code
- [x] สร้าง GitHub Repository
- [ ] สร้าง Pull Request

---

# 3. Implemented Features

## Main Menu

```text
1. View Games
2. Search Game
3. View Statistics
4. View Genres
5. View Top Rated Games
0. Exit
```

## View Games

แสดงข้อมูลเกมทั้งหมดจาก Local Sample Dataset

Sprint 1 มีข้อมูลตัวอย่างทั้งหมด **8 เกม**

## Search Game

ผู้ใช้งานสามารถค้นหาเกมด้วยชื่อเกม

รองรับ:

- Partial Search
- Case-insensitive Search
- Empty Search Validation
- Unknown Game Handling

ตัวอย่าง:

```text
Search: portal
Result: Portal 2
```

## View Statistics

ระบบสามารถคำนวณ Basic Statistics จาก Local Sample Dataset

```text
Total Games: 8
Average Rating: 4.64
Highest Rating: 4.9
```

เกมที่มี Rating สูงที่สุดคือ:

```text
Baldur's Gate 3 — 4.9
```

## View Genres

ระบบสามารถแสดง Genre Summary จากข้อมูลเกมตัวอย่างได้

## View Top Rated Games

ระบบสามารถแสดงเกมโดยเรียงตาม Rating จากสูงไปต่ำได้

---

# 4. Sprint 1 Sample Dataset

Sprint 1 ใช้ Local Sample Dataset จำนวน 8 เกม

| Game | Rating | Genre | Platform |
|---|---:|---|---|
| Portal 2 | 4.6 | Puzzle | PC |
| The Witcher 3 | 4.8 | RPG | PC |
| Minecraft | 4.5 | Sandbox | Multi-platform |
| Hades | 4.7 | Action | Nintendo Switch |
| God of War | 4.7 | Action | PlayStation |
| Stardew Valley | 4.4 | Simulation | PC |
| Mario Kart 8 Deluxe | 4.5 | Racing | Nintendo Switch |
| Baldur's Gate 3 | 4.9 | RPG | PC |

Local Sample Dataset ถูกใช้เพื่อให้สามารถพัฒนาและทดสอบ Front-End CLI ได้โดยยังไม่ต้องพึ่งพา External API

---

# 5. Quality Assurance & Debugging Report

Sprint 1 มีการทดสอบทั้งหมด **14 Test Cases**

| No. | Test Case | Input / Action | Expected Result | Actual Result | Status |
|---:|---|---|---|---|---|
| 1 | Application Start | Run `main()` | แสดง Welcome Screen และ Main Menu | แสดงถูกต้อง | PASS |
| 2 | View Games | `1` | แสดงรายการเกม | แสดงเกมทั้ง 8 เกม | PASS |
| 3 | Valid Search | `Portal` | แสดง Portal 2 | แสดง Portal 2 | PASS |
| 4 | Case-insensitive Search | `portal` | แสดง Portal 2 | แสดง Portal 2 | PASS |
| 5 | View Statistics | `3` | แสดง Statistics | แสดงค่าถูกต้อง | PASS |
| 6 | View Genres | `4` | แสดง Genre Summary | แสดงถูกต้อง | PASS |
| 7 | View Top Games | `5` | เรียงเกมตาม Rating | เรียงถูกต้อง | PASS |
| 8 | Invalid Number | `99` | Warning และกลับ Main Menu | ทำงานถูกต้อง | PASS |
| 9 | Negative Number | `-1` | Warning และกลับ Main Menu | ทำงานถูกต้อง | PASS |
| 10 | Text Input | `abc` | Warning และไม่ Crash | ทำงานถูกต้อง | PASS |
| 11 | Blank Menu Input | Blank | Warning และไม่ Crash | ทำงานถูกต้อง | PASS |
| 12 | Empty Search | Blank | Search Warning | ทำงานถูกต้อง | PASS |
| 13 | Unknown Game | `XYZXYZ` | Game not found | แสดง Game not found | PASS |
| 14 | Exit | `0` | Goodbye และ Exit | ออกจากโปรแกรมถูกต้อง | PASS |

---

# 6. QA Summary

จากการทดสอบทั้ง 14 Test Cases:

- Test Cases ทั้งหมดผ่านการทดสอบ
- ไม่พบ Critical Defect ใน Sprint 1
- Normal Input ทำงานได้ตาม Requirements
- Invalid Input ไม่ทำให้ Application Crash
- Menu Navigation ทำงานได้ถูกต้อง
- Search Validation ทำงานได้ถูกต้อง
- Safe Exit ทำงานได้ถูกต้อง

---

# 7. Sprint Retrospective

## Wow! — สิ่งที่ทำได้ดี

CLI ถูกแบ่งออกเป็น Functions ที่มีหน้าที่ชัดเจน เช่น:

- Menu Display
- User Input
- Game Search
- Statistics
- Genre Summary
- Game Ranking

การแบ่งหน้าที่ของ Functions ทำให้ Code อ่านง่ายและสามารถพัฒนาต่อได้สะดวก

Input Validation สามารถจัดการ:

- Non-numeric Input
- Blank Input
- Negative Number
- Out-of-range Number
- Empty Search
- Unknown Game

ได้โดยไม่ทำให้โปรแกรม Crash

การใช้ Local Sample Dataset ยังช่วยให้สามารถสาธิต Front-End Features ได้โดยไม่ต้องพึ่งพา Backend หรือ External API ใน Sprint 1

---

## Whoops! — ปัญหาที่พบ

### Problem

ในระหว่างการพัฒนา เมื่อผู้ใช้งานกรอกค่าที่ไม่ใช่ตัวเลข เช่น:

```text
abc
```

ใน Menu Choice โปรแกรมสามารถเกิด `ValueError`

### Cause

ใน Version แรกมีการแปลง User Input เป็น Integer โดยตรง โดยยังไม่มีการจัดการ Non-numeric Input

### Solution

เพิ่ม:

- `.strip()`
- `try-except ValueError`
- Menu Range Validation
- Search Input Validation

### Result

หลังจากแก้ไข Application สามารถรองรับ:

- Text Input
- Blank Input
- Negative Number
- Out-of-range Menu Option
- Empty Search

ได้โดยไม่ Crash และสามารถกลับไปทำงานต่อที่ Main Menu ได้

---

# 8. Learning Summary

จาก Sprint 1 ทีมได้เรียนรู้:

- การออกแบบ Python CLI
- การแบ่ง Code ออกเป็น Functions
- Separation of Responsibilities
- Input Validation
- Exception Handling
- Normal-case Testing
- Edge-case Testing
- การทำงานตาม Sprint Goal และ Definition of Done
- การทำงานร่วมกันตามบทบาท Planner, Coder และ Debugger
- การใช้ GitHub สำหรับจัดเก็บและส่งมอบ Project

---

# 9. Sprint 1 Architecture

```text
User
  ↓
CLI
  ↓
Menu Navigation
  ↓
Input Validation
  ↓
Sprint 1 Local Sample Dataset
  ↓
Display Result
```

---

# 10. GitHub Submission

**Repository:**  
https://github.com/Phanuwatphk/Gaming-Statistics-Dashboard

**Pull Request:**  
`[Add Sprint 1 Pull Request URL]`

---

# 11. Sprint 1 Status

**STATUS: COMPLETE**
