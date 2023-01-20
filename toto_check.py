import requests
from bs4 import BeautifulSoup

def toto_check():
    url = "https://www.singaporepools.com.sg/en/product/sr/Pages/toto_results.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    draw_results = []

    for winning_numbers in soup.find_all('td', width="16%"):
        draw_results.append(winning_numbers.text)

    additional_number = soup.find('td', class_='additional').text
    draw_results.append(additional_number)

    draw_results = ','.join(draw_results)
    draw_results = set(draw_results.split(","))
    draw_results = {int(i) for i in draw_results}
    print("\nDraw results: ", draw_results)

    with open("numbers.txt", "r") as f:
        for line in f:
            ticket_numbers = set(line.strip().split(","))
            ticket_numbers = {int(i) for i in ticket_numbers}
            match = draw_results.intersection(ticket_numbers)
            counter = len(match)
            print("Ticket Number: ", ticket_numbers)
            match = match if counter > 0 else "{}"
            print("Matched numbers: ", match)
            if counter == 3:
                print("\033[0;32m" + "3 Matches!" + "\033[00m")
            elif counter == 4:
                print("\033[0;32m" + "4 Matches!" + "\033[00m")
            elif counter == 5:
                print("\033[0;32m" + "5 Matches!" + "\033[00m")
            elif counter == 6:
                print("\033[0;32m" + "Time to buy a lambo!" + "\033[00m")
            print()

toto_check()