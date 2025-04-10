from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException
import time
import json


def load_cookies(driver, cookies_path):
    with open(cookies_path, 'r') as f:
        cookies = json.load(f)
    for cookie in cookies:
        if 'sameSite' in cookie and cookie['sameSite'] == 'no_restriction':
            cookie['sameSite'] = 'None'
        try:
            driver.add_cookie(cookie)
        except Exception as e:
            print(f"❌ Cookie error: {cookie.get('name', 'unknown')}: {e}")

def load_keywords(keywords_path):
    with open(keywords_path, 'r', encoding='utf-8') as f:
        return [line.strip().lower() for line in f.readlines() if line.strip()]


def expand_post(post, driver):
    try:
        buttons = post.find_elements(By.XPATH, './/div[@role="button" and (normalize-space(text())="Ещё" or normalize-space(text())="More" or normalize-space(text())="Ще")]')
        
        for btn in buttons:
            driver.execute_script("arguments[0].click();", btn)
            time.sleep(0.3)
    except Exception as e:
        print(f'⚠️ Ошибка при раскрытии текста: {e}')



def extract_post(post, keywords, seen_posts, driver):
    try:
        expand_post(post, driver)

        text_blocks = post.find_elements(By.XPATH, './/div[@dir="auto"]')
        post_text = '\n'.join([el.text for el in text_blocks if el.text.strip()])

        links = post.find_elements(By.XPATH, './/a[contains(@href, "/groups/")]')
        post_link = None
        for link in links:
            href = link.get_attribute('href')
            if 'posts' in href:
                post_link = href
                break

        if post_text and post_link and post_link not in seen_posts:
            print(f'\n🔍 Пост: {post_link}')
            print(f'📝 Текст: {post_text[:100]}...')

            if any(keyword in post_text.lower() for keyword in keywords):
                seen_posts.add(post_link)
                with open('results.txt', 'a', encoding='utf-8') as f:
                    f.write(f'{post_link}\n{post_text}\n{"-"*50}\n')
                print(f'✅ Подходит по ключевым словам')
            else:
                print(f'⚠️ Нет ключевых слов')

    except StaleElementReferenceException:
        print('♻️ Устаревший элемент, пропуск')
    except Exception as e:
        print(f'❌ Ошибка при разборе поста: {e}')


def extract_n_posts(driver, keywords, max_posts):
    seen_posts = set()
    post_index = 0

    while post_index < max_posts:
        posts = driver.find_elements(By.XPATH, '//div[@role="feed"]/div')
        if post_index >= len(posts):
            print('🔚 Достигнут конец доступных постов')
            break

        post = posts[post_index]
        extract_post(post, keywords, seen_posts, driver)
        post_index += 1

        driver.execute_script("arguments[0].scrollIntoView(true);", post)
        time.sleep(1)


options = Options()
options.add_argument('--disable-notifications')
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.get('https://www.facebook.com/')


load_cookies(driver, 'cookies.json')
driver.refresh()
time.sleep(5)


with open('groups.txt', 'r') as f:
    groups = [line.strip() for line in f if line.strip()]


keywords = load_keywords('keywords.txt')

# Сколько постов смотреть
MAX_POSTS = 40

for group_url in groups:
    print(f'\n🔗 Переход в группу: {group_url}')
    driver.get(group_url)
    time.sleep(5)
    extract_n_posts(driver, keywords, MAX_POSTS)

print("\n🎉 Готово!")
driver.quit()