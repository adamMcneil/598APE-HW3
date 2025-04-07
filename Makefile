FUNC := g++
copt := -c 
OBJ_DIR := ./bin/
FLAGS := -O3 -lm -g -Werror

CPP_FILES := $(wildcard src/*.cpp)
OBJ_FILES := $(addprefix $(OBJ_DIR),$(notdir $(CPP_FILES:.cpp=.obj)))

all:
	$(FUNC) ./main.cpp -o ./main.exe $(FLAGS)

time:
	make -j
	sudo perf record -g ./main.exe 1000 500

flame:
	sudo perf script | ./FlameGraph-master/stackcollapse-perf.pl > out.perf-folded
	sudo ./FlameGraph-master/flamegraph.pl out.perf-folded > perf.svg
	sudo firefox perf.svgsudo perf script | ./FlameGraph-master/stackcollapse-perf.pl > out.perf-folded

clean:
	rm -f ./*.exe
