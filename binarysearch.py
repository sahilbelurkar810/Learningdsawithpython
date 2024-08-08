from jovian.pythondsa import evaluate_test_cases
def binary_search(cards, query):
    low, high = 0, len(cards) - 1
    while low <= high:
        mid = (low + high) // 2
        if cards[mid] == query:
            return mid
        elif cards[mid] < query:
            low = mid + 1
        else:
            high = mid - 1
    return -1

    return -1
tests = [
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':50}, 'output':4},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':110}, 'output':-1},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':10}, 'output':0},
    {'input':{'cards':[10, 20, 30, 40, 50, 60, 70, 80, 90, 100],'query':100}, 'output':9},
    {'input':{'cards':[5, 10, 15, 20, 25, 30, 35, 40, 45, 50],'query':25}, 'output':4},
    {'input':{'cards':[5, 10, 15, 20, 25, 30, 35, 40, 45, 50],'query':55}, 'output':-1},
    {'input':{'cards':[-10, -5, 0, 5, 10, 15, 20, 25, 30, 35],'query':0}, 'output':2},
    {'input':{'cards':[-10, -5, 0, 5, 10, 15, 20, 25, 30, 35],'query':-15}, 'output':-1},
    {'input':{'cards':[1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000],'query':5000}, 'output':4},
    {'input':{'cards':[],'query':50}, 'output':-1},
    {'input':{'cards':[50],'query':50}, 'output':0},
    {'input':{'cards':[50],'query':60}, 'output':-1},
]
evaluate_test_cases(binary_search,tests)