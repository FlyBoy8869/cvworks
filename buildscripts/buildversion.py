from datetime import datetime

now = datetime.now()
d = now.date()
t = now.time()
version = (
    f"{d.year}.{d.month:02d}"
)

build = f"{d.day:02d}{t.hour:02d}{t.minute:02d}{t.second:02d}"

m_version = f'version = "{version}"\n'
m_build = f'build = "{build}"\n'

with open("_version.py", "wt", encoding="utf-8") as outfile:
    outfile.write(m_version)
    outfile.write(m_build)
