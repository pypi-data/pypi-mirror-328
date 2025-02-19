from jinja2 import Template
from promptflow.core import tool
from promptflow.connections import CustomConnection
from promptflow.contracts.types import PromptTemplate


@tool
def export_esasy_gaia_determine_reply(
    connection: CustomConnection,
    api: str,
    deployment_name: str,
    temperature: float,
    prompt: PromptTemplate,
    **kwargs
) -> str:
    # Replace with your tool code, customise your own code to handle and use the prompt here.
    # Usually connection contains configs to connect to an API.
    # Not all tools need a connection. You can remove it if you don't need it.
    kwargs.pop('is_new_session')
    kwargs.pop('context_first')
    kwargs.pop('context_second')
    
    rendered_prompt = Template(prompt, trim_blocks=True, keep_trailing_newline=True).render(kwargs)
    return rendered_prompt