"""
# MarkTen / term tools

Simple functions to handle terminal output.
"""
import sys

if sys.platform == "win32":
    def getch():
        """
        Getch on Windows.

        https://stackoverflow.com/a/3523340/6335363
        """
        import msvcrt
        return msvcrt.getch()
else:
    def getch():
        """
        Getch on unix systems.

        https://stackoverflow.com/a/72825322/6335363
        """
        import termios
        import tty
        fd = sys.stdin.fileno()
        orig = termios.tcgetattr(fd)

        try:
            # or tty.setraw(fd) if you prefer raw mode's behavior.
            tty.setcbreak(fd)
            return sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSAFLUSH, orig)


def get_position() -> tuple[int, int]:
    """
    Returns the position in the terminal, as `(row, col)`.

    https://stackoverflow.com/a/8353312/6335363
    """
    print("\033[6n", end='', flush=True)
    assert getch() == "\033"
    assert getch() == "["

    row = ''
    while (ch := getch()) != ';':
        row += ch
    col = ''
    while (ch := getch()) != 'R':
        col += ch

    return int(row), int(col)


def set_position(pos: tuple[int, int]) -> None:
    """
    Set the terminal position to the given state.

    https://stackoverflow.com/a/54630943/6335363
    """
    r, c = pos
    print(f"\033[{r};{c}H", end='', flush=True)


def save_cursor():
    """Instruct the terminal to save the current cursor position."""
    print('\0337', end='', flush=True)


def restore_cursor():
    """Instruct the terminal to restore the saved cursor position."""
    print('\0338', end='', flush=True)


def clear_line():
    """
    Clear the current line of output.
    """
    print('\033[2K', end='', flush=True)


def print_clear(*args: object, **kwargs):
    """
    Print text after clearing the current line.
    """
    clear_line()
    print(*args, **kwargs)


if __name__ == '__main__':
    # Simple test program
    # print("\n" * 100)
    set_position((-10, 0))
    print("What about now?\n" * 10)
