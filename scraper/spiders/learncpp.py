import dataclasses
import os
import pathlib
import threading
import typing
import urllib.request

import bs4
import pdfkit
import scrapy


@dataclasses.dataclass
class URL:
    index: int
    url: str


class LearncppSpider(scrapy.Spider):
    name = "learncpp"
    allowed_domains = ["learncpp.com"]

    def create_working_directory(self) -> None:
        # Create a directory named "learncpp" if it doesn't exist
        if not os.path.exists(self.name):
            os.mkdir(self.name)
        self.log(f"Created working directory: {self.name}")

    def start_requests(self) -> typing.Union[scrapy.Request, None]:
        # Create a working directory
        self.create_working_directory()

        # Use get_urls function to dynamically generate start_urls
        urls = self.get_urls()
        self.log(f"Found {len(urls)} URLs to scrape.")

        for url in urls:
            self.log(f"Processing URL: {url.url}")

            # Yield a Request object for each URL
            yield scrapy.Request(
                url=url.url,
                callback=self.parse,
                cb_kwargs={"page_index": str(url.index)},
            )

    def parse(
        self,
        response: scrapy.http.response.Response,
        page_index: int,
    ) -> None:
        # Modify the filename to include the index
        parsed_url = pathlib.Path(response.url)
        filename = f"{page_index}-{parsed_url.parts[-1]}.html"
        self.log(f"Processing HTML for {filename}")

        # Save the HTML file
        with open(os.path.join(self.name, filename), "wb") as f:
            f.write(response.body)
        self.log(f"Saved HTML file: {filename}")

        # Clean the HTML file
        self.clean(filename)
        self.log(f"Cleaned HTML for {filename}")

        # Run convert_to_pdf function in a ThreadPool
        threading.Thread(target=self.convert_to_pdf, args=(filename,)).start()
        self.log(f"Started PDF conversion for {filename}")

    def clean(self, filename: str) -> None:
        # Read the HTML file
        with open(os.path.join(self.name, filename), "r") as file:
            html_content = file.read()

        # Parse the HTML content
        soup = bs4.BeautifulSoup(html_content, "html.parser")

        # List of div IDs to remove
        div_ids_to_remove = [
            "comments",
            "site-header-main",
            "header-image-main",
            "colophon-inside",
        ]

        # Class name to remove
        classes_to_remove = ["code-block code-block-10", "cf_monitor"]

        # Remove elements by tag, attribute, and values
        self.remove_elements_by_attribute(
            soup,
            "div",
            "id",
            div_ids_to_remove,
        )
        self.remove_elements_by_attribute(
            soup,
            "div",
            "class",
            classes_to_remove,
        )

        # Remove the footer
        self.remove_elements_by_attribute(
            soup, "footer", "class", ["entry-meta entry-utility"]
        )

        # Save the modified HTML content
        with open(os.path.join(self.name, filename), "w") as file:
            file.write(str(soup))
        self.log(f"Saved cleaned HTML for {filename}")

    def remove_elements_by_attribute(
        self,
        soup: bs4.BeautifulSoup,
        tag: str,
        attribute: str,
        values: typing.List[str],
    ) -> None:
        for value in values:
            elements = soup.find_all(tag, {attribute: value})
            for element in elements:
                element.decompose()

    def convert_to_pdf(self, filename: str) -> None:
        # Original file path
        pdf_filename = pathlib.Path(filename).with_suffix(".pdf")

        # Convert the modified HTML file to PDF
        pdfkit.from_file(
            os.path.join(self.name, filename),
            os.path.join(self.name, pdf_filename),
            options={"enable-local-file-access": ""},
        )
        self.log(f"Converted {filename} to PDF: {pdf_filename}")

    def get_urls(self) -> typing.List[URL]:
        try:
            # Parse the HTML content with BeautifulSoup
            html_content = urllib.request.urlopen(
                urllib.request.Request(
                    "http://www.learncpp.com",
                    headers={"User-Agent": "Mozilla/5.0"},
                )
            ).read()
        except urllib.error.URLError as e:
            self.log(f"Error accessing the website: {e}")
            return []

        try:
            soup = bs4.BeautifulSoup(html_content, "html.parser")

            # Find all divs with class "lessontable-row-title"
            all_divs = soup.find_all("div", class_="lessontable-row-title")

            # List to store the URLs
            fetched_urls = []

            # Variable to store indices
            page_index = 1

            # Iterate through each div and find all <a> tags inside
            for div in all_divs:
                all_a_tags = div.find_all("a")

                for a_tag in all_a_tags:
                    # Append the URL to the list
                    fetched_urls.append(URL(page_index, a_tag["href"]))

                    # Increment the index
                    page_index += 1

            self.log(f"Successfully fetched {len(fetched_urls)} URLs")
            return fetched_urls

        except Exception as e:
            self.log(f"Error parsing HTML content: {e}")
            return []
