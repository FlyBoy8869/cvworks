ICON_SRC = /Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png
ICON_DEST = ./cvworks_gui
INFO_ICON = $(ICON_SRC):$(ICON_DEST)

DATA_TO_INCLUDE = --add-data=$(INFO_ICON)

app:
	pyinstaller --noconfirm --windowed --name cvworks $(DATA_TO_INCLUDE) app.py

update-version:
	python buildscripts/buildversion.py

release-mac: update-version app install-mac

release-win: app install-win

install-mac:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

install-win:
	copy /Y .\dist\cvworks.exe C:\Users\charles\Desktop
