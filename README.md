# Quest

Quest allows asking SQL databases questions in natural language. It is composed of API/model, front-end, and proxy containers.

## Installation and Running

1. Clone the repository
2. Copy `api/config.yml.sample` to `config.yml`
3. Change `engine_url` and `schema` values as required
4. Run `docker compose up`

_Note_: it might take several minutes to download and initialize the models on the first run.

### Configuration

`engine_url` has the SQLAlchemy format, check [here](https://docs.sqlalchemy.org/en/20/core/engines.html#database-urls) for more details.

`schema` is the `CREATE TABLE` statements that represent the underlying database.

## Model

Natural SQL 7B model is used for SQL generation.
