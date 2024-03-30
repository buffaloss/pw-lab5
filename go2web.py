import sys
import socket

def show_help():
    print("\nUsage: go2web [options]")
    print("Options:")
    print("  -u <URL>            Make an HTTP request to a specified URL and print the response")
    print("  -s <search-term>    Make an HTTP request to search a term using a search engine and print the top 10 results")
    print("  -h                  Show help")
    print()

import socket

import socket

def http_request(url):
    url_parts = url.split('/')
    target_host = url_parts[2]
    target_path = '/' + '/'.join(url_parts[3:])
    
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.connect((target_host, 80))
    http_request_msg = f"GET {target_path} HTTP/1.1\r\nHost: {target_host}\r\n\r\n"
    connection.send(http_request_msg.encode())
    http_response = b''
    while True:
        data = connection.recv(1024)
        if not data:
            break
        http_response += data
    
    connection.close()
    
    print(http_response.decode())

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != '-h':
        print("Invalid usage. Please use 'go2web -h' for help.")
        sys.exit(1) 

    show_help()
