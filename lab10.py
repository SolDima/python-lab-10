try:
    with open('students_file.txt', 'w') as file:
        # Записуємо прізвище та питання
        file.write("Прізвище: Іваненко\n")
        file.write("Питання: Як обробляти виключення в Python?\n")
    print("Файл успішно створений та заповнений.")
except Exception as e:
    print(f"Сталася помилка: {e}")
