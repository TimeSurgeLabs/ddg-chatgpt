from bs4 import BeautifulSoup

def get_text(html_content):
    # parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # find all the p tags and div tags in the HTML content
    p_tags = soup.find_all('p')
    # div_tags = soup.find_all('div')

    # extract the raw text from all the p tags and div tags and concatenate them
    raw_text = '\n'.join([tag.get_text() for tag in p_tags])

    return raw_text
