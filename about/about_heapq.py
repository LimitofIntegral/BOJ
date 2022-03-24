"""

    파이썬에서는 기본 내장 모듈로 heap을 제공한다.
    일단은 최소 힙의 형태로 정렬해준다.

    import heapq

    메소드는 다음과 같다

    heappush(heap, item) 힙에 아이템 추가
    heappop(heap)        힙에서 가장 작은 원소 제거 후 리턴, 비어있으면 에러
    heappushpop(heap, item) 힙에 아이템을 푸시하고, 가장 작은 원소를 제거하고 리턴.
                            결합해서 수행하면 push호출 후 pop을 호출하는 것보다 더 효율적
    heapreplace(heap, item) 힙에서 팝하고 푸시함. 따로 호출하는 것보다 효율적.
                            단, 리턴된 값이 추가된 item보다 클 수 있음에 주의할 것.

    heapify(list_x)      list_x라는 리스트를 힙으로 변환 

    nlargest(n, iterable, key=None)
        iterable에 의해 정의된 데이터 집합에서 큰 순서로 n개의 원소가 들어있는 리스트 반환.

    nsmallest(n, iterable, key=None)
        작은 순서로 n개의 원소가 들어있는 리스트 반환.

    ex) heapq.nsmallest(3, heap)

"""