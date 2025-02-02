RESOURCES_FOLDER = ./cvworks_gui/resources
RESOURCES_FOLDER_DST = "./cvworks_gui/resources"
DATA_TO_INCLUDE = --add-data=$(RESOURCES_FOLDER):$(RESOURCES_FOLDER_DST)
WINDOWS_APP_ICON = icon.ico
MAC_APP_ICON = icon.icns

app:
	uv run pyinstaller --noconfirm --windowed --name cvworks --icon $(MAC_APP_ICON) $(DATA_TO_INCLUDE) app.py

update-version:
	uv run buildscripts/buildversion.py
	uv run buildscripts/update-pyproject-toml-version.py

install:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

release: update-version app

setup:
	uv sync --all-groups

# MS Windows targets
win-app:
	uv run pyinstaller --noconfirm --windowed --name cvworks --icon $(WINDOWS_APP_ICON) $(DATA_TO_INCLUDE) app.py

win-install:
	IF EXIST "$(HOMEPATH)\cvworks" (rmdir /S /Q $(HOMEPATH)\cvworks)
	mkdir $(HOMEPATH)\cvworks
	xcopy .\dist\cvworks $(HOMEPATH)\cvworks /E /H /C /I
	uv run buildscripts/create_windows_shortcut.py

win-release: win-app

win-setup:
	uv sync --all-groups
