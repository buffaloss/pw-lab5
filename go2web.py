import sys
from urllib.parse import urlparse
import socket
import ssl
from bs4 import BeautifulSoup
import json

with open('cache.json', 'r') as f:
    cache = json.load(f)


def send_request(url):
    parsed_url = urlparse(url)
    host = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query
    if query:
        path = path + '?' + query
    if path:
        ...
    else:
        path = "/"

    if host + path in cache:
        print('Found in cache')
        return cache[host + path]

    port = 80
    ssl_port = 443
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if url[:5] == "https":
        sock.connect((host, ssl_port))
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=host)
    else:
        sock.connect((host, port))

    sock.send(
        f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n'.encode())
    response = b''
    data = 1
    while data:
        data = sock.recv(1024)
        response += data
    sock.close()

    headers = response.split(b"\r\n\r\n")[0].decode().splitlines()

    for header in headers:
        if header.lower().startswith("location"):
            redirect_url = header.split(": ")[1]
            print('Redirecting')
            return send_request(redirect_url)

    try:
        decoded_response = response.decode('utf-8')
    except UnicodeDecodeError:
        decoded_response = response.decode('ISO-8859-1')

    cache[host + path] = decoded_response
    with open('cache.json', 'w') as f:
        json.dump(cache, f)

    return decoded_response


def get_page(url):
    res = send_request(url)
    soup = BeautifulSoup(res, 'html.parser')
    contents = soup.body.get_text(separator='\n\n', strip=True).strip()
    print(contents)


def google_search(search_terms):
    query = ""
    for term in search_terms:
        query += term + '+'
    url = f"https://www.google.com/search?q={query[:-1]}"
    res = send_request(url)
    soup = BeautifulSoup(res, 'html.parser')
    for h3_tag in soup.find_all('h3'):
        parent_anchor = h3_tag.find_parent('a')
        if parent_anchor:
            addr = parent_anchor.get('href')
            if addr:
                addr = addr.split("?q=")[-1].split('&')[0]
                print(addr)


def main():
    if len(sys.argv) == 1 or sys.argv[1] == "-h":
        print(
            '''
go2web -u <URL>            Make an HTTP request to a specified URL and print the response
go2web -s <search-term>    Make an HTTP request to search a term using a search engine and print the top 10 results
go2web -h                  Show help
            '''
        )
        sys.exit(0)

    if sys.argv[1] == "-u":
        url = sys.argv[2]
        get_page(url)

    elif sys.argv[1] == "-s":
        search_term = tuple(sys.argv[2:])
        google_search(search_term)

    else:
        print("Invalid usage.  Please use 'go2web -h' for help.")


if __name__ == "__main__":
    main()
