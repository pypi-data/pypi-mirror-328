# 📁 futilz – A Simple & Powerful File Utility Library  

## 🌟 Overview  

**futilz** is a lightweight and efficient Python utility library designed to simplify file system operations, checksum generation, and file downloading. Whether you're working on automation scripts, data processing, or general file management, **futilz** provides essential tools to make your tasks easier.  

With **futilz**, you can:  
✅ Locate the root directory of a Git repository.  
✅ Manage directories and create nested folders effortlessly.  
✅ Normalize and clean file paths to avoid inconsistencies.  
✅ Retrieve and validate file extensions (including images and fonts).  
✅ Search for files recursively with filtering options.  
✅ Compute SHA hash values for files and content to ensure integrity.  
✅ Download files from URLs while handling encoding formats.  
✅ **And more in the future! 🚀**  

## 🚀 Features  

### 🔍 Repository & Path Management  
- **Find Git Repository Root** – Detects the base directory of a Git repository.  
- **Fix File Paths** – Cleans up redundant path elements like `//` or `/./`.  
- **Create Directories** – Ensures nested directories exist without errors.  

### 📂 File Operations  
- **File Extension Handling** – Retrieve and validate file extensions.  
- **Detect Image & Font Files** – Supports formats like PNG, JPG, SVG, TTF, and more.  
- **Recursive File Search** – Search directories while filtering by file type.  

### 🔒 Data Integrity & Checksums  
- **Generate SHA Hashes** – Compute secure hash values (SHA-1, SHA-256, etc.) for file verification.  
- **Hash Content & Files** – Validate file integrity using checksum functions.  

### 🌐 File Downloading  
- **Download Any File** – Fetch files from the web with built-in support for handling encoding issues.  
- **Automatic Directory Creation** – Ensures the destination folder exists before saving files.  

### 🔮 Future Enhancements  
- **More file-handling utilities** 🔄  
- **Additional hashing algorithms** 🔑  
- **Performance optimizations** ⚡  
- **And much more to come! 🚀**  

## 📥 Installation  

Installing **futilz** is quick and easy with pip:  

```sh
pip install futilz
```

## 🔧 Usage Examples  

### 1️⃣ Find All `.txt` Files in a Directory  
```python
import futilz

files = futilz.find(dirname=".", extensions=["txt"])
print(files)
```

### 2️⃣ Generate a SHA-256 Hash of a String  
```python
import futilz

hash_value = futilz.shasum_content("Hello, World!", algo="sha256")
print(hash_value)
```

### 3️⃣ Download a File from a URL  
```python
import futilz

futilz.download_file("https://example.com/sample.txt", "downloads/sample.txt")
print("Download complete!")
```

## 🎯 Why Use futilz?  
✔️ **Lightweight & Efficient** – Minimal dependencies, optimized for performance.  
✔️ **Easy to Use** – Simple, intuitive functions for common tasks.  
✔️ **Versatile** – Suitable for automation, data processing, and file management.  
✔️ **Cross-Platform** – Works on Windows, macOS, and Linux.  
✔️ **Actively Improved** – More features and optimizations coming soon!  

---

## 📢 Connect with Me  
💻 **GitHub**: [github.com/abdelmathin/futilz](https://github.com/abdelmathin/futilz)  
🌍 **Website**: [abdelmathin.com](https://abdelmathin.com)  
🔗 **LinkedIn**: [linkedin.com/in/abdelmathin](https://linkedin.com/in/abdelmathin)  

💡 **Contribute**: Have suggestions or improvements? Feel free to contribute!  
🐞 **Issues**: Found a bug? Open an issue on the GitHub repository.  
📜 **License**: Open-source and free to use under the MIT License.  

🚀 **Start using futilz today and make file handling in Python easier than ever!** 🎉
