rm -rf doc/build 
sphinx-apidoc -o doc/source/ ./neurodeploy
sphinx-build -b html doc/source doc/build
sphinx-build -b pdf doc/source doc/build
