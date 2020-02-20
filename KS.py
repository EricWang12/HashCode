  
# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W , wt , val , n): 
  
    # Base Case 
    if n == 0 or W == 0 : 
        return 0
  
    # If weight of the nth item is more than Knapsack of capacity 
    # W, then this item cannot be included in the optimal solution 
    if (wt[n-1] > W): 
        return knapSack(W , wt , val , n-1) 
  
    # return the maximum of two cases: 
    # (1) nth item included 
    # (2) not included 
    else: 
        return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
                   knapSack(W , wt , val , n-1)) 
  
# end of function knapSack 
  
class Library:
    def __init__(self, books, signupDate,booksPerDay):
        self.books = books
        self.signupDate = signupDate
        self.booksPerDay = booksPerDay



def readFile(fileName):

    Libraries = list()
    with open(fileName) as f:
        a, b, totalDays = [int(x) for x in next(f).split()]
        bookValue = [int(x) for x in next(f).split()]
        line = f.readline()
        while line:
            bookNum, signupDate, booksPerDay = next(f).split()
            line = next(f)
            books = [int(x) for x in line.split()]
            Libraries.append(Library(books, signupDate, booksPerDay))
    return bookValue, totalDays, Libraries 


# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print (readFile('a_example.txt')) 
  