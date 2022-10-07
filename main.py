from rental_listings import RentalListings
from research_results import ResearchResults
import time

rental_listings = RentalListings()
rental_listings.get_property_links()
rental_listings.get_listings_prices()
rental_listings.get_listings_addresses()

research_results = ResearchResults()
for i in range(len(rental_listings.addresses)):
    research_results.fill_in_form(
        rental_listings.addresses[i],
        rental_listings.prices[i],
        rental_listings.property_links[i]
    )
    time.sleep(2)
research_results.quit()
