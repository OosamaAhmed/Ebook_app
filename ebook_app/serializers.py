from rest_framework import serializers

from .models import EBooksModel

class EbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = EBooksModel  
        fields = ("__all__" )

        fields = ['title', 'summary', 'pages', 'pdf', 'author', 'category', 'author_id']

  