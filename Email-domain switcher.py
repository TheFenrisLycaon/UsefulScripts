def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        print (new_email)
    else:    
     print (email) 
replace_domain("saurabhsrivastva10@gmail.com", "gmail.com", "yahoo.com")
replace_domain("saurabhsrivastva10@gmail.com", "gmail.com", "yahoo.com")



