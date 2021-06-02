class Article:
    def __init__(self, title, link, thumbnail):
        self.title = title
        self.link = link
        self.thumbnail = thumbnail

    def __str__(self):
        return self.title

    def get_link(self):
        return self.link

    def get_title(self):
        return self.title
