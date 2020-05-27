import requests
texy = open ('dataset_3378_3.txt','r')
sl = texy.readline().strip()
mame_file = requests.get(sl).text
while mame_file[0:2] != 'We':




    url='https://stepic.org/media/attachments/course67/3.6.3/'+ mame_file
    print(url)
    mame_file = requests.get(url).text

print(requests.get(url).text)