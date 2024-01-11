app:
	pyinstaller --noconfirm --windowed --name cvworks --add-data "/Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png:./cvworks_gui" app.py

update-version:
	python buildscripts/buildversion.py

release-mac: update-version app install-mac

release-win: app install-win

install-mac:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

install-win:
	copy /Y .\dist\cvworks.exe C:\Users\charles\Desktop
