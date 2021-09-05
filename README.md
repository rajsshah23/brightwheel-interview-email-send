# brightwheel-interview-email-send
Brightwheel Interview Question

Python 3.9.7
  - Using it because it is the latest Python version.
  - Using Python because I am most comfortable with it right now, as I use it
    daily

Pre-commit:
pip install pre-commit

Justfile:
https://github.com/casey/just


To setup:
```shell script
just dev-setup
```


API Docs: http://127.0.0.1:8000/docs






Snailgun get errors -
```json5
{"error":"undefined method `[]' for nil:NilClass"}
```

Snailgun send errors -
```json5
{"error":"783: unexpected token at 'from_email=noreply%40mybrightwheel.com\u0026from_name=brightwheel\u0026to_email=rajsshah23%40gmail.com\u0026to_name=Raj+Shah\u0026subject=Your+Weekly+Report\u0026body=%3Ch1%3EWeekly+Report%3C%2Fh1%3E%3Cp%3EYou+saved+11+hours+this+week%21%3C%2Fp%3E'"}
```


Spendgrid send error -
```json5
{"error":"783: unexpected token at 'sender=brightwheel+noreply%40mybrightwheel.com\u0026recipient=Raj+Shah+rajsshah23%40gmail.com\u0026subject=Your+Weekly+Report\u0026body=%3Ch1%3EWeekly+Report%3C%2Fh1%3E%3Cp%3EYou+saved+11+hours+this+week%21%3C%2Fp%3E'"}
```

Other TODOs:
1. Add better responses for when there is an exception.
2. Add support for spinning up the app in a Docker container
3. Setup a SQL database to store the incoming requests, their send status, which email vendor was used, vendor send id, etc.
