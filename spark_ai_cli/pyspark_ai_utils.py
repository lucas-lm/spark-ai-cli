from pyspark_ai import SparkAI
from langchain.chat_models import ChatOpenAI

def create_spark_ai_with_gpt(model_name, verbose=True, temperature=0):

  llm = ChatOpenAI(model_name=model_name, temperature=temperature)
  spark_ai = SparkAI(llm=llm, verbose=verbose)
  spark_ai.activate()
  return spark_ai

