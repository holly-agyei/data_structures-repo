import heapq

class FoodRatings:

    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        self.food_to_rating = {}
        self.food_to_cuisine = {}
        self.cuisine_to_heap = {}

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_rating[food] = rating
            self.food_to_cuisine[food] = cuisine

            if cuisine not in self.cuisine_to_heap:
                self.cuisine_to_heap[cuisine] = []
            # Push (-rating, food) because heapq is min-heap, so -rating makes it max-heap by rating
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        # Push new rating to the heap for this cuisine
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_to_heap[cuisine]

        # Pop outdated entries until top of heap matches current rating
        while True:
            rating, food = heap[0]
            # Check if this rating matches current rating (remember rating stored negated)
            if -rating == self.food_to_rating[food]:
                return food
            else:
                # Outdated rating, remove it
                heapq.heappop(heap)
