Sometimes I like rabbit holes LOL

Index

1. Rabbit Hole 1 - editior shows the function signature with type hints.
2. Python is a ZERO-BASED

## rabbit hole 2

zero-based, stop-exclusive

this zero based thing means that python starts to count arrays at zero

## rabbit hole 1

okay I was today years old when I learned about VS code screen that pops up its called 🔮 FUNCTION SIGNATURE with TYPE HINTS 🔮

I got here cuz I wrote a littel print statment and saw this shit pop up:

(\*values: object, sep: str | None = " ", end: str | None = "\n",
file: SupportsWrite[str] | None = None, flush: Literal[False] = False) -> None

and was like WTF hahaha my curser got stuck kinda wait my arrow key caused a toggle... anyways!!

| Parameter | Meaning                                              | Default                              |
| --------- | ---------------------------------------------------- | ------------------------------------ |
| `*values` | One or more things to print (numbers, strings, etc.) | —                                    |
| `sep`     | Separator between each printed value                 | `" "` (a space)                      |
| `end`     | What to append at the end of the line                | `"\n"` (newline)                     |
| `file`    | Where to write output (like `sys.stdout` or a file)  | `None` (defaults to standard output) |
| `flush`   | If `True`, forces the output to appear immediately   | `False`                              |

💬 3. Why the message changes

When you type print( and pause, the editor first shows the function signature.
If you expand the tooltip or move the cursor over a parameter, you’ll see a more detailed docstring (like this below the signature):

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file: a file-like object (stream); defaults to the current sys.stdout.
sep: string inserted between values, default a space.
end: string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.

---
