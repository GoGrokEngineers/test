import subprocess
from apps.test_case.models import TestCase

def format_cases(task):
    cases = TestCase.objects.filter(task=task)
    result = []
    for task, input, output, input_type, output_type in cases:
        buff = {"input": input, "expected_output": output}
        result.append(buff)
    
    return result


def evaluate_code(code: str, task, competion_uid, nick_name):
    file_name = f"submission_{nick_name}_{competion_uid}.py"
    with open(file_name, "w") as f:
        f.write(code)

    results = []
    test_cases = format_cases(task)
    for i, test_case in enumerate(test_cases):
        result = subprocess.run(
            ['python', file_name],
            input=test_case['input'],
            text=True,
            capture_output=True
        )

        if result.returncode == 0:
            if result.stdout.strip() == test_case['expected_output'].strip():
                results.append({"test_case": i + 1, "result": "pass", "output": result.stdout})
            else:
                results.append({"test_case": i + 1, "result": "fail", "output": result.stdout, "expected": test_case['expected_output']})
        else:
            results.append({"test_case": i + 1, "result": "error", "error": result.stderr})

    return results