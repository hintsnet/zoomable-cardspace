#!/bin/sh

export TARGET=${1}
echo Target Directory is ${TARGET}

cp -v flare.json ${TARGET}
cp -v index.html ${TARGET}
