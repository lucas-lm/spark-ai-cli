# PySparkAI CLI

SparkAI on CLI

## Installation

### Prerequisites

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
pip install git+https://github.com/lucas-lm/spark-ai-cli
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