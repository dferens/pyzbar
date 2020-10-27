EGG=pyzbar_x.egg-info

build-wheels:
	rm -rf build dist

	rm -rf MANIFEST.in $(EGG) build
	cp MANIFEST.in.all MANIFEST.in
	./setup.py bdist_wheel

	rm -rf MANIFEST.in $(EGG) build
	cat MANIFEST.in.all MANIFEST.in.win32 > MANIFEST.in
	./setup.py bdist_wheel --plat-name=win32

	rm -rf MANIFEST.in $(EGG) build
	cat MANIFEST.in.all MANIFEST.in.win64 > MANIFEST.in
	./setup.py bdist_wheel --plat-name=win_amd64

release-test:
	twine upload -r testpypi dist/*
