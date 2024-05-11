from balance import Balance
from validations import Validate


class ServicesWallet:
    @staticmethod
    def show_balance(df) -> str:
        """Данная функция запрашивает данные по балансу
        с помощью класса Balance"""

        result_sum = Balance.show_balance(df)
        print(f"\nВаш баланс составляет: {result_sum} рублей.")

    @staticmethod
    def append_transaction() -> str:
        """Данная функция выполняет запрос данных у пользователя
        и сохраняет данные в файл csv
        с помощью класса Balance"""

        date = Validate.validation_date()
        category = Validate.choice_category()
        summ = Validate.validation_sum()
        describe = input("Введите описание: ")
        balance = Balance(date, category, summ, describe)
        result_append = balance.append_transaction()
        print(result_append)

    @staticmethod
    def update_transaction(df, csv_name) -> str:
        """Данная функция необоходима для редактирования
        данных по определенным транзакциям
        """
        result_update = Balance.update_transaction(df, csv_name)
        print(result_update)

    @staticmethod
    def search_transactions(df):
        results_find = Balance.search_transactions(df)
        print(results_find)
