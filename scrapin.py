# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

# Import Dependecies
import pandas as pd 

# # Set-up-Slinters
# Executable path and set up the URL for scraping
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# Declare and define finction
def mars_news(browser): 
    
    # Assign the url and instruct the browser to visit it
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    # Convert the brower html to a soup object
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    # Add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # Begin scraping
        slide_elem.find('div', class_='content_title')

        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()

        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None

    return news_title, news_p

# # Scrape Mars Data: Featured Image
# ## Featured Images

# Declare and define function
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add error handling for AttributeError
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    return img_url

# ## Scrape Mars Data: Mars Facts

# Declare and define function
def mars_facts:
    
    # Add try/except for error handling
    try:
        # Set up code. Scrape the entire table with Pandas 
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    
    except BaseException:
        return None
        
    # Assign columns and set index of dataframe
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)

    # Convert DataFrame back into HTML-ready format, add bootstrap
    return df.to_html()

# End the automated browsing session
browser.quit()

