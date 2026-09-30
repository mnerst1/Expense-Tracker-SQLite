import sqlite3
from math import isfinite


# Название файла нашей базы данных.
DATABASE_NAME = "expenses.db"


def get_connection():
    """
    Создаёт подключение к SQLite.

    Если expenses.db ещё не существует,
    SQLite автоматически создаст файл.
    """

    connection = sqlite3.connect(DATABASE_NAME)

    return connection


def create_database():
    """
    Создаёт таблицу расходов.

    IF NOT EXISTS нужен для того,
    чтобы программа не пыталась создавать
    таблицу повторно при каждом запуске.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL CHECK(amount > 0),
            expense_date TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
        """
    )

    # Сохраняем изменения.
    connection.commit()

    # Закрываем соединение.
    connection.close()


def add_expense(
    title,
    category,
    amount,
    expense_date
):
    """
    Добавляет новый расход.
    """

    if not isfinite(amount) or amount <= 0:
        raise ValueError("Amount must be finite and greater than 0.")

    connection = get_connection()

    cursor = connection.cursor()

    # Вместо вставки значений прямо в SQL
    # используем параметры ?.
    #
    # Это правильнее и безопаснее.
    cursor.execute(
        """
        INSERT INTO expenses (
            title,
            category,
            amount,
            expense_date
        )
        VALUES (?, ?, ?, ?)
        """,
        (
            title,
            category,
            amount,
            expense_date
        )
    )

    connection.commit()

    connection.close()


def get_all_expenses():
    """
    Возвращает все расходы.

    Новые записи отображаются первыми.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            title,
            category,
            amount,
            expense_date
        FROM expenses
        ORDER BY expense_date DESC, id DESC
        """
    )

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def delete_expense(expense_id):
    """
    Удаляет расход по его ID.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        DELETE FROM expenses
        WHERE id = ?
        """,
        (expense_id,)
    )

    # rowcount покажет,
    # была ли реально удалена строка.
    deleted = cursor.rowcount

    connection.commit()

    connection.close()

    return deleted > 0


def search_by_category(category):
    """
    Ищет расходы по категории.

    COLLATE NOCASE делает сравнение
    нечувствительным к регистру.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            id,
            title,
            category,
            amount,
            expense_date
        FROM expenses
        WHERE category = ? COLLATE NOCASE
        ORDER BY expense_date DESC
        """,
        (category,)
    )

    expenses = cursor.fetchall()

    connection.close()

    return expenses


def get_total_amount():
    """
    Возвращает сумму всех расходов.
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(amount), 0)
        FROM expenses
        """
    )

    total = cursor.fetchone()[0]

    connection.close()

    return total


def get_category_statistics():
    """
    Группирует расходы по категориям.

    Например:

    Food      -> 15000
    Transport -> 8000
    Study     -> 5000
    """

    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT
            category,
            COUNT(*) AS expense_count,
            SUM(amount) AS total
        FROM expenses
        GROUP BY category
        ORDER BY total DESC
        """
    )

    statistics = cursor.fetchall()

    connection.close()

    return statistics
