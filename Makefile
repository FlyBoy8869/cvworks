RESOURCES_FOLDER = ./cvworks_gui/resources
RESOURCES_FOLDER_DST = "./cvworks_gui/resources"
DATA_TO_INCLUDE = --add-data=$(RESOURCES_FOLDER):$(RESOURCES_FOLDER_DST)

app:
	pyinstaller --noconfirm --windowed --name cvworks $(DATA_TO_INCLUDE) app.py

update-version:
	python buildscripts/buildversion.py

install:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

release: update-version app install

setup:
	# run this only after creating a virtualenv and activating it
	python -m pip install -r requirements.txt

# MS Windows targets
win-install:
	IF EXIST "$(HOMEPATH)\cvworks" (rmdir /S /Q $(HOMEPATH)\cvworks)
	mkdir $(HOMEPATH)\cvworks
	xcopy .\dist\cvworks $(HOMEPATH)\cvworks /E /H /C /I
	python.exe buildscripts/create_windows_shortcut.py

win-release: app win-install

win-setup:
	python.exe -m pip install -r win_requirements.txt
