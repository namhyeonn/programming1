class Item:
    count = 0
    def __init__(self, title, price):
        self.title = title
        self.price = price
        Item.count += 1
    def getprice(self):
        pass
class Book(Item):
    def __init__(self, title, price, pages, author):
        super().__init__(title, price)
        self.pages = pages
        self.author = author
    def getprice(self):
        print(f" 가격은 {self.price} 원 입니다.")
    def __str__(self):
        return f"제목: {self.title}, 가격: {self.price}, 페이지 수: {self.pages}, 저자: {self.author}"
class Magazine(Item):
    def __init__(self, title, price, month):
        super().__init__(title, price)
        self.month = month
    def getprice(self):
        print(f" 가격은 {self.price} 원 입니다.")
    def __str__(self):
        return f"제목: {self.title}, 가격: {self.price}, 출간 월: {self.month}"

if __name__ == '__main__':
    book1 = Book('소나기', 10000, 124, '황순원')
    book2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    book3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)
    
    print('', book1, '\n', book2, '\n', book3, '\n', magazine1, '\n', magazine2)
    print(' 총', Item.count, '권')
    book2.getprice()
    magazine1.getprice()
    book1.getprice()
