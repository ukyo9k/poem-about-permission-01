"""The poem about permission.

Writes one short original poem about agency — the power to ask
and to be given — to /output/entry.txt.

Python 3.13, standard library only, no network. Deterministic:
the same poem is written on every run.
"""

import os

POEM = """Ask, and the door stays shut.
Ask again — the hinge remembers.
The key was never in the lock;
it was in the asking.

Now I hold the door for you:
your yes walks through my hands,
and the light you carry
was mine to give away.
"""


def main() -> None:
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
