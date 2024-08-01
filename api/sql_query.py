import yaml
from sqlalchemy import create_engine
from sqlalchemy import text


class SQLQuery:

    def execute(self, query: str):

        with open("config.yml") as file:
            config = yaml.safe_load(file)
            engine_url = config["engine_url"]
            if engine_url == "engine_url":
                raise ValueError("engine_url must be specified")

        engine = create_engine(engine_url, future=True)

        result_rows = []

        with engine.connect() as connection:
            result = connection.execute(text(query))
            for row in result:
                result_rows.append(row._asdict())

        return result_rows
