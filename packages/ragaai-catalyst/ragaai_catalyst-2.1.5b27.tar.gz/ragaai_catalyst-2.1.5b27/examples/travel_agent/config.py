

import os
from dotenv import load_dotenv

from ragaai_catalyst import RagaAICatalyst, Tracer, init_tracing
import uuid
def initialize_tracing():
    load_dotenv()
    print(f"Access key: {os.getenv('RAGAAI_CATALYST_STAGING_ACCESS_KEY')}")
    print(f"Secret key: {os.getenv('RAGAAI_CATALYST_STAGING_SECRET_KEY')}")
    print(f"Base url: {os.getenv('RAGAAI_CATALYST_STAGING_BASE_URL')}")

    catalyst = RagaAICatalyst(
        access_key=os.getenv("RAGAAI_CATALYST_STAGING_ACCESS_KEY"),
        secret_key=os.getenv("RAGAAI_CATALYST_STAGING_SECRET_KEY"),
        base_url=os.getenv("RAGAAI_CATALYST_STAGING_BASE_URL"),
    )

    tracer = Tracer(
        project_name="Execute_Metric_Test1",
        dataset_name="travel_agent_dataset",
        tracer_type="Agentic",  # langchain, llamaindex, Agentic
    )

    init_tracing(catalyst=catalyst, tracer=tracer)
    return tracer
