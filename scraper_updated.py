import requests
import time
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def get_blog_urls(base_url, is_blog_post, get_next_page_url, delay=1):
    current_url = base_url
    visited = set()
    blog_urls = set()

    while current_url:
        if current_url in visited:
            break

        visited.add(current_url)
        
        try:
            response = requests.get(current_url)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error fetching {current_url}: {e}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        blog_urls.update({link['href'] for link in soup.find_all('a', href=True) if is_blog_post(link['href']) and link['href'] not in visited})

        current_url = urljoin(base_url, get_next_page_url(soup))
        time.sleep(delay)

    return blog_urls

def is_blog_post(href):
    # Check if href matches the blog post link pattern
    pattern = re.compile(r'^https://blog\.samaltman\.com/[a-z0-9-]+$')
    return bool(pattern.match(href))

def get_next_page_url(soup):
    # Extract and return the URL for the "Next" page
    next_link = soup.find('a', string='Next')
    if next_link:
        return next_link.get('href')
    return None

def write_to_file(blog_urls):
    with open('blog_urls.txt', 'w') as f:
        f.write('\n'.join(blog_urls))

def main():
    base_url = "https://blog.samaltman.com"
    blog_urls = get_blog_urls(base_url, is_blog_post, get_next_page_url)
    write_to_file(blog_urls)

if __name__ == "__main__":
    main()
