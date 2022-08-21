import requests

API_URL = "https://api-inference.huggingface.co/models/kaliani/flair-ner-skill"
headers = {"Authorization": "Bearer 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"}

def query(line):
	response = requests.post(API_URL, headers=headers, json={"inputs": line})
	return response.json()

