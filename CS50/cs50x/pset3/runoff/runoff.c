#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
} candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    // TODO
    // Loop through candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // Compare to array of valid candidate names
        if ((strcmp(candidates[i].name, name)) == 0)
        {
            // If valid
            // Update preferences array to indicate voter's choice of candidate
            preferences[voter][rank] = i;
            return true;
        }
    }
    // If invalid
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    // TODO
    // Loop through voters
    for (int i = 0; i < voter_count; i++)
    {
        // Loop through candidates
        for (int j = 0; j < candidate_count; j++)
        {
            // If candidate has not been eliminated
            if (!candidates[preferences[i][j]].eliminated)
            {
                // Update vote count for candidate
                candidates[preferences[i][j]].votes += 1;
                break;
            }
        }
    }
    // Exit the function
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    // TODO
    // Determine who has the most votes
    int most = (voter_count / 2 + 1);
    // Loop through candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // If the candidate has more votes, candidate is the winner
        // Print candidate's name
        if (candidates[i].votes >= most)
        {
            printf("%s", candidates[i].name);
            return true;
        }
    }
    // Candidate is not the winner
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    // Determine who has the least votes
    int least = INT_MAX;

    // Loop through candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate has not been eliminated and has fewer votes, this candidate has the least votes
        // Update the variable
        if (!candidates[i].eliminated && candidates[i].votes < least)
        {
            least = candidates[i].votes;
        }
    }
    // Return the updated variable
    return least;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    // Variables to store values
    int still_in = 0;
    int least_votes = 0;

    // Loop through candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // If the candidate has not been eliminated
        if (!candidates[i].eliminated)
        {
            // Update the variable
            still_in += 1;

            // If candidate has the least votes, update the variable
            if (candidates[i].votes == min)
            {
                least_votes = candidates[i].votes;
            }
        }
    }

    // If the candidates who are still in all have the same number of votes
    if (still_in == least_votes)
    {
        return true;
    }
    // If not
    return false;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    // Loop through candidates
    for (int i = 0; i < candidate_count; i++)
    {
        // If candidate has not been eliminated and has the least votes, update the candidate status
        if (!candidates[i].eliminated && candidates[i].votes == min)
        {
            candidates[i].eliminated = true;
        }
    }
    // Exit the function
    return;
}