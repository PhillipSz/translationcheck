#!/usr/bin/env bash
# add right hash to README.md
sed -i '$d' README.md
sha256sum translationcheck.bash >> README.md
