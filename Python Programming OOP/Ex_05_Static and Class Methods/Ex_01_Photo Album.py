"""
Output:

baby photo added successfully on page 1 slot 1
first grade photo added successfully on page 1 slot 2
eight grade photo added successfully on page 1 slot 3
party with friends photo added successfully on page 1 slot 4
[['baby', 'first grade', 'eight grade', 'party with friends'], []]
prom photo added successfully on page 2 slot 1
wedding photo added successfully on page 2 slot 2
-----------
[] [] [] []
-----------
[] []
-----------


"""
from math import ceil

class PhotoAlbum:
    PHOTOS_PER_PAGE = 4

    def __init__(self, pages):
        self.pages = pages
        self.photos = self.build_photos()

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = ceil(photos_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages)

    def add_photo(self, label):
        for page in range(self.pages):
            if len(self.photos[page]) < PhotoAlbum.PHOTOS_PER_PAGE:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page+1} slot {len(self.photos[page])}"
        return "No more free slots"

    def display(self):
        delimeter = "-" * 11 + "\n"
        result = delimeter

        for page in self.photos:
            page_str = ' '.join(["[]" for _ in page])
            result += page_str + "\n" + delimeter
        return result.strip()

    # def display(self):
    #     delimeter = "-" * 11
    #     result = delimeter+"\n"
    #     for page in range(self.pages):
    #         for slot in range(len(self.photos[page])):
    #             if self.photos[page][slot] != '':
    #                 result += "[] "
    #         result = result.strip()
    #         result += "\n"
    #         result += delimeter+"\n"
    #     return result.strip()

    def build_photos(self):
        result = []
        for _ in range(self.pages):
            result.append([])
        return result



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.display())
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())

'-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n-----------'
'-----------\n[] [] [] []\n-----------\n[] [] [] []\n-----------\n\n-----------'