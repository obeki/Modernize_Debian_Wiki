import requests
import html2text

# Get the url for the news page of debian wiki
url = 'https://wiki.debian.org/News'

# Retrieve the contents of page using a get request
response = requests.get(url)

# Confirm if request was successful (i.e. 200 OK)
if response.status_code == 200:
    # Get the HTML content from the response
    html_content = response.text

    # Convert HTML retrieved to Markdown
    markdown_content = html2text.html2text(html_content)

    # Print or save the Markdown content as needed
    print(markdown_content)

    # Open the file in write mode and write the Markdown content to it
    with open("debian_news_wiki.md", "w", encoding="utf-8") as md_file:
        md_file.write(markdown_content)

else:
    print(f"Failed to retrieve content from {url} (Status Code: {response.status_code})")
