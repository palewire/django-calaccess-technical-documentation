.PHONY: html livehtml

html:
	src/manage.py createcalaccessrawdbtabledocs
	src/manage.py createcalaccessrawformdocs
	cd docs && make html

livehtml:
	cd docs && make livehtml
