# Define the directory where the PNG files will be generated
PNG_DIR := png

# Find all the .puml files in the current directory
PUML_FILES := $(wildcard *.puml)

# Generate the corresponding PNG files using vscode "export workspace diagrams"
$(PNG_DIR)/%.png: %.puml
	code --export-extension vscode.plantuml --export-type png --export-dir $(PNG_DIR) $<

# Define a target to generate all the PNG files
all: $(patsubst %.puml,$(PNG_DIR)/%.png,$(PUML_FILES))

# Clean the PNG directory
clean:
	rm -rf $(PNG_DIR)