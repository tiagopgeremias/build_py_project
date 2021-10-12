import httpx
import json

def runModule():
	http = httpx.get("https://randomuser.me/api/")
	data_json = json.loads(http.text)
	print(data_json)


if __name__ == '__main__':
	runModule()

