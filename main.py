from datetime import datetime

from database import (
    create_database,
    add_expense,
    get_all_expenses,
    delete_expense,
    search_by_category,
    get_total_amount,
    get_category_statistics
)


def print_header():
    """
    Выводит название приложения.
    """

    print()
    print("=" * 60)
    print("                 EXPENSE TRACKER")
    print("=" * 60)


def print_menu():
    """
    Главное меню.
    """

    print()
    print("1. Add expense")
    print("2. Show all expenses")
    print("3. Search by category")
    print("4. Delete expense")
    print("5. Show total")
    print("6. Category statistics")
    print("0. Exit")
    print()


def format_money(amount):
    """
    Красиво форматирует денежную сумму.

    15000 -> 15 000.00 ₸
    """

    return f"{amount:,.2f} ₸".replace(",", " ")


def print_expenses(expenses):
    """
    Выводит список расходов.
    """

    if not expenses:

        print()
        print("No expenses found.")

        return

    print()

    print(
        f"{'ID':<5}"
        f"{'TITLE':<24}"
        f"{'CATEGORY':<18}"
        f"{'AMOUNT':>15}"
        f"{'DATE':>14}"
    )

    print("-" * 76)

    for expense in expenses:

        expense_id = expense[0]
        title = expense[1]
        category = expense[2]
        amount = expense[3]
        date = expense[4]

        # Ограничиваем длинный текст,
        # чтобы таблица не ломалась.
        short_title = title[:21]

        short_category = category[:15]

        print(
            f"{expense_id:<5}"
            f"{short_title:<24}"
            f"{short_category:<18}"
            f"{format_money(amount):>15}"
            f"{date:>14}"
        )


def input_amount():
    """
    Запрашивает сумму и проверяет,
    что пользователь ввёл число больше нуля.
    """

    while True:

        value = input(
            "Amount: "
        ).strip()

        # Разрешаем вводить:
        #
        # 1500.50
        #
        # или:
        #
        # 1500,50
        value = value.replace(
            ",",
            "."
        )

        try:

            amount = float(value)

            if amount <= 0:

                print(
                    "Amount must be greater than 0."
                )

                continue

            return amount

        except ValueError:

            print(
                "Please enter a valid number."
            )


def input_date():
    """
    Запрашивает дату.

    Если оставить поле пустым,
    используется сегодняшняя дата.
    """

    while True:

        value = input(
            "Date (YYYY-MM-DD, Enter = today): "
        ).strip()

        if not value:

            return datetime.now().strftime(
                "%Y-%m-%d"
            )

        try:

            # Проверяем, существует ли такая дата.
            datetime.strptime(
                value,
                "%Y-%m-%d"
            )

            return value

        except ValueError:

            print(
                "Invalid date. Example: 2026-09-25"
            )


def handle_add_expense():
    """
    Добавление нового расхода.
    """

    print()
    print("--- Add Expense ---")

    title = input(
        "Title: "
    ).strip()

    if not title:

        print(
            "Title cannot be empty."
        )

        return

    category = input(
        "Category: "
    ).strip()

    if not category:

        print(
            "Category cannot be empty."
        )

        return

    amount = input_amount()

    expense_date = input_date()

    add_expense(
        title,
        category,
        amount,
        expense_date
    )

    print()
    print("Expense added successfully.")


def handle_show_expenses():
    """
    Показывает все расходы.
    """

    expenses = get_all_expenses()

    print_expenses(
        expenses
    )


def handle_search():
    """
    Поиск расходов по категории.
    """

    print()
    print("--- Search by Category ---")

    category = input(
        "Category: "
    ).strip()

    if not category:

        print(
            "Category cannot be empty."
        )

        return

    expenses = search_by_category(
        category
    )

    print_expenses(
        expenses
    )


def handle_delete():
    """
    Удаление расхода.
    """

    print()
    print("--- Delete Expense ---")

    try:

        expense_id = int(
            input(
                "Expense ID: "
            )
        )

    except ValueError:

        print(
            "ID must be a number."
        )

        return

    deleted = delete_expense(
        expense_id
    )

    if deleted:

        print(
            "Expense deleted successfully."
        )

    else:

        print(
            "Expense not found."
        )


def handle_total():
    """
    Показывает общую сумму расходов.
    """

    total = get_total_amount()

    print()
    print(
        "Total expenses:",
        format_money(total)
    )


def handle_statistics():
    """
    Показывает статистику
    расходов по категориям.
    """

    statistics = get_category_statistics()

    if not statistics:

        print()
        print(
            "No statistics available."
        )

        return

    print()
    print("--- Category Statistics ---")
    print()

    print(
        f"{'CATEGORY':<20}"
        f"{'COUNT':>10}"
        f"{'TOTAL':>20}"
    )

    print("-" * 50)

    for category, count, total in statistics:

        print(
            f"{category[:18]:<20}"
            f"{count:>10}"
            f"{format_money(total):>20}"
        )


def main():
    """
    Главная функция приложения.
    """

    # При первом запуске создаст expenses.db
    # и таблицу expenses.
    #
    # При следующих запусках существующие
    # данные останутся на месте.
    create_database()

    print_header()

    while True:

        print_menu()

        choice = input(
            "Select option: "
        ).strip()

        if choice == "1":

            handle_add_expense()

        elif choice == "2":

            handle_show_expenses()

        elif choice == "3":

            handle_search()

        elif choice == "4":

            handle_delete()

        elif choice == "5":

            handle_total()

        elif choice == "6":

            handle_statistics()

        elif choice == "0":

            print()
            print(
                "Goodbye!"
            )

            break

        else:

            print()
            print(
                "Unknown option. Try again."
            )


if __name__ == "__main__":
    main()