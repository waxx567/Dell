import os
import random
import re
import sys


DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    # Variable representing number of files in corpus
    N = len(corpus)
    n = 1 / N
    # Variable representing number of links on page
    L = len(corpus[page])
    # Variable to store damping factor value
    d = damping_factor

    # Initialize probability distribution dictionary using dictionary comprehension, and set value of pages to zero
    prob_dist = {pg: 0 for pg in corpus}

    # If page has no links, the corpus has equal probability
    if L == 0:
        for pg in prob_dist:
            prob_dist[pg] = n

        return prob_dist

    # Variable to store random probability
    prob_rand = (1 - d) / N
    # Variable to store link probability
    prob_link = d / L

    # All pages start with random probability
    for pg in prob_dist:
        prob_dist[pg] += prob_rand
        # If page has links
        if pg in corpus[page]:
            prob_dist[pg] += prob_link

    return prob_dist


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Initialize sample dictionary using dictionary comprehension, and set value of pages to zero
    samples = {pg: 0 for pg in corpus}

    # Variable to store damping factor value
    d = damping_factor

    # Select first page randomly
    current = random.choice(list(samples))
    samples[current] += 1

    for i in range(0, n - 1):
        # Call transition model function on first page
        trans_mod = transition_model(corpus, current, d)

        # Select next page
        next = random.random()
        # Variable to add probabilities
        probability = 0

        for item, value in trans_mod.items():
            probability += value
            if next <= probability:
                current = item
                break

        samples[current] += 1

    ranks = {pg: (sample_num / n) for pg, sample_num in samples.items()}

    return ranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    # Variables to store number of pages and calculation constant
    N = len(corpus)
    n = 1 / N

    # Variable to store damping factor value
    d = damping_factor

    # Random probability variable
    prob_rand = (1 - d) / N

    # Initialize page rank dictionary using dictionary comprehension, and set value of pages to 1 divided by number of pages
    pageranks = {pg: n for pg in corpus}

    # Initialize storage dictionary using dictionary comprehension, and set value of pages to None
    storage = {pg: None for pg in corpus}

    # Counter to count iterations
    counter = 0

    # Set variable tracking rank changes to 1 divided by number of pages
    tracker = n

    # Iterate until no changes greater than 0.001
    while tracker > 0.001:
        # Update counter
        counter += 1
        # Reset tracker
        tracker = 0

        # Loop over corpus
        for pg in corpus:
            # Changing probability variable
            probability = 0
            for pg_next in corpus:
                # Variable to store page links
                L = len(corpus[pg_next])
                # If next page has no links, select any page
                if L == 0:
                    probability += pageranks[pg_next] * n
                # If page has links, select any link
                elif pg in corpus[pg_next]:
                    probability += pageranks[pg_next] / L

            # Update new page rank
            update = prob_rand + (d * probability)
            storage[pg] = update

        # Normalize the ranks
        normalize = sum(storage.values())
        storage = {page: (rank / normalize) for page, rank in storage.items()}

        # Find maximum change
        for pg in corpus:
            change = abs(pageranks[pg] - storage[pg])
            if change > tracker:
                tracker = change

        # Update pageranks
        pageranks = storage.copy()

    return pageranks


if __name__ == "__main__":
    main()