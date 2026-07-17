def calculate(expression):
    # Strip whitespace from both ends of the input expression.
    expression = expression.strip()
    # If the expression is empty after trimming, raise a clear error.
    if not expression:
        raise ValueError('Empty expression')
    # Evaluate the expression in a restricted global namespace with no builtins.
    # This limits access to dangerous functions while allowing numeric operations.
    return eval(expression, {'__builtins__': None}, {})


def main():
    # Print a user-facing prompt explaining how to quit.
    print('Simple calculator. Type "quit" or "exit" to stop.')
    while True:
        try:
            # Read a line of input from the user and strip surrounding whitespace.
            expr = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            # Handle Ctrl-D, Ctrl-C, or other console interruptions cleanly.
            print('\nBye.')
            break

        # Ignore empty input lines and prompt again.
        if not expr:
            continue
        # Allow the user to exit the program with quit or exit.
        if expr.lower() in {'quit', 'exit'}:
            print('Bye.')
            break
        # Allow a clear command to clear the terminal output.
        if expr.lower() in {'clear', 'c'}:
            print('\033c', end='')
            continue

        try:
            # Evaluate the expression and print the result.
            print(calculate(expr))
        except Exception as exc:
            # Print any error raised during parsing or evaluation.
            print('Error:', exc)


if __name__ == '__main__':
    # Run the main loop only when the script is executed directly.
    main()

