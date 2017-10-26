def top10(text):
	from xml.etree import ElementTree as ET

	tree = ET.parse(text)
	root=tree.getroot()
	channel = root.find('channel')
	news_items = channel.findall('item')
	all_news = []
	words = []
	for i in range(len(news_items)):
		all_news.append(news_items[i])
	for i in range(len(news_items)):
		words.append((news_items[i][2].text).split())
	words_sort = []
	for i in range(len(words)):
		for j in range(len(words[i])):
			words_sort.append(words[i][j])
	words_sort.sort()
	words_repeat = {}
	repeat = 0
	for i in range(0, len(words_sort)-1):
		if words_sort[i] == words_sort[i+1] and len(words_sort[i])>6:
			repeat += 1
		else:
			words_repeat[words_sort[i]] = repeat
			repeat = 0

	def max_pair():
		for key, repeat in words_repeat.items():
			if repeat == max(words_repeat.values()):
				print(key, repeat)
				words_repeat.pop(key)
				break

	for i in range(10):
		max_pair()


def program():
  print('введите команду: ')
  print('1 - вывод по всем файлам')
  print('2 - ручной ввод')
  command = input('введите команду: ')
  if command == '1':
    print('файл newsafr.xml')
    top10('newsafr.xml')
    print()
    print('файл newscy.xml')
    top10('newscy.xml')
    print()
    print('файл newsfr.xml')
    top10('newsfr.xml')
    print()
    print('файл newsit.xml')
    top10('newsit.xml')
    print()
    program()
  elif command == '2':
    text = input('Введите название текста с расширением ')
    top10(text)
    program()
  
  

program()    