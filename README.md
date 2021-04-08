# Web-Scraping-Workshop
Web Scraping Workshop for Spring 2021 CUWIC Collaboration

## Prerequisites
To complete this workshop, you need to have Python 3 installed. Directions on how to install Python3 can be found here: https://www.python.org/downloads/

You will also need to install `BeautifulSoup4` and `requests`, both of which can be installed using:
```
pip3 install BeautifulSoup4
pip3 install requests
```

## High Level Idea
> "Recycle, or not to recycle? That is the question." 

Quoth modern humans who have read _Hamlet_.

Determining whether you can or cannot recycle something is a common occurrence in many people's daily lives. Thanks to the Internet, we can usually find that information fairly quickly by browsing a couple recycling articles or pamphlets after a Google Search. However, what if we could automate this? We're going to use web scraping to do just that.

Ideally, we would be able to scrape information from many articles about recycling using a web crawler and put together a comprehensive list. Alas, due to the time constraints of this workshop, we will focus on the scraping and parsing portion of web scraping, and thus only scrape from a single site. Perhaps we will have a workshop about web crawling in the future. 🤔

## Instructions

1. The particular article that we will be scraping is: https://removeandreplace.com/2013/09/24/complete-list-can-recycle/. Go to that site, and familiarize yourself with its contents.

2. Before we can scrape data, we need to check whether the site allows it -- go to: https://removeandreplace.com/robots.txt (i.e. append `/robots.txt` to the primary domain). You should see the file contents below:
```
User-agent: *
Allow: /

Sitemap: https://removeandreplace.com/sitemap_index.xml
Sitemap: https://removeandreplace.com/post-sitemap1.xml
Sitemap: https://removeandreplace.com/post-sitemap2.xml
Sitemap: https://removeandreplace.com/page-sitemap.xml
```

3. By saying `Allow: /`, the robots.txt file indicates that we are permitted to scrape any folder in the website. Huzzah! We now have permission to proceed. Open your starter code, and note that Part A (defining the URL the item to search) has already been done for you. In Part B, we want to grab all of the HTML code for this article: to do that, we use a GET request (which is part of HTTP protocol -- if you are unfamiliar with it, more info here: https://rapidapi.com/blog/api-glossary/get/). Insert the following code:
```
r = requests.get(URL)
print(r.text)
```

4. `r` from Step 3 is a Python object containing all of the relevant information returned from the GET request, including status and the actual values returned. Run the current Python script: whoa! You should see _a lot_ of HTML code printed to the console. How the heck are we supposed to interpret this??

5. There is a lovely library out there that can help us called **Beautiful Soup**. It's an HTML parser/extraction tool, more info about it can be found here: https://www.crummy.com/software/BeautifulSoup/bs4/doc/. Basically, we can use it to target specific HTML tags containing the information we want -- in this case, recyclable items. So, we need to know what sorts of HTML tags house the relevant information.

    a. Go to the article we're extracting info from, and choose a recyclable item -- preferably one that is uncommon out of context, like `phone book`.

    b. Right click on the page, and select "Inspect Element" or "View Page Source".

    c. Search for your recyclable item, i.e. `[Cmd + f] phone book`. Do you notice a pattern with how the recyclable items are stored?

6. As you saw in Step 5, each item falls within a `<strong>` tag nested within an `<li>` tag (which makes sense, seeing as 'li' stands for list item). Let's parse on the `<strong>` tag to make our lives easier: the following code creates uses Beautiful Soup to parse the raw HTML, and then specifies which tags we should filter on. `items` should now contain all of the `strong` tags from the HTML -- delete the print statement from Part B, and add the following:
```
soup = BeautifulSoup(r.text, 'html.parser')
items = soup.findAll('strong')
print(items)
```

6. You should still be getting firehosed with information, but less so than before. Notice: what sorts of data is being returned? It's difficult to read with all of the strong tags, so insert the code below, and you should notice the following 3 types of information:

    a. Irrelevant data (i.e. headers and descriptions from the blog portion of the article)

    b. Recyclable Items

    c. Non-Recyclable Items

```
for item in items:
    print(item.text)
```

7. We only want the recyclable items -- so, how do we extract them? We can make use of the article structure, which has alternating headings of "YOU CAN RECYCLE:" and "YOU CANNOT RECYCLE:" for each material type. Iterate through each item in `items` and toggle a flag indicating when you should include items, and when you shouldn't, using these alternating headings. Be sure to use `item.text` to extract the text without the `<strong>` tags -- implementations may vary, but here's one such simple solution (delete the code from Step 6 if you included it):
```
recyclable = []
include = False
for item in items:
    val = item.text                     # Extract text from the HTML tag
    if val == 'YOU CAN RECYCLE:':       # Include items following this tag
        include = True
    elif val == 'YOU CANNOT RECYCLE:':  # Stop including items when you encounter this tag
        include = False
    else:
        if include:
            recyclable.append(val)
```

8. Sweet! Now all we have left is to actually search for our item -- we can do that with a simple for loop:
```
print('----------------')
for item in recyclable:
    if ITEM in item:
        print('> ' + item)
print('----------------')
print('-End of Results-')
```

9. Now you should be able to run the code, enter your desired search item, and if it's a recyclable item (on this specific website's list), relevant items should pop up! To test your output, you should see the following if you search `plastic`:
```
Item to recycle?: plastic
----------------
> shredded paper (in plastic bag)
> empty paper coffee cups (plastic lids removed)
> plastics numbers 1-7
> plastic cups (lids and straws taken out)
> grocery and retail plastic bags
> plastic jugs and bottles – soda bottles & laundry detergent bottles
----------------
-End of Results-
```

And you're done! Congrats, you have completed the workshop!

## More Resources
Want to learn more about web scraping? Here are some great resources!
- High level overview: https://www.parsehub.com/blog/what-is-web-scraping/
- Extensive Python web scraping tutorial: https://www.tutorialspoint.com/python_web_scraping/python_web_scraping_introduction.htm
- Other methods for web scraping (including ScraPy): https://www.scrapingbee.com/blog/web-scraping-101-with-python/
- Web scraping ethics/best practices: https://www.zyte.com/learn/web-scraping-best-practices/
- Real life application, Blueprint Boulder Spring 2021 project for Thinking Huts!: https://github.com/blueprintboulder/s21-thinking-huts

Happy learning!