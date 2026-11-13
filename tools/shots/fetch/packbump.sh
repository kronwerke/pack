#!/bin/sh
# packbump.sh <core version|-> <pack version> "<commit subject>": waits for the Core release asset, bumps the pack,
# pushes, waits for the CI commit and prints its sha (the pack release goes on that commit)
set -e
cd /home/claude/kw/pack
git stash -q 2>/dev/null || true; git pull -q --rebase; git stash pop -q 2>/dev/null || true
if [ "$1" != "-" ]; then
  for i in $(seq 60); do d=$(gh api repos/kronwerke/core/releases/tags/v$1 --jq '.assets[0].digest' 2>/dev/null || true); [ -n "$d" ] && [ "$d" != "null" ] && break; sleep 10; done
  [ -n "$d" ] && [ "$d" != "null" ] || { echo "no digest for Core $1"; exit 1; }
  h=${d#sha256:}
  python3 - "$1" "$h" <<'PY'
import re,sys
v,h=sys.argv[1:]
p='mods/kronwerke-core.pw.toml'; s=open(p).read()
s=re.sub(r'filename = "[^"]+"','filename = "kronwerke-%s.jar"'%v,s); s=re.sub(r'url = "[^"]+"','url = "https://github.com/kronwerke/core/releases/download/v%s/kronwerke-%s.jar"'%(v,v),s); s=re.sub(r'hash = "[0-9a-f]+"','hash = "%s"'%h,s)
open(p,'w').write(s)
PY
fi
sed -i "s/^version = \".*\"/version = \"$2\"/" pack.toml
git add -A
git -c user.name=Elchi -c user.email=github@elchi.dev commit -q -m "$3

Co-Authored-By: Claude Fable 5.2 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01DeioewV7AQpkCYwb4tLmpD"
# the CI commit of an earlier push may have landed in between: pull and try again
git push -q 2>/dev/null || { sleep 5; git pull -q --rebase; git push -q; }
for i in $(seq 60); do sleep 8; git pull -q --rebase 2>/dev/null || true; git log --format=%s -1 | grep -q "^build: regenerate" && break; done
git log --format="%H %s" -1
grep '^version' pack.toml
