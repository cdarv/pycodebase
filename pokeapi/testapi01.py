import requests



URL = 'https://pokeapi.co/api/v2'

def main():
    resp = requests.get(URL).json()
    print(resp)


if __name__ == "__main__":
    main()
