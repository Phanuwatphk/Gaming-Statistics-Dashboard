# Changelog

All notable changes to the **Gaming Statistics Dashboard** project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project follows Semantic Versioning.

---
## [v0.2.0] - Sprint 2: Web Application, API & Database

### Added

- Added Streamlit Web Application.
- Added Web Dashboard with navigation.
- Added RAWG API integration for real game data.
- Added RAWG game search and pagination.
- Added Steam API integration.
- Added Steam current player count.
- Added Steam Top 100 / Live Players feature.
- Added SQLite database for game data storage.
- Added Game Service for application logic.
- Added data processing and data normalization.
- Added Game Library.
- Added Genre, Platform, and Rating filters.
- Added Top Rated Games page.
- Added Game Detail page.
- Added pagination for game data.
- Added API and database error handling.
- Added empty-state handling for unavailable data.
- Added Steam player data refresh and snapshot system.
- Added automated tests for API, database, service, and data processing modules.
- Added Sprint 2 daily task allocation and contribution metrics.

### Changed

- Changed the application from CLI to Web Application.
- Changed game data source from local sample data to RAWG API.
- Changed data management from local data to SQLite database.
- Updated project structure by separating API, database, service, data processing, and UI components.
- Updated game search and data retrieval workflow.
- Updated error handling for API and database operations.

### Fixed

- Fixed handling of API errors and unavailable data.
- Fixed data format inconsistencies from API responses.
- Fixed handling of missing game information.
- Fixed large game data display by adding pagination.

## Planner / Coder / Debugger Roles

| สมาชิก | ชื่อเล่น | Role | หน้าที่ |
|---|---|---|---|
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค | Planner | Defined Sprint 2 scope, requirements, Web Application plan, system architecture, task allocation, and Sprint 2 documentation. |
| นายเดโชชิต โตวินัส | ออม | Coder | Developed the Streamlit Web Application, RAWG API, Steam API, SQLite database, Game Service, data processing, and application features. |
| นายชิษณุพงศ์ ซู | คิม | Debugger / QA | Tested Web Application, APIs, database, data processing, error handling, edge cases, and verified Sprint 2 features. |

---

## [v0.1.0] - Sprint 1: CLI Foundation

### Added

- Created Gaming Statistics Dashboard project.
- Added project structure and documentation files.
- Added CLI application with main menu and navigation.
- Added local sample game dataset.
- Added game search functionality.
- Added game statistics functionality.
- Added genre and top-rated game views.
- Added input validation and error handling.
- Added Sprint 1 testing and QA test cases.
- Added Sprint 1 daily task allocation and contribution metrics.

### Changed

- Updated project documentation based on Sprint 1 requirements.
- Updated project plan and Sprint 1 documentation.
- Updated Learning Log and Change Log for Sprint 1.

## Planner / Coder / Debugger Roles

| สมาชิก | ชื่อเล่น | Role | หน้าที่ |
|---|---|---|---|
| นายชิษณุพงศ์ ซู | คิม | Planner | Defined the project scope, requirements, Sprint 1 plan, documentation, and daily task allocation. |
| นายภานุวัฒน์ ผองแก้ว | ฟลุ๊ค | Coder | Developed the CLI application, main menu, game search, statistics, genres, top-rated games, and input validation. |
| นายเดโชชิต โตวินัส | ออม | Debugger / QA | Tested system functions, checked invalid inputs and edge cases, and verified the results of Sprint 1 features. |
