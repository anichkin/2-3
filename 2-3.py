import json
from pprint import pprint

def top10(text, coding):
	with open (text, encoding=coding) as news_file:
		all_news = []
		words_sort = []
		news = json.load(news_file)
		pprint(len(((news.get("rss")).get("channel")).get('items')))
		for i in range(len(((news.get("rss")).get("channel")).get('items'))):
			all_news.append((((((news.get("rss")).get("channel")).get('items'))[i]).get('description')).split())

		words = []	
		for i in range(len(((news.get("rss")).get("channel")).get('items'))):
			for j in range(len(all_news[i])):
				words.append(all_news[i][j])
		words.sort()
		words_repeat = {}
		repeat = 0
		for i in range(0, len(words)-1):
			if words[i] == words[i+1] and len(words[i])>6:
				repeat += 1
			else:
				words_repeat[words[i]] = repeat
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
    print('файл newsafr.json')
    top10('newsafr.json', 'UTF-8')
    print()
    print('файл newscy.json')
    top10('newscy.json', 'KOI8-R')
    print()
    print('файл newsfr.json')
    top10('newsfr.json', 'ISO-8859-5')
    print()
    print('файл newsit.json')
    top10('newsit.json', 'CP1251')
    print()
    program()
  elif command == '2':
    text = input('Введите название текста с расширением ')
    coding = input('Введите кодировку файла ')
    top10(text, coding)
    program()
  
  

program()    		
			

	

	
	
		
	
	
		









	# pprint(((((news.get("rss")).get("channel")).get('items'))[0]).get('description'))
