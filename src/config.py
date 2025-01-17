VECTORSTORE_TYPE = "docs"  # Mögliche Werte: 'docs', 'code', 'api_ref'

VECTORSTORE_SETTINGS = {
    "docs": {
        "docs": [
            "https://docs.databricks.com/en/dev-tools/databricks-connect/python/limitations.html",
            "https://docs.databricks.com/en/dev-tools/databricks-connect/index.html#pyspark-dataframe-api-limitations",
            "https://spark.apache.org/docs/latest/spark-connect-overview.html",
        ],
    },
    "code": {
        "repo_branch_list": [
            {"repo": "mrpowers-io/quinn", "branch": "main"},
            {"repo": "debugger24/pyspark-test", "branch": "main"},
            {"repo": "julioasotodv/spark-df-profiling", "branch": "master"},
            {"repo": "Labelbox/labelspark", "branch": "master"},
            {"repo": "lvhuyen/SparkAid", "branch": "master"},
        ],
    },
    "api_ref": {
        "vector_store_path": "/raid/shared/masterproject2024/vector_stores/vector_store"
    },
}


ITERATE = True
ITERATION_LIMIT = 5

# Types of messages the linter should return. Possible values: 'error', 'warning', 'convention' (maybe more) 
LINTER_FEEDBACK_TYPES = {"error"}

# current model options:
# - neuralmagic/Meta-Llama-3.1-405B-Instruct-quantized.w8a16
# - neuralmagic/Meta-Llama-3.1-405B-Instruct-quantized.w4a16
# - meta-llama/CodeLlama-70b-Python-hf
MODEL_NAME = "neuralmagic/Meta-Llama-3.1-405B-Instruct-quantized.w8a16"

INITIAL_PROMPT = f"""

        This is code using classic spark that we want to rewrite to work with spark connect.
        The rewritten code should have exactly the same functionality as the original code and should return exactly the same output.
        This is the original code that does not work with spark connect:

        <code>
        {{code}}
        </code>

        When executed, the code produces the following error:
        {{error}}

        In case it is helpful you can use the following context to help you with the task:

        <context>
        {{context}}
        </context>

        Make sure to only return the rewritten code and nothing else.
    """

ITERATED_PROMPT = f"""
        We wanted to rewrite this code snippet to work with spark connect. 
        The rewritten code should have exactly the same functionality as the original code and should return exactly the same output. 
        This is your latest attempt to rewrite the code. Double check if the code is correct and adjust it if necessary:

        <code>
        {{code}}
        </code>

        When this code is executed, it produces the following error:
        {{error}}

        In case it is helpful you can use the following context to help you with the task:

        <context>
        {{context}}
        </context>

        Make sure to only return the rewritten code and nothing else.
    """
