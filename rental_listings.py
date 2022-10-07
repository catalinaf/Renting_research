from bs4 import BeautifulSoup
import requests

USER_AGENT = "en-GB,en;q=0.5"
ACCEPT_LANGUAGE = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:105.0) Gecko/20100101 Firefox/105.0"
RENTAL_WEBSITE = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%" \
               "22%3A37.86031714729698%2C%22east%22%3A-122.31488314990234%2C%22south%22%3A37.69016886406611%2C%22west" \
               "%22%3A-122.55177585009766%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A" \
               "20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%" \
               "3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%" \
               "7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22" \
               "value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C" \
               "%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible" \
               "%22%3Atrue%7D"


class RentalListings:
    def __init__(self):
        self.headers = {"User-Agent": USER_AGENT, "Accept-Language": ACCEPT_LANGUAGE}
        self.addresses = []
        self.prices = []
        self.property_links = []

    def make_soup(self):
        response = requests.get(url=RENTAL_WEBSITE, headers=self.headers)
        listings_page = response.text
        soup = BeautifulSoup(listings_page, "html.parser")
        return soup

    def get_property_links(self):
        links = self.make_soup().select(".dYZVUW.property-card-link")
        for link in links:
            listing_url = link.get("href")
            if "/b/" in listing_url:
                listing_url = "https://www.zillow.com" + listing_url
            self.property_links.append(listing_url)

    def get_listings_prices(self):
        prices = self.make_soup().select("span[data-test='property-card-price']")
        for price in prices:
            listing_price = price.getText()
            if "+" in listing_price:
                listing_price = listing_price.split("+", 1)[0]
            elif "/" in listing_price:
                listing_price = listing_price.split("/", 1)[0]
            self.prices.append(listing_price)

    def get_listings_addresses(self):
        addresses = self.make_soup().select(".dYZVUW.property-card-link")
        self.addresses = [address.getText().split(" | ")[-1] for address in addresses]
