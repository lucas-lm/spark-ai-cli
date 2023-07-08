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