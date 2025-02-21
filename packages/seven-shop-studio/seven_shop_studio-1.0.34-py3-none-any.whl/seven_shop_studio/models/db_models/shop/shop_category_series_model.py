
#此文件由rigger自动生成
from seven_framework.mysql import MySQLHelper
from seven_framework.base_model import *


class ShopCategorySeriesModel(BaseModel):
    def __init__(self, db_connect_key='db_shopping_center', sub_table=None, db_transaction=None, context=None):
        super(ShopCategorySeriesModel, self).__init__(ShopCategorySeries, sub_table)
        self.db = MySQLHelper(config.get_value(db_connect_key))
        self.db_connect_key = db_connect_key
        self.db_transaction = db_transaction
        self.db.context = context

    #方法扩展请继承此类
    
class ShopCategorySeries:

    def __init__(self):
        super(ShopCategorySeries, self).__init__()
        self.id = 0  # 
        self.category_id = 0  # 分类id
        self.series_id = 0  # 系列id

    @classmethod
    def get_field_list(self):
        return ['id', 'category_id', 'series_id']
        
    @classmethod
    def get_primary_key(self):
        return "id"

    def __str__(self):
        return "shop_category_series_tb"
    