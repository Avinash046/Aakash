import webbrowser

def handle(command):
    command = command.lower()
    if 'movie' in command:
        print("Aakash: Opening BookMyShow for movie booking...")
        webbrowser.open('https://in.bookmyshow.com/')
    elif 'train' in command:
        print("Aakash: Opening IRCTC for train booking...")
        webbrowser.open('https://www.irctc.co.in/')
    elif 'flight' in command:
        print("Aakash: Opening MakeMyTrip for flight booking...")
        webbrowser.open('https://www.makemytrip.com/flights/')
    elif 'bus' in command:
        print("Aakash: Opening RedBus for bus booking...")
        webbrowser.open('https://www.redbus.in/')
    elif 'uber' in command:
        print("Aakash: Opening Uber website...")
        webbrowser.open('https://m.uber.com/')
    elif 'ola' in command:
        print("Aakash: Opening Ola website...")
        webbrowser.open('https://www.olacabs.com/')
    elif 'rapido' in command:
        print("Aakash: Opening Rapido website...")
        webbrowser.open('https://www.rapido.bike/')
    else:
        print("Aakash: Please specify what you want to book (movie, train, bus, flight, Uber, Ola, Rapido, etc.)")