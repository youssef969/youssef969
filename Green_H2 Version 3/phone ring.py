import requests
url = "https://calling.api.sinch.com/calling/v1/callouts"
payload="{\n  \"method\": \"ttsCallout\",\n  \"ttsCallout\": {\n    \"cli\": \"+447520652429\",\n    \"domain\": \"pstn\",\n    \"destination\": {\n      \"type\": \"number\",\n      \"endpoint\": \"+201096923909\"\n    },\n    \"locale\": \"en-US\",\n    \"prompts\": \"#tts[There is a hydrogen gas leak. Please go to the hydrogen field to fix the problem]\"\n  }\n}"
headers = {
'Content-Type': 'application/json',
'Authorization': 'Basic YjgxNGE1OGUtMTkxMy00ZGZhLTgzN2YtZDJjMDE5YmRkYjIyOkxTeGdjTWcyaVVpaXB4SUg1anM1aWc9PQ=='
                        }
response = requests.request("POST", url, headers=headers, data=payload)