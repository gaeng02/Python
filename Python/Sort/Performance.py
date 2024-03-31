import time
import random

import "bubble_sort.py"
import "exchange_sort.py"
import "heap_sort.py"
import "insection_sort.py"
import "merge_sort.py"
import "quick_sort.py"
import "selection_sort.py"

# 1. Test Case Copy
# 2. Timer Start 
# 3. Function call
# 4. Print Result
# 5. Timer End
# 6. Append timer result

def Comparison_Sort (test_case: list) -> list : 

  measure_list = []
  
  test_list = test_case[:]
  
  start = time.time()
  bubble.sort(test_list)
  end = time.time()

  if (Check(test_case)) : measure_list.append(false)
  else : measure_list.append(end - start)


def Check (check_case: list) -> bool :
  
  size = 100
  for i in range (size) : 
    if (check_case[i] != answer[i]) : 
      return False

  return True

if (__name__ == "__main__") : 
  
  random_list = []
  insert_list = []
  reversed_list = []
  duplicated_list = []
  check_list = []
