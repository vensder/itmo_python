def parse_html():
	from html.parser import HTMLParser
	
	
	class MyHTMLParser(HTMLParser):
		def handle_starttag(self, tag, attrs):
			print("Encountered a start tag:", tag)
		def handle_endtag(self, tag):
			print("Encountered an end tag :", tag)
		def handle_data(self, data):
			print("Encountered some data  :", data)

	parser = MyHTMLParser()
	parser.feed(open('index.html').read())

if __name__=='__main__':
	parse_html()
