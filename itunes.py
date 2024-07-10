import requests
import json
import sys


def main():
    if len(sys.argv) != 2:
        print(len(sys.argv))
        sys.exit()

    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
    o = response.json()
    # print(json.dumps(o, indent=2))
    for result in o["results"]:
        print(result["trackName"])


main()
