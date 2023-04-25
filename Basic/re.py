import re
ret_val = re.search("(.*)([abc])(.*)",'dabc')
print(ret_val.group(0))
print(ret_val.group(1))
print(ret_val.group(2))
print(ret_val.group(3))