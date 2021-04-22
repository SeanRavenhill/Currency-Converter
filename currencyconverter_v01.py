import requests

print('''
Welcome to my simple currency converter.

The exchange rates are pulled from http://www.floatrates.com/json-feeds.html
which updates daily (once in 12 hours at 12 AM/PM).

Instructions:
 - Please make use of standard 3 character currency code at inputs.

 - Note you can input amounts with fractional values ie. 12.22.

 - When you are finished, to exit the program either type "exit" or simply
   hit your Enter key when prompted for an input.
''')

curr_code = input("Please input the code for the currency you have: ").lower()

if curr_code == "" or curr_code == "exit":
    exit()

r = requests.get("http://www.floatrates.com/daily/" +
                 curr_code + ".json").json()

while True:
    exch_code = input("Please input the code for the currency"
                      " you want: ").lower()

    if exch_code == "" or exch_code == "exit":
        break
    else:
        amnt_to_exch = input("Please enter the amount you want to exchange: ")

    print(str(amnt_to_exch) + " " + curr_code.upper() + " exchanges to " +
          str(round((float(amnt_to_exch) * r[exch_code]["rate"]), 2)) + " "
          + exch_code.upper() + ".\n")

exit()
