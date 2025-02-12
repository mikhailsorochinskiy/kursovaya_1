from views import main_page

if __name__ == '__main__':
    user_date = input("Введите дату в формате YYYY-MM-DD HH:MM:SS\n")
    print(main_page(user_date))
