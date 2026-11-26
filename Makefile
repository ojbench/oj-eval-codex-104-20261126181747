CXX = g++
CXXFLAGS = -std=c++11 -O2 -Wall -Wextra -Wpedantic

code: main.cpp
	$(CXX) $(CXXFLAGS) main.cpp -o code

.PHONY: clean
clean:
	rm -f code
