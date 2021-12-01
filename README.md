<h1 align="center">
    Fairfield College Preparatory School<br>
    Computer Programming - Mr. Mesquita<br>
    HW 8-2
</h1>

<h2 align="center">Due before 8:30 AM on 12/10 (20 pts.)</h2>

### For Loops
---
Answer each of the following questions in a separate Python file named `hw8-2-#.py` where `#` is the number of the question. In your heading, put your name and the date you began working on the file.

1. Write a function called `count_odds` that takes a list and uses a for loop to count how many odd numbers are in the list. The program should return `True` for each of the following tests:
    ```python
    count_odds([1, 2, 3, 4, 5, 6]) == 3
    count_odds([1, 3, 5, 7, 9]) == 0
    count_odds([2, 4, 6, 8, 10]) == 5
    ```

2. Write a function called `sum_odds` that takes a list and uses a for loop to find the sum of all of the odd numbers in the list. The program should return `True` for each of the following tests:
    ```python
    sum_odds([1, 2, 3, 4, 5, 6]) == 9
    sum_odds([1, 3, 5, 7, 9]) == 25
    sum_odds([2, 4, 6, 8, 10]) == 0
    ```

3. Write a function called `three_letter_words` that takes a list of words and uses a for loop to count the number of three letter words that are in the list of words. The program should return `True` for each of the following tests:
    ```python
    three_letter_words(["cat", "bat", "apple"]) == 2
    three_letter_words(["apple", "hippo", "mouse"]) == 0
    three_letter_words(["hop", "pop", "bop"]) == 3
    ```

4. Write a function that takes a word and a letter and counts how many times a letter appears in a word. The program should return `True` for each of the following tests. Be sure to replace `your_function_name` with a name valid function name that better describes the function:
    ```python
    your_function_name("cat", "t") == 1
    your_function_name("apple", "p") == 2
    your_function_name("supercalifragilisticexpialidocious", "i") == 7
    ```

5. Write a function that takes a list and sums up all the elements in the list up to but not including the first odd number. Make sure the function can handle if there are no odd numbers in the list. The program should return `True` for each of the following testsBe sure to replace `your_function_name` with a name valid function name that better describes the function:
    ```python
    your_function_name([2, 4, 6, 8, 9]) == 20
    your_function_name([13, 12, 10]) == 0
    your_function_name([14, 16, 32]) == 62
    ```

<p align="center">Be sure to commit your code before the deadline. Only the latest commit will be graded.</p>
