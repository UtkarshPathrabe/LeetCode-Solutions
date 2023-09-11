class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groupSizeMap = defaultdict(list)
        for person, groupSize in enumerate(groupSizes):
            groupSizeMap[groupSize].append(person)
        result = []
        for groupSize, persons in groupSizeMap.items():
            while persons:
                group, persons = persons[:groupSize], persons[groupSize:]
                result.append(group)
        return result