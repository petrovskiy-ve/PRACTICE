from selenium import webdriver
import pandas


class Coin:  # Custom class
    name = ""
    short_name = ""
    market_cap = ""
    price = ""


def search_coin(coin_name: str):  # Search function
    search_results = dataframe_[dataframe_.eq(coin_name).any(1)]
    if(not search_results.empty):
        return search_results
    else:
        return 'ERROR: NOT FOUND, try another one'


# Parcing
driver = webdriver.Chrome()
driver.get("https://coinmarketcap.com/")
driver.execute_script(f"window.scrollTo(0, 1250);")
coins = []
n = 25
tbody = driver.find_element_by_tag_name('tbody')
coins_rows = tbody.find_elements_by_tag_name('tr')[0:n]
for i in range(n):
    new_coin = Coin()
    new_coin.name = coins_rows[i].find_elements_by_tag_name('p')[1].text
    new_coin.short_name = coins_rows[i].find_elements_by_tag_name('p')[2].text
    new_coin.price = coins_rows[i].find_elements_by_tag_name('span')[2].text
    new_coin.market_cap = coins_rows[i].find_elements_by_tag_name('span')[
        8].text
    coins.append(new_coin)
driver.close()

# Making dataframe
dataframe_ = pandas.DataFrame([vars(coin) for coin in coins])
dataframe_.index = dataframe_.index + 1
dataframe_.to_csv('output.csv', sep=';')
print(dataframe_)

# Main cycle
while True:
    print('Input a name or acronym of the cryptocurrency to get info from dataframe >>', end=" ")
    print(search_coin(str(input())))
