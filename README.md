# UI Automation Project

Проект автоматизации UI-тестов для формы на сайте practice-automation.com

Тест-кейсы

Позитивный тест-кейс

ID: TC001

Название: Успешное заполнение и отправка формы

Предусловие: Открыта страница https://practice-automation.com/form-fields/

Шаги:

1.Заполнить поле Name: "Test User"

2.Заполнить поле Password: "TestPassword123"

3.Выбрать из списка напитков: "Milk" и "Coffee"

4.Выбрать из списка цветов: "Yellow"

5.Заполнить поле Email: "name@example.com"

6.Заполнить поле Message информацией об инструментах автоматизации

7.Нажать кнопку Submit

Ожидаемый результат: Появился алерт с текстом "Message received!"

Негативный тест-кейс

ID: TC002

Название: Попытка отправки формы без обязательного поля Name

Предусловие: Открыта страница https://practice-automation.com/form-fields/

Шаги:


1.Оставить поле Name пустым

2.Заполнить поле Password: "TestPassword123"

3.Выбрать из списка напитков: "Milk"

4.Выбрать из списка цветов: "Red"

5.Заполнить поле Email: "test@example.com"

6.Заполнить поле Message: "Testing without required field"

7.Нажать кнопку Submit

Ожидаемый результат: Форма не отправляется, появляется валидация обязательного поля Name

<img width="1914" height="867" alt="image" src="https://github.com/user-attachments/assets/3f030450-5408-4c4d-b504-14a0e589700d" />

<img width="1919" height="962" alt="image" src="https://github.com/user-attachments/assets/5d5bc833-ec02-4149-a304-92e8f76546d4" />


