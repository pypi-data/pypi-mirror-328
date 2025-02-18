from comicbot_api.v1.comic_bot_api_client import ComicBotAPIClientV1Builder
from pprint import pprint


def main():
    builder = ComicBotAPIClientV1Builder()
    builder.with_base_url("https://leagueofcomicgeeks.com")
    client = builder.build()
    pprint(client.get_releases_for_week(week_num=1, formats=["hardcover"], publishers=["marvel"]))


if __name__ == '__main__':
    main()
