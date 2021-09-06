from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import numpy as np
from sqlalchemy import create_engine

opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument('--ignore-certificate-errors-spki-list')
opt.add_argument('--ignore-ssl-errors')
opt.add_experimental_option(
    "excludeSwitches", ["enable-logging", 'enable-automation'])
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1,
    "profile.default_content_setting_values.notifications": 1,
    "credentials_enable_service": False,
    "profile.password_manager_enabled": False
})

url = 'https://www.amazon.in/s?bbn=976419031&rh=n%3A976419031%2Cp_89%3Arealme&dc&qid=1624216249&rnid=3837712031&ref=lp_976420031_nr_p_89_3'

driver = webdriver.Chrome(
    executable_path=r'./src/chromedriver', options=opt)
driver.get(url)

sleep(1)

ele = driver.find_elements_by_xpath('//div[@class="sg-col-inner"]')
csv_data = [i.text.split('\n') for i in ele[3:-2]]
columns = ['Name', 'Reviews', 'Price', 'Savings', 'Delivery',
           'Free Option', 'More Option', 'More Prices', 'Special']

df = pd.DataFrame(csv_data, columns=columns)

for i in range(len(df.index)):
    if df.loc[df.index[i]].Name == "Amazon's Choice":
        df.loc[df.index[i], columns] = df.loc[df.index[i],
                                              columns].shift(-1, axis=0)
        df.loc[df.index[i]].Special = ["Amazon's Choice"]

for i in range(len(df.index)):
    if df.loc[df.index[i]].Price == "Limited time deal":
        df.loc[df.index[i], columns[2:-1]] = df.loc[df.index[i],
                                                    columns[2:-1]].shift(-1, axis=0)
        try:
            df.loc[df.index[i]].Special.append("Limited time deal")
        except:
            df.loc[df.index[i]].Special = "Limited time deal"

for i in range(len(df.index)):
    if df.loc[df.index[i]].Delivery == "FREE Delivery by Amazon":
        df.loc[df.index[i], columns[4:6]] = df.loc[df.index[i],
                                                   columns[4:6]].shift(1, axis=0)

for i in range(len(df.index)):
    if df.loc[df.index[i]].Delivery == "No Cost EMI available on select car...":
        df.loc[df.index[i], columns[4:7]] = df.loc[df.index[i],
                                                   columns[4:7]].shift(-1, axis=0)

df['Reviews'] = df['Reviews'].str.replace(',', '', regex=True)
df['Price'] = df['Price'].str.replace(',', '', regex=True)
df['Price'] = df['Price'].str.replace('₹', '', regex=True)
df['Price'] = df['Price'].str.replace('Currently unavailable.', '0')

df['Reviews'] = df['Reviews'].astype(int)
df['Price'] = df['Price'].astype(int)

df = df.sort_values('Reviews', ascending=False, ignore_index=True)

engine = create_engine(
    'postgresql://fenris:wtf@localhost:5432/Banao')
df.to_sql('Amazon', engine)
df.to_html('templates/main.html')

driver.quit()
