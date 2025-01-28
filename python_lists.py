#Problem 1
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #the list of positive integers
nums.append(11) #appends 11 to the list
print(nums) #will output the updated list with 11 added
nums.remove(5) #removes 5 from the list
print(nums) #will output the updated list with 5 removed
nums.reverse() #reverses the order of the list
print(nums) #outputs the reversed list

#Problem 2
nums_2 = [12, 14, 16, 18, 20]
print(max(nums_2)) #outputs the maximum number in the list
print(min(nums_2)) #outputs the minimum number in the list
avg = sum(nums_2) / len(nums_2) #calcuates the average of the list.
# ^^ The formula is the sum of all the list's values, sum(), divided by the number of values in the list, len()
print(avg) #outputs the average of nums_2