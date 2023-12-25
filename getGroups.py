import pandas as pd
import os

cwd = os.getcwd()
mySys = "Mac"
if mySys == "Mac":
    mainFs = cwd + '/MainSheet.xlsx'
    routeFS = cwd + '/RouteGroups.xlsx'
    outDir = cwd + '/out/'
else:
    mainFs = cwd + '\\MainSheet.xlsx'
    routeFS = cwd + '\\RouteGroups.xlsx'
    outDir = cwd + '\\out\\'

def getRoutes():
    cwd = os.getcwd()
    df = pd.read_excel(routeFS)
    return df

def gerRoutesList(df):
    route_all_list = df['Route'].to_list()
    route_list = list(dict.fromkeys(route_all_list))
    return route_list

def getCities(df, route):
    cities_df = df.loc[df['Route'] == route]
    cities_all = cities_df['City'].to_list()
    cities = list(dict.fromkeys(cities_all))
    return cities

def getMaindf():
    cwd = os.getcwd()
    mdf = pd.read_excel(mainFs)
    return mdf

def filterCities(mdf, cityList, route):
    cityListUpper = []
    for city in cityList:
        cityListUpper.append(city)
        cityListUpper.append(city.upper())
        cityListUpper.append(city.title())
    rdf = mdf.loc[mdf['City'].isin(cityListUpper)]
    outpath = outDir + route + ".xlsx"
    rdf.to_excel(outpath, index=False)


if __name__ == '__main__':
    df_route = getRoutes()
    route_list = gerRoutesList(df_route)
    # print(route_list)
    df_main = getMaindf()
    for route in route_list:
        cities = getCities(df_route, route)
        filterCities(df_main, cities, route)
