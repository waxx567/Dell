from model import model

# Calculate probability for a given observation
probability = model.probability([["none", "no", "on time", "attend"]])

print(probability)


# python likelihood.py
# 0.34019999999999995
# Meaning that is the probability that the above circumstances happen ie. no rain, no track maintenance, train on time, and keep appointment (able to attend)
# 34% of the time

# Change appointment on line 4 thusly
# probability = model.probability([["none", "no", "on time", "miss"]])
# python likelihood.py
# 0.03700000000000014
# Meaning this is the probability of everything going right and still missing the appointment
# 3.7% of the time