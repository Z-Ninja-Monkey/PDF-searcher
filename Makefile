CXX = gcc
CXXFLAGS = -Wall -Wextra -pedantic -std=c++17 -m64
SRCDIR = src
BINDIR = bin
SOURCES = $(wildcard $(SRCDIR)/*.c)
OBJECTS = $(patsubst $(SRCDIR)/%.c,$(BINDIR)/%.o,$(SOURCES))

all: $(BINDIR)/ocr_searcher.dll

$(BINDIR)/ocr_searcher.dll: $(OBJECTS)
	$(CXX) -shared $(CXXFLAGS) $^ -o $@

$(BINDIR)/%.o: $(SRCDIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(BINDIR)/*
