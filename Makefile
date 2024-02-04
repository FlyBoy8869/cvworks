INFO_ICON = /Users/charles/PycharmProjects/cvworks/cvworks_gui/info.png
OFF_ICON = /Users/charles/PycharmProjects/cvworks/cvworks_gui/ui/off.png
WORKS_ICON = /Users/charles/PycharmProjects/cvworks/cvworks_gui/ui/works.png
INFO_ICON_DST = ./cvworks_gui
OFF_ICON_DST = ./cvworks_gui/ui
WORKS_ICON_DST = ./cvworks_gui/ui
INFO_ICON_INCLUDE = $(INFO_ICON):$(INFO_ICON_DST)
DATA_TO_INCLUDE = --add-data=$(INFO_ICON_INCLUDE) --add-data=$(OFF_ICON):$(OFF_ICON_DST) --add-data=$(WORKS_ICON):$(WORKS_ICON_DST)

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
