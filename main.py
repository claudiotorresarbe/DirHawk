
import sys
import requests

session = requests.Session()

def record(filename,row):
    with open(filename,'a+') as f:
        f.write(f'{row}\n')

def call(url):
    try:
        response = session.get(url, timeout=3)
        return response.status_code, len(response.text)
    except requests.exceptions.RequestException as erro:
        return None, 0

if __name__ == '__main__':
    url = sys.argv[1]
    filename = sys.argv[2]
    condition = sys.argv[3]
    save = sys.argv[4] if len(sys.argv) > 4 else None

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

            status = str(s1) if s1 is not None else "ERR"
            text = f"Url: {test.ljust(50)} | Status: {status:>4} | Length: {t1:>6}"

            if condition == 'True':
                if t0 != t1:
                    print(f"[+] {text}  ← possible target")

            if save:
                record(save, text)

            else:
                pass

    session.close()
