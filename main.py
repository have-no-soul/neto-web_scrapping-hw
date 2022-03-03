import requests
import bs4

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
              "application/signed-exchange;v=b3;q=0.9",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,de;q=0.6",
    "Cache-Control": "no-cache",
    "Cookie": "_ym_uid=1603394073839520639; _ga=GA1.2.750685852.1603394073; web_override=true; "
              "you_are_lucky_man=true; _ym_d=1635349364; fl=ru; hl=ru; "
              "__gads=ID=a9aad876bbf386a6:T=1637169750:S=ALNI_MaK-48HCggTpBTyamTP1j4X6gGKzg; "
              "feature_streaming_comments=true; visited_articles=531472:491048:524460:322552:591573:596533; "
              "_ym_isad=1; _gid=GA1.2.1530322094.1646307433; habr_web_home_feed=/all/; _gat=1",
    "sec-ch-ua-mobile": "?0",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/98.0.4758.102 Safari/537.36 "
}

DATA_URL = 'https://habr.com/ru/all'
KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'DevOps']
SOURCE = requests.get(DATA_URL, headers=HEADERS).text

soup = bs4.BeautifulSoup(SOURCE, features='html.parser')
articles = soup.find_all('article', class_='tm-articles-list__item')


def search_posts_by_tags():
    for article in articles:
        article_date = article.find('time')['title'].split(',')[0]
        article_link = article.find('a', class_='tm-article-snippet__readmore').get('href')
        full_article_link = "https://habr.com/ru/all" + article_link
        article_title = article.find('a', class_='tm-article-snippet__title-link').text
        article_preview_text = article.find(class_='article-formatted-body').text
        article_tags = article.find_all('a', class_='tm-article-snippet__hubs-item-link')
        article_tags = [tag.find('span').text.lower() for tag in article_tags]


        for search_word in KEYWORDS:
            search_word = search_word.lower()
            if any(
                (
                    search_word in article_title,
                    search_word in article_preview_text,
                    search_word in article_tags,
                )
            ):
                print(f'Дата: {article_date} -- Заголовок: {article_title} -- Ссылка: {full_article_link}')


            # if (search_word in article_title.lower()) or (search_word in article_preview_text.lower()) \
            #         or (search_word in article_tags):
            #   print(f'Дата: {article_date} -- Заголовок: {article_title} -- Ссылка: {full_article_link}')


if __name__ == "__main__":
    search_posts_by_tags()
