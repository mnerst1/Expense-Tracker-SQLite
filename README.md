# Day 006 — Expense Tracker — SQLite

A lightweight command-line expense tracker built with **Python and SQLite**.

<img width="700" alt="{C87219B1-3AA7-4FD8-9868-FA25B452B5A2}" src="https://github.com/user-attachments/assets/d0751f53-409b-40fa-8b92-ae0f7c3a8b48" />


---

## 🇬🇧 English

### 📖 About

**Expense Tracker** is a command-line application for storing, managing, and analyzing personal expenses.

The application uses **SQLite** for persistent data storage, which means your expenses remain saved even after the program is closed.

### ✨ Features

- ➕ Add new expenses
- 📋 View all expenses
- 🗑️ Delete expenses
- 🔎 Search expenses by category
- 💰 Calculate total spending
- 📊 View spending statistics by category
- 💾 Persistent SQLite database
- 📅 Store expense dates
- ✅ Input validation
- 🧹 Simple command-line interface

### 🛠️ Technologies

- Python 3
- SQLite
- SQL
- Git

---

## 🇰🇿 Қазақша

### 📖 Жоба туралы

**Expense Tracker** — жеке шығындарды сақтау, басқару және талдауға арналған консольдік бағдарлама.

Бағдарлама деректерді тұрақты сақтау үшін **SQLite** деректер базасын пайдаланады. Бағдарламаны жапқаннан кейін де барлық шығындар сақталады.

### ✨ Мүмкіндіктер

- ➕ Жаңа шығын қосу
- 📋 Барлық шығындарды көру
- 🗑️ Шығындарды жою
- 🔎 Санат бойынша іздеу
- 💰 Жалпы шығын сомасын есептеу
- 📊 Санаттар бойынша статистиканы көру
- 💾 SQLite деректер базасында сақтау
- 📅 Шығын күнін сақтау
- ✅ Енгізілген деректерді тексеру
- 🧹 Қарапайым консольдік интерфейс

### 🛠️ Технологиялар

- Python 3
- SQLite
- SQL
- Git

---

## 🇷🇺 Русский

### 📖 О проекте

**Expense Tracker** — консольное приложение для хранения, управления и анализа личных расходов.

Программа использует базу данных **SQLite**, поэтому все добавленные расходы сохраняются даже после закрытия приложения.

### ✨ Возможности

- ➕ Добавление новых расходов
- 📋 Просмотр всех расходов
- 🗑️ Удаление расходов
- 🔎 Поиск расходов по категории
- 💰 Подсчёт общей суммы расходов
- 📊 Статистика расходов по категориям
- 💾 Постоянное хранение данных в SQLite
- 📅 Хранение даты расхода
- ✅ Проверка введённых данных
- 🧹 Простой консольный интерфейс

### 🛠️ Технологии

- Python 3
- SQLite
- SQL
- Git

---

## 📁 Project Structure

```text
Day-006-Expense-Tracker/
│
├── main.py
├── database.py
├── README.md
└── .gitignore
```

The SQLite database file `expenses.db` is generated automatically when the application runs and is not stored in the repository.

---

## 🗄️ Database

The application uses an SQLite database with an `expenses` table.

```sql
CREATE TABLE expenses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    category TEXT NOT NULL,
    amount REAL NOT NULL,
    expense_date TEXT NOT NULL,
    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
```

### SQL operations practiced

```sql
CREATE TABLE
INSERT
SELECT
WHERE
DELETE
SUM
COUNT
GROUP BY
ORDER BY
```

---

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project directory

```bash
cd Expense-Tracker-SQLite
```

### 3. Run the application

```bash
python main.py
```

No external Python packages are required.

---

## 💻 Example

```text
========================================
           EXPENSE TRACKER
========================================

1. Add expense
2. View expenses
3. Delete expense
4. Search by category
5. Total spending
6. Category statistics
0. Exit

Choose an option:
```

---

## 🧠 What I Practiced

During this project I practiced:

- Python functions
- Working with modules
- SQLite databases
- SQL queries
- CRUD operations
- Input validation
- Exception handling
- Persistent data storage
- Database connections
- Working with user input
- Git and version control

---

## 🎯 365 Days of Code

| Day | Project | Technology |
|---|---|---|
| Day 001 | Password Generator | Python |
| Day 002 | Multilingual Calculator | C# / WPF |
| Day 003 | StudyFlow | Kotlin / Android |
| Day 004 | Text Analyzer | Python |
| Day 005 | TaskFlow | HTML / CSS / JavaScript |
| **Day 006** | **Expense Tracker** | **Python / SQLite / SQL** |

---

## 📌 Challenge Progress

```text
Day 001  ████████████████████  Completed
Day 002  ████████████████████  Completed
Day 003  ████████████████████  Completed
Day 004  ████████████████████  Completed
Day 005  ████████████████████  Completed
Day 006  ████████████████████  Completed
Day 007  ░░░░░░░░░░░░░░░░░░░░  Next
```

**6 / 365 days completed** 🚀

---

## 👨‍💻 Author

Developed by **Miras**.

Part of my **365 Days of Code** challenge.

---

⭐ If you found this project useful, feel free to star the repository.
