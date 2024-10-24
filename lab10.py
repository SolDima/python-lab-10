try:
    with open('students_file.txt', 'a', encoding='utf-8') as file:
        file.write("\nПрізвище: Сидоренко\n")
        file.write("Відповідь: Декоратори дозволяють змінювати поведінку функції без зміни її коду.\n")
        file.write("Питання: Що таке генератори в Python?\n")
    print("Файл оновлено.")
except Exception as e:
    print(f"Сталася помилка: {e}")
