#!/bin/bash
rm -fr ./html
./manage.py staticsitegen
cp -r ./sapo/static ./html