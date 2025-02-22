import sys
from perchance.transform import transform_code

def run_perchance_script(script_path):
    """Reads a .pyp script, transforms it, and executes it as Python."""
    with open(script_path, "r", encoding="utf-8") as f:
        dsl_code = f.read()

    python_code = transform_code(dsl_code)

    # Execute the transformed Python code in the current global namespace
    exec(python_code, globals())

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: perchance-run <script.pyp>")
        sys.exit(1)

    script_file = sys.argv[1]
    run_perchance_script(script_file)
