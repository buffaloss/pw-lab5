import sys

def make_request(url):
    print(f"Making an HTTP request to the URL: {url}")

def search(search_term):
    print(f"Searching for the term: {search_term}")

def show_help():
    print("\nUsage: go2web [options]")
    print("Options:")
    print("  -u <URL>            Make an HTTP request to the specified URL and print the response")
    print("  -s <search-term>    Make an HTTP request to search the term using your favorite search engine and print top 10 results")
    print("  -h                  Show this help")
    print()

def process_input(user_input):
    if user_input.startswith("go2web"):
        parts = user_input.split()
        if len(parts) == 2:
            if parts[1] == '-h':
                show_help()
            else:
                print("Incomplete command. Please provide more details.")
        elif len(parts) == 3:
            if parts[1] == '-u':
                make_request(parts[2])
            elif parts[1] == '-s':
                search(parts[2])
            else:
                print("Invalid command. Please use '-u' or '-s' options.")
        else:
            print("Invalid command. Please provide valid options.")

if __name__ == "__main__":
    while True:
        user_input = input()
        process_input(user_input)
