.PHONY: gerber_zip
	
gerber_zip: gerbers.zip
	
gerbers.zip: $(wildcard gerber/*)
	rm -f $@
	zip $@ $^
