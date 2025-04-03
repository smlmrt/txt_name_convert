# 📂 Text File Renamer

A simple Python script that renames all text (.txt) files in a specified folder with a sequential numbering system.

## 🔍 Overview

This utility script allows you to batch rename all .txt files in a folder using a consistent naming pattern: `prefix_number.txt`. It's useful for organizing collections of text files, standardizing filenames, or preparing datasets.

## ✨ Features

- 🔄 Renames all .txt files in a specified directory
- 🔢 Applies sequential numbering to files
- 🏷️ Customizable prefix for the new filenames
- 📋 Provides console output of all renaming operations
- ⚠️ Includes error handling for failed renaming attempts

## 🛠️ Requirements

- Python 3.x
- No external libraries required (uses only the built-in `os` module)

## 📋 Usage

1. Save the script as `rename_txt_files.py`

2. Modify the script with your folder path and desired prefix:
   ```python
   klasor_yolu = "/path/to/your/folder"  # Replace with your folder path
   rename_txt_files(klasor_yolu, prefix="metin")  # Change "metin" to your desired prefix
   ```

3. Run the script:
   ```bash
   python rename_txt_files.py
   ```


## 🔄 Function Parameters

- `folder_path`: The directory containing the .txt files to rename
- `prefix`: The text to prepend to each numbered filename (default: "yeni_dosya")

## 📋 Example

If your folder contains:
- notes.txt
- data.txt
- important.txt

After running the script with prefix="metin", they will be renamed to:
- metin_1.txt
- metin_2.txt
- metin_3.txt

## ⚠️ Important Notes

- The script only processes files with a `.txt` extension
- The original filenames are completely replaced
- The numbering starts at 1 and increments sequentially
- Make sure you have write permissions for the folder
- Consider backing up your files before running this script

## 🤝 Contributing

Feel free to fork this repository and submit pull requests to improve the functionality.

## 📝 License

This project is open source and available under the [MIT License](LICENSE).
