import requests

def try_me():
    print("You want a chuck norris joke?")
    x = input('y/n: ')
    if x.lower() == 'y':
        url = 'https://api.chucknorris.io/jokes/random'
        response = requests.get(url)
        data = response.json()
        return data['value']
    if x.lower() == 'n':
        return 'Bye then'
    else:
        return 'I said either y or n'
