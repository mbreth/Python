import webbrowser

while True:
    search=input('Search: ')
    if search in ('amazon.com', 'games.com'):
        print('Invalid search criteria. Try again')

    if search not in ('amazon.com', 'games.com'):
webbrowser.open('http://'+search)
