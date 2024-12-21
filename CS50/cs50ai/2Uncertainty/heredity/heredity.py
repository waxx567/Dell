import csv
import itertools
import sys

# PROBS is a dictionary containing a number of constants representing probabilities of various different events. All of these events have to do with how many copies of a particular gene a person has (hereafter referred to as simply “the gene”), and whether a person exhibits a particular trait (hereafter referred to as “the trait”) based on that gene. The data here is loosely based on the probabilities for the hearing impairment version of the GJB2 gene and the hearing impairment trait, but by changing these values, you could use your AI to draw inferences about other genes and traits as well!

PROBS = {

    # Unconditional probabilities for having gene (i.e., the probability if we know nothing about that person’s parents).
    "gene": {
        2: 0.01,
        1: 0.03,
        0: 0.96
    },

    # PROBS["trait"] represents the conditional probability that a person exhibits a trait (like hearing impairment).
    "trait": {

        # Probability of trait given two copies of gene
        2: {
            True: 0.65,
            False: 0.35
        },

        # Probability of trait given one copy of gene
        1: {
            True: 0.56,
            False: 0.44
        },

        # Probability of trait given no gene
        0: {
            True: 0.01,
            False: 0.99
        }
    },

    # Mutation probability is the probability that a gene mutates from being the gene in question to not being that gene, and vice versa.
    "mutation": 0.01
}
# Ultimately, the probabilities you calculate will be based on these values in PROBS.


def main():

    # Check for proper usage
    if len(sys.argv) != 2:
        sys.exit("Usage: python heredity.py data.csv")

    # The main function first loads data from a file into a dictionary people.
    people = load_data(sys.argv[1])
    # people maps each person’s name to another dictionary containing information about them: including their name, their mother (if one is listed in the data set), their father (if one is listed in the data set), and whether they are observed to have the trait in question (True if they do, False if they don’t, and None if we don’t know).

    # Keep track of gene and trait probabilities for each person
    # Next, main defines a dictionary of probabilities, with all probabilities initially set to 0.
    probabilities = {
        person: {
            "gene": {
                2: 0,
                1: 0,
                0: 0
            },
            "trait": {
                True: 0,
                False: 0
            }
        }
        for person in people
    }
    # This is what your project will compute: for each person, your AI will calculate the probability distribution over how many of copies of the gene they have, as well as whether they have the trait or not. probabilities["Harry"]["gene"][1], for example, will be the probability that Harry has 1 copy of the gene, and probabilities["Lily"]["trait"][False] will be the probability that Lily does not exhibit the trait.

    # We’re looking to calculate these probabilities based on some evidence: given that we know certain people do or do not exhibit the trait, we’d like to determine these probabilities. Recall from lecture that we can calculate a conditional probability by summing up all of the joint probabilities that satisfy the evidence, and then normalize those probabilities so that they each sum to 1. Your task in this project is to implement three functions to do just that: joint_probability to compute a joint probability, update to add the newly computed joint probability to the existing probability distribution, and then normalize to ensure all probability distributions sum to 1 at the end.

    # Loop over all sets of people who might have the trait
    names = set(people)
    for have_trait in powerset(names):

        # Check if current set of people violates known information
        fails_evidence = any(
            (people[person]["trait"] is not None and
             people[person]["trait"] != (person in have_trait))
            for person in names
        )
        if fails_evidence:
            continue

        # Loop over all sets of people who might have the gene
        for one_gene in powerset(names):
            for two_genes in powerset(names - one_gene):

                # Update probabilities with new joint probability
                p = joint_probability(people, one_gene, two_genes, have_trait)
                update(probabilities, one_gene, two_genes, have_trait, p)

    # Ensure probabilities sum to 1
    normalize(probabilities)

    # Print results
    for person in people:
        print(f"{person}:")
        for field in probabilities[person]:
            print(f"  {field.capitalize()}:")
            for value in probabilities[person][field]:
                p = probabilities[person][field][value]
                print(f"    {value}: {p:.4f}")


def load_data(filename):
    """
    Load gene and trait data from a file into a dictionary.
    File assumed to be a CSV containing fields name, mother, father, trait.
    mother, father must both be blank, or both be valid names in the CSV.
    trait should be 0 or 1 if trait is known, blank otherwise.
    """
    data = dict()
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = row["name"]
            data[name] = {
                "name": name,
                "mother": row["mother"] or None,
                "father": row["father"] or None,
                "trait": (True if row["trait"] == "1" else
                          False if row["trait"] == "0" else None)
            }
    return data


