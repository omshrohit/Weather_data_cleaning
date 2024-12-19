import pandas as pd

weather=pd.read_csv('nyc_weather.csv',na_values=['T'])
print(weather)

weather.shape

weather.head(1)

weather.columns

weather.info()

weather.describe()

weather.isnull().sum()

weather.isnull().sum()/weather.shape[0]*100

weather['EST']=pd.to_datetime(weather['EST'])

type(weather['EST'][0])

weather.set_index('EST',inplace=True)

weather['WindSpeedMPH'].interpolate(method='time',inplace=True)

weather['PrecipitationIn'].interpolate(method='time',inplace=True)

weather[['WindSpeedMPH','PrecipitationIn']]

weather['Events'].fillna('no event',inplace=True

weather.isnull().sum()

print('Data is ready to Data Analysis---')

weather
