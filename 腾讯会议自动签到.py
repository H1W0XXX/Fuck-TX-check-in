from pywinauto import Application
# from pywinauto import mouse
import time
app = Application(backend="uia").connect(process=18404)
# app = Application(backend='uia').start(r"X:\voov\WeMeet\wemeetapp.exe")


while 1:
	# time.sleep(10)
	# try:
	# 	left1 = app["(InMeetingPopupWebWnd)"]["go_forward_refresh"].Button3.rectangle().left
	# 	top1 = app["(InMeetingPopupWebWnd)"]["go_forward_refresh"].Button3.rectangle().top
	# 	mouse.click(button='left', coords=(left1+9, top1+9))
	# 	print('刷新成功')
	# except:
	# 	print('没有找到刷新按钮')
	time.sleep(5)
	try:
		app['(inMettingPopupWebWnd)']['点击签到'].click()
		print('签到成功')
	except:
		print('没有找到签到按钮')

