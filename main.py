import time

import requests
import re
from bs4 import BeautifulSoup


class BenchMarker:
    def __init__(self, start):
        self.start = start

    def benchmark(self):
        end = time.time()  # End of function
        print("Function=%s, Time=%s" % ("get_episode_links", end - self.start))


class Scraper:

    def __init__(self, benchmark):
        self.do_benchmark = benchmark

    def get_page_html(self, url):
        "Returns Html for a given link"
        try:
            return BeautifulSoup(requests.get(url).text, 'html.parser')
        except Exception:
            print("Error for url: "+url)
            pass

    def get_episode_links(self):
        i = 1

        if self.do_benchmark == 1:
            benchmark = BenchMarker(time.time())

        while True:
            html = self.get_page_html('https://videoportal.joj.sk/moja-mama-vari-lepsie-ako-tvoja/epizody?content5043-page=' + i.__str__() + '&content5043-seasonId=1065&do=content5043-listing')
            if len(html.find_all('article')) <= 6:  # Break if no more content
                if self.do_benchmark == 1:
                    benchmark.benchmark()
                print("Break!")
                break
            i += 1
            # Playground
            for articles in html.find_all('article'):  # find all article elements in html
                for link in articles.find_all('a'):  # Find all a tags in artilce
                    video = self.get_page_html(link.get('href'))  # Get link from a tag
                    video_page = self.get_page_html(video.select('.s-video-detail iframe')[0].get('src'))  # Find iframe in html
                    txt = video_page.find_all('script')[-1].__str__()
                    for s in txt.split():
                        if s.find("-720p.mp4") != -1:
                            print(s)


s = Scraper(1)
s.get_episode_links()
