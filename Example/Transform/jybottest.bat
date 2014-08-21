@echo off

set sikuli_jar=C:\Users\Brian\Documents\Sikuli\sikuli-ide.jar

set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

jybot --pythonpath=TransLib ^
      --outputdir=results ^
      --loglevel=TRACE ^
      %*