
# import re
# ret_val = re.search("(.*)([abc])(.*)",'dabc')
# print(ret_val.group(0))
# print(ret_val.group(1))
# print(ret_val.group(2))
# print(ret_val.group(3))

# import re
# x = re.search("cat", "A cat and a rat can't be friends.")
# print(x)


# import re
# txt = "The rain in Spain"
# x = re.search("^The.*Spain$", txt)

# if x:
#   print("YES! We have a match!")
# else:
#   print("No match")

# import re

# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)

import re

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

