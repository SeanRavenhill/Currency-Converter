import requests

curr_code = input().lower()

r = requests.get("http://www.floatrates.com/daily/" +
                 curr_code + ".json").json()

cache = {}

if curr_code != "usd":
    cache["usd"] = r["usd"]["rate"]

if curr_code != "eur":
    cache["eur"] = r["eur"]["rate"]

while True:
    exch_code = input().lower()
    if exch_code == "":
        break
    else:
        amnt_to_exch = input()
        print("Checking the cache...")
        if exch_code in cache:
            print("Oh! It is in the cache!")
        else:
            print("Sorry, but it is not in the cache!")
            cache[exch_code] = r[exch_code]["rate"]
    print("You received " + str(round((float(amnt_to_exch) *
          r[exch_code]["rate"]), 2)) + " " + exch_code.upper() + ".")

exit()
