# Security Checklist

## SQL Injection
Never build SQL queries with f-strings or string concatenation. Always use parameterized queries so user input cannot change the query.

## Hardcoded Secrets
Never put passwords, API keys or tokens in source code. Load them from environment variables or a secrets manager, and keep `.env` out of version control.

## Dangerous Functions
Never pass user input to `eval`, `exec` or `os.system`. Do not use `subprocess` with `shell=True` on untrusted input.

## Password Storage
Hash passwords with bcrypt or argon2. Never store plain text passwords, and never use MD5 or SHA1 for passwords.