class thanks_Gift:
    def __init__(self, s, r, so):
        self.shampoo = s
        self.rinse = r
        self.soap = so

    def price(self):
        total = self.shampoo * 7000 + self.rinse * 7000 + self.soap * 4000
        return total

class vip_Set(thanks_Gift):
    def __init__(self, s, r, so, bs, bl):
        super().__init__(s, r, so)
        self.bodyshower = bs
        self.bodylotion = bl

    def price(self):
        total = self.shampoo * 7000 + self.rinse * 7000 + self.soap * 4000 + self.bodyshower * 14000 + self.bodylotion * 20000
        return total

if __name__ == '__main__':
    vipgift01 = vip_Set(3, 1, 4, 2, 1)

    print(f'샴푸, 린스, 비누가 {vipgift01.shampoo}, {vipgift01.rinse}, {vipgift01.soap}개 샤워비누와 샤워로션은 {vipgift01.bodyshower}, {vipgift01.bodylotion}개 입니다')
    print(f'vipgift01의 가격은 : {vipgift01.price()}')