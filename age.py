drive = input('請問您有開過車嗎? ')
age = input('請問您的年齡? ')
age = int(age)
if drive == '有':
	if age >= 18:
		print('請務必注意安全喔!')
	else:
		print('請不要無照駕駛!')
elif drive == '沒有' or drive == '無':
	if age >= 18:
		print('可以嘗試去考取駕照喔!')
	else:
		print('你需要年滿18歲才可以考取駕照喔!')