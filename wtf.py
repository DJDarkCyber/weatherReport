import requests
from bs4 import BeautifulSoup

my_headers = {
	"GET": "/en/in/chennai/206671/weather-forecast/206671 HTTP/1.1",
	"Host": "www.accuweather.com",
	"User-Agent": "Mozilla/5.0 (Linux x86_64) Firefox",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
	"Accept-Language": "en-US,en;q=0.5",
	"Referer": "www.accuweather.com",
	"Connection": "close",
	"Cookie": "awx_id=1f07f9dd-5cdb-4cd1-928e-5027d6673672; awx_session_essential=pageView%3A2; AKA_A2=A; ak_bmsc=9CA0F92EB945AAA546B606FF2453097E~000000000000000000000000000000~YAAQWXbNF1K8JB+CAQAASdTxJhB0TQjJaBuS0XBFFPZMIm825eYSZhe68zzzx11/xbnPs1zmLVfHcvBkUxp375z8yUSO5yHvTwWRLiCCDnU28fsvkTuPihYt3mNoSN4larMGkHPkwS/FH7uusCf3fOiUHj9VLX4UbYG92X4in6rcDtQCRsP9TifU86CZb07ET2/b8XAJ13Zh6kmluspN+2vWIwzrOkM7o3F2QhvTSLaRqtGjtecUtaUyYXB8tA4ECiNCw6p2KCHWBU47HTUojq8TtA2wxe64S9YOJ9hx941G5GEnfsqv9Dw7JcHkTSJUW4O50eV7iYyy2nRPgU+RDdI/b3a2v8XUHWQttsGv0e0Fj4WYpPA5WpWQy+awZT6oz9mom5RwO3QU4BxWSdqm; us_privacy=1YNN; awx_user=tp:C|lang:en-us|rl:[206671]|cDate:2022-07-22; _pbjs_userid_consent_data=3524755945110770; userid3p=active; .AspNet.Consent=yes; bm_mi=E212BA9343A5F1440017570E36651FDA~YAAQWXbNF/m9JB+CAQAApvvxJhAphNk42V38ejkePSt9NhdcUUr1hZ5CaRnmaf4C/aWAeFpKVZSsKT9Tgvig39n6mpBmC2TwbtSWREkRREEYfBTdzF6w6glBIvNXxWSalV+qPKEAvTSf90FjiZqb/5qLyk5KIUfAn9UkXiEsvtYPs/CKfFDKDcuSDTgqg8Jt1rV+8Jb7VBHdUkXwXWNGcdqevmmaSoT9B7gLQ0sKa5IEGNOPCPS3DekeeYKHlSpMKtpWkBUPJXjBETOcwR2e3qvF+BTY5njeKBNNzhqlYYDyQV5a17oAp8w07z6a0uEM9PryJFwuBDysLOoMA7YJ2fUHoX1wvR3uMLT+iMIO5r3WL4zHPSInMYBLw9sVQg==~1; bm_sv=4C9E2175FF22A4C6FF246EFF253E41E9~YAAQWXbNF/q9JB+CAQAAp/vxJhA9BNyvk18MGZbKfypWcF19z0m9vhA+Ju0AIhaFnc6TR4fS/ZI5YCN4d04w6jfp4cnNlEtatY/AiHhsdolTBe+FQyhXx898jxQTUnFSBPmc2VepkYUNu2ycqlVLj+IIjsC15ZcRRhoeI50tZtKBvk5pnxUUGU7Wy3CDCY62tmDNa7LV7mNrE4AAEGmBge5wldzrtdLIwzmSQCsf69x9JfrvutSFkJlXqZNG1bhluO3ae/s=~1",
	"Upgrade-Insecure-Requests": "1",
	"Sec-Fetch-Dest": "document",
	"Sec-Fetch-Mode": "navigate",
	"Sec-Fetch-Site": "cross-site",
	"Sec-Fetch-User": "?1",
	"Cache-Control": "max-age=0",
}
mainUrl = "https://www.accuweather.com"
usrLocation = input("Enter the location > ")

query_location = requests.get("https://www.accuweather.com/en/search-locations?query=" + str(usrLocation), headers=my_headers)
soup_locations = BeautifulSoup(query_location.content, "html.parser")
links_sorted = soup_locations.find_all("div", class_="locations-list content-module")
collectd_location = []
collected_links = []
for aTags in links_sorted:
    for links in aTags.find_all("a"):
        collected_links.append(links.get("href"))
        collectd_location.append(links.get_text().replace("\n", "").replace("\t", ""))
i = 1
print(f"\n--Found {len(collected_links)} locations--")
if(len(collectd_location)) == 0:
    exit()
for prnLink in collectd_location:
    print(f"{i}. {prnLink}")
    i+=1
usrOpt = int(input("\n>_ "))
if usrOpt > len(collectd_location) or usrOpt < 1:
    print("Invalid choice!")
    exit()
cloud_data = requests.get(mainUrl+collected_links[usrOpt-1], headers=my_headers)
data_content = cloud_data.content

sort = BeautifulSoup(data_content, "html.parser")
temp_sort = sort.find_all("div", class_="temp")[0]
print(f"Current Weather in {collectd_location[usrOpt-1]} --> {temp_sort.get_text()}")
# print(sort.prettify())