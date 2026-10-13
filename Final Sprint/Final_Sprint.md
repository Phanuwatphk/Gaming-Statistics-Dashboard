# Gaming Statistics Dashboard — Final Sprint Report

**Final Term Project — CP352301 Script Programming**

**ช่วงตามแผน:** 2–6 October 2026
**วันตรวจ source/เอกสารส่งมอบ:** 13 October 2026
**สถานะ:** ตรวจโค้ดและ QA สำหรับ final commit; commit/push และ submission เป็นขั้นตอนของเจ้าของโปรเจกต์

## เป้าหมายและบทบาท

รวมระบบจาก Sprint 1–3 แก้ข้อผิดพลาด ตรวจ regression และเตรียมเอกสาร/source ให้ผู้อื่น clone แล้วรันได้

| สมาชิก | บทบาทตามแผน |
|:--|:--|
| คิม | Planner |
| ฟลุ๊ค | Coder |
| ออม | Debugger |

รอบตรวจนี้บันทึกสิ่งที่ยืนยันจาก source และการทดสอบ ไม่ได้ระบุ daily contribution หรือผลการนำเสนอที่ไม่มีหลักฐาน

## สิ่งที่ส่งมอบ

- Streamlit Home, Library, Search, Genres, Top Rated, Live Players, Details และ Statistics
- RAWG popularity snapshot 24 ชั่วโมง และ Steam snapshot 15 นาที แยก metadata/config
- Developer metadata โหลดเฉพาะ Details; cache ทั้งผลว่างและผลที่มีข้อมูล
- Rating ที่ยังไม่มีคะแนนแสดง N/A; optional/malformed fields ไม่ทำให้แอปล้ม
- SQLite migrations, upserts, rollback และการปิด connection หลังจบงาน
- Pagination 50 การ์ด; เปลี่ยนหน้าไม่ล้างการ์ดเดิมเมื่อ API ล้มเหลว
- Bulk import กำหนด ranges ในโค้ด, HTTP workers แยก sessions และ SQLite writer เดียว
- Statistics metrics รวม standard deviation, กราฟ 6 ชุด และ comparison
- Config กลาง, package/script imports, runtime/dev dependencies และ CI
- Source attribution ใน sidebar และ snapshot ตั้งต้นใน repository

## ปัญหาที่ตรวจพบและแก้ไข

| ปัญหา | ผลลัพธ์หลังแก้ |
|:--|:--|
| โหลดผู้พัฒนาทุกเกมใช้คำขอมาก | รายชื่อเกมไม่มีคำขอเพิ่ม; Details ใช้ 1 request เมื่อยังไม่มี cache |
| RAWG กับ Steam ใช้ interval เดียว | RAWG 24 ชั่วโมง; Steam 15 นาที |
| API pagination ล้มเหลวแล้วการ์ดหาย | เก็บหน้าปัจจุบันและแสดง error |
| RAWG rating=0 แสดงเหมือนคะแนนจริง | แสดง N/A รวม snapshot เก่า |
| รายการผิดรูปแบบ/NaN/Infinity | Normalize เป็น missing หรือข้าม record ที่ใช้ไม่ได้ |
| Home อ่านทั้งฐานแล้วตัดเหลือ 50 | จำกัดที่ SQL ก่อน decode |
| Statistics เตรียมข้อมูลซ้ำ | ใช้ DataFrame ร่วมกัน |
| SQLite connection ไม่ปิดทันที | ปิดหลัง commit/rollback |
| Relative paths/package imports ไม่สม่ำเสมอ | Config ร่วมและตรวจจากโฟลเดอร์อื่น |
| Scripts ถูก ignore แต่ tests/docs ต้องใช้ | import scripts ไม่ถูก ignore; CLI เก่าเก็บเป็นประวัติและไม่อยู่ใน test suite ของเว็บแอป |

## ผลตรวจ

หลักฐาน คำสั่ง จำนวน tests และขอบเขตการตรวจอยู่ใน [Final QA](../docs/FINAL_QA.md) ซึ่งเป็นรายงานอ้างอิงเดียวสำหรับตัวเลขผลตรวจ เพื่อไม่ให้หลายเอกสารระบุจำนวน tests ต่างกัน

การวัดระหว่างปรับประสิทธิภาพด้วยข้อมูลประมาณ 40,000 เกม: การอ่าน Home เดิมประมาณ 1.6 วินาที เทียบ SQL LIMIT ประมาณ 25 ms; การเตรียม/คำนวณสถิติชุดเดียวกันประมาณ 0.79 เทียบ 0.23 วินาที เป็นผลเฉพาะงานข้อมูลในเครื่อง ไม่ใช่ benchmark เวลาโหลดเว็บหรือ SLA

## ข้อจำกัดและการส่งมอบ

SQLite snapshot ไม่ใช่ cloud storage ถาวร และการเปลี่ยนข้อมูลบน Streamlit instance ไม่ sync กลับ GitHub ข้อมูล API และรูปอาจไม่สมบูรณ์ Steam Top อาจมีน้อยกว่า 100 เกม

รอบตรวจในเครื่องไม่อ้างว่า CI บน GitHub, deployment ของ final commit หรือ presentation/submission ผ่านแล้ว ให้เจ้าของโปรเจกต์ตรวจ diff, commit/push และตรวจ branch ที่ deploy จริง

วิธีติดตั้งและรันอยู่ใน [README](../README.md) รายงาน Sprint 1–3 เก็บไว้เป็นประวัติของรุ่นก่อนหน้า
