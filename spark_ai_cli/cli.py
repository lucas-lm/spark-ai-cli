import typer
from .pyspark_ai_utils import create_spark_ai_with_gpt
# If 'gpt-4' is unavailable, use 'gpt-3.5-turbo' (might lower output quality)
DEFAULT_GPT_MODEL_NAME = 'gpt-3.5-turbo'  

app = typer.Typer()

@app.command()
def explore(extract: str, transform: str = None, limit: int = None, gpt_model_name=DEFAULT_GPT_MODEL_NAME):
  spark_ai = create_spark_ai_with_gpt(gpt_model_name)
  df = spark_ai.create_df(extract)
  print(df.ai.explain())
  
  if transform is not None:
    df = df.ai.transform(transform)
    print(df.ai.explain())
  
  df.show() if limit is None else df.show(n=limit)

def main():
  app()