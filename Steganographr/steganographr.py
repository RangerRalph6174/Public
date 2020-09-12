import requests, sys, subprocess

def steganographr(public, private="Hello, World"):
    parameters = {"public":public, "private":private}
    url = "https://neatnik.net/steganographr/api/?"

    response = requests.get(url, params=parameters).text
    subprocess.run("pbcopy", universal_newlines=True, input=response)
    return response

def main(args):
    if len(args) > 1:
        steganographr(args[0], args[1])
    else:
        steganographr(args[0])

if __name__ == '__main__':
    if len(sys.argv) > 1:  
        main(sys.argv[1:])
    else:
        sys.exit("No message given")
