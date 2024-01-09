from datetime import datetime

now = datetime.now()
d = now.date()
t = now.time()
version = (
    f"{d.year}.{d.month:02d}.{d.day:02d} - build {t.hour:02d}{t.minute:02d}.{t.second}"
)

m_text = f"VERSION = '{version}'\n"

with open("version.py", "wt", encoding="utf-8") as outfile:
    outfile.write(m_text)
