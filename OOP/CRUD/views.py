# CRUD - C: create, R: read(listing,detail), U: update, D: delete
from search import search_object

class CreateMixin:
    def _get_or_set_objexts_and_id(self):
        try:
            self.id
            self.objects 
        except (NameError,AttributeError):
            self.objects = []
            self.id = 0 
    
    def __init__(self):
        self._get_or_set_objexts_and_id()

    def post(self,**kwargs):
        self.id += 1
        obj = dict(id=self.id,**kwargs)
        self.objects.append(obj)
        return {"status":"201 created","msg": obj}
    
class ReadMixin:
    def list(self):
        res = [{"id":obj["id"],"title":obj["title"]} for obj in self.objects]
        return {"status":"200 OK","msg":res}
    
    @search_object
    def detail(self,id,**kwargs):
        obj=kwargs["object_"]
        if obj:
            return {"status":"200 OK","msg":obj}
        return {"status":"404 Not Found"}
    
class UpdateMixin:
    @search_object
    def patch(self,id,**kwargs):
        obj= kwargs.pop("object_")
        if obj:
            obj.update(**kwargs)
            return {"status":"200 OK","msg":obj}
        return {"status":"404 Not Found"}

class DeleteMixin:
    @search_object
    def delete(self,id,**kwargs):
        obj=kwargs["object_"]
        if obj:
            self.objects.remove(obj)
            return {"status":"204 No content","msg":"Deleted"}
        return {"status":"404 Not Found"}
