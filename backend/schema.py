import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField
from models import db_session, Verse as VerseModel


class Verse(SQLAlchemyObjectType):
    class Meta:
        model = VerseModel
        interfaces = (relay.Node, )


class VerseConnection(relay.Connection):
    class Meta:
        node = Verse

# passing arguments?
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    # Allows sorting over multiple columns, by default over the primary key
    all_verses = SQLAlchemyConnectionField(VerseConnection)


schema = graphene.Schema(query=Query)