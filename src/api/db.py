import peewee as pw
import config
from datetime import datetime
from playhouse.shortcuts import model_to_dict


db = pw.PostgresqlDatabase(
    config.POSTGRES_DB,
    user=config.POSTGRES_USER, password=config.POSTGRES_PASSWORD,
    host=config.POSTGRES_HOST, port=config.POSTGRES_PORT
)


class BaseModel(pw.Model):
    class Meta:
        database = db


# Table Description
class Mushroom(BaseModel):

    cap_shapes = pw.TextField()
    cap_surfaces = pw.TextField()
    cap_colors = pw.TextField()
    bruises = pw.TextField()
    odors = pw.TextField()
    gill_attachments = pw.TextField()
    gill_spacings = pw.TextField()
    gill_sizes = pw.TextField()
    gill_colors = pw.TextField()
    labels = pw.IntegerField()

    # user_agent = pw.TextField()
    # ip_address = pw.TextField()
    # created_date = pw.DateTimeField(default=datetime.now)

    def serialize(self):
        review_dict = model_to_dict(self)
        review_dict["created_date"] = (
            review_dict["created_date"].strftime('%Y-%m-%d %H:%M:%S')
        )

        return review_dict


# Connection and table creation
db.connect()
print('connected!')
db.create_tables([Mushroom])
