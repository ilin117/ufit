from typing import AsyncGenerator
from django.shortcuts import render, redirect
from django.http import HttpRequest, StreamingHttpResponse, HttpResponse
from . import models
import asyncio
import json


# Create your views here.
def chatpage(request: HttpRequest) -> HttpResponse:
    if not request.session.get("username"):
        return redirect("lobby")
    return render(request, "base/chatpage.html")


def create_message(request: HttpRequest) -> HttpResponse:
    content = request.POST.get("content")
    username = request.session.get("username")

    if not username:
        return HttpResponse(status=403)
    author, _ = models.Author.objects.get_or_create(name=username)

    if content:
        models.Message.objects.create(author=author, content=content)
        return HttpResponse(status=201)
    else:
        return HttpResponse(status=200)


# this'll make it so that the chats appear on screen as we submit it ong
async def stream_chat_messages(request: HttpRequest) -> StreamingHttpResponse:
    async def event_stream():
        # do later
        async for message in get_existing_messages():
            yield message

        last_id = await get_last_message_id()

        while True:
            new_messages = (
                models.Message.objects.filter(id__gt=last_id)
                .order_by("created_at")
                .values("id", "author__name", "content")
            )
            async for message in new_messages:
                yield f"data: {json.dumps(message)}\n\n"
                last_id = message["id"]
            await asyncio.sleep(0.1)

    async def get_existing_messages() -> AsyncGenerator:
        messages = (
            models.Message.objects.all()
            .order_by("created_at")
            .values("id", "author__name", "content")
        )
        async for message in messages:
            yield f"data: {json.dumps(message)}\n\n"

    async def get_last_message_id() -> int:
        last_message = await models.Message.objects.all().alast()
        return last_message.id if last_message else 0

    return StreamingHttpResponse(event_stream(), content_type="text/event-stream")


def welcomePage(request):

    return render(request, "base/welcome.html", {})


def privacyPage(request):
    return render(request, "base/privacy.html")


def homePage(request):
    return render(request, "base/home.html")


def registration_page(request):
    return render(request, "base/registrationpage.html")


# def chatpage(request):
#     return render(request, "base/chatpage.html")


def postpage(request):
    return render(request, "base/postpage.html")


def profilepage(request):
    return render(request, "base/profilepage.html")


def login_page(request):
    return render(request, "base/loginpage.html")
