from django.contrib.gis.geos import Point
from places.models import Place
import graphene
from graphene_django import DjangoObjectType
from graphene_gis.converter import gis_converter


class PlaceType(DjangoObjectType):
    class Meta:
        model = Place
        fields = '__all__'

class CreatePlace(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
        coordinates = graphene.String(required=True) # To save a coordinate input must be: POINT(lat long) ex: POINT(34.9435, -87.4934)
    
    # Being returned by mutation
    place = graphene.Field(PlaceType)

    def mutate(root, info, title, description, coordinates):
        place_instance = Place(
            title=title,
            description=description,
            coordinates=coordinates
        )

        place_instance.save()
        return CreatePlace(place=place_instance)

class Query(graphene.ObjectType):
    all_places = graphene.List(PlaceType)

    def resolve_all_places(self, info, **kwargs):
        return Place.objects.all()


class Mutation(graphene.ObjectType):
    create_place = CreatePlace.Field()
