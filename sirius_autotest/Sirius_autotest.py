from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Код участника
participant_code = "4602/test/8/wzgr6"

# Тестовые данные
test_data = [
    "тест",
    "Test",
    "!@#$%&?,.",
    12340,
    "     ",
    ['1', 2],
    True,
    {"object": "JSON"},
    None,
    "NULL"
]

# Запуск веб-драйвера
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service)

# Открываем страницу
driver.get("https://uts.sirius.online/")

try:
    # Ожидание появления поля ввода кода участника
    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/div[2]/div/div/label/div[2]/input'))  # XPath для поля ввода
    )

    # Вводим код участника
    input_field.send_keys(participant_code)

    # Найдем кнопку для отправки формы (по XPath)
    submit_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="index"]/div/div[2]/div[4]/button'))  # XPath для кнопки отправки
    )

    # Нажимаем кнопку "Отправить"
    submit_button.click()

    # Даем странице больше времени для ответа
    time.sleep(0.5)

    # Ожидание появления элемента для клика на следующий шаг
    click_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="index"]/div/div[2]/div/div[5]/div[1]'))  # XPath для кнопки
    )

    # Прокручиваем страницу до кнопки, чтобы она была видима
    driver.execute_script("arguments[0].scrollIntoView();", click_button)

    # Нажимаем на найденный элемент
    click_button.click()

    # Даем странице время для выполнения действия
    time.sleep(0.5)

    # Ожидание кнопки на следующей странице
    next_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div[3]/button[1]'))
        # XPath для кнопки на новой странице
    )

    # Прокручиваем страницу до кнопки, чтобы она была видима
    driver.execute_script("arguments[0].scrollIntoView();", next_button)

    # Нажимаем на кнопку на новой странице
    next_button.click()

    # Даем время для выполнения действия
    time.sleep(0.5)

    # Ожидание кнопки на следующей странице (по новому XPath)
    final_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="index"]/div/div/div[4]/div/button[2]/span'))
        # XPath для финальной кнопки
    )

    # Прокручиваем страницу до кнопки, чтобы она была видима
    driver.execute_script("arguments[0].scrollIntoView();", final_button)

    # Нажимаем на финальную кнопку
    final_button.click()

    # Даем время для выполнения действия
    time.sleep(0.5)

    # Ожидание появления поля ввода тестовых данных
    textarea = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="task_0"]/div[2]/div/form/textarea'))
        # XPath для поля ввода тестовых данных
    )

    for data in test_data:  # Цикл для проверки всех тестовых данных
        # Очищаем поле ввода перед вводом данных
        textarea.clear()

        # Вводим одно из тестовых данных
        textarea.send_keys(data)

        # Даем время для выполнения действия
        time.sleep(0.5)

        # Ожидание кнопки для сохранения
        save_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="task_0"]/div[4]/button'))  # XPath для кнопки "Сохранить"
        )

        # Прокручиваем страницу до кнопки сохранения, чтобы она была видима
        driver.execute_script("arguments[0].scrollIntoView();", save_button)

        # Нажимаем на кнопку сохранения
        save_button.click()

        # Даем время для выполнения действия
        time.sleep(0.5)

        # Проверка успешного завершения работы (например, появление сообщения)
        success_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Завершить работу")]'))
            # Проверка на завершение
        )

        print(f"Тест с данными '{data}' прошел успешно!")

        # Ожидание кнопки возврата для перехода к следующему тесту
        return_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="index"]/div/div/div[4]/div/button[2]/span'))
            # XPath для кнопки возврата
        )

        # Прокручиваем страницу до кнопки возврата
        driver.execute_script("arguments[0].scrollIntoView();", return_button)

        # Нажимаем на кнопку возврата
        return_button.click()

        # Даем время для выполнения действия
        time.sleep(0.5)

        # Ожидание повторного появления поля ввода тестовых данных
        textarea = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="task_0"]/div[2]/div/form/textarea'))
            # XPath для поля ввода тестовых данных
        )

    print("Все тесты прошли успешно!")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()
