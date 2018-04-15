import requests

'''
TODO: how the fuck python parse the json string?
save to a file everything? meeh lets see it
'''

# def requestDivisions(self, region, summoner, api):

def requestChallenjours(region, queue, api):
        URL = "https://"+ region + ".api.riotgames.com/lol/league/v3/challengerleagues/by-queue/"+ queue + "?api_key=" + api
        print(URL)
        get = requests.get(URL)
        # filtering the json to shows:
        # name of the league
        # playerOrTeamName -- about the player
        # leaguePoints -- about the player
        # wins -- about the player
        # losses -- about the player
        return get.json()

def requestPlayerData(region, ID, api): # or requestPlayerData(region, summonerName, api): ?
	URL = None # read the doc on riot api
	get = request.get(URL)
	return get.json()

def main():
    print("Current, only GET all of the Challenger on a certain region.")
    print("List of all functions on this script:" \
                                                "\n\t1 - GET all players on challenger ladder" \
                                                "\n\tThats it")
    try:
        option = int(input("Enter your option: "))

        if option == 1:
            region = str(input("[*] Enter your region: "))
            # summoner = str(input("[*] Enter your summoner name: "))
            api = str(input("[*] Enter your API Key: "))
            availableQueues = [
                                "RANKED_SOLO_5x5",
                                "RANKED_FLEX_SR",
                                "RANKED_FLEX_TT"
                            ]
            print("Available queues: {}".format(availableQueues))
            queue = str(input("Enter your desired queue: "))
            # print("It looks like you have entered: {}, {}, {}".format(region, summoner, api))
            print(requestChallenjours(region, queue, api))

	elif option == 2:
	   region = str(input("[*] Enter the region: "))
	   summoner = str(input("[*] Enter the summoner ID: "))
	   # how does the api search for a summoner? summoner ID or summonerName???
	   summonerName = str(input("[*] Enter the summoner Name: "))
	   api = str(input("[*] Enter your API key: "))
	   print(requestPlayerData(region, summoner, api)) # or requestPlayerData(region, summonerName, api))

    except ValueError:
            print("Only numbers allowed")

if __name__ == "__main__":
    main()
