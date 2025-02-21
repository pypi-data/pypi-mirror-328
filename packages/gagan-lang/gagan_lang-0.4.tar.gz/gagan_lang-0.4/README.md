# Gagan Language (.ggn)

The world's simplest programming language.

## Installation

```bash
pip install gagan-lang
```
## Usage
Create a .ggn file, e.g., hello.ggn.

Run it using:

```bash

gagan hello.ggn
```
## Syntax

gprint "text": Print to console.
gscan variable: Read input.
Example


```
gprint "Hello, World!"
```
```
gscan name
```
```
gprint "Welcome, " + name
```

---

### **3. How to Run**
1. Clone the repo:
   ```bash
   git clone https://github.com/higgn/gagan-lang.git
   ```
   ```
   cd gagan-lang
   ```
Install the package:
```
pip install .
```
Run the example:
```
gagan examples/hello.ggn
```