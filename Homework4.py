import requests
from selenium import webdriver
import names

repos = requests.get("https://api.github.com/users/avielb/repos")
number_of_repos = len(repos.json())
try:
    assert number_of_repos > 5
except AssertionError:
    print("avielb has less than 5 repos")
else:
    print(f"the number of repos is {number_of_repos}")

names_array = []
for i in range(3):
    random_name = names.get_first_name()
    random_name_age = requests.get(f"https://api.agify.io/?name={random_name}").json()["age"]
    if not 0 <= random_name_age <= 120:
        names_array.append((random_name, random_name_age))
try:
    assert len(names_array) == 0
except AssertionError:
    print(f"The following names were not between 0 and 120:\n {names_array}")
else:
    print("All ages are between 0 and 120")
universities = requests.get("http://universities.hipolabs.com/search?country=Israel")
number_of_universities = len(universities.json())
try:
    assert number_of_universities > 5
except AssertionError:
    print(f"Israel has only {number_of_universities} universities")
else:
    print(f"Israel has {number_of_universities} universities")


def compare_title_text(given, expected):
    try:
        assert given == expected
    except AssertionError:
        print(f"Expected \"{expected}\" but received \"{given}\"")
    else:
        print(f"The title of the site is {given}")


test_driver = webdriver.Chrome()
test_driver.get("https://www.ycombinator.com/")
compare_title_text(test_driver.title, "Y Combinator")
test_driver.get("https://hub.docker.com")
compare_title_text(test_driver.title, "Docker Hub Container Image Library |App Containerization")
