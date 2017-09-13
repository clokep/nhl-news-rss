## NHL News to RSS

**Deprecation notice:** This is no longer being developed. This was previously deployed to Heroku, but is now deployed at https://www.to-rss.xyz/nhl/

To my knowledge, [NHL.com](https://www.nhl.com/) does not provide an
RSS feed for their [news feed](https://www.nhl.com/news/). This is a simple
proxy that loads the NHL.com news site and serves it back as an RSS feed. This
is deployed at https://www.to-rss.xyz/nhl/. You can get an RSS feed for
[NHL news](https://www.to-rss.xyz/nhl/news/) or for a specific team
(e.g. the
[New York Islanders news](https://www.to-rss.xyz/nhl/islanders/)). The
[site root](https://www.to-rss.xyz/nhl/) lists all possible feeds.

Information is pulled on demand on each refresh of the page (and is always
current).

### About

This project runs on Heroku. It is a Flask application that serves a few
endpoints: one HTML page and a bunch of RSS feeds. It pulls the current list of
news articles from [NHL.com](https://www.nhl.com), processes them using
[BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/bs4/) and
generates an RSS feed using
[FeedGenerator](https://github.com/getpelican/feedgenerator).
