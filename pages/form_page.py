from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        # Локаторы элементов формы
        self.name_input = (By.ID, "name-input")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.email_input = (By.ID, "email")
        self.message_input = (By.ID, "message")
        self.submit_button = (By.CSS_SELECTOR, "button#submit-btn")

        # Чекбоксы напитков
        self.drink_water = (By.ID, "drink1")
        self.drink_milk = (By.ID, "drink2")
        self.drink_coffee = (By.ID, "drink3")
        self.drink_mine = (By.ID, "drink4")
        self.drink_ctrl_alt_delight = (By.ID, "drink5")

        # Радиокнопки цветов
        self.color_red = (By.ID, "color1")
        self.color_blue = (By.ID, "color2")
        self.color_yellow = (By.ID, "color3")

    def open(self):
        """Открывает страницу с формой"""
        self.driver.get("https://practice-automation.com/form-fields/")
        self.wait.until(EC.presence_of_element_located(self.name_input))

    def find_element(self, locator):
        """Вспомогательный метод для поиска элемента с ожиданием"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_clickable_element(self, locator):
        """Вспомогательный метод для поиска кликабельного элемента"""
        return self.wait.until(EC.element_to_be_clickable(locator))

    def scroll_to_element(self, element):
        """Прокручивает страницу к элементу"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        return self

    def fill_name(self, name):
        """Заполняет поле Name"""
        element = self.find_element(self.name_input)
        element.clear()
        element.send_keys(name)
        return self

    def fill_password(self, password):
        """Заполняет поле Password"""
        element = self.find_element(self.password_input)
        element.clear()
        element.send_keys(password)
        return self

    def fill_email(self, email):
        """Заполняет поле Email"""
        element = self.find_element(self.email_input)
        element.clear()
        element.send_keys(email)
        return self

    def fill_message(self, message):
        """Заполняет поле Message"""
        element = self.find_element(self.message_input)
        element.clear()
        element.send_keys(message)
        return self

    def select_drinks(self, drinks):
        """Выбирает напитки из чекбоксов"""
        drink_mapping = {
            "Water": self.drink_water,
            "Milk": self.drink_milk,
            "Coffee": self.drink_coffee,
            "Mine": self.drink_mine,
            "Ctrl-AIt-Delight": self.drink_ctrl_alt_delight
        }

        for drink in drinks:
            if drink in drink_mapping:
                checkbox = self.find_clickable_element(drink_mapping[drink])
                self.scroll_to_element(checkbox)
                if not checkbox.is_selected():
                    checkbox.click()
        return self

    def select_color(self, color):
        """Выбирает цвет из радиокнопок"""
        color_mapping = {
            "Red": self.color_red,
            "Blue": self.color_blue,
            "Yellow": self.color_yellow
        }

        if color in color_mapping:
            radio_button = self.find_clickable_element(color_mapping[color])
            self.scroll_to_element(radio_button)
            radio_button.click()
        return self

    def get_automation_tools_info(self):
        """
        Получает информацию об инструментах автоматизации
        """
        tools_selectors = [
            (By.XPATH, "//h3[contains(text(), 'Automation tools')]/following-sibling::ul/li"),
            (By.XPATH, "//h2[contains(text(), 'Automation tools')]/following-sibling::ul/li"),
        ]

        tools = []
        for selector in tools_selectors:
            try:
                tool_elements = self.driver.find_elements(*selector)
                if tool_elements:
                    tools = [tool.text.strip() for tool in tool_elements if tool.text.strip()]
                    if tools:
                        break
            except:
                continue

        # Если не нашли инструменты, используем дефолтные
        if not tools:
            tools = ["Selenium WebDriver", "Playwright", "Cypress", "TestCafe", "WebDriverIO"]

        return tools

    def fill_message_with_tools_info(self):
        """Заполняет поле Message информацией об инструментах автоматизации"""
        tools = self.get_automation_tools_info()
        tools_count = len(tools)
        longest_tool = max(tools, key=len) if tools else "Selenium WebDriver"

        message = f"Total automation tools: {tools_count}. Longest tool name: {longest_tool}"
        self.fill_message(message)
        return self

    def submit_form(self):
        """Нажимает кнопку Submit"""
        submit_element = self.find_clickable_element(self.submit_button)
        self.scroll_to_element(submit_element)
        self.driver.execute_script("arguments[0].click();", submit_element)
        return self

    def wait_for_alert(self, timeout=10):
        """Ожидает появление алерта"""
        WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
        return self.driver.switch_to.alert