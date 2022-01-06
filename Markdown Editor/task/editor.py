def ordered_list(lst=''):
	num = int(input('Number of rows: '))
	if num <= 0:
		print('The number of rows should be greater than zero')
		return ordered_list(lst)

	new_list = []
	if lst == 'ordered-list':
		new_list = [f"{elem}. {input(f'Row #{elem}: ')}\n" for elem in range(1, num + 1)]
	elif lst == 'unordered-list':
		new_list = [f"* {input(f'Row #{elem}: ')}\n" for elem in range(1, num + 1)]

	stroke = ''.join(new_list)
	return stroke


def plain():
	text = input('Text: ')
	return text


def inline_code():
	text = input('Text: ')
	return '`' + text + '`'


def bold():
	text = input('Text: ')
	return '**' + text + '**'


def italic():
	text = input('Text: ')
	return '*' + text + '*'


def new_line():
	return '\n'


def link():
	link_text = input('Label: ')
	url = input('URL: ')
	return f'[{link_text}]({url})'


def header():
	while True:
		level = int(input('Level: '))
		if 6 >= level >= 1:
			text = input('Text: ')
			return '#' * level + ' ' + text + '\n'
		else:
			print('The level should be within the range of 1 to 6')


def markedown():

	new_dict = {'!help': """Available formatters: plain bold italic header link inline-code new-line
Special commands: !help !done""",
		            'plain': plain,
		            'bold': bold,
		            'italic': italic,
		            'header': header,
		            'link': link,
		            'inline-code': inline_code,
		            'new-line': new_line,
	            'ordered-list': ordered_list,
	            'unordered-list': ordered_list
		            }


	stroke = ''
	while True:
		action = input('Choose a formatter: ')
		if action in new_dict:
			if action == '!help':
				print(new_dict[action])
			else:
				if action == 'ordered-list':
					stroke += new_dict[action]('ordered-list')
				elif action == 'unordered-list':
					stroke += new_dict[action]('unordered-list')
				else:
					stroke += new_dict[action]()
		elif action == '!done':
			with open('output.md', 'w') as write_file:
				write_file.write(stroke)
			break
		else:
			print('Unknown formatting type or command')
			continue

		print(stroke)


markedown()
