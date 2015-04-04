#!/usr/bin/env bash
# add right hash to README.md
sed -ie '$d' README.md
sha256sum translationcheck.bash >> README.md
