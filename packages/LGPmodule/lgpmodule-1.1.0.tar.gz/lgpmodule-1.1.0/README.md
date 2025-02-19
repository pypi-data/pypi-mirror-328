- **`bold(text, start="<b>", end="</b>")`**
    - `text` (str): The text to be formatted in bold.
    - `start` (str, optional): The start tag for bold formatting (default is `<b>`).
    - `end` (str, optional): The end tag for bold formatting (default is `</b>`).

    This function replaces the provided HTML-like `<b>` and `</b>` tags with ANSI escape codes to make the text bold in the terminal. For example, if the string contains the tags `<b>Text</b>`, they will be replaced with the corresponding ANSI escape codes for bold text.

- **`print(text="", mode="t", icon=None)`**
    - `text` (str, optional): The text to be displayed in the console. If no text is provided, an empty string will be printed.
    - `mode` (str, optional): Defines the color and category of the message. The following options are supported:
        - `"d"` — Green (for debug messages).
        - `"w"` — Yellow (for warnings).
        - `"e"` — Red (for errors).
        - `"c"` — Purple (for critical messages).
        - `"i"` — Cyan (for info messages).
        - `"t"` — White (for text messages).
    - `icon` (str, optional): A custom icon to be displayed before the message. If `None`, the default icon for the given `mode` will be used.

    The `print()` function combines color formatting and optional icons to output the message to the console. If the text contains HTML-like tags (`<b>` and `</b>`), they will be converted into bold formatting using ANSI escape codes.

- **`debug(message, icon=None)`**
    - `message` (str): The message to be printed in green color (for debug purposes).
    - `icon` (str, optional): A custom icon to precede the message. Defaults to the debug icon.

    This function is shorthand for printing a debug message using `print()` with the `"d"` mode.

- **`info(message, icon=None)`**
    - `message` (str): The message to be printed in cyan color (for informational purposes).
    - `icon` (str, optional): A custom icon to precede the message. Defaults to the info icon.

    This function is shorthand for printing an informational message using `print()` with the `"i"` mode.

- **`warn(message, icon=None)`**
    - `message` (str): The message to be printed in yellow color (for warning purposes).
    - `icon` (str, optional): A custom icon to precede the message. Defaults to the warning icon.

    This function is shorthand for printing a warning message using `print()` with the `"w"` mode.

- **`error(message, icon=None)`**
    - `message` (str): The message to be printed in red color (for error purposes).
    - `icon` (str, optional): A custom icon to precede the message. Defaults to the error icon.

    This function is shorthand for printing an error message using `print()` with the `"e"` mode.

- **`critical(message, icon=None, exit_code=1)`**
    - `message` (str): The message to be printed in purple color (for critical errors).
    - `icon` (str, optional): A custom icon to precede the message. Defaults to the critical icon.
    - `exit_code` (int, optional): The exit code to be used when terminating the program (default: `1`). If `exit_code` is greater than `0`, the program will exit after printing the critical message.

    This function is shorthand for printing a critical message using `print()` with the `"c"` mode. It also terminates the program if the exit code is non-zero.

### Constants:

- `lgp_default_icons`: A dictionary mapping message types (`i`, `d`, `w`, `e`, `c`, `t`) to their default icon representations.
- `COLORS`: A dictionary mapping message types (`i`, `d`, `w`, `e`, `c`, `t`) to their corresponding ANSI color codes.
