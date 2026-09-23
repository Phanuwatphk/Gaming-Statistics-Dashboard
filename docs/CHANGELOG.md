# Changelog

All notable changes to the Gaming Statistics Dashboard project will be documented in this file.

## [Unreleased] - Dashboard pagination and data snapshots

### Added

- Added 50-card pagination for Home, Game Library, Search, Genres, Top Rated,
  and Live Players.
- Added Previous/Next navigation for remote RAWG result pages on Home and Search.
- Added persistent RAWG catalog positions in SQLite so Home retains the API order
  across pages.
- Added ordered database retrieval by game ID for preserving the API response order.
- Added a configurable RAWG page argument to the RAWG client.
- Added tests for fixed-size RAWG page requests and consecutive 50-game windows.

### Changed

- Changing a navigation page or a list page now returns the viewport to the top.
- Home continues its popular-game feed from RAWG after the stored page instead of
  only paginating the local list.
- Search now distinguishes local results from RAWG results: local matches paginate
  only in SQLite, while remote results request subsequent RAWG pages.
- RAWG multi-request reads use fixed 40-record API pages before slicing the
  requested display window, preventing duplicate or skipped games at page bounds.
- Updated `.env.example` comments to describe the RAWG key, shared refresh interval,
  and optional SQLite database location.

### Fixed

- Fixed inconsistent Home ordering caused by sorting a mixed SQLite game library;
  the RAWG discovery sequence is now stored separately from general library order.
- Fixed long card pages sometimes remaining at the old scroll position after a
  Streamlit rerun.

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
