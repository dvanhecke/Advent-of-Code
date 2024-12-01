# Advent of Code 2024 writeouts

## Day 1

### Part 1

Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances.

For this part of the challenges I first splitted the input in 2 lists representing each column and then sorted them in ascending order.

I went through each number in the columns and calculated the distance between them with this formila: `abs(x-y)`. All the distances are saved in another list which then gets the total sum calculated with the `sum()` function and immediately returns the output

### Part 2

This time, you'll need to figure out exactly how often each number from the left list appears in the right list. Calculate a total similarity score by adding up each number in the left list after multiplying it by the number of times that number appears in the right list.

For this part of the challenge I used the same setup of the previous part as in splitting the input in the two columns and then sorting them, after that I used the `count()` function to count the number of occurences in the **second column** for any number in the **first column**. After I get all the multiplacations done I used the same `sum()` function and returned the output.

