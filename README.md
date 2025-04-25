# git-updation
# GitQ

**GitQ** is an enhanced Git commit navigation tool using Deque and Smart Queues. It allows you to:

- Traverse commits efficiently (front or back).
- Store forward/backward traversals using separate queues.
- Support undo/redo of commits.
- Improve commit checkout performance over long histories.

---

## 🚀 Features

- 📚 **Smart Checkout**: Jump to any commit with intelligent queue tracking.
- 🔄 **Undo/Redo**: Seamlessly revert or reapply changes.
- 🧠 **Deque Navigation**: Pops commits from front or back for efficient traversal.
- 🗃️ **Separate Queues**: Maintains clarity between past and future commits.

---

## 🛠️ Installation

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/gitq.git
cd gitq
```

### 2. Install locally
```bash
pip install .
```

---

## ⚙️ Usage

```bash
gitq checkout <commit-hash>   # Smart checkout
gitq undo                      # Undo last checkout
gitq redo                      # Redo last undone commit
gitq reset                     # Clear queues
```

> Example:
```bash
gitq checkout abc1234
gitq undo
gitq redo
gitq reset
```

---

## 🔗 Git Alias Setup (Optional)

```bash
git config --global alias.qcheckout '!gitq checkout'
git config --global alias.qundo '!gitq undo'
git config --global alias.qredo '!gitq redo'
```

Then you can do:
```bash
git qcheckout abc1234
git qundo
git qredo
```

---

## 🐳 Docker (Optional)

```Dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install .
ENTRYPOINT ["gitq"]
```

Build & Run:
```bash
docker build -t gitq .
docker run -it --rm gitq checkout abc1234
```

---

## 📦 PyPI Publish (Optional)

1. Create an account on [PyPI](https://pypi.org/)
2. Upload package:
```bash
python setup.py sdist bdist_wheel
twine upload dist/*
```

---

## 👨‍💻 Author
**M. Hemanth Reddy**  
Innovator & Developer of GitQ - Enhanced Git Commit Queue System

