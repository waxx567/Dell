# Implement rejection sampling

import pomegranate

from collections import Counter

from model import model

def generate_sample():

    # Mapping of random variable name to sample generated
    sample = {}

    # Mapping of distribution to sample generated
    parents = {}

    # Loop over all states, assuming topological order
    for state in model.states:

        # If we have a non-root node, sample conditional on parents
        if isinstance(state.distribution, pomegranate.ConditionalProbabilityTable):
            sample[state.name] = state.distribution.sample(parent_values=parents)

        # Otherwise, just sample from the distribution alone (ie. rain, which has no parents)
        else:
            sample[state.name] = state.distribution.sample()

        # Keep track of the sampled value in the parents mapping
        parents[state.distribution] = sample[state.name]

    # Return generated sample
    return sample

# Rejection sampling
# Compute distribution of Appointment given that train is delayed
N = 10000 # Take 10000 samples
data = []
for i in range(N):
    sample = generate_sample()
    # Take the sample (10000) and only consider samples where the train is delayed
    if sample["train"] == "delayed":
        # If so, add the value of the appointment to the data that is being collected
        data.append(sample["appointment"])
print(Counter(data))


# python sample.py
# Counter(("attend": 1251, "miss": 856))

# This is an approximation, run python sample.py again and the numbers will be similar but not identical because there is some randomization, some likelihood that things might be higher or lower
# More samples will allow for more confidence in the results

# One problem that rejection sampling has is that if the evidence you're looking for is a fairly unlikely event, you will reject a lot of samples

# There are other methods
# One of which is Likelihood Weighting
# Start by fixing the values for evidence variables
# Sample the non-evidence variables using conditional probabilities in the Bayesian Network
# Weight each sample by its likelihood: the probability of all of the evidence