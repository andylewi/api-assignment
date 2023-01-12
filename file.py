import requests
import json
from PIL import Image
import shutil

num_of_quotes = 20
key = ''

api_url = 'https://api.breakingbadquotes.xyz/v1/quotes/{0}'.format(num_of_quotes)
print()
response = requests.get(api_url)
json_data = json.loads(response.text)
#json_data = []
quotes = {}
names = set()

question = None

for data in json_data:
    quote = data['quote']
    author = data['author']
    quotes[quote] = author
    names.add(author)


for q in quotes.keys():
    question = q
    break

multiple_choice = set()
multiple_choice.add(quotes[question])
for i in names:
    multiple_choice.add(i)
    if len(multiple_choice) == 4:
        break
print("Quote:")
print(question)
print('\nPotential names to choose from\n')
for choice in multiple_choice:
    print(choice)
author = input('\nPlease enter a guess:\n')
while(author.lower() != quotes[question].lower()):
    author = input('\nThat was incorrect, try again!:\n')

print("Correct!")
#print(quotes)
search_name = quotes[question].replace(' ', '+')

print()
api_url = 'https://serpapi.com/search.json?q={0}&tbm=isch&ijn=0&api_key={1}'.format(search_name, key)
response = requests.get(api_url)
json_data = json.loads(response.text)
#print(json_data['images_results'][0]['original'])
img_url = json_data['images_results'][0]['original']

#url = input('Please enter an image URL (string):') #prompt user for img url
#file_name = input('Save image as (string):') #prompt user for file_name
file_name = 'a.png'

#url = 'https://media.geeksforgeeks.org/wp-content/uploads/20190712221555/png-248x300.png'
res = requests.get(img_url, stream = True)

if res.status_code == 200:
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    #print('Image sucessfully Downloaded: ',file_name)
else:
    print('Image Couldn\'t be retrieved')


im = Image.open(r"a.png")
im.show()

import climage

# converts the image to print in terminal
# inform of ANSI Escape codes
output = climage.convert('a.png')

# prints output on console.
print(output)
