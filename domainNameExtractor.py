# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
# test.assert_equals(domain_name("http://google.com"), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# test.assert_equals(domain_name("https://youtube.com"), "youtube")

def domain_name(url):
    for char in url:
        print(char)
        
domain_name("http://google.com")

