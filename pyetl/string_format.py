test_template_1 = "test {}"
test_template_2 = "test %s"

test_var = "test_result"

print(test_template_1.format(test_var))
print(test_template_2 % (test_var))

test_template_3 = "test {test_var_2}"
print(test_template_3.format(test_var_2=test_var))

print(f"test {test_var}")
