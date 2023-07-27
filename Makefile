CXX = g++
CXXFLAGS = -Wall -Wextra -pedantic -std=c++17 -m64
SRCDIR = src
BINDIR = bin
SOURCES = $(wildcard $(SRCDIR)/*.cpp)
OBJECTS = $(patsubst $(SRCDIR)/%.cpp,$(BINDIR)/%.o,$(SOURCES))

all: $(BINDIR)/ocr_searcher.dll

$(BINDIR)/ocr_searcher.dll: $(OBJECTS)
	$(CXX) -shared $(CXXFLAGS) $^ -o $@

$(BINDIR)/%.o: $(SRCDIR)/%.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

clean:
	rm -f $(BINDIR)/*
