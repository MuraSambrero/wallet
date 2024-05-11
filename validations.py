import re


class Validate:
    @classmethod
    def validation_date(cls) -> str:
        date = input("\nВведите дату в формате dd-mm-yyyy: ")
        if re.match(r"\d{2}\-\d{2}\-\d{4}", date):
            return date
        else:
            return cls.validation_date()

    @classmethod
    def validation_sum(cls) -> int:
        summ = input("\nВведите сумму: ")
        try:
            summ = int(summ)
        except ValueError:
            print("Сумма должна состоять из цифр.")
            return cls.validation_sum()
        return summ

    @classmethod
    def choice_category(cls) -> str:
        print(
            "\nВыберите категорию транзакции:\
            \n1. Расход\
            \n2. Доход"
        )
        try:
            choice = int(input("Выберите число: "))
        except ValueError:
            print(
                "\nДля выбора, можно вводить только число\
                \nВ данном случае, это 1 или 2."
            )
            cls.choice_category()
        if choice == 1:
            category = "Расход"
        elif choice == 2:
            category = "Доход"
        else:
            print("\nНужно выбрать 1 или 2.")
            cls.choice_category()
        return category

    @classmethod
    def validation_describe(cls) -> str:
        describe = input(
            "\nВведите описание транзакции.\
                         \nМаксимальное колличество симоволов 40):"
        )
        if len(describe) <= 40:
            return describe
        else:
            print("\nОписание транзакции не должно превышать 40 символов.")
            return cls.validation_describe()
