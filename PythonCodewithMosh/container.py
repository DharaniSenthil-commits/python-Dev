class TagCloud:
    def __init__(self) -> None:
        # __tag --> mentioning it is private members
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0)+1

    def __getitem__(self, tag):
        return self.__tags.get(tag, 0)

    def __setitem__(self, tag, count):
        self.__tags[tag] = count

    def __len__(Self):
        return len(Self.__tags)

    def __iter__(self):
        return iter(self.__tags.items())


cloud = TagCloud()
print(cloud["python"])
cloud["python"] = 10
print(len(cloud))
cloud.add("python")
cloud.add("Python")

for tag, count in cloud:
    print(tag, count)

# print(cloud.tags["Python"]) --> will shows error
print(cloud.__dict__)
print(cloud._TagCloud__tags['python'])
