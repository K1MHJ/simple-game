PROJECT := "Demo C++"
APP := DemoApp
STATIC_LIB_DIR := libStat
STATIC_LIB := $(STATIC_LIB_DIR)/libStat.a
DYNLIB_DIR := "\"./libDyn\""
DEFINES := -DDYNLIB_DIR=$(DYNLIB_DIR)
SRC_DIR := src
OBJ_DIR := obj
BIN_DIR := bin

CPP_FILES = $(wildcard $(SRC_DIR)/*.cpp)
OBJ_FILES = $(CPP_FILES:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)
DEP_FILES = $(OBJ_FILES:%.o=%.d)
-include $(DEP_FILES)

CXX := clang++
CXXFLAGS := -Wall -std=c++11 -Iinclude -I$(STATIC_LIB_DIR) $(DEFINES)
LD := clang++
LDFLAGS := -L$(STATIC_LIB_DIR)
LDLIBS := -lStat

all : $(BIN_DIR)/$(APP)

clean :
	rm -rf $(OBJ_DIR) $(BIN_DIR)
	make clean -C ./libStat
	make clean -C ./libDyn

$(OBJ_DIR)/%.o: $(SRC_DIR)/%.cpp
	mkdir -p $(@D)
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(BIN_DIR)/$(APP): $(OBJ_FILES) ./libStat/libStat.a
	@echo "Project : $(value PROJECT)"
	@echo "Application : $(value APP)"
	mkdir -p $(@D)
	$(LD) $(LDFLAGS) $(LDLIBS) $(OBJ_FILES) -o $(BIN_DIR)/$(APP)

./libStat/libStat.a :
	make -C ./libStat

run :
#	$(BIN_DIR)/$(APP)
	python3 $(SRC_DIR)/main.py

.PHONY: all run
