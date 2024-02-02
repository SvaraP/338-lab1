import json
import matplotlib.pyplot as plt 

with open('songdata.json', 'r') as json_file:
    content = json.load (json_file)
    
loud = []
quiet = []

for songs in content:
    if songs['loudness'] >= -8:
        loud.append(songs)
    else:
        quiet.append(songs)
        
        
tempo_loud = []
tempo_quiet =[]

for songs in loud:
    tempo_loud.append(songs['tempo'])

for songs in quiet:
    tempo_quiet.append(songs['tempo'])
    
    
plt.figure(figsize = (10,10))
plt.hist(tempo_loud, color ='green', edgecolor = 'black')
plt.xlabel('Tempo')
plt.ylabel('Songs')
plt.title('Tempo of Loud Songs Vs. the Number of Songs')
plt.savefig('hist1.png')


plt.figure(figsize = (10,10))
plt.hist(tempo_quiet, color ='blue', edgecolor = 'black')
plt.xlabel('Tempo')
plt.ylabel('Songs')
plt.title('Tempo of Quiet Songs Vs. the Number of Songs')
plt.savefig('hist2.png')

