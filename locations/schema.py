import graphene

import places.schema
import users.schema

class Query(users.schema.Query, places.schema.Query, graphene.ObjectType):
    pass

class Mutation(users.schema.Mutation, places.schema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)
