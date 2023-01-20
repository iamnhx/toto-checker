import requests
from bs4 import BeautifulSoup

def toto_check():
    url = "https://www.singaporepools.com.sg/en/product/sr/Pages/toto_results.aspx"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    draw_results = set()

    for winning_numbers in soup.find_all('td', width="16%"):
        draw_results.update(map(int, winning_numbers.text.split(',')))
    additional_number = soup.find('td', class_='additional').text

    draw_results.add(int(additional_number))

    print(f"\033[0;31m Draw Results: {draw_results} \033[00m")
    print()

    with open("numbers.txt", "r") as f:
        for line in f:
            ticket_numbers = set(map(int, line.strip().split(",")))
            match = draw_results.intersection(ticket_numbers)
            counter = len(match)
            match = match if counter > 0 else "{}"
            print("Ticket Numbers: ", ticket_numbers)
            print("Matched Numbers: ", match)
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
