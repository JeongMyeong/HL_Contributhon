## Sorting Algorithm 만들기
## 첫번째 기여자 10점
## 매 성능 향상시 2점
import timeit

def sort(collection):
  """최고의 성능을 가진 정렬 알고리즘을 만들어 보세요 ! """
  ARRAY_LENGTH = len(collection)
  if (ARRAY_LENGTH <= 1):
      return collection
  else:
      PIVOT = collection[0]
      GREATER = [element for element in collection[1:] if element > PIVOT]
      LESSER = [element for element in collection[1:] if element <= PIVOT]
      return sort(LESSER) + [PIVOT] + sort(GREATER)
  return collection

# 메인 함수
collection = [100, 99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

start = timeit.default_timer()
collection = sort(collection)
stop = timeit.default_timer()
print(stop - start)
print(collection)

# 나의 수행 시간
# 0.0003475579997029854
