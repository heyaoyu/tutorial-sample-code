#! /usr/bin/python

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def h_down2(arr, i, l):
  ele = arr[i]
  while 2*i+1<=l:
    child_index = 2*i+1
    child_ele = arr[child_index]
    if 2*i+2<=l and child_ele > arr[2*i+2]:
      child_index = 2*i+2
      child_ele = arr[child_index]
    if ele>child_ele:
      arr[i] = child_ele
      i = child_index
    else:
      break
  arr[i] = ele      

def h_down(arr, i, l):
  while 2*i+1 <= l:
    ele = arr[i]
    child_index = 2*i+1
    child_ele = arr[child_index]
    if 2*i+2 <= l and child_ele>arr[2*i+2]:
      child_index = 2*i+2
      child_ele = arr[child_index]
    if ele>child_ele:
      swap(arr, i, child_index)
      i = child_index
    else:
      break

def build_heap(arr):
  for i in range(len(arr)-1, -1, -1):
    h_down2(arr, i, len(arr)-1)

def hsort(arr):
  build_heap(arr)
  for i in range(0, len(arr)):
    swap(arr, 0, len(arr)-1-i)
    h_down2(arr, 0, len(arr)-2-i)

def q_recur(arr, start, end):
  if start>end:
    return
  mid_ele = arr[(start+end)/2]
  swap(arr, start, (start+end)/2)
  k = start
  for i in range(start+1, end+1):
    if arr[i]<mid_ele:
      swap(arr, i, k+1)
      k+=1
  swap(arr, start, k)
  q_recur(arr, start, k-1)
  q_recur(arr, k+1, end)

def qsort(arr):
  q_recur(arr, 0, len(arr)-1) 

def main():
  arr = [1,4,8,2,9,2,-7,42,31]
  print arr
  qsort(arr)
  print arr
  arr = [4,1,2,8,2,9,31,-7,42]
  print arr
  qsort(arr)
  print arr
  arr = [4,1,2,8,2,9,31,-7,42]
  print arr
  hsort(arr)
  print arr

if __name__=='__main__':
  main()
