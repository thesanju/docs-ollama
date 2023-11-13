# Docs-Ollama

chat with you're documents fully on local using [ollama](https://github.com/jmorganca/ollama)
## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Fine-Tuning the Model](#fine-tuning-the-model)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project combines text extraction capabilities with a Conversational LLM using [ollama](https://github.com/jmorganca/ollama). The goal is to extract text from various document formats, such as PDF and TXT, and utilize a fine-tuned model to engage in interactive conversations, (the extracting part is still on development you can only use .txt, .pdf and .docx).


## Features

key features:
- talk with documents
- history enabled
- ...

## Getting Started

follow this steps to use ollama.

### Prerequisites

make sure you have  [ollama](https://github.com/jmorganca/ollama) installed if not download [here](ollama.ai)

### Installation 

## setting up ollama

**1. pull a model**

   ```bash
ollama pull mistral
```
**2. test it**

   ```bash
ollama run mistral
```
**2. create a fine tuned model using Modelfile**

   ```bash
ollama create docsGPT -f Modelfile.txt
```
>If this does not work or you'll get this `Error: failed to open file: open /home/sanju/ex-models/Modelfile.xt: permission denied`

>move the ModelFile to tmp folder
   ```bash
 cp Modelfile.txt /tmp/
```
 try again

   ```bash
ollama create docsGPT -f /tmp/Modelfile.txt
```
   ```bash
ollama list
```

**set up script locally**

**1. Clone Repo**

```bash
git clone https://github.com/thesanju/docs-ollama
```

**2. cd into it**

```bash
cd docs-ollama
```

**3. Craete a virtual environment**

Create a create a virtual environment
```bash
 python -m venv myenv
```
**4. activate environment**

``` bash
source /home/(username)/pyTest/myenv/bin/activate
```

**4. install requirements**

```bash
python -r install requirements.txt
```
**4. run the script**

```bash
python3 main.py story.txt
```
> you can give path of file or just put the file into this project and the file name while executing


**5. Use It**
