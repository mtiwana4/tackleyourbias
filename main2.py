keywords = ['stupid', 'rumor', 'rumored', 'rumors', 'spread', 'conspiracy', 'hate', 'fake', 'most', 'worst', 'brilliant', 'terrible', 'truth', 'freedom', 'really', 'intense', 'aggressive', 'hostile', 'hateful', 'outraged', 'vengeful', 'violent', 'bitter', 'disgusted', 'dread', 'dreadful', 'horrified', 'panicked', 'paralyzed', 'petrified', 'phobic', 'shocked', 'terrorized', 'blissful', 'ecstatic', 'elated', 'radiant', 'thrilled', 'anguished', 'depressed', 'despair', 'grief', 'heartbroken', 'hopeless', 'inconsolable', 'shame', 'guilt', 'disgraced', 'ostracized', 'shameful', 'stigma', 'stigmatized', 'possessive', 'greedy', 'reckless', 'agonized', 'bleak', 'doomed', 'gutted', 'you', 'fault', 'faulty']

emotionalwords = []
emotionalcount = 0
import urllib.request
website = input("Enter your website link here: ")
#website = "https://www.cbc.ca/player/play/1842148419691"
print(website)
f = urllib.request.urlopen(website)
myfile = f.read()
decoded_line = myfile.decode('UTF-8', 'strict')
#print(decoded_line)

for i in range(len(keywords)):
  if keywords[i] in decoded_line:
      emotionalwords.append(keywords[i])
      n = decoded_line.count(keywords[i])
      emotionalcount = emotionalcount + n
print(emotionalwords)
print(emotionalcount)
