#Daily Report

# Calculate statistics
prices=$(cut -d',' -f1 stock_price.txt)
IFS=$'\n' read -rd '' -a prices_array <<<"$prices"
min_price=$(echo "${prices_array[@]}" | tr ' ' '\n' | sort -n | head -1)
max_price=$(echo "${prices_array[@]}" | tr ' ' '\n' | sort -n | tail -1)
first_price=${prices_array[0]}
last_price=${prices_array[-1]}
price_range=$(echo "$max_price - $min_price" | bc)
price_stddev=$(awk '{sum+=$1; sumsq+=($1)^2} END {print sqrt(sumsq/NR - (sum/NR)^2)}' <<<"${prices_array[@]}")
today=$(date +%Y-%m-%d)

# Write statistics to file
echo "Daily Report $today :" > stock_stats.txt
echo "Daily Low : $min_price" >> stock_stats.txt
echo "Daily High : $max_price" >> stock_stats.txt
echo "Oppening price : $first_price" >> stock_stats.txt
echo "Closing Price : $last_price" >> stock_stats.txt
echo "Daily Price range : $price_range" >> stock_stats.txt
echo "Daily Volatility : $price_stddev" >> stock_stats.txt
