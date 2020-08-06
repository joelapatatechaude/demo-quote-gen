import os
import random

quotes = [
    {"name": "Steve Jobs", "quote": "Real Artists Ship."},
    {"name": "Isaac Asimov", "quote": "I do not fear computers. I fear lack of them."},
    {
        "name": "Bill Gates",
        "quote": "The computer was born to solve problems that did not exist before.",
    },
    {
        "name": "IBM Manual, 1925",
        "quote": "All parts should go together without forcing.  You must remember that the parts you are reassembling were disassembled by you.  Therefore, if you can’t get them together again, there must be a reason.  By all means, do not use a hammer.",
    },
    {
        "name": "Alan Bennett",
        "quote": "Standards are always out of date.  That’s what makes them standards.",
    },
    {
        "name": "Socrates",
        "quote": "The more you know, the more you realize you know nothing.",
    },
    {
        "name": "Benjamin Franklin",
        "quote": "Tell me and I forget.  Teach me and I remember.  Involve me and I learn.",
    },
]


def get_quote_random():
    index = int(random.randint(0, len(quotes) - 1))
    return quotes[index]["name"], quotes[index]["quote"]