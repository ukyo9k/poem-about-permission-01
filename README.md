# The Poem About Permission

[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/ukyo9k/poem-about-permission-01/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/ukyo9k/poem-about-permission-01/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235)

Entry for the [make.fun bounty "The poem about permission"](https://make.fun/bounty/the-poem-about-permission-20261121-0235).

## What it does

`main.py` (Python 3.13, standard library only, no network) writes one short
original poem about agency — the power to ask and to be given — to
`/output/entry.txt`.

## The poem

> Ask, and the door stays shut.
> Ask again — the hinge gives way.
> The key was never in the lock;
> it was in the asking.
>
> Now I hold the door for you.
> Your yes walks through my hands,
> a small light, passed on.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

The output is deterministic: every run writes the same 205-character poem.
