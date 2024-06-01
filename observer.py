# Subject (Observable)
class NewsPublisher:
    def __init__(self):
        self._subscribers = []
        self.news = ""

    def add_subscriber(self, subscriber):
        self._subscribers.append(subscriber)

    def remove_subscriber(self, subscriber):
        self._subscribers.remove(subscriber)

    def create_news(self, news):
        self.news = news
        for subscriber in self._subscribers:
            subscriber.update(news)

# Observer
class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, news):
        print(f"{self.name} received news: {news}")

# Usage
publisher = NewsPublisher()

subscriber1 = Subscriber("Subscriber 1")
subscriber2 = Subscriber("Subscriber 2")

publisher.add_subscriber(subscriber1)
publisher.add_subscriber(subscriber2)

publisher.create_news("Breaking news: Python is awesome!")