import argparse
from .transform import transform_code

def main():
    parser = argparse.ArgumentParser(
        description='Transform DSL code (with "perchance", etc.) into valid Python'
    )
    parser.add_argument('input', help='Input DSL file')
    parser.add_argument('output', nargs='?', help='Output Python file (optional)')
    args = parser.parse_args()

    with open(args.input, 'r') as f:
        source = f.read()

    transformed = transform_code(source)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(transformed)
        print(f"Transformed code written to {args.output}")
    else:
        print(transformed)

if __name__ == '__main__':
    main()
