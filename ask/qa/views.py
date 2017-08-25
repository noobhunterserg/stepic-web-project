from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseNotFound
from django.core.urlresolvers import reverse
from django.utils import timezone
from qa.models import Question, Answer
from qa.forms import Add_Question, Add_Answer
import random

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def notfound(request, *args, **kwargs):
    return HttpResponseNotFound('Not Found!')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10

    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404

    paginator = Paginator(qs, limit)

    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page, paginator

def new(request):
    qs = Question.objects.all().order_by('-added_at')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('new') + '?page='

    return render(request, 'main_page.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        })

def popular(request):
    qs = Question.objects.all().order_by('-rating')
    page, paginator = paginate(request, qs)
    paginator.baseurl = reverse('popular') + '?page='

    return render(request, 'main_page.html', {
        'questions': page.object_list,
        'page': page,
        'paginator': paginator,
        })

def question(request, num):
    qs = get_object_or_404(Question, id=num)
    answers = Answer.objects.filter(question_id=num).order_by('-added_at').all()
    form = Add_Answer()
    return render(request, 'question_page.html', {
        'question': qs,
        'answers': answers,
        'form': form,
        })

def add_question(request):
    if request.method == "POST":
        form = Add_Question(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author_id = '1'
            question.added_at = timezone.now()
            question.save()
            return redirect('question_page', num=question.pk)
    else:
        form = Add_Question()
    return render(request, 'add_question.html', {'form': form})

def add_answer(request, num):
    if request.method == "POST":
        form = Add_Answer(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author_id = '1'
            answer.question_id = num
            answer.added_at = timezone.now()
            answer.save()
    return redirect('/question/%s/' % num)

def add_like(request, num):
    question = Question.objects.get(id=num)
    question.rating += 1
    question.save()

    return redirect('/')

# for i in range(1, 100):
#     title = 'title' + str(i)
#     text = 'text' + str(i)
#     q = Question.objects.create(title=title, text=text, author_id=str(random.randrange(1,5)))
#     q.save()
#     for k in range (5):
#         comment = 'comment' + str(k)
#         a = Answer.objects.create(text=comment, author_id=str(random.randrange(1,5)), question_id=q.id)
#         a.save()
