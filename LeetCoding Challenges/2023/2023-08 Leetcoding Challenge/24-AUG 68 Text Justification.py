class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        def getWords(i):
            currentLine = []
            currentLength = 0
            while i < len(words) and currentLength + len(words[i]) <= maxWidth:
                currentLine.append(words[i])
                currentLength += len(words[i]) + 1
                i += 1
            return currentLine
        
        def createLine(line, i):
            baseLength = -1
            for word in line:
                baseLength += len(word) + 1
            extraSpaces = maxWidth - baseLength
            if len(line) == 1 or i == len(words):
                return " ".join(line) + " " * extraSpaces
            wordCount = len(line) - 1
            spacesPerWord = extraSpaces // wordCount
            needsExtraSpace = extraSpaces % wordCount
            for j in range(needsExtraSpace):
                line[j] += " "
            for j in range(wordCount):
                line[j] += " " * spacesPerWord
            return " ".join(line)

        result = []
        i = 0
        while i < len(words):
            currentLine = getWords(i)
            i += len(currentLine)
            result.append(createLine(currentLine, i))
        return result