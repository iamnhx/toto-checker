from datetime import datetime
def toto_check():
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    open(date + ' TOTO Results.txt', 'w').close()
    draw_results = set(input("Enter the draw results(comma separated): ").split(","))
    draw_results = {int(i) for i in draw_results}
    with open("numbers.txt", "r") as f:
        for line in f:
            ticket_numbers = set(line.strip().split(","))
            ticket_numbers = {int(i) for i in ticket_numbers}
            match = draw_results.intersection(ticket_numbers)
            counter = len(match)
            with open(date + ' TOTO Results.txt', 'a+', encoding='utf-8') as f:
                f.write("Draw results: " + str(draw_results) + "\n")
                f.write("Ticket Number: " + str(ticket_numbers) + "\n")
                f.write("Number of matches: " + str(counter) + "\n")
                match = match if counter > 0 else "none"
                f.write("Matched numbers: " + str(match) + "\n\n")
toto_check()