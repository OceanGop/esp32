from requests.exceptions import ConnectionError
import time


url = 'http://192.168.1.57/'

while True:
        try:
                result = requests.get(url)
        except ConnectionError:
                print('Connection error, sleep for 15 seconds')
        else:
                if result.status_code == 200:
                        names = ['temp', 'hum', 'pressure', 'altitude', 'co2']
                        a, b, c, d, e, *other = result.text.split('|')
                        data = [a, b, c, d, e]
                        for name, value in zip(names, data):
                                with open(name, 'w') as f:
                                        f.write(value)
                        print(data)
                else:
                        print(f'Status code: {result.status_code}')
        time.sleep(15)
