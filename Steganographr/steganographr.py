import requests, sys, subprocess, argparse

class steganographr():

    def hide(self, public, private="Hello, World!"):

        parameters = {"public":public, "private":private}
        url = f"https://neatnik.net/steganographr/api/?"

        response = requests.get(url, params=parameters).text
        subprocess.run("pbcopy", universal_newlines=True, input=response)
        return response

    def reveal(self, public):

        url = f"https://neatnik.net/steganographr/api?decode={public}"
        response = requests.get(url).text

        if len(response) > 2:
            print(response)
        else:
            print("No secret message found")

def create_parser():
    parser = argparse.ArgumentParser(usage= "%(prog)s -d -p 'public message' || %(prog)s -p 'public message' || %(prog)s -p 'public message' -s 'secret message'",
     description="Hides a secret message inside a public message or reveals the private message hidden inside a public message.")
    parser.add_argument("-d", action="store_true", help="Required with -p to (d)ecrypt the hidden message inside the provided Public message.")
    parser.add_argument("-s", metavar='', help="an optional (s)ecret message to replace the default")
    parser.add_argument("-p", required=True, metavar='', help="The (p)ublic message. If entered alone the default secret message will be hidden within.")
    return parser

def main(args):
    parser = create_parser()
    ns = parser.parse_args(args)
    steg = steganographr()

    if not ns.d and not ns.p:
        sys.exit("No public and/or private message given")
    elif ns.d and ns.p:
        steg.reveal(ns.p)
    elif ns.p and not ns.s and not ns.d:
        steg.hide(ns.p)
    elif ns.p and ns.s:
        steg.hide(ns.p, ns.s)

if __name__ == '__main__':
    main(sys.argv[1:])
   


