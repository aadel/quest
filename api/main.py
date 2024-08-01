from fastapi import FastAPI
from pydantic import BaseModel

from nsql import NSql
from sql_query import SQLQuery


class Question(BaseModel):
    text: str


app = FastAPI()


@app.post("/query")
def query(question: Question) -> list[dict]:
    nsql = NSql()
    sql_query = SQLQuery()
    query = nsql.answer(question.text)
    result = sql_query.execute(query)
    return result
