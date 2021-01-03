import logging

from grab import Grab

logging.basicConfig(level=logging.DEBUG)

g = Grab()
g.setup(headers={'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'})

g.go('https://www.youtube.com/channel/UCy3eOZh9n5P3aWWKXmrq6yg')

# g.doc.save('x.html')

result = g.doc('//a[@id="video-title"]').exists()


print(result)
