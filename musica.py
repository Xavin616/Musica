from time import sleep
from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from plyer import notification

def notify(num):
    notification.notify(
        title="Music Downloader Successful",
        message=f"{num} songs have been downloaded successfully!",
        timeout=3
    )
    sleep(5)

def download(file):
    slist = open(file).readlines()
    not_found_list = []
    for song in slist:
        search = driver.find_element_by_name("searchSong")
        search.send_keys(Keys.CONTROL, 'a')
        search.send_keys(Keys.BACKSPACE)
        search.send_keys(str(song))
        driver.find_element_by_class_name("el-button").click()
        sleep(5)
        try: 
            downl = driver.find_element_by_class_name('downl')
            if not downl:
                not_found_list.append(song)
                continue
        except NoSuchElementException:
            continue
        downl.click()
        print(f"Downloaded {song}")
    sleep(100)
    notify(len(slist))
    return "Done"


s = Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Chrome(service=s, options=chrome_options)
params = {'behavior': 'allow', 'downloadPath': r'/home/xavin616/Music'}
driver.execute_cdp_cmd('Page.setDownloadBehavior', params)

if __name__ == '__main__':
    
    driver.get("https://freemp3cloud.com/")
    download("/home/xavin616/Documents/Projects/Python Scripts/Music Downloader/music.txt")