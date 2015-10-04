# auto_pass

Generate a random password, assign it to a user & email it to them.

* Must be run with appropriate privileges.
* If using gmail, enable 2 factor authentication and app password.
* email_cred.json = {"default-mail": ["<email_address>", "<password>"], "alt-mail": ["<alt_address>", "<password>"]} etc...


####TODO:

1. Get current user. ~ done.
2. Add command line arguments (argparse) (user, password strength, logging).
3. Move password gen to function. ~ done.
4. Store email credentials in json. ~ done.
5. Add subject / html email. ~ done.
6. Test as cron job on logoff.
7. ???
8. Profit!
