app:
	pyinstaller --onefile --noconfirm --windowed --name cvworks app.py

update-version:
	python buildscripts/buildversion.py

install-mac:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

install-win:
	copy /Y .\dist\cvworks.exe C:\Users\charles\Desktop
