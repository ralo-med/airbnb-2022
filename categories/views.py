from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from .models import Category
from .serializers import CategorySerializer


@api_view(["GET", "POST"])
def categories(request):
    if request.method == "GET":
        all_categories = Category.objects.all()
        serializer = CategorySerializer(all_categories, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            # Python 객체를 받았고 이를 JSON으로 다시 받고 response로 보내주는 것이다!
            return Response(
                CategorySerializer(new_category).data,
            )
        else:
            return Response(serializer.errors)


@api_view(["GET", "PUT"])
def category(request, pk):
    try:
        category = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        raise NotFound

    # 먼저 category를 가져오고  (pk는 url에서 온거다)

    if request.method == "GET":
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    # PUT 은 (데이터베이스와, 유저 데이터를 둘다 사용한다)
    # partial은 데이터가 일부분만 들어와도 ㄱㅊ, 걍 데이터베이스를 사용함
    # save가 알아서 create쓸지, update쓸지 정해줌
    elif request.method == "PUT":
        serializer = CategorySerializer(
            category,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_category = serializer.save()
            return Response(CategorySerializer(updated_category).data)
        else:
            return Response(serializer.errors)
