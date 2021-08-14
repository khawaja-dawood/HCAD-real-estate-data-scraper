from HCAD_URL import url, REQUEST_HEADERS
import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
import time

toaster = ToastNotifier()

response = requests.get(url, headers=REQUEST_HEADERS).text
soup = BeautifulSoup(response, "lxml")


rows_data = soup.find_all(bgcolor="ffffff")
count = len(rows_data)
print("Total record from url: ", count)
print()
for line in rows_data:

    # account = row.td.a.text
    row = line.find_all("td")
    account_num = row[0].text.strip()
    owner_name = row[1].text.strip()
    prop_address = row[2].text.strip()
    loc_zip = row[3].text.strip()
    sq_ft = row[4].text.strip()
    market_val = row[5].text.strip()
    appraised_val = row[6].text.strip()

    print(f'Account: {account_num}, Owner Name: {owner_name}, Property Address: {prop_address}, Zip Code: {loc_zip}, '
          f'Impr Sq Ft: {sq_ft}, Market Value: {market_val}, Appraised Value: {appraised_val}')



toaster.show_toast("HCAD!", f"Data Extracted Successfully! Total Count: {count}", threaded=True, icon_path=None, duration=12)
while toaster.notification_active():
    time.sleep(0.1)