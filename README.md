
# SA Replacer
Basic SladeAbility (2.0.5) store replacer for all abilities

## Screenshots

![App Screenshot](https://raw.githubusercontent.com/Compromissed/cdn/main/j6dIrYy.png)

## Usage

If this is going out of support. To get all abilities config use the following commands:
```bash
grep -r 'store.youserver.com' | sort -u | awk '{print $1}'
grep -r 'skilled-dev.club' | sort -u | awk '{print $1}'
```
Then replace the ':' with nothing and update the files variables, don't leave changes of line like this:
```python
lines = """
Abilities/ExampleAbility.yml
Abilities/ExampleAbility2.yml
Abilities/ExampleAbility3.yml
"""
```
Leave it like this:
```python
lines = """Abilities/ExampleAbility.yml
Abilities/ExampleAbility2.yml
Abilities/ExampleAbility3.yml"""
```

Created it because changing every SladeAbility store takes a lot of time. You need to set up the following variables and put the script on the SladeAbility plugin folder:
```python
store = "store.vexpvp.club" # This is an example
domain = "vexpvp.club" # This is an example
```
Only python3 required. No imports or sketchy stuff.
