import sys
from urllib.parse import urlparse
import socket, ssl
from bs4 import BeautifulSoup

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

    port = 80
    ssl_port = 443
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if url[:5] == "https":
        sock.connect((host, ssl_port))
        context = ssl.create_default_context()
        sock = context.wrap_socket(sock, server_hostname=host)
    else:
        sock.connect((host, port))

    sock.send(f'GET {path} HTTP/1.1\r\nHost:{host}\r\nConnection: close\r\n\r\n'.encode())
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

    return decoded_response

def get_page(url):
    res = send_request(url)
    soup = BeautifulSoup(res, 'html.parser')
    contents = soup.body.get_text(separator='\n\n', strip=True).strip()
    print(contents)
    

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

    else:
        print("Invalid usage.  Please use 'go2web -h' for help.")


if __name__ == "__main__":
    main()