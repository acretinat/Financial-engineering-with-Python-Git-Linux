#Fichier de scrap
url="https://finance.yahoo.com/quote/MC.PA"
html=$(curl -s "$url")

price=$(echo "$html" | grep -o '<fin-streamer class="[^"]*" data-symbol="MC.PA" data-test="qsp-price" data-field="regularMarketPrice" data-trend="none" data-pricehin>

france_time=$(TZ="Europe/Paris" date "+%Y-%m-%d %H:%M:%S")

echo "$price,$france_time" >> stock_price.txt
