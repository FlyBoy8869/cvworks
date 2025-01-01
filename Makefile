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

setup-mac:
	# run this only after creating a virtualenv and activating it
	python -m pip install -r requirements.txt
