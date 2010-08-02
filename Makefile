PREFIX=/usr/local
BINDIR=$(PREFIX)/bin

install:
	install -m755 vault $(BINDIR)/vault

