from bs4 import BeautifulSoup


def get_text(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, head, header, and navbar elements
    for element in soup(['script', 'style', 'head', 'header', 'nav', 'footer']):
        element.decompose()

    text = soup.get_text()

    # Remove leading and trailing spaces on each line
    lines = (line.strip() for line in text.splitlines())
    # Break multi-headlines into a line each
    chunks = (phrase.strip()
              for line in lines for phrase in line.split("  "))
    # Drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk)

    return text
