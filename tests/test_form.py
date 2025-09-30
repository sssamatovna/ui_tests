import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@allure.epic("Form Fields Automation")
@allure.feature("Form Submission")
class TestFormFields:

    @allure.story("Positive Test - Successful Form Submission")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_successful_form_submission(self, driver):
        """
        Позитивный тест: успешное заполнение и отправка формы

        Шаги:
        1. Заполнить поле Name
        2. Заполнить поле Password
        3. Выбрать Milk и Coffee из списка напитков
        4. Выбрать Yellow из списка цветов
        5. Заполнить поле Email
        6. Заполнить поле Message информацией об инструментах автоматизации
        7. Нажать кнопку Submit

        Ожидаемый результат: появился алерт с текстом "Message received!"
        """
        page = FormPage(driver)

        with allure.step("Открыть страницу с формой"):
            page.open()

        with allure.step("Заполнить все поля формы корректными данными"):
            (page.fill_name("Test User")
             .fill_password("TestPassword123")
             .select_drinks(["Milk", "Coffee"])
             .select_color("Yellow")
             .fill_email("name@example.com")
             .fill_message_with_tools_info())

        with allure.step("Нажать кнопку Submit"):
            page.submit_form()

        with allure.step("Проверить успешную отправку формы"):
            time.sleep(2)
            alert = page.wait_for_alert()
            alert_text = alert.text
            alert.accept()

            assert alert_text == "Message received!", \
                f"Ожидался текст 'Message received!', но получен '{alert_text}'"

    @allure.story("Negative Test - Form Submission Without Required Fields")
    @allure.severity(allure.severity_level.NORMAL)
    def test_form_submission_without_required_fields(self, driver):
        """
        Негативный тест: попытка отправки формы без обязательных полей

        Шаги:
        1. Оставить поле Name пустым
        2. Заполнить остальные поля
        3. Нажать кнопку Submit

        Ожидаемый результат: форма не отправляется, появляется валидация обязательных полей
        """
        page = FormPage(driver)

        with allure.step("Открыть страницу с формой"):
            page.open()

        with allure.step("Заполнить форму без обязательного поля Name"):
            (page.fill_name("")  # Пустое поле Name
             .fill_password("TestPassword123")
             .select_drinks(["Milk"])
             .select_color("Red")
             .fill_email("test@example.com")
             .fill_message("Testing without required field")
             .submit_form())

        with allure.step("Проверить что форма не отправилась"):
            time.sleep(2)

            # Проверяем что остались на той же странице
            assert "form-fields" in driver.current_url, \
                "Форма не должна была отправиться при пустом поле Name"

            # Проверяем что поле Name имеет атрибут required
            name_field = page.find_element(page.name_input)
            assert name_field.get_attribute("required") is not None, \
                "Поле name должно быть обязательным"

            # Проверяем HTML5 валидацию
            is_valid = driver.execute_script("return arguments[0].checkValidity();", name_field)
            assert not is_valid, "Поле Name должно быть невалидным при отправке пустого значения"


if __name__ == "__main__":
    pytest.main(["-v", "--alluredir=allure-results"])