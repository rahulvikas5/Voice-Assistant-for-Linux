from newsapi import NewsApiClient
import pycountry
from sp_function import *

# you have to get your api key from newsapi.com
newsapi = NewsApiClient(api_key='04b548362d2d46ec920c68c3f15277ff')


def get_news():
    # Country is set to India by default
    input_country = 'India'
    input_countries = [f'{input_country.strip()}']
    countries = {}

    # iterate incase multiple countries are mentioned!!
    for country in pycountry.countries:
        # and store the unique code of each country
        # in the dictionary along with it's full name
        countries[country.name] = country.alpha_2

    # now we will check that the entered country name is
    # valid or invalid using the unique code
    codes = [countries.get(country.title(), 'Unknown code')
             for country in input_countries]

    # now we have to display all the categories from which user will
    # decide and ask the name of that category
    print(
        "Linux Assistant: Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
    speak("Which category are you interested in?")
    option = takeCommand()
    # now we will fetch the new according to the choice of the user
    top_headlines = newsapi.get_top_headlines(

        # getting top headlines from all the news channels
        category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

    # fetch the top news under that category
    Headlines = top_headlines['articles']
    c = 0
    # now we will display the that news with a good readability for user
    print("Linux Assistant: ")
    if Headlines:
        for articles in Headlines:
            b = articles['title'][::-1].index("-")
            if "news" in (articles['title'][-b + 1:]).lower():
                print(
                    f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
                g_speak(f"{articles['title'][-b + 1:]}: {articles['title'][:-b - 2]}.")
            else:
                print(
                    f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
                g_speak(f"{articles['title'][-b + 1:]} News: {articles['title'][:-b - 2]}.")
            c = c + 1
            if c == 5:
                break

    else:
        print(f"Sorry no articles found for {input_country}, Something Wrong!!!")
        g_speak(f"Sorry no articles found for {input_country}, Something Wrong!!!")
