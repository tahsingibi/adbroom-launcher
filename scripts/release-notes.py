#!/usr/bin/env python3
import pathlib,re,sys
version=sys.argv[1]
if not re.fullmatch(r'\d+\.\d+\.\d+',version):raise SystemExit('Use a stable SemVer version')
text=(pathlib.Path(__file__).resolve().parents[1]/'CHANGELOG.md').read_text()
match=re.search(r'^## '+re.escape(version)+r'(?:\s[^\n]*)?\n(.*?)(?=^## |\Z)',text,re.M|re.S)
if not match:raise SystemExit('Missing changelog section: '+version)
print(match[1].strip())
