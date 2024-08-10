from jovian.pythondsa import evaluate_test_cases
from jovian.pythondsa import evaluate_test_case
def test_location(cards, query, mid):
    mid_number = cards[mid]
    # print("mid", mid, "midnumber", mid_number)
    if mid_number == query:
        if mid == 0 or cards[mid-1] != query:
            return 'found'
        else:
            return 'left'
    elif mid_number < query:
        return 'right'
    else:
        return 'left'

def locate_card(cards, query):
    if not cards:
        return -1
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        result = test_location(cards, query, mid)
        if result == 'found':
            return mid
        elif result == 'right':
            low = mid + 1
        elif result == 'left':
            high = mid - 1
    return -1

tests = [
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':50}, 'output':4},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':110}, 'output':-1},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':10}, 'output':0},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':100}, 'output':9},
    {'input':{'cards':[5, 10, 15, 20, 25, 30, 35, 40, 45, 50],'query':25}, 'output':4},
    {'input':{'cards':[5, 10, 15, 20, 25, 30, 35, 40, 45, 50],'query':55}, 'output':-1},
    {'input':{'cards':[-10, -5, 0, 5, 10, 15, 20, 25, 30, 35],'query':0}, 'output':2},
    {'input':{'cards':[-10, -5, 0, 5, 5, 15, 20, 25, 30, 35],'query':5}, 'output':3},
    {'input':{'cards':[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],'query':5000}, 'output':4},
    {'input':{'cards':[],'query':50}, 'output':-1},
    {'input':{'cards':[50],'query':50}, 'output':0},
    {'input':{'cards':[50],'query':60}, 'output':-1},
    
]
test = {'input':{'cards':list(range(1000000,0,-1)),'query':2},'output':9999998}
result,passed,runtime = evaluate_test_case(locate_card, test,display=False)
print("result: {}\nPassed:{}\nExecutiontime: {} ms".format(result,passed,runtime))