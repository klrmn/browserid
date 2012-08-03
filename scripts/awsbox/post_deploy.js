#!/bin/bash

if [ ! -f $HOME/var/root.cert ] ; then
    echo ">> generating keypair"
    scripts/generate_ephemeral_keys.sh
    mv var/root.{cert,secretkey} $HOME/var
else
    echo ">> no keypair needed.  you gots one"
fi

echo ">> updating strings"
cd $HOME/locale
svn up
cd $HOME
./locale/compile-json.sh locale/ code/resources/static/i18n/

echo ">> generating production resources"
code/scripts/compress
