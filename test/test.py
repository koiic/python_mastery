import urllib

url = "http://textfiles.com/adventure/aencounter.txt"
pathname = urllib.url2pathname(url)
file = urllib.request.urlopen(url)
print(file)
# for line in file:
# 	decoded_line = line.decode("utf-8")
# 	print(decoded_line)