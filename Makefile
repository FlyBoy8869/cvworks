RESOURCES_FOLDER = ./cvworks_gui/resources
RESOURCES_FOLDER_DST = "./cvworks_gui/resources"
DATA_TO_INCLUDE = --add-data=$(RESOURCES_FOLDER):$(RESOURCES_FOLDER_DST)

app:
	uv run pyinstaller --noconfirm --windowed --name cvworks $(DATA_TO_INCLUDE) app.py

update-version:
	uv run buildscripts/buildversion.py
	uv run buildscripts/update-pyproject-toml-version.py

install:
	# command must be structured this way
	cp -R -f ./dist/cvworks.app /Applications

release: update-version app install

setup:
	uv sync --all-groups

# MS Windows targets
win-install:
	IF EXIST "$(HOMEPATH)\cvworks" (rmdir /S /Q $(HOMEPATH)\cvworks)
	mkdir $(HOMEPATH)\cvworks
	xcopy .\dist\cvworks $(HOMEPATH)\cvworks /E /H /C /I
	uv run buildscripts/create_windows_shortcut.py

win-release: app win-install

win-setup:
	uv sync --all-groups
