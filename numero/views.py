from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.viewsets import ModelViewSet

from .forms import BirthdayForm
from .calculator.matrix_pertceva import post_date, calc_matrix, make_dict
from psycopg2 import connect as p_conn, Error as PError
from .config.db import PG_HOST, PG_DB_NAME, PG_DB_PASS, PG_DB_USER
from .models import Celeb, CelebData, CalcMatrix
from datetime import datetime, date, time
import json

from .serializer import CelebsSerializer


class CalcView(ModelViewSet):
    today = datetime.today()
    queryset = Celeb.objects.filter(
        birthday__year__gt=str(today.year - 60),
        birthday__month=str(today.month),
        birthday__day=str(today.day)
    ).order_by('-birthday')
    serializer_class = CelebsSerializer


def index(request):
    bday_form = BirthdayForm()
    # create_celeb_db()
    # create_celeb_data_db()
    data = {
        'form': bday_form,
    }
    return render(request, "numero.html", context=data)


# TODO: calc matrix on over moviestar photo
def calc(request):
    bdate = request.POST.get("bday")
    parse_date = datetime.strptime(bdate, '%d.%m.%Y')
    yy = parse_date.year
    mm = parse_date.month
    dd = parse_date.day
    if not bdate:
        return HttpResponse("calculate matrix...")

    try:
        d = CalcMatrix.objects.get(calc_date=f'{yy}-{mm}-{dd}')
        res_dict = json.loads(d.calc_result)
    except Exception:
        rs, dn = calc_matrix(post_date(bdate))
        _, res_dict, _ = make_dict(rs, dn)
        res_json = json.dumps(res_dict)
        jd = CalcMatrix.objects.create(calc_date=f'{yy}-{mm}-{dd}', calc_result=res_json)
        jd.save()

    match_bday = Celeb.objects.filter(
        birthday__year=str(yy),
        birthday__month=str(mm),
        birthday__day=str(dd)
    )
    same_day_celebs_list = []
    for c in match_bday:
        c_data = CelebData.objects.get(celeb_id=c.id)
        to_list = (c.name, c.birthday, c_data.profession, c_data.profile_url, c_data.photo_url)
        same_day_celebs_list.append(to_list)

    celebs = Celeb.objects.filter(
        birthday__year__gt=str(yy - 30),
        birthday__month=str(mm),
        birthday__day=str(dd)
    ).order_by('-birthday')#[:12]
    celebs_list = []
    for c in celebs:
        c_data = CelebData.objects.get(celeb_id=c.id)
        to_list = (c.name, c.birthday, c_data.profession, c_data.profile_url, c_data.photo_url)
        celebs_list.append(to_list)

    data = {
        'bday': bdate,
        'celebs': celebs_list,
        'same_day': same_day_celebs_list
    }
    data.update(res_dict)
    return render(request, "calc.html", context=data)


# def connect_postgres(bdate):
#     bds = bdate.split(".")
#     mm = f"0{bds[1]}" if len(bds[1]) == 1 else f"{bds[1]}"
#     dd = f"0{bds[0]}" if len(bds[1]) == 1 else f"{bds[0]}"
#     try:
#         connection = p_conn(
#             host=PG_HOST,
#             database=PG_DB_NAME,
#             user=PG_DB_USER,
#             password=PG_DB_PASS)
#         cursor = connection.cursor()
#
#         sql_req = f"""
#             SELECT bdate, pname, profession FROM people
#             WHERE bdate::text LIKE '____-{mm}-{dd}'
#             AND bdate > '1970-01-01'
#             ORDER BY bdate DESC;
#         """
#         cursor.execute(sql_req)
#         result = cursor.fetchall()
#         return result
#     except (Exception, PError) as error:
#         print("Error while connecting to PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")


# def get_all_from_db():
#     try:
#         connection = p_conn(
#             host=PG_HOST,
#             database=PG_DB_NAME,
#             user=PG_DB_USER,
#             password=PG_DB_PASS)
#         cursor = connection.cursor()
#
#         sql_req = f"""
#             SELECT * FROM people
#             ORDER BY id ASC;
#         """
#         cursor.execute(sql_req)
#         result = cursor.fetchall()
#         return result
#     except (Exception, PError) as error:
#         print("Error while connecting to PostgreSQL", error)
#     finally:
#         if connection:
#             cursor.close()
#             connection.close()
#             print("PostgreSQL connection is closed")


# def filter_db():
#     list_ = get_all_from_db()
#     person_id_set = set()
#     pname_set = set()
#     id_to_delete = []
#     for tuple_item in list_:
#         id_, pname, _, _, _, _, persid = tuple_item
#         if pname in pname_set:
#             # print(id_, persid, pname)
#             id_to_delete.append(id_)
#         # person_id_set.add(persid)
#         pname_set.add(pname)
#     return id_to_delete


# def create_celeb_db():
#     list_ = get_all_from_db()
#     for tuple_item in list_:
#         _, pname, bdate, _, _, _, persid = tuple_item
#         p = Celeb.objects.create(name=pname, birthday=bdate, persid=int(persid))
#         # print(f"{p.id} {p.name} {p.birthday}\tOK")


# def create_celeb_data_db():
#     list_ = get_all_from_db()
#     for tuple_item in list_:
#         _, pname, bdate, photo_url, prof, profile_url, persid = tuple_item
#         if pname:
#             persone = Celeb.objects.get(persid=int(persid))
#             # print(f"{persone.id}{type(persone.id)} {persone.name} {persone.birthday}")
#             # print(f"{pname} {bdate}")
#             p = CelebData(
#                 celeb=persone,
#                 profession=prof,
#                 profile_url=profile_url,
#                 photo_url=photo_url
#             )
#             p.save()
