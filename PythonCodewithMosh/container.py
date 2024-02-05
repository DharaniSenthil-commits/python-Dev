class TagCloud:
    def __init__(self) -> None:
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.tags[tag] = count

    def __len__(Self):
        return len(Self.tags)

    def __iter__(self):
        return iter(self.tags.items())


cloud = TagCloud()
print(cloud["python"])
cloud["python"] = 10
print(len(cloud))
cloud.add("python")
cloud.add("Python")
print(cloud.tags)
for tag, count in cloud:
    print(tag, count)
