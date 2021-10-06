import webbrowser
import time

repeats = 0

while repeats < 5:
	print("Zeit für eine Pause!")
	time.sleep(10)
	webbrowser.open('https://www.youtube.com/watch?v=kXYiU_JCYtU')
	time.sleep(40)
	print("Zeit zum Weiterarbeiten!\n")
	repeats += 1

print("Ende!")
