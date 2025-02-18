from dataclasses import dataclass
from comicbot_api.utils.comic import Comic
from bs4 import BeautifulSoup, Tag
import stealth_requests as srequests
from typing import List


def comic_title_finder(tag: Tag) -> bool:
    return tag.has_attr('class') and 'title' in tag.get('class')


@dataclass
class WebScraper:
    base_url: str
    parser: str = 'html.parser'

    def scrape_comics(self, url: str) -> List:
        comic_releases_response = srequests.get(url)
        if comic_releases_response.status_code == 200:
            comic_releases_html = comic_releases_response.json().pop('list')
            soup = BeautifulSoup(comic_releases_html, self.parser)
            all_comic_titles = soup.findAll(comic_title_finder)
            return list(map(lambda link:
                            Comic(url=self.base_url + link.attrs.pop('href'),
                                  title=link.contents[0].strip()),
                            all_comic_titles))
        return []
