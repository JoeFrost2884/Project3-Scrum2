import pygal
import lxml
import requests


api_key = "65210ZZ38CVFIWM4"
#api docs https://www.alphavantage.co/documentation/
print("Stock Data Visualizer\n======================")

symbol = input("\nEnter the stock symbol are looking for: ")
#check and see if symbol exist > error handling
#probably just hit the api with a constant time_series value and input the requested symbol
#see if we get a good respone

print("\nChart Types\n==================\n1. Bar\n2. Line")
chart_type = input("Enter the chart type you want (1 , 2):")
#make sure it's 1 or 2, while loop > error handling
if (chart_type == 1):
    #implement function to get bar chart > API integration
    print("1")
if (chart_type == 2):
    #implement function to get line chart > API inegration
    print("2")

print("\nSelect the Time Series of chart you want to Generate\n=================================================================")
print("\n1. Intraday\n2. Daily\n3. Weekly\n4. Monthly")
time_series = input("Enter the time series option (1, 2, 3, 4): ")
# error check option picked > error handling


start_date = input("Enter the start Date (YYYY-MM-DD):")
# error handling > check valid date in YYYY-MM-DD
end_date = input("Enter the end Date (YYYY-MM-DD):")
# error hadling > check valid date in YYYY-MM-DD and that it is after the start date


#Daily Time Series API Func
#https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo
#TIME_SERIES = TIME_SERIES_DAILY
#symbol = symbol 
#apikey = api_key

#Intraday Time Series API Func
#https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&symbol=IBM&interval=15min&slice=year1month1&apikey=demo
#time_series = TIME_SERIES_INTRADAY
#symbol = symbol
#apikey = api_key
#interval = interaval? api required interval 

#Weekly Time Series API Func
#https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=IBM&apikey=demo
#time_series = TIME_SERIES_WEEKLY
#symbol = symbol 
#apikey = api_key 

#Monthly Time Series API Func
#https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY&symbol=IBM&apikey=demo
#time_series = TIME_SERIES_MONTHLY
#symbol = symbol
#apikey = api_key

#parse out json data that comes back from API

#use that data to create graph data 
#create lmxl file with graph data

#send lxml to http and open file
