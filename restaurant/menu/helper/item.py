from menu.models import Item, ItemCategory, ItemSubCategory, Category, SubCategory

class ItemObject():

    def __init__(self, id):
        self.item = dict()
        self.id = id
        if self.isValid():
            self.__createItem()

    def isValid(self):
        if Item.objects.filter(id=id).count() > 0:
            return True
        return False

    def getItem(self):
        return self.item
    
    def __getItemObject(self):
        return Item.objects.get(id=self.id) 

    def __createItem(self):
        _item = list(Item.objects.filter(id=self.id).values())[0]
        self.item["id"] = _item["id"]
        self.item["name"] =  _item["name"]
        self.item["price"] = _item["price"]
        self.item["small_description"] = _item["small_description"]
        self.item["description"] = _item["description"]
        self.item["rating"] = _item["rating"]
        self.item["icon_image_url"] = _item["icon_image"]

        self.item["categories"] = self.getItemCategory()
        self.item["subcategories"] = self.getItemSubCategory()


    def getItemCategory(self):
        _item_object = self.__getItemObject()

        _category_list = list(ItemCategory.objects.filter(item=_item_object).values())
        return _category_list

    def getItemSubCategory(self):
        _item_object = self.__getItemObject()

        _subcategory_list = list(ItemSubCategory.objects.filter(item=_item_object).values())
        return _subcategory_list
