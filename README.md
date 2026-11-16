<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#f472b6&height=180&section=header&text=Wheel%20Inspector&fontSize=42&fontColor=ffffff" alt="Wheel Inspector banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=F472B6&center=true&vCenter=true&width=650&lines=Inspect%20Python%20wheels%20before%20they%20enter%20your%20environment." alt="Animated project tagline"/></p>
<p align="center"><img src="https://img.shields.io/github/license/CyberLoop-dev/wheel-inspector?style=for-the-badge" alt="License"/> <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/wheel-inspector?style=for-the-badge" alt="Top language"/> <img src="https://img.shields.io/github/stars/CyberLoop-dev/wheel-inspector?style=for-the-badge" alt="Stars"/> <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/wheel-inspector?style=for-the-badge" alt="Last commit"/></p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Wheel Inspector illustration"/></p>

## 🚀 Overview

Wheel Inspector reads a Python .whl archive as data. It extracts package metadata and entry points, checks for key dist-info files, and summarizes declared dependencies without installing or executing package code.

## ✨ Features

- 📦 Read wheel metadata without installation
- 🧾 List declared dependencies and console scripts
- 🔎 Check for METADATA, WHEEL, and RECORD files
- 🛡️ Never import or execute the inspected package

## 🎬 Demo

~~~bash
python main.py dist/example_package.whl --list-files
~~~

The wheel is inspected as an archive; it is never installed.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/wheel-inspector.git
cd wheel-inspector
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
wheel-inspector/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#f472b6,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
