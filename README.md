# pw-lab5
# Web Programming laboratory work no.5 - Websockets

## Requirements 
- Implement a command line program named ***go2web***.
- The program should implement the following CLI options:
    - **-u `<URL>`** : Make an HTTP request to the specified URL and print the response
    - **-s `<search-term>`** : Make an HTTP request to search the term using a preferred search engine and print the top 10 results.
    - **-h** : Display help information.
- Responses from requests should be in human-readable format, without HTML tags in the output.
- No built-in or third-party libraries for making HTTP requests are allowed.
- No GUI applications.
- The application must be launched using the ***go2web*** executable.
- Include a GIF with a working example in the README file.

### Points:
- executable with `-h`, (`-u` or `-s`) options - `+5 points`
- executable with `-h`, (`-u` and `-s`) options - `+6 points`

### Extra points:
- Results/links froms earch engine can be accessed (unsing the CLI) `+1 point`
- HTTP request redirects implementation `+1 point`
- HTTP cache mechanism `+2 points`
- Content negotiation (accepting and handling both JSON and HTML content types) `+2 points`
