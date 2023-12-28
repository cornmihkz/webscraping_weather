from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from datetime import date, datetime
from dateutil.rrule import rrule, DAILY
import time
import csv


import pandas as pd

date_municipality_df = pd.read_csv("monna.csv", parse_dates = ['Collection Date'], date_format = format("%B %d, %Y"))

municipality_group = date_municipality_df.groupby('Municipality')

# ['Ormoc City' 'Matalom' 'Carigara' 'Bato' 'Maasin City' 'Malitbog'
#  'Balangkayan' 'Salcedo' 'Hinunangan' 'Hinundayan' 'Giporlos' 'Bontoc'
#  'Sogod' 'Liloan']


# ormoc_dates_list = pd.to_datetime(list(municipality_group.get_group('Ormoc City')['Collection Date'])).strftime('%d/%m/%Y')
# matalom_dates_list = pd.to_datetime(list(municipality_group.get_group('Matalom')['Collection Date'])).strftime('%d/%m/%Y')
# carigara_dates_list = pd.to_datetime(list(municipality_group.get_group('Carigara')['Collection Date'])).strftime('%d/%m/%Y')
# bato_dates_list = pd.to_datetime(list(municipality_group.get_group('Bato')['Collection Date'])).strftime('%d/%m/%Y')
# maasin_dates_list = pd.to_datetime(list(municipality_group.get_group('Maasin City')['Collection Date'])).strftime('%d/%m/%Y')
# malitbog_dates_list = pd.to_datetime(list(municipality_group.get_group('Malitbog')['Collection Date'])).strftime('%d/%m/%Y')
# balangkayan_dates_list = pd.to_datetime(list(municipality_group.get_group('Balangkayan')['Collection Date'])).strftime('%d/%m/%Y')
# salcedo_dates_list = pd.to_datetime(list(municipality_group.get_group('Salcedo')['Collection Date'])).strftime('%d/%m/%Y')
# hinunangan_dates_list = pd.to_datetime(list(municipality_group.get_group('Hinunangan')['Collection Date'])).strftime('%d/%m/%Y')
# hinundayan_dates_list = pd.to_datetime(list(municipality_group.get_group('Hinundayan')['Collection Date'])).strftime('%d/%m/%Y')
# bontoc_dates_list = pd.to_datetime(list(municipality_group.get_group('Bontoc')['Collection Date'])).strftime('%d/%m/%Y')
# sogod_dates_list = pd.to_datetime(list(municipality_group.get_group('Sogod')['Collection Date'])).strftime('%d/%m/%Y')
# liloan_dates_list = pd.to_datetime(list(municipality_group.get_group('Liloan')['Collection Date'])).strftime('%d/%m/%Y')
giporlos_dates_list = pd.to_datetime(list(municipality_group.get_group('Giporlos')['Collection Date'])).strftime('%d/%m/%Y')


# Giporlos
driver = webdriver.Chrome()
driver.get('https://www.worldweatheronline.com/giporlos-weather/eastern-samar/ph.aspx')
driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

with open('Giporlos Rainfall - Cassava Project.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

	for date in giporlos_dates_list:
		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
		date_input.clear()	
		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

		new_date_value = date
		date_input.send_keys(f"{new_date_value}")
		date_weather_button.send_keys(Keys.RETURN)

		# 9 am rainfall
		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
		writer.writerow(["Giporlos", date, rain])

f.close()
time.sleep(10)




# # Liloan
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/liloan-weather/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Liloan Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in liloan_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Liloan", date, rain])

# f.close()
# time.sleep(10)


# # Sogod
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/sogod-weather/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Sogod Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in sogod_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Sogod", date, rain])

# f.close()
# time.sleep(10)


# # Bontoc
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/bontoc-weather/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Bontoc Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in bontoc_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Bontoc", date, rain])

# f.close()
# time.sleep(10)


# # Hinundayan
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/hinundayan-weather/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Hinundayan Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in hinundayan_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Hinundayan", date, rain])

# f.close()
# time.sleep(10)




# # Hinunangan
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/hinunangan-weather/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Hinunangan Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in hinunangan_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Hinunangan", date, rain])

# f.close()
# time.sleep(10)


# # Salcedo
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/salcedo-weather/eastern-samar/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Salcedo Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in salcedo_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Salcedo", date, rain])

# f.close()
# time.sleep(10)


# # Balangkayan
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/balangkayan-weather/eastern-samar/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Balangkayan Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in balangkayan_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Balangkayan", date, rain])

# f.close()
# time.sleep(10)





# # Malitbog
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/malitbog-weather-history/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Malitbog Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in malitbog_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Malitbog", date, rain])

# f.close()
# time.sleep(10)




# # Maasin City
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/maasin-weather-history/southern-leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Maasin City Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in maasin_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Maasin City", date, rain])

# f.close()
# time.sleep(10)


# # Bato
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/bato-weather-history/leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Bato Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in bato_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Bato", date, rain])

# f.close()
# time.sleep(10)


# # Carigara
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/carigara-weather-history/leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Carigara Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in carigara_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Carigara", date, rain])

# f.close()
# time.sleep(10)





# # Matalom
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/matalom-weather-history/leyte/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Matalom Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in matalom_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Matalom", date, rain])

# f.close()
# time.sleep(10)





# # Ormoc City
# driver = webdriver.Chrome()
# driver.get('https://www.worldweatheronline.com/ormoc-city-weather-history/ormoc/ph.aspx')
# driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[1]/div/div/div/div[1]/div/div/a[4]').click()

# with open('Ormoc City Rainfall - Cassava Project.csv', 'w') as f:
# 	writer = csv.writer(f)
# 	writer.writerow(["Municipality", "Date", "9AM Rainfall"])

# 	for date in ormoc_dates_list:
# 		date_input = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_txtPastDate"]')
# 		date_input.clear()	
# 		date_weather_button = driver.find_element(By.XPATH, '//*[@id="ctl00_MainContentHolder_butShowPastWeather"]')

# 		new_date_value = date
# 		date_input.send_keys(f"{new_date_value}")
# 		date_weather_button.send_keys(Keys.RETURN)

# 		# 9 am rainfall
# 		rain = driver.find_element(By.XPATH, '//*[@id="aspnetForm"]/section[2]/div/div/div[1]/div[4]/div[1]/div/div[3]/table/tbody/tr[6]/td[4]/div/div[3]').text[:4].strip()
# 		writer.writerow(["Ormoc City", date, rain])

# f.close()
# time.sleep(10)
