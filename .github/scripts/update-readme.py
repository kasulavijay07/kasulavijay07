import datetime
import random

# List of quotes
quotes = [
    ("“Talk is cheap. Show me the code.”", "Linus Torvalds"),
    ("“Programs must be written for people to read.”", "Harold Abelson"),
    ("“First, solve the problem. Then, write the code.”", "John Johnson"),
    ("“Simplicity is the soul of efficiency.”", "Austin Freeman"),
    ("“Code never lies, comments sometimes do.”", "Ron Jeffries"),
    ("“The only way to go fast, is to go well.”", "Robert C. Martin"),
]

# Pick day and random quote
today = datetime.datetime.now().strftime("%A")
quote, author = random.choice(quotes)

# Create new content block
quote_block = f"> **Today is {today}**  \n> _{quote}_ — **{author}**"

# Read README
with open("README.md", "r", encoding="utf-8") as file:
    content = file.read()

# Replace section
new_content = content.split("<!--QUOTE-SECTION:START-->")[0] + \
              "<!--QUOTE-SECTION:START-->\n" + quote_block + "\n<!--QUOTE-SECTION:END-->" + \
              content.split("<!--QUOTE-SECTION:END-->")[1]

# Write back
with open("README.md", "w", encoding="utf-8") as file:
    file.write(new_content)
