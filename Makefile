$EGG=pyzbar_x.egg-info

build-wheels:
	rm -rf build dist MANIFEST.in $EGG
	cp MANIFEST.in.all MANIFEST.in
	./setup.py bdist_wheel

	cat MANIFEST.in.all MANIFEST.in.win32 > MANIFEST.in
	./setup.py bdist_wheel --plat-name=win32

	# Remove these dirs to prevent win32 DLLs from being included in win64 build
	rm -rf build $EGG
	cat MANIFEST.in.all MANIFEST.in.win64 > MANIFEST.in
	./setup.py bdist_wheel --plat-name=win_amd64

	rm -rf build MANIFEST.in $EGG

release-test:
	twine upload -r testpypi dist/*
