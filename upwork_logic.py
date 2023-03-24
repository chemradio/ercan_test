import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from config import AD_TIME_INTERVAL_MIN, UPWORK_URL


def upwork_ad_collector() -> list[dict]:
    # upworka gir ilanlari topla ve parse et - zaman ve link
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(UPWORK_URL)
    driver.implicitly_wait(5)
    time.sleep(10)

    return_list = []
    cards = driver.find_elements(By.CLASS_NAME, "up-card-list-section")

    for card in cards:
        # link islemi
        job_title_element = card.find_element(By.CLASS_NAME, "job-tile-title")
        a_element = job_title_element.find_element(By.TAG_NAME, "a")
        link = a_element.get_attribute("href")

        # post time
        posted_time_ago = card.find_element(
            By.XPATH, "//span[@data-test='UpCRelativeTime']"
        ).get_attribute("innerHTML")

        "5 minutes ago"
        "44 seconds ago"
        post_time_string = posted_time_ago
        post_time_list = posted_time_ago.split()
        zaman_olcemi = post_time_list[1]
        sayi = int(post_time_list[0])

        if zaman_olcemi == "minutes" and sayi > AD_TIME_INTERVAL_MIN:
            break

        ad = {"link": link, "posted_min_ago": f"{sayi} {zaman_olcemi}"}
        return_list.append(ad)

    driver.quit()
    return return_list
