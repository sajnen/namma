from pathlib import Path
import re
text = Path('index.html').read_text('utf8')
lines = text.splitlines()
print('LINE_COUNT', len(lines))
if len(lines) > 550:
    print('LINE_551:', lines[550])
else:
    print('LINE_551: NONE')
script_match = re.search(r'<script[^>]*>([\s\S]*?)</script>', text, re.I)
print('SCRIPT_FOUND', bool(script_match))
if script_match:
    script = script_match.group(1)
    print('SCRIPT_LENGTH', len(script))
    print('LAST_5_CHARS', repr(script[-5:]))
    # Basic check for unclosed quote or braces
    d = {'(':0, ')':0, '{':0, '}':0, '[':0, ']':0}
    for c in script:
        if c in d: d[c] += 1
    print('COUNTS', d)
