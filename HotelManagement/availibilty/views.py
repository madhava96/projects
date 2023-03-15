from django.shortcuts import render,HttpResponse
import MySQLdb as sql
from login.views import user
# Create your views here.
'''
def show(request):
    print(request)
    try:
        print('hii')
        conn = sql.connect(user='root',passwd='root',db='hotel')
        cur = conn.cursor()
        cur.execute("select * from rooms where status='No'")
        l = list(cur.fetchall())
        #print(l)
        cur.execute("select * from rooms inner join book on room_no = a_room where status='YES'")
        l1 = list(cur.fetchall())
        print(l1)
        return render(request,"check.html",{'data':l,'d':l1})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))

def cancle(request):
    if request.method == "POST":
        try:
            conn = sql.connect(user='root',passwd='root',db='hotel')
            cur = conn.cursor()
            data = request.POST
            d = int(list(data.keys())[1])
            print(d)
            cur.execute('delete from book where a_room ={}'.format(d))
            cur.execute("update rooms set status='NO' where room_no = {}".format(d))
            conn.commit()
            print('hii')
            #return redirect('/redirect-success/')
            show(request)
        except Exception as e:
            #HttpResponse(e)
            return HttpResponse('something went wrong check:'+str(e)) #errors from db
    #return render(request,"check.html")

'''
def show(request):
    #print(request)
    try:
        conn = sql.connect(host='192.168.30.75',user='user',passwd='pass',db='hotel')
        cur = conn.cursor()
        data = request.POST
        print(len(data))
        if len(data) != 0:
            d = int(list(data.keys())[1])
            #print(d)
            cur.execute('delete from booking_booking where a_room ={}'.format(d))
            cur.execute("update availibilty_rooms set status='NOT BOOKED' where room_no = {}".format(d))
            conn.commit()
        cur.execute("select * from availibilty_rooms where status='NOT BOOKED'")
        l = list(cur.fetchall())
        #print(l)
        cur.execute("select room_no,name,mobile_no,checkin,checkout,status from availibilty_rooms inner join booking_booking on room_no = a_room order by room_no;")
        l1 = list(cur.fetchall())
        return render(request,"check.html",{'data':l,'d1':l1})
    except Exception as e:
        #HttpResponse(e)
        return HttpResponse('something went wrong check:'+str(e))