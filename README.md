# Web-Scraping-Workshop
Web Scraping Workshop for Spring 2021 CUWIC Collaboration

## Prerequisites
To complete this workshop, you need to have Python 3 installed. You will also need to install `BeautifulSoup4`, `requests`, and `pandas`, all of which can be installed using:
```
pip3 install BeautifulSoup4
pip3 install requests
pip3 install pandas
```

To download Python 3: https://www.python.org/downloads/

## High Level Idea
Recycle, or not to recycle? That is the question. TODO: continue

## Instructions

1. First, let's scrape ethical brands for our desired clothing type from https://goodonyou.eco/. Before we can scrape data though, we need to check whether the site allows it -- so, append `/robots.txt` to the end of the URL (full URL: `https://goodonyou.eco/robots.txt`), and see what they allow. You should see the file contents below:
```
User-agent: *
Allow: /
```

2. By saying `Allow: /`, the robots.txt file indicates that we are permitted to scrape any folder in the website. Huzzah! We now have permission to proceed. CONTINUE HERE

3. 

And you're done! Congrats, you have completed the workshop!

## More Resources
Want to learn more about web scraping? Here are some great resources!
- High level overview: https://www.parsehub.com/blog/what-is-web-scraping/
- Extensive Python web scraping tutorial: https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_introduction.htm
- Other methods for web scraping (including ScraPy): https://www.scrapingbee.com/blog/web-scraping-101-with-python/
- Web scraping ethics/best practices: https://www.zyte.com/learn/web-scraping-best-practices/
- Real life application, Blueprint Boulder Spring 2021 project for Thinking Huts!: https://github.com/blueprintboulder/s21-thinking-huts

Happy learning!