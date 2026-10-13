
import sys
import requests

session = requests.Session()

def call(url):
    try:
        response = session.get(url, timeout=10)
        return response.status_code, len(response.text)
    except requests.exceptions.RequestException as erro:
        return None, 0

if __name__ == '__main__':
    url, filename, condition = sys.argv[1], sys.argv[2], sys.argv[3]

    print(url.replace('{hack}', 'n4buc0d0n0s0r'))
    s0, t0 = call(url.replace('{hack}', 'n4buc0d0n0s0r'))

    print(60 * '#')
    print(f"url: {url.replace('{hack}', '')}")
    print(f"file: {filename}")
    print(f"Status test: {s0} | Length test: {t0}")
    print(60 * '#')

    with open(filename, 'r') as f:
        for row in f:
            hack = row.strip()
            test = url.replace('{hack}', hack)

            s1, t1 = call(test)

            text =  f"Url: {test.ljust(45, ' ')} | Status: {s1} | Length: {t1}"

            if condition == 'True':
                if t0 != t1:
                    print(text, '<- possible target' if t0 != t1 else '')
            else:
                print(text, '<- possible target' if t0 != t1 else '')

    session.close()
