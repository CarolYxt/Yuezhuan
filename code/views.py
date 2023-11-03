from django.http import HttpResponse
from .models import Question
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.http import Http404
#如果具有请求的 ID 的问题不存在，则视图会引发异常。
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    #该行查询数据库中最新的问题。它从数据库中检索 Question 对象的列表，按“pub_date”字段降序排列它们（最新问题在前），并将结果限制为前 5 个问题。
    templates = loader.get_template("userfeedback/index.html")
    #这里，它使用 Django 的模板加载器加载名为“polls/index.html”的 HTML 模板。
    context = {
        "latest_question_list": latest_question_list
    }
    #它创建一个上下文字典，其中包含latest_question_list从数据库查询中获得的内容。此上下文将用于将数据传递到 HTML 模板，以便它可以呈现问题。
    return render(request, "userfeedback/index.html", context)
    return HttpResponse("Hello, world. You're at the userfeedback index.")
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "userfeekback/detail.html", {"question": question})
    return HttpResponse("You're looking at question %s." % question_id)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "userfeedback/detail.html", {"question": question})
def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
#它显示系统中最新的 5 个民意调查问题，根据发布日期以逗号分隔