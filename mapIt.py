import webbrowser
import sys

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
    webbrowser.open('https://www.google.com/maps/place/' + address)
else:
    print("Usage: add a place to find on the map while running. For eg. mapIt.py New York")