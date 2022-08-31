# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
import datetime as dt
import time

def scrape_all():
    # Initiate headless driver for deployment
    # Set the executable path and initialize Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "hemispheres": hemispheres(browser),
        "last_modified": dt.datetime.now()
    }

    # Stop webdriver and return data
    browser.quit()
    return data

def mars_news(browser):

    # Visit the mars news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:

        slide_elem = news_soup.select_one('div.list_text')
        #slide_elem.find('div', class_='content_title')


        # Use the parent element to find the first a tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
        #news_title


        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
        #news_p

    except AttributeError:
        return None, None

    return news_title, news_p


def featured_image(browser):
# JPL Space Images Featured Image

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    #img_soup

    # Add try/except for error handling
    try:



        # find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
        #img_url_rel
    except AttributeError:
        return None



    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    return img_url


def mars_facts():
#Mars Facts
# Add try/except for error handling
    try:

        df = pd.read_html('https://galaxyfacts-mars.com')[0]
        #df.head()
    except BaseException:
        return None


    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)
    #df


    #df.to_html()
    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")


def hemispheres(browser):
    url = 'https://marshemispheres.com/'
    browser.visit(url)

    # Create a list to hold the images and titles.
    hemisphere_image_urls = []

    # Write code to retrieve the image urls and titles for each hemisphere.
    links = browser.find_by_css('a.product-item h3')

    # Loop through those links click the link find the sample anchor return href
    for index in range(4):
        hemisphere = {}
    
        # Find the elements on each loop to avoid a state element exception
        browser.find_by_css('a.product-item h3')[index].click()

        # Find the sample image anchor tag and extract href
        sample_element = browser.links.find_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]
    
        # Get Hemisphere title
        hemisphere["title"] = browser.find_by_css("h2.title").text
        
        hemisphere_image_urls.append(hemisphere)
        
        browser.back()
        
    return hemisphere_image_urls
    

if __name__ == "__main__":
    # If running as script, print scraped data
    print(scrape_all())





