import json
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run Chrome in headless mode
driver = webdriver.Chrome(options=options)


# URL
url1 = 'https://www.qantas.com/hotels/properties/18482?adults=2&checkIn=2023-12-05&checkOut=2023-12-06&children=0'
url2 = url1 + '&infants=0&location=London%2C%20England%2C%20United%20Kingdom&page=1&payWith=cash'
url = url2 + '&searchType=list&sortBy=popularity'

print(url)
driver.get(url)
wait = WebDriverWait(driver, 10)
page_source = driver.page_source

soup = BeautifulSoup(page_source, 'html.parser')
script_tag = soup.find('script', {'type': 'application/ld+json'})

if script_tag:
    try:

        json_data = json.loads(script_tag.string)
        print("JSON is valid.")
        json_str = script_tag.string
        data2 = json.loads(json_str)

        hotel_name = data2.get('name', 'N/A')
        print(f"Hotel Name: {hotel_name}")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
else:
    print("Script tag not found or does not have the expected type attribute.")

amounts = soup.select("[data-testid='amount']")
room_names = soup.select(".e1yh5p93")
number_of_guests = soup.select(".epfmh1m0")
cancellation_policies = soup.select("#cancellation-policy-button")
is_top_deals = soup.select(".css-1jr3e3z-Text-BadgeText.e34cw120")
currencies = soup.select(".css-1dvtiwl-Box.e1m6xhuh0")

rates = []

max_length = max(len(amounts), len(room_names), len(number_of_guests), len(cancellation_policies), len(is_top_deals), len(currencies))

for i in range(max_length):
    rate = {
        'Room_Name': room_names[i].text.strip() if i < len(room_names) else '',
        'Rate': amounts[i].text.strip() if i < len(amounts) else '',
        'Number_of_Guests': number_of_guests[i].text.strip().split('•')[0].strip() if i < len(number_of_guests) else '',
        'Cancellation_Policy': cancellation_policies[i].text.strip().replace("cancellation", "cancellation ") if i < len(cancellation_policies) else '',
        'Top_Deal': 'Top Deal' in is_top_deals[i].text.strip() if i < len(is_top_deals) else False,
        'Currency': currencies[i].text.strip().split('/')[0].strip() if i < len(currencies) else '',
    }
    rates.append(rate)

print(rates)
driver.quit()
