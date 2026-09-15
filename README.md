# 🎮 Gaming Statistics Dashboard

A Python-based application for exploring and analyzing video game information such as ratings, genres, platforms, and other gaming statistics.

This project is developed as part of the **CP352301 Script Programming** course.

---

## 📌 Project Overview

Gaming data such as ratings, genres, platforms, and release information can be difficult to explore when distributed across large datasets.

**Gaming Statistics Dashboard** aims to provide a simple application that allows users to search, explore, and analyze video game information through an easy-to-use interface.

The final project is planned to use the **RAWG Video Games Database API** as the primary external data source.

- RAWG Website: https://rawg.io/
- RAWG API: https://api.rawg.io/

---

## 🚀 Sprint 1 — Front-End App Development

Sprint 1 focuses on building the **Command Line Interface (CLI)** foundation of the application.

### Sprint Goal

Build a functional CLI that provides:

- Menu navigation
- User input handling
- Input validation
- Error handling
- Basic game-data exploration
- Safe program termination

A small **local sample dataset** is used during Sprint 1.

> The RAWG API is planned for a future Sprint and is not integrated into the Sprint 1 implementation.

---

## ✨ Sprint 1 Features

The current CLI provides the following menu:

```text
============================================================
             GAMING STATISTICS DASHBOARD
============================================================

1. View Games
2. Search Game
3. View Statistics
4. View Genres
5. View Top Rated Games
0. Exit
```

### Implemented Features

- View all sample games
- Search games by name
- Case-insensitive and partial-name searching
- View basic gaming statistics
- View genre summary
- View games ranked by rating
- Validate invalid menu input
- Handle blank input
- Handle unknown game searches
- Safe application exit

---

## 🏗️ Sprint 1 Architecture

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

## 🛠️ Technologies

### Sprint 1

- Python 3
- Google Colab
- GitHub

### Planned for Future Sprints

- RAWG Video Games Database API
- Pandas
- SQLite
- Data Visualization
- Streamlit
- pytest
- GitHub Actions / CI/CD

---

## ▶️ How to Run

### Google Colab

1. Open `Sprint_1.ipynb` in Google Colab.
2. Run the Sprint 1 Python code cell.
3. Run the CLI demonstration cell:

```python
main()
```

4. Select a menu option from `0–5`.
5. Follow the instructions displayed by the application.

No API key or additional package installation is required for Sprint 1.

---

## 🧪 Testing

Sprint 1 includes QA testing for:

- Application startup
- All main menu features
- Valid game search
- Case-insensitive search
- Unknown game search
- Empty search input
- Invalid numeric menu input
- Negative menu input
- Non-numeric menu input
- Blank menu input
- Safe program exit

Detailed test cases and results are documented in `Sprint_1.ipynb`.

---

## 👥 Team Roles

| Role | Member |
|---|---|
| Planner | คิม |
| Coder | ฟลุ๊ค |
| Debugger | ออม |

---

## 📂 Repository Structure

```text
gaming-statistics-dashboard/
│
├── README.md
└── Sprint_1.ipynb
```

The repository structure will be expanded in future Sprints as backend, data processing, testing, and deployment components are introduced.

---

## 🔮 Future Development

Future Sprints are planned to extend the project with:

- RAWG API integration
- Data processing
- File I/O and persistent storage
- Search, filter, and sort functionality
- Gaming statistics and analysis
- Data visualization
- Web-based dashboard
- Automated testing
- CI/CD

---

## 📊 Sprint 1 Status

**Sprint 1 — Front-End CLI Development**

✅ CLI implemented  
✅ Menu navigation implemented  
✅ Input validation implemented  
✅ Basic features implemented  
✅ QA testing completed  

**Status: COMPLETE**