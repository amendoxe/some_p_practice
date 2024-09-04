import sys
import requests
import json  # if you want to print a json instead of raw file


def main():
    if len(sys.argv) != 2:
        print(len(sys.argv))
        sys.exit()
    # r is used for raw
    response = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=20&term=" + sys.argv[1])
    o = response.json()
    # print(json.dumps(o, indent=2))
    for result in o["results"]:
        print(result["trackName"])


main()
