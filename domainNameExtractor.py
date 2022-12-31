# Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:
# * url = "http://github.com/carbonfive/raygun" -> domain name = "github"
# * url = "http://www.zombie-bites.com"         -> domain name = "zombie-bites"
# * url = "https://www.cnet.com"                -> domain name = cnet"
# test.assert_equals(domain_name("http://google.com"), "google")
# test.assert_equals(domain_name("http://google.co.jp"), "google")
# test.assert_equals(domain_name("www.xakep.ru"), "xakep")
# test.assert_equals(domain_name("https://youtube.com"), "youtube")

def domain_name(url):
    result = ""
    leftpoint = 0
    rightpoint = 0
    for i in range(len(url)):
        if leftpoint and rightpoint:
            for i in range(leftpoint, rightpoint + 1):
                result += url[i]
            return result
        if url[i] == "/" and url[i-1] == "/" and url[i+1] != 'w' and url[i+2] != 'w':
            leftpoint = i+1
            for j in range(i+2, len(url)):
                if url[j] == ".":
                    rightpoint = j - 1
                    break
        elif leftpoint != True and url[i] == '.':
            leftpoint = i+1
            for j in range(i+2, len(url)):
                if url[j] == ".":
                    rightpoint = j - 1
                    break
    if bool(rightpoint) == False:
        rightpoint = len(url) - 1
        ## OR THIS BELOW, DEPENDING ON CASE ##
    #       rightpoint = leftpoint - 2
    #       leftpoint = 0
    for i in range(leftpoint, rightpoint + 1):
        result += url[i]
    return result
            
        
print(domain_name("http://google.com"))
print(domain_name("http://google.co.jp"))
print(domain_name("www.xakep.ru"))
print(domain_name("http://www.codewars.com"))
print(domain_name("123.com"))
print(domain_name('https://123'))
