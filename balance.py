import pandas as pd
from validations import Validate


class Balance:
    def __init__(self, date, category, summ, describe):
        self.date = date
        self.category = category
        self.summ = summ
        self.describe = describe

    @staticmethod
    def show_balance(df) -> str:
        """Рассчитывает баланс"""

        group_by_categories = df.groupby("category")["summ"].sum()
        income = group_by_categories["Доход"]
        expence = group_by_categories["Расход"]
        result_sum = income - expence
        return result_sum

    def append_transaction(self) -> str:
        """Добавляет транзакцию в файл csv"""
        
        df_create = pd.DataFrame(
            {
                "date": [self.date],
                "category": [self.category],
                "summ": [self.summ],
                "describe": [self.describe],
            }
        )
        df_create.to_csv("transactions.csv", mode="a", index=False, header=False)
        return "Транзакция добавлена."

    @staticmethod
    def update_transaction(df, csv_name) -> str:
        """Вносит изменения в существующую запись"""

        print("\nТранзакцию за какое число вы хотите редактировать?")
        update_by_date = Validate.validation_date()
        if not update_by_date:
            return "Дата введена не корректно."
        transactions = df[df["date"] == update_by_date]
        if transactions.empty:
            return "Транзакций за данную дату не существует."
        print(f"\n{transactions}")
        id = int(input("Введите id записи(первый столбец слева): "))
        date = Validate.validation_date()
        df.loc[id, "date"] = date
        df.loc[id, "category"] = Validate.choice_category()
        summ = Validate.validation_sum()
        df.loc[id, "summ"] = summ
        describe = Validate.validation_describe()
        df.loc[id, "describe"] = describe
        df.to_csv(csv_name, index=False)
        return "Транзакция сохранена."
    
    @staticmethod
    def search_transactions(df):
        """Выполняет поиск по одному из трех критериев"""
        
        print("Выберите критерий поиска:\
              \n1. По категории\
              \n2. По дате\
              \n3. По сумме")
        critery_num = input("Введите номер пункта: ")
        if critery_num == "1":
            category = Validate.choice_category()
            transactions = df[df["category"] == category]
        elif critery_num == "2":
            date = Validate.validation_date()
            transactions = df[df["date"] == date]
        elif critery_num == "3":
            summ = Validate.validation_sum()
            transactions = df[df["summ"] == summ]
        if transactions.empty:
            return 'Нет данных поиска по заданным критериям.'
        return transactions
