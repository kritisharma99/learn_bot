import glob

def search_topic(topic_to_find):

	topics_on_files = []

	for chapters in  glob.glob("*.txt"):

		try:
			with open(chapters,"r") as f:
				text = f.read()

				paragraphs = text.split("\n\n")

				topic = paragraphs[1].strip()
				print(topic)

				if topic.lower().find( topic_to_find.lower() ) > 0:
					topics_on_files.append(chapters)
		except Exception as ex:
			print(ex)

	#print( topics_on_files )
	return topics_on_files

def whole_chapter(file):

	with open(file) as f:
		text = f.read()

	return text


if __name__ == "__main__":

	for i in search_topic("AI"):

		print( whole_chapter(i) )
