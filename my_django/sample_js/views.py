import datetime
from django.shortcuts import render
from django.http import JsonResponse
from sample_js.models import Carandar


def index(request):
    ary = []
    data = Carandar.objects.all()
    for c in data:
        ary.append({
            "id": "{}".format(c.id),
            "title": "{}".format(c.subject),
            "start_date": "{}".format(c.start_date),
            "end_date": "{}".format(c.end_date),
            "all_day_flg": "{}".format(c.all_day_flg),
            "contents": "{}".format(c.contents),
        })

    return render(request, 'sample_js/index.html', {
        "data": ary
    })


def api(request):
    id = request.GET.get('id')
    subject = request.GET.get('subject')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    contents = request.GET.get('contents')

    if request and subject and contents:
        all_day_flg = True if request.GET.get('end_flg') == u"true" else False
        if start_date:
            start_date = datetime.datetime.strptime(start_date, "%Y/%m/%d %H:%M")
        if end_date:
            end_date = datetime.datetime.strptime(end_date, "%Y/%m/%d %H:%M") + datetime.timedelta(days=1)

        print("id")
        print(id)

        if id:
            carandar = Carandar.objects.filter(
                id=id,
            )
            carandar.update(
                subject=subject,
                start_date=start_date,
                end_date=end_date,
                all_day_flg=all_day_flg,
                contents=contents,
            )
        else:
            carandar = Carandar.objects.create(
                subject=subject,
                start_date=start_date,
                end_date=end_date,
                all_day_flg=all_day_flg,
                contents=contents,
            )
            carandar.save()
            print("登録完了")

    ary = []
    data = Carandar.objects.all()
    for c in data:
        ary.append({
            "id": c.id,
            "title": c.subject,
            "start": c.start_date.strftime("%Y/%m/%d %H:%M:%S"),
            "end": c.end_date.strftime("%Y/%m/%d %H:%M:%S"),
            "allDay": c.all_day_flg,
            "description": c.contents,
        })

    return JsonResponse(ary, safe=False)


def api_delete(request):
    delete_id = int(request.GET.get('delete_id'))

    print(delete_id)

    Carandar.objects.filter(
        id=delete_id
    ).delete()
    print("登録完了")

    ary = []
    data = Carandar.objects.all()
    for c in data:
        ary.append({
            "id": c.id,
            "title": c.subject,
            "start": c.start_date.strftime("%Y/%m/%d %H:%M:%S"),
            "end": c.end_date.strftime("%Y/%m/%d %H:%M:%S"),
            "allDay": c.all_day_flg,
            "description": c.contents,
        })

    return JsonResponse(ary, safe=False)