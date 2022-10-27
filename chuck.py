import sys

import requests

def main():
    response = requests.get('https://api.github.com')

    if response.status_code != 200:
        sys.exit('Nooo!')
        
    print('Success!')
    sys.exit()

if __name__ == "__main__":
    main()
