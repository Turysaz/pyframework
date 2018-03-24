set drelease=release

mkdir %drelease%
xcopy project %drelease%
xcopy python %drelease%
xcopy pygame %drelease%
xcopy pgw %drelease%

copy configuration.txt %drelease%
copy launcher.py %drelease%
copy start.bat %drelease%
