# # # 1.Complete the solution so that it splits the string into pairs of two characters. If the string contains an odd number of characters then it should replace the missing second character of the final pair with an underscore ('_').

# # # Examples:

# # # * 'abc' =>  ['ab', 'c_']
# # # * 'abcdef' => ['ab', 'cd', 'ef']


# # # def solution(s):
# # #     n = 2
# # #     if len(s)%2==0:
# # #         return [s[i:i+n] for i in range(0, len(s), n)]
# # #     else:
# # #         first=[s[i:i+n] for i in range(0, len(s)-1, n)]
# # #         first.append(s[len(s)-1]+'_')
        
# # #         return first
        
        
# # # 2.Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

# # # It should remove all values from list a, which are present in list b keeping their order.

# # # array_diff([1,2],[1]) == [2]
# # # If a value is present in b, all of its occurrences must be removed from the other:

# # # array_diff([1,2,2,2,3],[2]) == [1,3]


# # # def array_diff(a, b):
# # #     return [item for item in a if item not in b]
    
# # # 3. You live in the city of Cartesia where all roads are laid out in a perfect grid. You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, so create a function that will return true if the walk the app gives you will take you exactly ten minutes (you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

# # # Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). It will never give you an empty array (that's not a walk, that's standing still!).


# # # def isValidWalk(walk):
# # #     return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')



# # 4. Jamie is a programmer, and James' girlfriend. She likes diamonds, and wants a diamond string from James. Since James doesn't know how to make this happen, he needs your help.

# # Task
# # You need to return a string that looks like a diamond shape when printed on the screen, using asterisk (*) characters. Trailing spaces should be removed, and every line must be terminated with a newline character (\n).

# # Return null/nil/None/... if the input is an even number or negative, as it is not possible to print a diamond of even or negative size.

# # Examples
# # A size 3 diamond:

# #  *
# # ***
# #  *
# # ...which would appear as a string of " *\n***\n *\n"

# # A size 5 diamond:

# #   *
# #  ***
# # *****
# #  ***
# #   *
# # ...that is:

# # "  *\n ***\n*****\n ***\n  *\n"



# # def diamond(n):
  
# #     if n<1 or n%2==0:
# #         return None
# #     if n==1:
# #         return "*\n"
# #     if n>=1 and n%2!=0:
# #         result, spaces = [], 0
# #         for stars in range(n, -1, -2):
# #             result.append(' ' * spaces + '*' * stars + '\n')
# #             spaces+=1
# #         result = result[::-1][:-1] + result
# #         return ''.join(result)

# You are a khmmadkhm scientist and you decided to play with electron distribution among atom's shells. You know that basic idea of electron distribution is that electrons should fill a shell untill it's holding the maximum number of electrons.

# Rules:

# Maximum number of electrons in a shell is distributed with a rule of 2n^2 (n being position of a shell).
# For example, maximum number of electrons in 3rd shield is 2*3^2 = 18.
# Electrons should fill the lowest level shell first.
# If the electrons have completely filled the lowest level shell, the other unoccupied electrons will fill the higher level shell and so on.


# def atomic_number(e):
#     arr=[]
#     sum=0
#     n=1

#     while sum<e:
        
#         a=2*n**2
#         if sum+a>e:a=e-sum
#         arr.append(a)
#         sum+=a
#         n+=1
#     return arr
        
