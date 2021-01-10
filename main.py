keywords = ['COVID-19', 'vaccine', 'coronavirus']
googlescholar = []
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
      googlescholar.append(keywords[i])
print(googlescholar)

url = 'https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q='

for i in range(len(googlescholar)):
  if i > 0:
    url = url + "+" + str(googlescholar[i])
  else:
    url = url + str(googlescholar[i])

url = url + '&btnG='

print (url)
