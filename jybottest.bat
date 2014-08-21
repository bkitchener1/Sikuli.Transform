@echo off

set sikuli_jar=C:\Program Files\Sikuli X\sikuli-script.jar

set CLASSPATH=%sikuli_jar%
set JYTHONPATH=%sikuli_jar%/Lib

jybot --pythonpath=C:\Users\Brian\Documents\Sikuli\Transform\TransformLib ^
      --outputdir=results ^
      --loglevel=TRACE ^
      %*