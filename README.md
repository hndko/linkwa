# 🟢 LinkWa - Powerful WhatsApp Link Generator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**LinkWa** is a powerful, lightweight, and easy-to-use tool to generate direct WhatsApp chat links. Whether you need a single link or are automating usage via CLI, LinkWa handles phone number formatting and URL encoding effortlessly.

## ✨ Features

- 🚀 **Fast & Lightweight**: Zero external dependencies required.
- 🎨 **Beautiful CLI**: Interactive menu with emoji support and colors.
- 🔧 **Auto-Formatting**: Automatically converts local format (e.g., `0812...`) to international format (`62812...`).
- 📝 **Message Support**: Add pre-filled text messages with automatic URL encoding.
- 🤖 **CLI Support**: Fully automatable with command-line arguments.
- 💻 **Cross-Platform**: Works on Windows, macOS, Linux, and Termux.

## 📦 Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/hndko/linkwa
   cd linkwa
   ```

2. **Run the tool**
   ```bash
   python linkwa.py
   ```

## 📖 Usage Guide

### Interactive Mode

Simply run the script without arguments to enter the interactive menu:

```bash
python linkwa.py
```

Follow the on-screen prompts to input the number and message.

### Command Line Mode (Power User)

You can generate links directly from the terminal for scripts or quick access:

**Basic Usage:**

```bash
python linkwa.py -n 08123456789
```

**With Message:**

```bash
python linkwa.py -n 08123456789 -t "Hello, I am interested in your product!"
```

**Silent Mode (Output only link):**

```bash
python linkwa.py -n 08123456789 --no-output
```

## 📸 Spec (Screenshots)

_CLI Interface with rich colors and icons._

## 🤝 Contribution

Feel free to open issues or submit pull requests.
Created by **Kyuoko** | Updated by **Collaborators**

## 📜 License

This project is open-source and available under the terms of the MIT License.
