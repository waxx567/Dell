#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
} candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // TODO

    // Iterates through candidate struct
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        // Confirms candidate name
        if (strcmp(name, candidates[i].name) == 0)
        {
            // Adds one vote to that candidate's name
            candidates[i].votes++;
            return true;
        }
    }
    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // TODO

    // Declares variables
    string winner;
    string draw;
    int most_votes = 0;
    int draw_votes = 0;

    // Iterates through candidate struct
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        // Finds candidate with highest number of votes
        if (candidates[i].votes > most_votes)
        {
            // Assigns name and amount of votes to variables
            winner = candidates[i].name;
            most_votes = candidates[i].votes;
        }
    }
    // Iterates through candidate struct for draw
    for (int i = 0, n = candidate_count; i < n; i++)
    {
        // Assigns draw to variables
        if (candidates[i].votes == most_votes)
        {
            draw = candidates[i].name;
            draw_votes = candidates[i].votes;
        }
    }
    // Ensures winner and draw are not the same
    if (strcmp(winner, draw) != 0)
    {
        printf("%s\n", winner);
        printf("%s\n", draw);
    }
    else
    {
        printf("%s\n", winner);
    }
    return;
}