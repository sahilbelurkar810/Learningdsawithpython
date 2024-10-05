# from jovian.pythondsa import evaluate_test_cases
# first = 0
# last = 0
# def test_location(cards,query,mid,hi):
#     global first, last
#     mid_number = cards[mid]
#     if mid_number == query:
#         if mid-1 >=0 and cards[mid-1]==query:
#             last= mid
#             first = mid-1
#             return 'left'
#         if mid+1 <= hi  and cards[mid+1]==query:
#             print("im last",mid+1)
#             last= mid+1
#             first = mid
#             if(mid+1==hi):
#                 print("i was hit")
#                 return "found"
#             return 'right'
#         else:
#             return 'found'
#     elif mid_number < query:
#         return 'right'
#     else:
#         return 'left'

# def locate_card(cards,query):
#     lo,hi=0,len(cards)-1

#     while lo <= hi:
#         mid = (lo+hi)//2
#         # print("lo",lo,"hi",hi,"mid",mid)
#         # mid_number=cards[mid]
#         result=test_location(cards,query,mid,hi)
#         if result == 'found':
#             return mid
#         elif result == 'right':
#             lo = mid+1
#         elif result == 'left':
#             hi = mid-1
#         elif result == 'special':
#             lo = mid+2
#     return -1
# def ans():
#     return([first,last])
# tests = [
#     {'input':{'cards':[10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100],'query':50}, 'output':4},
#     {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100,100],'query':100}, 'output':9},
#     {'input':{'cards':[5,7,7,8,8,10],'query':8},'output':3},
# ]
# evaluate_test_cases(locate_card,tests)
# result = ans()
# print(result)

first = 0
last = 0
def test_location(cards,query,mid,hi):
    global first, last
    mid_number = cards[mid]
    if mid_number == query:
        if mid-1 >=0 and cards[mid-1]==query:
            last= mid
            first = mid-1
            return 'left'
        if mid+1 <= hi  and cards[mid+1]==query:
            print("im last",mid+1)
            last= mid+1
            first = mid
            if(mid+1==hi):
                print("i was hit")
                return "found"
            return 'right'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    else:
        return 'left'

def searchRange( nums, target) :
    lo,hi=0,len(nums)-1

    while lo <= hi:
        mid = (lo+hi)//2
        # print("lo",lo,"hi",hi,"mid",mid)
        # mid_number=cards[mid]
        result=test_location(nums,target,mid,hi)
        if result == 'found':
            return ([first,last])
        elif result == 'right':
            lo = mid+1
        elif result == 'left':
            hi = mid-1
        elif result == 'special':
            lo = mid+2
    return ([-1,-1])
number = [1]
results = searchRange(number,1)
print(results)
