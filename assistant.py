from model_config import chat
from prompts import generate_code_prompt, explain_code_prompt, fix_bug_prompt, optimize_code_prompt


def generate_code(description: str) -> str:
    return chat(generate_code_prompt(description))

def explain_code(code: str) -> str:
    return chat(explain_code_prompt(code))

def fix_bug(code: str, error_message: str = "") -> str:
    return chat(fix_bug_prompt(code, error_message))

def optimize_code(code: str) -> str:
    return chat(optimize_code_prompt(code))