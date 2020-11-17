from src import api 
from src.database import models 
import json
app = api.app 
models.setup_db(app)
models.db_drop_and_create_all()

## Create a new drink 
drink1 = models.Drink(id=1,title="drink1",recipe=json.dumps({'color':'red','name':'cola','parts':1}))
drink1.insert()