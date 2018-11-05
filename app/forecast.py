import datetime
from datetime import datetime as dt
import json
import mysql.connector
from darksky import forecast
from conf import token, cities, start, end

conn = mysql.connector.connect( user='root', 
							host = '127.0.0.1', 
							db= 'weather', 
							passwd='hidden')
cur = conn.cursor()
 

def main():
	""" Collect all summer dates in a list and iterate through it""" 
	date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start).days)]
	
	for summer_day in date_generated:
		my_date = dt.strptime(str(summer_day), "%Y-%m-%d").isoformat() #api's time arg requires isoformat
		for city, coordinates in cities.items():
			
			"""connect to the api using darkskylib 
			and fetch the highest temperature and humidity index 
			per each day"""
			
			with forecast(token, *coordinates, time=my_date) as values:
				maxTemp = round(((values['daily']['data'][0]['temperatureMax']) - 32) * 5/9, 1) #convert Fahrenheit to Celsius
				humidity = values['daily'] ['data'] [0] ['humidity']

				""" populate database tables with the city names 
				and respective temperatures and humidity indexes per each summer day"""
				
				city_query = """ INSERT IGNORE INTO weather.location(city) VALUES (%s)"""
				cur.execute(city_query, [city])
				temperature_query = "('{0}', '{1}',{2}, {3}, '{4}')".format(city, summer_day, maxTemp, humidity, datetime.date.today())
				cur.execute ("""INSERT INTO weather.summer_time 
							(city, summer_day, highest_temp, humidity, in_date) 
							VALUES {0} """.format(temperature_query))
			
			conn.commit()
	
	conn.close()

if __name__ == "__main__":
	main()
	


