import re

import torch
import yaml
from transformers import AutoModelForCausalLM
from transformers import AutoTokenizer


class NSql:

    tokenizer = AutoTokenizer.from_pretrained("chatdb/natural-sql-7b")
    model = AutoModelForCausalLM.from_pretrained(
        "chatdb/natural-sql-7b",
        device_map="cuda",
        torch_dtype=torch.float16,
    )

    def answer(self, question: str):
        with open("config.yml") as file:
            config = yaml.safe_load(file)
            engine_url = config["engine_url"]
            schema = config["schema"]
            if schema == "schema":
                raise ValueError("Schema must be specified")

        prompt = f"""
# Task
Generate a SQL query to answer the following question: `{question}`

### PostgreSQL Database Schema
The query will run on a database with the following schema:

{schema}

# SQL
Here is the SQL query that answers the question: `{question}`
'''sql
    """

        inputs = NSql.tokenizer(prompt, return_tensors="pt").to("cuda")
        generated_ids = NSql.model.generate(
            **inputs,
            num_return_sequences=1,
            eos_token_id=100001,
            pad_token_id=100001,
            max_new_tokens=400,
            do_sample=False,
            num_beams=1,
        )

        outputs = NSql.tokenizer.batch_decode(generated_ids, skip_special_tokens=True)

        answer = outputs[0].split("```sql")[-1]
        query = "SELECT" + answer.split("SELECT")[1].replace("'''sql", "")

        # Tweak the query to match engine SQL syntax
        if engine_url.index("solr") == 0:
            query = query.replace(";", "").replace("ILIKE", "LIKE")
            m = re.search(r"LIMIT (\d+)$", query)
            if not m:
                query += " LIMIT 1000"  # Avoid DocValues error
        return query
