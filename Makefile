ICON_SRC = /Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png
ICON_DST = ./cvworks_gui
INFO_ICON = $(ICON_SRC):$(ICON_DST)

DATA_TO_INCLUDE = --add-data=$(INFO_ICON)

app:
	pyinstaller --noconfirm --windowed --name cvworks $(DATA_TO_INCLUDE) app.py

update-version:
	python buildscripts/buildversion.py

mac-install:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

mac-release: update-version app mac-install

windows-build:
	pyinstaller --noconfirm --windowed $(WIN_DATA_TO_INCLUDE) --name cvworks app.py
win-app: windows-build
	WIN_ICON_SRC = C:/Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png
	WIN_INFO_ICON = $(WIN_ICON_SRC);$(ICON_DST)
	WIN_DATA_TO_INCLUDE = --add-data=$(WIN_INFO_ICON)

win-install:
	IF EXIST "C:\Users\charles\cvworks" (rmdir /S /Q C:\Users\charles\cvworks)
	mkdir C:\Users\charles\cvworks
	xcopy .\dist\cvworks C:\Users\charles\cvworks /E /H /C /I
	python.exe buildscripts/create_shortcut.py

win-release: win-app win-install
