import json
import urllib.request


class XKCDTHING(object):
	def __init__(self):
		self.subscribers = []  # list of functions to call

	def subscriber(self, func):
		self.subscribers.append(func)  # decorator add func() to list
		return func

	def publish(self, title, link):
		for func in self.subscribers:
			func(title, link)  # call every function in the list

	def run(self):
		url = "https://xkcd.com/info.0.json"
		with urllib.request.urlopen(url) as req:
			data = json.loads(req.read().decode())
			title = data['safe_title']
			link = data['img']
			self.publish(title, link)

		# do things and publish events


if __name__ == '__main__':
	app = XKCDTHING()


	@app.subscriber
	def eventhander1(title, link):
		print("Event handler 1 called")
		print(f'Title: {title}')


	@app.subscriber
	def eventhander2(title, link):
		print("Event handler 2 called")
		print(f'Link: {link}')

	app.run()