ICON_SRC = /Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png
ICON_DST = ./cvworks_gui
INFO_ICON = $(ICON_SRC):$(ICON_DST)
DATA_TO_INCLUDE = --add-data=$(INFO_ICON)

app:
	pyinstaller --noconfirm --windowed --name cvworks $(DATA_TO_INCLUDE) app.py

update-version:
	python buildscripts/buildversion.py

install:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

release: update-version app install

setup-mac:
	python -m pip install -r requirements.txt
