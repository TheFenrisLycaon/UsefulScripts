def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    else:
        return email


replace_domain("trial0@gmail.com", "abc.com", "rishabhanand.ninja")
replace_domain("trial@gmail.com", "abc.com", "rishabhanand.ninja")
