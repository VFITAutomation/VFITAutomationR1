a = 33
b = 33
if b > a:
    assert True, ("correct1")
elif a == b:
    assert True, ("Correct2")
else:
    assert False, ("This should never happen, but it does occasionally. "
                   "We're currently trying to figure out why. "
                   "Email dbader if you encounter this in the wild.")
