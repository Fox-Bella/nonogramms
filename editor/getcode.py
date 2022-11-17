from square import Square

class GetCode:

    def get_code(self, sq: Square):

        # 20 и -1, если ничего не найдено
        minHorizontal = len(sq)
        maxHorizontal = -1
        for i in range(len(sq)):
            p1 = 0
            p2 = len(sq) - 1
            while p1 < len(sq):
                if sq[i][p1].enabled:
                    if p1 < minHorizontal:
                        minHorizontal = p1
                p1 += 1
            while p2 > -1:
                if sq[i][p2].enabled:
                    if p2 > maxHorizontal:
                        maxHorizontal = p2
                p2 -= 1

        # 20 и -1, если ничего не найдено
        minVertical = len(sq)
        maxVertical = -1
        for i in range(len(sq[0])):
            p1 = 0
            p2 = len(sq) - 1
            while p1 < len(sq):
                if sq[p1][i].enabled:
                    if p1 < minVertical:
                        minVertical = p1
                p1 += 1
            while p2 > -1:
                if sq[p2][i].enabled:
                    if p2 > maxVertical:
                        maxVertical = p2
                p2 -= 1

        print(minHorizontal, maxHorizontal)
        print(minVertical, maxVertical)

        if (minVertical == 20 and maxVertical == -1 and \
                minHorizontal == 20 and maxHorizontal == -1):
            return False
        r = "["
        for i in range(minHorizontal, maxHorizontal + 1):
            r += "["
            for j in range(minVertical, maxVertical + 1):
                if (sq[j][i].enabled):
                    r += "1"
                else:
                    r += "0"
                if (j != maxVertical):
                    r += ", "
            r += "]"
            if (i != maxHorizontal):
                r += ",\n "
        r += "]"
        print(r)

        return True


