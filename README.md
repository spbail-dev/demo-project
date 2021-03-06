# Welcome to the demo project!

This is a demo project for my "Getting started with Open Source" talk. **PRs welcome!**

---

### ☕ Buy me a coffee ☕

If you enjoy this workshop and want to say thanks, you can buy me a coffee here: https://www.buymeacoffee.com/sambail
Thank you 😄

---

## What does this project do?

Ok, this is really just a dummy project I hacked together to demonstrate contribution workflows. **But** it does do something fun: The code in `brewery_api.py` queries an API that provides a list of breweries for any US state a user inputs. Thanks to [openbrewerydb.org](https://www.openbrewerydb.org/) for maintaining this API.

## How do I run this?

You can run the code with 
```bash
python src/brewery_api.py <state name>
``` 
or
```bash
python -m src.brewery_api <state name>
```

For example: 
```bash
python -m src.brewery_api ohio
```

If using a state name with a space, you'll need to quote it, e.g.
```bash
python -m src.brewery_api "new york"
```

## How to contribute

1. Check out the open issues and the #TODOs in the code
2. Then follow the instructions in [CONTRIBUTING.md](CONTRIBUTING.md)!
