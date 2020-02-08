#passw = 'a123456'
while True:
	password = input('請輸入您的密碼: ')
	if password == 'a123456':
		print('登入成功')
		break
	elif password != 'a123456':
		print('還有二次機會')
