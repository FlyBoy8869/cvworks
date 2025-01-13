with open("_version.py", mode="rt") as input_file:
    version_info = input_file.readline().split("=")[1].strip()
    version_info.replace('"', "")
    build_info = input_file.readline().split("=")[1].strip()
    build_info.replace('"', "")

pyproject_toml_contents = []
with open("pyproject.toml", mode="rt") as input_file:
    for line in input_file:
        if line.startswith("version"):
            pyproject_toml_contents.append(f'version = {version_info}\n')
        elif line.startswith("build_version"):
            pyproject_toml_contents.append(f'build_build = {build_info}\n')
        else:
            pyproject_toml_contents.append(line)

with open("pyproject.toml", mode="wt") as output_file:
    output_file.writelines(pyproject_toml_contents)
