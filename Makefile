
build:
	# Nothing to see
	# replace me (make) by something better
	#
	# steps needed:
	# build and move thirdparty to pgw/lib
	# run tests
	# create bundle for shipping

test:
	python -m unittest -v

clean-pycache:
	find . | grep "__pycache__" | xargs rm -rfv
