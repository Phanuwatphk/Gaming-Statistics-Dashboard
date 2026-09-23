# 🎮 Gaming Statistics Dashboard

เว็บแอป Streamlit สำหรับค้นหา สำรวจ และเปรียบเทียบข้อมูลเกมจาก RAWG พร้อมแสดงอันดับเกม Steam Top 100 ตามจำนวนผู้เล่นปัจจุบัน

## Features

- หน้า Home แสดงเกมยอดนิยมที่ดึงจาก RAWG และยอดรวมผู้เล่นของ Steam Top 100
- Game Library สำหรับเรียกดู กรอง และเปรียบเทียบเกมที่บันทึกไว้
- ค้นหาจาก RAWG แล้วบันทึกผลลง SQLite
- สำรวจเกมตาม Genre และจัดอันดับตาม Rating
- หน้า Live Players แสดงอันดับ Steam ล่าสุด พร้อมจำนวนผู้เล่นและเวลาอัปเดต
- ใช้ SQLite เก็บข้อมูลและ snapshot ร่วมกัน เพื่อลดการเรียก API ซ้ำ

## Data sources

- [RAWG Video Games Database API](https://rawg.io/apidocs) สำหรับรายละเอียดเกมและรายการเกมยอดนิยม
- Steam Store และ Steam Web API สำหรับข้อมูลเกมและจำนวนผู้เล่นปัจจุบัน

## Run the app

ต้องใช้ Python 3.10+ และ dependencies ตาม `requirements.txt`.

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
cp .env.example .env
# ใส่ RAWG API key ของคุณใน .env
streamlit run src/app.py
```

แอปจะเปิดที่ URL ที่ Streamlit แสดงในเทอร์มินัล

## Configuration

| Variable | Required | Description |
| --- | --- | --- |
| `RAWG_API_KEY` | Yes | API key สำหรับดึงข้อมูลจาก RAWG |
| `PLAYER_REFRESH_MINUTES` | No | อายุ snapshot ของ RAWG และ Steam Top 100 เป็นนาที; ค่าเริ่มต้น `15`, ใช้ `0` เพื่อ refresh ทุกครั้ง |
| `GAMING_DASHBOARD_DB` | No | ตำแหน่งไฟล์ SQLite; ค่าเริ่มต้นคือ `data/gaming_statistics.db` |

อย่า commit ไฟล์ `.env` เพราะมี API key. ใช้ `.env.example` เป็นแม่แบบแทน

## Tests

```bash
python -m pytest -q
```

## Project structure

```text
src/
├── api/          # RAWG และ Steam clients
├── components/   # Streamlit dashboard และ styles
├── database/     # SQLite persistence
├── services/     # application workflows
└── utils/        # data normalization และ time helpers
tests/            # automated tests
docs/             # project plan และเอกสาร Sprint
Sprint1/, Sprint2/# historical sprint reports
```

เอกสารแผนและรายงานของแต่ละ Sprint อยู่ใน `docs/`, `Sprint1/` และ `Sprint2/`; เอกสารเหล่านั้นเก็บบริบทของช่วงเวลาที่จัดทำไว้ จึงอาจอธิบายสถานะการพัฒนาในอดีต.
