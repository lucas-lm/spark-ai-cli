# PySparkAI CLI

SparkAI on CLI

## Installation

It is recommended to use a virtual environment to install and run the CLI using python. This way you can avoid conflicts and incompatibilities if you already have some version of spark and pyspark (or any other dependency) installed in your computer.

```sh
# make sure to run the command in a test folder, or maybe new project folder
python3 -m venv venv
source ./venv/bin/activate
```

If you are not so sure about virtual environment, you can read this [article](https://medium.com/@pdx.lucasm/python-virtual-environments-18ee3e8d2c3f).

### Prerequisites

Python supported version: ^3.10

Java JDK 8 is required as a dependency of spark/pyspark itself. Make sure to have the JAVA_HOME environment variable setup as well.

If your environment is already configured to run pyspark applications, you are good to go.

### Setup your environment

Setup OpenAI API key in environment variables:

```sh
export OPENAI_API_KEY='sk-...'
```

To use Google's search mechanism to find data on web, you must also setup Google API key in environment variables:

```sh
export GOOGLE_API_KEY='...'
```

### Install pyspark-ai-cli

```sh
pip install spark-ai-cli
```

## Usage

Call CLI in your shell

```sh
python -m pyspark-ai "https://github.com/topics/google --limit=20"
```

Applying transformations over the source data:

```sh
pyspark-ai https://github.com/topics/google --transform "top 3 python repos with more stars"
```

By default the LLM used behind the scenes is `gpt-3.5-turbo`, but you can change it with `--gpt-model-name` flag:

```sh
pyspark-ai "https://github.com/topics/google" --transform "show me programming languages by stars from the most stared to the less stared" --gpt-model-name "gpt-4" --limit 20
```

Only OpenAI's LLMs are supported in the current version.

> **Warning**
>
> GPT-4 may be not be generally available, so you may face issues on it.  