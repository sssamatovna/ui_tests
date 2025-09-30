import pytest
import allure
from selenium import webdriver


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver', None)
        if driver is not None:
            # Делаем скриншот при падении теста
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )

            # Добавляем HTML страницы
            allure.attach(
                driver.page_source,
                name="page_source",
                attachment_type=allure.attachment_type.HTML
            )


@pytest.fixture(scope="function")
def driver():
    # ваша фикстура драйвера
    driver = webdriver.Chrome()
    yield driver
    driver.quit()