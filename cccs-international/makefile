# Variables
PYTHON = python
OPEN   = xdg-open

# List of all countries
COUNTRIES = india nepal pakistan china japan south-korea malaysia indonesia vietnam thailand

.PHONY: all clean $(COUNTRIES)

# Default target builds everything
all: $(COUNTRIES)

# Pattern rule: Matches any country in lowercase (e.g., south-korea)
# It capitalizes the string dynamically to pass to your Python script
$(COUNTRIES):
	@# Capitalize first letter (and handle hyphenated names like South-Korea)
	$(eval COUNTRY_NAME_CAPS := $(shell echo $@ | sed -e 's/\b\(.\)/\u\1/g'))

	$(PYTHON) src/main.py $(COUNTRY_NAME_CAPS)
	mkdir -p cccs-$@
	mv cccs-$@.html cccs-$@/index.html
	$(OPEN) cccs-$@/index.html

# Cleans up all generated country folders and stray HTML files
clean:
	rm -rf $(addprefix cccs-, $(COUNTRIES))
	rm -f cccs-*.html