def powerset(s):
    """
    Return a list of all possible subsets of set s.
    """
    s = list(s)
    return [
        set(s) for s in itertools.chain.from_iterable(
            itertools.combinations(s, r) for r in range(len(s) + 1)
        )
    ]

# Complete the implementations of joint_probability, update, and normalize.

# You should not modify anything else in heredity.py other than the three functions the specification calls for you to implement, though you may write additional functions and/or import other Python standard library modules. You may also import numpy or pandas, if familiar with them, but you should not use any other third-party Python modules.

# The get_gene helper function returns a person's gene information


def get_gene(person, one_gene, two_genes):
    if person in one_gene:
        return 1
    elif person in two_genes:
        return 2
    else:
        return 0

# The inherit helper function returns the probability of a person inheriting a mutated gene for a parent


def inherit(parent, one_gene, two_genes):
    if parent in one_gene:
        return 0.5
    elif parent in two_genes:
        return 1 - PROBS["mutation"]
    else:
        return PROBS["mutation"]

# The joint_probability function should take as input a dictionary of people, along with data about who has how many copies of each of the genes, and who exhibits the trait. The function should return the joint probability of all of those events taking place.


def joint_probability(people, one_gene, two_genes, have_trait):
    """
    Compute and return a joint probability.

    The probability returned should be the probability that
        * everyone in set `one_gene` has one copy of the gene, and
        * everyone in set `two_genes` has two copies of the gene, and
        * everyone not in `one_gene` or `two_gene` does not have the gene, and
        * everyone in set `have_trait` has the trait, and
        * everyone not in set` have_trait` does not have the trait.
    """
    # For anyone with no parents listed in the data set, use the probability distribution PROBS["gene"] to determine the probability that they have a particular number of the gene.
    # For anyone with parents in the data set, each parent will pass one of their two genes on to their child randomly, and there is a PROBS["mutation"] chance that it mutates (goes from being the gene to not being the gene, or vice versa).
    # Use the probability distribution PROBS["trait"] to compute the probability that a person does or does not have a particular trait.

    prob_joint = 1

    # Loop over all persons
    for person in people:

        # Initialize person probability variable
        prob_person = 1
        # Assign person information to variables
        gene = get_gene(person, one_gene, two_genes)
        trait = person in have_trait

        mother = people[person]["mother"]
        father = people[person]["father"]

        # If no parents given
        if not mother and not father:
            prob_person *= PROBS["gene"][gene]
        # If parents given
        else:
            prob_mother = inherit(mother, one_gene, two_genes)
            prob_father = inherit(father, one_gene, two_genes)

            # Assign probabilities
            if gene == 2:
                prob_person *= prob_mother * prob_father
            elif gene == 1:
                prob_person *= ((1 - prob_mother) * prob_father) + ((1 - prob_father) * prob_mother)
            else:
                prob_person *= (1 - prob_mother) * (1 - prob_father)

        prob_person *= PROBS["trait"][gene][trait]

        prob_joint *= prob_person

    return prob_joint

# The update function adds a new joint distribution probability to the existing probability distributions in probabilities.


def update(probabilities, one_gene, two_genes, have_trait, p):
    """
    Add to `probabilities` a new joint probability `p`.
    Each person should have their "gene" and "trait" distributions updated.
    Which value for each distribution is updated depends on whether
    the person is in `have_gene` and `have_trait`, respectively.
    """
    # For each person person in probabilities, the function should update the probabilities[person]["gene"] distribution and probabilities[person]["trait"] distribution by adding p (the probability of the joint distribution) to the appropriate value in each distribution. All other values should be left unchanged.
    # The function should not return any value: it just needs to update the probabilities dictionary.

    for person, distribution in probabilities.items():

        # Assign person information to variables
        gene = get_gene(person, one_gene, two_genes)
        trait = person in have_trait

        # Update distribution
        distribution["gene"][gene] += p
        distribution["trait"][trait] += p

# The normalize function updates a dictionary of probabilities such that each probability distribution is normalized (i.e., sums to 1, with relative proportions the same).


def normalize(probabilities):
    """
    Update `probabilities` such that each probability distribution
    is normalized (i.e., sums to 1, with relative proportions the same).
    """
    # For both of the distributions for each person in probabilities, this function should normalize that distribution so that the values in the distribution sum to 1, and the relative values in the distribution are the same.
    # The function should not return any value: it just needs to update the probabilities dictionary.

    # Loop over each probability distribution and random variables
    for person in probabilities.values():
        for value in person.values():
            # Add values together
            total = sum(value.values())
            # Normalize probability distribution
            for result, probability in value.items():
                value[result] = probability / total


if __name__ == "__main__":
    main()