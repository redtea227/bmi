height = input('請輸入身高(cm): ')
weight = input('請輸入體重(kg): ')
h = float(height)/100 # 換成公尺
w = float(weight)
b = w / (h ** 2) # bmi
if b < 18.5:
	print('你的BMI值為', b, '屬體重過輕')
elif b >= 18.5 and b < 24:
	print('你的BMI值為', b, '屬正常範圍')
elif b >= 24 and b < 27:
	print('你的BMI值為', b, '屬過重')
elif b >= 27 and b < 30:
	print('你的BMI值為', b, '屬輕度肥胖')
elif b >= 30 and b < 35:
	print('你的BMI值為', b, '屬中度肥胖')
else:
	print('你的BMI值為', b, '屬重度肥胖')