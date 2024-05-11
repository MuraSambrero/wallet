import pandas as pd
from services import ServicesWallet
from utils import Welcome

print("Добро пожаловать в кошелек!")


def welcome_user() -> str:
    """Функция предоставляет пользователю
    выбор из четырех пунктов и создает файл csv
    при первом пользовании программой"""


    csv_name = Welcome.path
    print(Welcome.text)
    request_answer = input("\nВведите номер пункта меню: ")
    try:
        df = pd.read_csv(csv_name)
    except FileNotFoundError:
        df = pd.DataFrame(Welcome._categories)
        df.to_csv(csv_name, index=False)
    if request_answer == "1":
        ServicesWallet.show_balance(df)
    elif request_answer == "2":
        ServicesWallet.append_transaction()
    elif request_answer == "3":
        ServicesWallet.update_transaction(df)
    elif request_answer == "4":
        ServicesWallet.search_transactions(df)
    else:
        print("Нужно ввести число от 1 до 4.")
    ask_continue()


def ask_continue() -> str | None:
    """Функция запрашивает у пользователя
    нужно ли продолжить выполнение программы
    после выполнения одного из сценариев"""

    ask = input("\nЖелаете продолжить? Да/нет: ")
    if ask.title() == "Да":
        welcome_user()
    else:
        pass


if __name__ == "__main__":
    welcome_user()
