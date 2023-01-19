# import requests

# url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer-text"

# payload = "text=Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another.&sentnum=5"
# headers = {
# 	"content-type": "application/x-www-form-urlencoded",
# 	"X-RapidAPI-Key": "a2e496fbc6mshfb15f8bab0980efp15cfc9jsn6aef1c1d3ccc",
# 	"X-RapidAPI-Host": "textanalysis-text-summarization.p.rapidapi.com"
# }

# response = requests.request("POST", url, data=payload, headers=headers)

# print(response.text)\


# import requests
# r = requests.post(
#     "https://api.deepai.org/api/summarization",
#     data={
#         'text': 'Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is another',
#     },
#     headers={'api-key': 'c2b6eae4-aeb6-418f-9d10-802264f08718'}
# )
# print(r.json())


import requests

url = "https://textanalysis-text-summarization.p.rapidapi.com/text-summarizer"

payload = {
	"url": "http://en.wikipedia.org/wiki/Automatic_summarization",
	"text": "Automatic summarization is the process of reducing a text document with a computer program in order to create a summary that retains the most important points of the original document. As the problem of information overload has grown, and as the quantity of data has increased, so has interest in automatic summarization. Technologies that can make a coherent summary take into account variables such as length, writing style and syntax. An example of the use of summarization technology is search engines such as Google. Document summarization is anothe",
	"sentnum": 8
}
headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "a2e496fbc6mshfb15f8bab0980efp15cfc9jsn6aef1c1d3ccc",
	"X-RapidAPI-Host": "textanalysis-text-summarization.p.rapidapi.com"
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)