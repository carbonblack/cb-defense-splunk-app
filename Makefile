all: app addon

addon: APPNAME=TA-Cb_Defense
addon: VERSION=2.0.2
addon: BUNDLE=$(APPNAME)-$(VERSION)
addon: $(APPNAME).spl

app: APPNAME=DA-ESS-CbDefense
app: VERSION=1.0.0
app: BUNDLE=$(APPNAME)-$(VERSION)
app: $(APPNAME).spl

clean:
	rm -f build/*.spl
	rm -rf build/*

test: APPNAME=DA-ESS-CbDefense
test: $(APPNAME).spl
	curl -X POST -H "Authorization: bearer $(SPLUNK_TOKEN)" -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -F "app_package=@build/$(APPNAME).spl" https://appinspect.splunk.com/v1/app/validate

$(APPNAME).spl:
	mkdir -p build/$(APPNAME)

	cp -r $(APPNAME)/appserver build/$(APPNAME)
	cp -r $(APPNAME)/bin build/$(APPNAME)
	cp -r $(APPNAME)/default build/$(APPNAME)
	cp -r $(APPNAME)/metadata build/$(APPNAME)
	cp -r $(APPNAME)/static build/$(APPNAME)
	cp -r $(APPNAME)/README build/$(APPNAME)
	cp $(APPNAME)/LICENSE.md build/$(APPNAME)
	cp $(APPNAME)/README.md build/$(APPNAME)

	find build/$(APPNAME) -name ".*" -delete
	find build/$(APPNAME) -name "*.pyc" -delete

	(cd build && gtar -cvzf $(APPNAME).spl $(APPNAME))
