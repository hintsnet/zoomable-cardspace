#!/bin/sh

export TARGET=${1}
echo Target Directory is ${TARGET}

rm -i ${TARGET}/flare.json
rm -i ${TARGET}/index.html
