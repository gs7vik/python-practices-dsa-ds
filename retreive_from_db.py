class Database():
    db={'1':'satvik','2':'sat'}
    
    def get_user_by_id(self, id:str) ->str:
        return self.db.get(id)
    
    
