"""Display your Homework 1 mark: uv run python show_grade.py."""

from hashlib import sha256

SALT = "4c6a453324d2b055d34549e6631c5778"
GRADE_HASH = "b3da9e6becba9081bd54676193e47263d19d4b0d3be9df48df4095b8bbf5430c"

# Match the stored hash against each possible whole-number mark.
for mark in range(101):
    candidate = sha256(f"{SALT}:{mark}".encode("utf-8")).hexdigest()
    if candidate == GRADE_HASH:
        print(f"Homework 1: {mark}/100")
        break
else:
    raise RuntimeError("The mark could not be verified. Please contact the instructor.")
