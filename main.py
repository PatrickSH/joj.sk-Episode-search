import requests
import re
from bs4 import BeautifulSoup


class Scraper:
    def get_page_html(self, url):
        "Returns Html for a given link"
        return BeautifulSoup(requests.get(url).text, 'html.parser')

    def get_episode_links(self):
        i = 1
        while True:
            html = self.get_page_html('https://videoportal.joj.sk/moja-mama-vari-lepsie-ako-tvoja/epizody?content5043-page=' + i.__str__() + '&content5043-seasonId=1065&do=content5043-listing')
            if len(html.find_all('article')) <= 6:  # Break if no more content
                print("Break!")
                break
            i += 1
            # Playground
            for articles in html.find_all('article'):
                for link in articles.find_all('a'):
                    video = self.get_page_html(link.get('href'))
                    video_page = self.get_page_html(video.select('.s-video-detail iframe')[0].get('src'))
                    
                    txt = video_page.body.children.pop().__str__()
                    for s in txt.split():
                        if s.find("-720p.mp4") != -1:
                            print("hej")

s = Scraper()
s.get_episode_links()




#links = []  # Create links array

#for link in html.find_all('a'):  # For all a tags
    #cur_link = link.get('href')  # Set our current a tag
    #deep_links = get_page_html(cur_link) # get deeplinks on page

   # if cur_link not in links:  # If a tag is not in our array append it
       # links.append(link.get('href'))

   # for deep_link in deep_links.find_all('a'):
        #if cur_link not in links:  # If a tag is not in our array append it
          #  links.append(link.get('href'))

#print(links)