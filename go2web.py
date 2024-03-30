import sys

def show_help():
    print("\nUsage: go2web [options]")
    print("Options:")
    print("  -u <URL>            Make an HTTP request to a specified URL and print the response")
    print("  -s <search-term>    Make an HTTP request to search a term using a search engine and print the top 10 results")
    print("  -h                  Show help")
    print()

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] != '-h':
        print("Invalid usage. Please use 'go2web -h' for help.")
        sys.exit(1) 

    show_help()
