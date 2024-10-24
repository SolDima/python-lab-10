#Соловйов Дмитро
try:
    with open('students_file.txt', 'w') as file:
        # Записуємо прізвище та питання
        file.write("Прізвище: Іваненко\n")
        file.write("Питання: Як обробляти виключення в Python?\n")
    print("Файл успішно створений та заповнений.")
except Exception as e:
    print(f"Сталася помилка: {e}")

#Яценко Іван
try:
    with open('students_file.txt', 'a') as file:
        file.write("\nПрізвище: Яценко\n")
        file.write("Відповідь: Виключення в Python обробляються за допомогою блоків try-except.\n")
        file.write("Питання: Як працюють декоратори в Python?\n")
    print("Файл оновлено.")
except Exception as e:
    print(f"Сталася помилка: {e}")
