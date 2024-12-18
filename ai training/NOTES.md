[Instructions]( https://docs.google.com/document/d/e/2PACX-1vQoF7-yQn8Hvd_H1PnxDz4YMgjoEbaelgbbUivY7saWoubjPBSskQnO-EW-Ih9PEKUxzQuDYMhL1ZSC/pub)

🧠 Concept: What is a user prompt?

A user prompt is a coding question or problem that guides the AI on what to say and how to say it. Prompts should reflect real-world questions a user would ask a chatbot to help them with a coding-related problem/ask. A good prompt has these elements:

Clear about what the response is asking for:
What it is: The background or main topic that tells the model what the response should answer.
The prompt should follow the language, locale, and topic assigned in the task.

Solvable:
Avoid problems that don't contain the information necessary to solve them.
Avoid problems containing terms or concepts unrelated to coding.

Example:
I work in the sales division, and we want to show our client a demo of the IoT solution we provide for injecting modeling machines. Since this is a demo, we will not use real data from sensors and use synthetic data instead.
Create an API endpoint that generates the following values using Flask:
- 5 temperature values ranging from 0 - 90, changing values every 5 seconds and then repeating.
- 5 pressure values ranging from 100 - 200, , changing values every 10 seconds and then repeating..
- 3 injecting time values ranging from 0.2 - 1.5 , changing values every 3 seconds and then repeating.
Using the Dash library, create a dashboard to visualize the values outputted from the API in card style.
Create a separate card for each data type:
- Display temperature as a thermometer chart.
- Pressure as a guage chart.
- Injecting time as plain text.
To guarantee a running demo, don't use deprecated libraries such as "dash_html_components" and make sure the dashboard components are not overlapping.

TOPIC
	What does the assigned topic mean for you? 🤔
Your assigned topic tells you exactly what kind of prompt to create. It's super important to stick to your assigned topic and make sure your prompt clearly aligns with it.

Here's a quick guide:

Code Generation: Ask for a code solution to a specific problem.
Problem Reflection: Ask for analysis and breakdown of a problem.
Tests Reasoning: Ask for explanations of test case results.
Code Refactoring: Ask for improvements to given code.
Bug Fixing: Ask for corrections to broken code.
Test Generation: Ask for creation of test cases.
Solution Reasoning: Ask for analysis of a working solution.

Get ready to explore each topic in detail! The following pages will provide:

Clear definitions of each topic 📖
Helpful guidelines for writing great prompts ✍️
Example prompts to inspire you (but don't copy them. This is critical to the project and your progression with the same. We want to hear your original thoughts and contributions!) 😉

1. Code Generation 💻
Definition: These prompts require the model to generate code in a specific programming language to solve a well-defined problem or implement a particular algorithm. The prompt should clearly specify the desired functionality, inputs, outputs, and any constraints (e.g., performance requirements, coding style). The goal is to produce code that is correct, efficient, and adheres to the given specifications.


What it means: You're asking the AI to write code that does something specific! 🤖 Think of it as giving the AI a coding challenge. 🦾 Be clear about what you want the code to do, what language it should be in, and any special instructions.

What it does NOT mean: This is not about analyzing existing code or explaining how code works. 🙅‍♀️ It's about creating brand new code from scratch. ✨
Guidelines for writing a good prompt:
Clearly state the problem: What should the code accomplish? 🤔
Specify the programming language: (e.g., Python, Java, C++) 🔤
Define inputs and outputs: What data should the code take in and what should it produce? ➡️ ⬅️
Include constraints: Are there any performance requirements, specific libraries to use, or coding style guidelines? ⚠️
Provide examples if helpful: Illustrate the desired behavior with input-output examples. 💡
Examples of a good prompt 🤓

"Generate Python code for a program that simulates a basic banking system. The program should allow users to create new accounts, deposit and withdraw funds, and check their account balance. Ensure the code includes error handling for invalid inputs (e.g., negative deposit amounts) and uses appropriate data structures to store account information. The code should be well-documented with comments explaining the functionality of each part."

"Implement a graph traversal algorithm in Java that identifies the shortest path between two nodes in a weighted, directed acyclic graph. The graph can be represented using an adjacency list. The algorithm should have a time complexity of O(V+E), where V is the number of vertices and E is the number of edges. Include a main method that demonstrates the usage of the algorithm with a sample graph and two nodes."

2. Problem Reflection 🤔
Definition: These prompts challenge the model to analyze a problem or scenario from multiple angles. The model should break down the problem into its key components, consider different approaches or solutions, and evaluate their potential strengths and weaknesses. The focus is on critical thinking, problem-solving, and exploring various perspectives.

What it means: You're asking the AI to think deeply about a problem and how to solve it. 🧠 Encourage the AI to consider different angles, possible solutions, and the pros and cons of each. ⚖️

What it does NOT mean: This is not about writing code or providing a single "correct" answer. 🙅‍♂️ It's about exploring the problem space and demonstrating understanding. 🗺️
Guidelines for writing a good prompt:
Clearly define the problem: What is the challenge or scenario? 🤔
Encourage critical thinking: Ask "why" and "how" questions. ❓
Prompt for multiple perspectives: Ask the AI to consider different approaches or solutions. 🔄
Focus on analysis and evaluation: Ask the AI to compare and contrast different methods or ideas. 🆚
Examples of a good prompt 🤓

"Analyze the challenges of implementing a concurrent system with multiple threads accessing shared resources. Discuss potential issues like race conditions and deadlocks. Explore different synchronization mechanisms (e.g., mutexes, semaphores) and their trade-offs in terms of complexity and performance. How can these mechanisms be used to ensure data integrity and prevent concurrency-related bugs?"

"Consider the problem of designing an efficient caching system for a web application. What are the key factors to consider when choosing a caching strategy (e.g., eviction policies, cache size, consistency)? Discuss the advantages and disadvantages of different caching techniques, such as LRU (Least Recently Used), FIFO (First-In, First-Out), and LFU (Least Frequently Used). How can you measure the effectiveness of a caching system?"

3. Tests Reasoning 🧪
Definition: These prompts present the model with specific test cases (input-output pairs) and require it to explain the reasoning behind the observed results. The model should analyze the code or algorithm's behavior, identify edge cases, and demonstrate an understanding of the underlying logic and constraints. The goal is to assess the model's ability to interpret and justify test outcomes.

What it means: You're giving the AI some test results and asking it to explain why those results happened. 🤔 This helps you see if the AI understands how the code works and can reason about its behavior. 🧠

What it does NOT mean: This is not about generating code or fixing bugs. 🙅‍♂️ It's about analyzing and explaining existing test results. 📊
Guidelines for writing a good prompt:
Provide clear test cases: Include specific inputs and their corresponding outputs. ➡️ ⬅️
Ask for explanations: Use prompts like "Explain why..." or "Justify the output..." 🤔
Focus on reasoning and logic: Encourage the AI to demonstrate its understanding of the code or algorithm. 💡
Consider edge cases: Include test cases that cover unusual or unexpected situations. ⚠️
Examples of a good prompt 🤓

"You are given a function that implements a binary search algorithm on a sorted array. The following test cases are provided:

Input array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], Target value: 23, Output: 5 (index of the target value)
Input array: [2, 5, 8, 12, 16, 23, 38, 56, 72, 91], Target value: 4, Output: -1 (target value not found)
Input array: [1], Target value: 1, Output: 0
Explain why the binary search algorithm produces these outputs for each of the given test cases. How does the algorithm handle cases where the target value is not present in the array? What is the time complexity of binary search and why is it efficient for searching sorted data?"

"Consider a machine learning model trained to classify images of cars and bikes. You are given the following test images and the model's predictions:

Image 1: A clear picture of a car, Prediction: car (correct)
Image 2: A blurry picture of a bike, Prediction: bike (correct)
Image 3: A picture of a car surrounded by bikes, Prediction: bike (incorrect)
Analyze the model's predictions and explain why it might have misclassified the image of the car with a bike. What factors could be influencing the model's decision? How can you improve the model's accuracy in such cases?"

4. Code Refactoring 🛠️
Definition: These prompts provide the model with existing code that needs improvement. The prompt should specify the desired changes, such as enhancing readability, adding documentation, optimizing for performance, or restructuring for better maintainability. The goal is to assess the model's ability to apply coding best practices and improve code quality.

What it means: You're giving the AI some code and asking it to make it better! ✨ This could involve making it easier to read, 📖 adding helpful comments, 📝 making it run faster, 🚀 or organizing it more logically. 🏗️

What it does NOT mean: This is not about fixing broken code (that's Bug Fixing). 🙅‍♀️ The code you provide should already work, but it might be messy or inefficient. 😥
Guidelines for writing a good prompt:
Provide the code to be refactored: Make sure the code is complete and runnable. ✅
Specify the desired improvements: Be clear about what aspects of the code need to be changed (e.g., "improve readability," "add documentation," "optimize for performance"). 🎯
Consider coding standards: If applicable, mention specific coding style guidelines (e.g., PEP 8 for Python). 📏
Examples of a good prompt 🤓


Example 1+++++++++++++++++

"Refactor the following Java code that calculates the area of different geometric shapes. The code currently uses a long series of if-else statements to determine the shape type. Improve the code by using polymorphism and abstract classes or interfaces to represent different shapes. Ensure the refactored code is more maintainable, extensible, and adheres to object-oriented design principles."
// Existing code to be refactored
public class AreaCalculator {
    public double calculateArea(String shapeType, double… dimensions) {
        if (shapeType.equals(“circle”))
            // Calculate area of circle
        } else if (shapeType.equals(“rectangle”)) {
            // Calculate area of rectangle
        } else if (shapeType.equals(“triangle”)) {
            // Calculate area of triangle
        } // … more else-if statements for other shapes
        return 0; 
    }
}


Example 2++++++++++++++++
“You are given Python code that implements a simple web server using sockets. The code works correctly but lacks proper error handling and logging. Refactor the code to include robust error handling for potential exceptions, such as network errors and invalid requests. Add logging statements to record important events, like client connections, requests, and errors. Ensure the refactored code is more reliable and easier to debug.”
def longest_common_subsequence(str1, str2):
  “”"
  Finds the longest common subsequence of two strings (BUGGY!).
  Args:
    str1: The first string.
    str2: The second string.
  Returns:
    The longest common subsequence as a string.
  “”"
  m = len(str1)
  n = len(str2)
  # Initialize a 2D array INCORRECTLY (should be (m+1) x (n+1))
  dp = [[0] * n for _ in range(m)] 
  for i in range(1, m + 1):
    for j in range(1, n + 1):
      if str1[i-1] == str2[j-1]: 
        dp[i][j] = dp[i-1][j-1] + 1  # IndexError due to incorrect initialization
      else:
        dp[i][j] = max(dp[i-1][j], dp[i][j-1])  # IndexError here as well
  # Backtracking with the same bug as before
  i = m
  j = n
  lcs = “”
  while i > 0 and j > 0:
    if str1[i-1] == str2[j-1]:
      lcs = str1[i-1] + lcs
      i -= 1
      j -= 1
    else:
      if dp[i-1][j] > dp[i][j-1]:  # Incorrect comparison
        i -= 1
      else:
        j -= 1
  return lcs

5. Bug Fixing 🐛
Definition: These prompts present the model with code that contains errors or does not function as intended. The prompt may include error messages, stack traces, or descriptions of the observed problems. The model should analyze the code, identify the root cause of the errors, and provide a corrected version. The goal is to assess the model's ability to debug and repair code.

What it means: You're giving the AI some broken code and asking it to fix it! 🔨 This is like being a code detective 🕵️‍♀️ – the AI needs to find the errors and make the code work correctly. ✅

What it does NOT mean: This is not about improving working code (that's Code Refactoring). 🙅‍♂️ The code you provide should have specific errors that need to be resolved. 🚫
Guidelines for writing a good prompt:
Provide the buggy code: Make sure the code is complete and clearly shows the error. ❌
Describe the problem: Explain what's going wrong with the code (e.g., "it's throwing an error," "it's producing the wrong output"). ⚠️
Include error messages or stack traces if available: This can help the AI pinpoint the issue. 📍
Examples of a good prompt 🤓

Example 1 +++++++++++++++
"A Java program that implements a multithreaded chat application is experiencing intermittent crashes. The crashes seem to occur randomly when multiple users are sending messages simultaneously. Analyze the code and identify the potential race conditions or synchronization issues that might be causing these crashes. Provide a corrected version of the code that addresses these concurrency problems and ensures thread safety."

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;
import java.util.ArrayList;
import java.util.List;
public class ChatServer {
  private List<PrintWriter> clientWriters = new ArrayList<>();
  public void start(int port) throws IOException {
    ServerSocket serverSocket = new ServerSocket(port);
    System.out.println("Chat server started on port " + port);
    while (true) {
      Socket clientSocket = serverSocket.accept();
      System.out.println("New client connected");
      // BUG: No synchronization when accessing shared clientWriters list
      clientWriters.add(new PrintWriter(clientSocket.getOutputStream(), true)); 
      Thread clientThread = new Thread(() -> {
        try {
          BufferedReader reader = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
          String message;
          while ((message = reader.readLine()) != null) {
            // BUG: No synchronization when accessing shared clientWriters list
            for (PrintWriter writer : clientWriters) { 
              writer.println(message);
            }
          }
        } catch (IOException e) {
          System.err.println("Error handling client: " + e.getMessage());
        }
      });
      clientThread.start();
    }
  }
  public static void main(String[] args) throws IOException {
    ChatServer server = new ChatServer();
    server.start(8080);
  }
}


Example 2+++++++++++++++++
"This Python code is supposed to find the longest common subsequence of two strings, but it's returning incorrect results for some inputs. Debug the code and identify the source of the error. Provide a corrected version of the code that produces the correct output for all valid input strings. Explain the bug you fixed and how your correction addresses the issue."

def longest_common_subsequence(str1, str2):
 """
 Finds the longest common subsequence of two strings (BUGGY!).
 Args:
  str1: The first string.
  str2: The second string.
 Returns:
  The longest common subsequence as a string.
 “”"
 m = len(str1)
 n = len(str2)
 # Initialize a 2D array with INCORRECT dimensions
 dp = [[0] * n for _ in range(m)]  
 for i in range(m): # Looping up to m instead of m+1
  for j in range(n): # Looping up to n instead of n+1
   if str1[i] == str2[j]: # Comparing characters at incorrect indices
    dp[i][j] = dp[i-1][j-1] + 1 # Potential IndexError due to incorrect loop bounds
   else:
    dp[i][j] = max(dp[i-1][j], dp[i][j-1]) # Potential IndexError here as well
 # Backtracking with incorrect indices and logic
 i = m - 1  
 j = n - 1
 lcs = “”
 while i >= 0 and j >= 0: # Incorrect loop condition
  if str1[i] == str2[j]: # Comparing characters at incorrect indices
   lcs = str1[i] + lcs
   i -= 1
   j -= 1
  else:
   if dp[i-1][j] > dp[i][j-1]: # Incorrect comparison and potential IndexError
    i -= 1
   else:
    j -= 1
 return lcs

6. Test Generation ✅
Definition: These prompts require the model to create test cases for a given code snippet, function, or program. The generated tests should cover various scenarios, including normal cases, edge cases, and potential error conditions. The goal is to assess the model's ability to design tests that effectively validate the functionality and robustness of the code.

What it means: You're asking the AI to create tests that check if some code is working correctly. ✅ This is like creating a challenge for the code to pass 💪 – the AI needs to come up with different scenarios to make sure the code handles them all correctly. 💯

What it does NOT mean: This is not about explaining existing test results (that's Tests Reasoning). 🙅‍♀️ It's about creating new tests from scratch. 🧪

Guidelines for writing a good prompt:
Provide the code to be tested: Make sure the code is complete and runnable. 🏃‍♂️
Specify the type of tests: Mention if you want unit tests, integration tests, or other specific types. 📝
Consider test coverage: Encourage the AI to create tests that cover a wide range of scenarios. 🌎
Examples of a good prompt 🤓


"Write a comprehensive set of unit tests in Python for a function that validates email addresses. The function should check for the presence of the @ symbol, a valid domain name, and optional top-level domain. The tests should cover various scenarios, including valid email formats, invalid formats (missing @, invalid characters, etc.), and edge cases (e.g., very long email addresses, unusual domain names). Aim for high test coverage to ensure the email validation function works reliably."



"Generate test cases for a C++ program that controls a robotic arm in a manufacturing environment. The program receives commands to move the arm to specific coordinates and perform actions like gripping and releasing objects. The test cases should cover a range of scenarios, including valid movement commands, invalid commands (e.g., out-of-bounds coordinates), and sequences of commands that test the robot's ability to perform complex tasks. Consider edge cases like obstacle avoidance and error handling for unexpected situations."

7. Solution Reasoning 💡
Definition: These prompts provide the model with a solution or algorithm and ask it to explain how it works and analyze its properties. The model should discuss the solution's logic, correctness, efficiency, and limitations. The goal is to assess the model's ability to understand and evaluate existing solutions.

What it means: You're giving the AI a solution and asking it to explain how it works ⚙️ and why it's a good (or not-so-good) solution. 🤔 This helps you see if the AI truly understands the solution and can analyze its strengths and weaknesses. 💪 🤕

What it does NOT mean: This is not about generating code or fixing bugs. 🙅‍♂️ It's about understanding and evaluating an existing solution. 🧐

Guidelines for writing a good prompt:
Provide the solution or algorithm: Make sure it's complete and understandable. ✅
Ask for a clear explanation: Encourage the AI to break down the solution step-by-step. 👣
Prompt for analysis: Ask about the solution's efficiency, correctness, limitations, and potential improvements. 🤔
Examples of a good prompt 🤓




"You are given a JavaScript implementation of a sorting algorithm called Merge Sort. Explain step-by-step how this algorithm works to sort an array of numbers. Analyze its time and space complexity in comparison to other sorting algorithms, such as Bubble Sort and Quick Sort. Discuss the advantages and disadvantages of Merge Sort, including its suitability for different types of data and use cases."

function mergeSort(arr) {
 if (arr.length <= 1) {
  return arr; 
 }
 const mid = Math.floor(arr.length / 2);
 const left = arr.slice(0, mid);
 const right = arr.slice(mid);
 return merge(mergeSort(left), mergeSort(right));
}
function merge(left, right) {
 let result = [];
 let leftIndex = 0;
 let rightIndex = 0;
 while (leftIndex < left.length && rightIndex < right.length) {
  if (left[leftIndex] < right[rightIndex]) {
   result.push(left[leftIndex]);
   leftIndex++;
  } else {
   result.push(right[rightIndex]);
   rightIndex++;
  }
 }
 return result.concat(left.slice(leftIndex)).concat(right.slice(rightIndex));
}
// Example usage:
const unsortedArray = [5, 2, 4, 6, 1, 3];
const sortedArray = mergeSort(unsortedArray);
console.log(sortedArray); // Output: [1, 2, 3, 4, 5, 6]


Example 2 ++++++++++++++++++++
“Analyze the following C# code that implements a data structure called a Trie. Explain how this data structure efficiently stores and retrieves a large collection of strings. Discuss its use cases, such as autocomplete functionality and spell checking. Compare the performance of a Trie with other data structures, like hash tables and balanced trees, for storing and searching strings. What are the strengths and weaknesses of using a Trie in different scenarios?”

public class TrieNode
{
  public char Value { get; set; }
  public bool IsEndOfWord { get; set; }
  public Dictionary<char, TrieNode> Children { get; set; }
  public TrieNode(char value)
  {

    Value = value;
    IsEndOfWord = false;
    Children = new Dictionary<char, TrieNode>();
  }
}
public class Trie

{
  private TrieNode root;
  public Trie()
  {
    root = new TrieNode(‘\0’); // Root node with null character
  }
  public void Insert(string word)
  {
    TrieNode currentNode = root;
    foreach (char c in word)
    {
      if (!currentNode.Children.ContainsKey©)
      {
        currentNode.Children.Add(c, new TrieNode©);
      }
      currentNode = currentNode.Children[c];
    }
    currentNode.IsEndOfWord = true;
  }
  public bool Search(string word)
  {
    TrieNode currentNode = root;
    foreach (char c in word)
    {
      if (!currentNode.Children.ContainsKey©)
      {
        return false;
      }
      currentNode = currentNode.Children[c];
    }
    return currentNode.IsEndOfWord;
  }
}
// Example usage:
Trie trie = new Trie();
trie.Insert(“apple”);
trie.Insert(“app”);
trie.Insert(“banana”);
Console.WriteLine(trie.Search(“apple”)); // Output: True
Console.WriteLine(trie.Search(“app”));   // Output: True
Console.WriteLine(trie.Search(“ban”));   // Output: False

⚠️ Key Differences and Pitfalls
Not all topics require code output: Keep in mind that some topics (Problem Reflection, Tests Reasoning, Solution Reasoning) might not ask for code as a direct answer, but they still require coding knowledge to evaluate the response.
Code Refactoring vs. Bug Fixing: In Code Refactoring, the input code works but might be inefficient or poorly written. In Bug Fixing, the input code is broken and needs to be corrected.
Test Reasoning vs. Solution Reasoning: Test Reasoning focuses on explaining why specific test inputs produce specific outputs. Solution Reasoning focuses on explaining how a solution works as a whole.
Other important points:

Be clear and concise: Use precise language and avoid ambiguity.
Provide context: Give the model enough information to understand the task.
Avoid bias: Ensure your prompts are neutral and objective.
Follow instructions carefully: Pay close attention to the assigned topic and any specific requirements.
