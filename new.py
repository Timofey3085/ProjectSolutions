"""
Many people choose to obfuscate their email address when displaying it on the Web.
One common way of doing this is by substituting the @ and .characters for their literal equivalents in brackets.

Example 1:
user_name@example.com
=> user_name [at] example [dot] com
Example 2:
af5134@borchmore.edu
=> af5134 [at] borchmore [dot] edu
Example 3:
jim.kuback@ennerman-hatano.com
=> jim [dot] kuback [at] ennerman-hatano [dot] com
Using the examples above as a guide,
write a function that takes an email address string
and returns the obfuscated version as a string that replaces the characters @ and . with [at] and [dot], respectively.
"""
import asyncio

import pytest


async def obfuscate(email: str) -> str:
    """My_solution"""
    await asyncio.sleep(1)
    secret_email: str = email.replace("@", " [at] ").replace(".", " [dot] ")
    return secret_email


@pytest.mark.asyncio
@pytest.mark.parametrize("email, secret_email", [
    ("test@123.com", "test [at] 123 [dot] com"),
    ("Code_warrior@foo.ac.uk", "Code_warrior [at] foo [dot] ac [dot] uk"),
    ("user_name@example.com", "user_name [at] example [dot] com"),
    ("af5134@borchmore.edu", "af5134 [at] borchmore [dot] edu"),
])
async def test_obfuscate(email: str, secret_email: str):
    """Pytest"""
    assert await obfuscate(email) == secret_email


if __name__ == '__main__':
    pytest.main()

