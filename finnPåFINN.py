# ! python3

# finnPåFINN.py - Opens FINN.no on the browser with the provided search term
# # usage: python finnPåFINN.py <query>

import webbrowser, sys, pyperclip


if len(sys.argv) > 1:
    # Get query from command line

        query = ' '.join(sys.argv[1:])

else:
    #Get query from clipboard

        query = pyperclip.paste()

webbrowser.open('https://www.finn.no/globalsearchlander?q=' + query)

