from selenium import webdriver


class music():
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(
            executable_path='C:/Users/being/Downloads/chromedriver_win32/chromedriver.exe')

    def play(self, query):
        self.query = query
        self.driver.get(
            url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath(
            '//*[@id="video-title"]/yt-formatted-string')
        video.click()


# assist = music()
# assist.play("dynamite")
