"""
Centralized prompt templates. Keeping these separate from assistant.py
means you can tune wording/structure without touching logic or UI code.
Each template asks for clear, structured, readable output explicitly.
"""

def generate_code_prompt(description: str) -> str:
    return f"""You are an expert Python developer.
Task: Write Python code for the following requirement.

Requirement:
{description}

Instructions:
- Return clean, working Python code only.
- Add brief inline comments explaining key steps.
- Use clear variable and function names.
- If helpful, include a short example usage at the bottom.
"""


def explain_code_prompt(code: str) -> str:
    return f"""You are an expert Python tutor.
Explain the following code clearly, step by step.

Code:
{code}

Instructions:
- Break the explanation into numbered steps.
- Explain what each function/block does.
- Keep language simple and readable.
- End with a one-line summary of the overall purpose.
"""


def fix_bug_prompt(code: str, error_message: str = "") -> str:
    return f"""You are an expert Python debugger.
Find and fix the bug in the following code.

Code:
{code}

Error/Issue (if any):
{error_message if error_message else "Not specified — inspect the code for likely bugs."}

Instructions:
- Clearly state what the bug is and why it happens.
- Provide the corrected, complete code.
- Keep formatting clean and structured (use headers: "Bug", "Explanation", "Fixed Code").
"""


def optimize_code_prompt(code: str) -> str:
    return f"""You are an expert in Python performance and code quality.
Optimize the following code.

Code:
{code}

Instructions:
- Identify inefficiencies or bad practices.
- Provide an optimized version of the code.
- Briefly explain what was improved and why (readability: use headers "Issues Found", "Optimized Code", "Improvements").
"""