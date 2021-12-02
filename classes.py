from selenium import webdriver


class myclass():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/being/Downloads/chromedriver_win32/chromedriver.exe')

    def schedule(self):
        self.driver.get('https://myclass.lpu.in/')
        username_textbox = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/form/div[6]/input[1]')
        username_textbox.send_keys("12002791")
        password_textbox = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/form/div[6]/input[2]')
        password_textbox.send_keys("Afridi@786")
        signin = self.driver.find_element_by_xpath(
            '/html/body/div[2]/div/form/div[7]/button')
        signin.click()
        view_classes = self.driver.find_element_by_xpath(
            '//*[@id="homeCenterDiv"]/div/div[1]/div/div[2]/a')
        view_classes.click()


# check = myclass()
# check.schedule()
