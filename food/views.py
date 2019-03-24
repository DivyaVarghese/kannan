import datetime
from django.utils import timezone
import ast
from django.http import HttpResponse
import json
from django.shortcuts import render
from django.contrib.auth.models import User
from food.models import CustomerR,HotelReg,Foodlist,Cart,Offer,Order,Rate
from django.contrib.auth import login as auth_login,logout,authenticate
# from app1.models import Userreg

def index(request):
	# print(request.GET["value"])

	return render(request,'index.html',{})


def contact(request):
	return render(request,'contact.html',{})


def blog(request):
	return render(request,'blog.html',{})


def chef(request):
	return render(request,'chef.html',{})


def menu(request):
	return render(request,'menu.html',{})


def customerreg(request):
	if request.method=='POST':
		name=request.POST.get('name')
		uname=request.POST.get('uname')
		location=request.POST.get('location')
		password=request.POST.get('password')
		pho=request.POST.get('phone')
		email=request.POST.get('email')
		print(name,uname,location,pho,email)
		u=User.objects.filter(username=uname).exists()
		if not u:
			r=User.objects.create_user(username=uname,email=email,first_name=name,last_name=1,password=password)
			u1=CustomerR(user1=r,location=location,pho=pho,name1=uname)
			u1.save()
			return render(request,'login.html',{})
		else:
			return render(request,'customerreg.html',{})
	else:
		return render(request,'customerreg.html',{})

def login1(request):
	if request.method=='POST':
		uname=request.POST.get('username')
		password=request.POST.get('password')
		u=authenticate(request,username=uname,password=password)
		if u:
			r=User.objects.get(username=uname)
			cat=r.last_name
			if cat=='1':
				print('customer')
				auth_login(request,u)
				u=HotelReg.objects.all()
				return render(request,'wcustomer.html',{'u':u})
			else:
				print('hotel')
				auth_login(request,u)
				print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
				p=[]
				c=[]
				g=[]
				h=[]
				em=[]
				oxx=[]
				t=Cart.objects.filter(status=0)
				
				for x in t:
					ox=x.orderid
					print(ox)
					print('cjvjvjhjhvjhvjhvhhvhvvh')
					oxx.append(ox)
					y=x.order
					cid=x.customerid
					c1=CustomerR.objects.get(cid=cid)
					c2=c1.user1.email
					em.append(c2)
					r=request.user
					r1=User.objects.get(username=r)
					r2=HotelReg.objects.get(user1=r1)
					r3=r2.hid
					hid=x.hotelid
					print(r3,type(r3),hid,type(hid))
					if int(hid)	==r3:
						for z in y.keys():
							u=Foodlist.objects.get(fid=z)
							f=u.foodname
							p.append(f)
						for z in y.values():
							c.append(z)
						print(x.payment)
						g.append(x.payment)
						print(g,type(g))
						
						h.append(x.totamt)

				return render(request,'whotel.html',{'p':p,'c':c,'g':g,'h':h,'em':em,'oxx':oxx})
		
		else:
			return render(request,'login.html',{})
	else:

		return render(request,'login.html',{})	

def hotelreg(request):
	if request.method=='POST':
		name=request.POST.get('name')
		uname=request.POST.get('uname')
		email=request.POST.get('email')
		password=request.POST.get('password')
		location=request.POST.get('location')
		ftype=request.POST.getlist('ftype')
		pho=request.POST.get('phone')
		address=request.POST.get('address')
		permit=request.POST.get('permit')
		opent=request.POST.get('opent')
		closet=request.POST.get('closet')
		img=request.FILES['img']
		print(name,uname,email,pho)
		r=User.objects.filter(username=uname).exists()
		if not r:
			u=User.objects.create_user(username=uname,first_name=name,last_name=2,password=password,email=email)
			u1=HotelReg(user1=u,name1=uname,location=location,pho=pho,ftype=ftype,address=address,permitno=permit,opent=opent,closet=closet,image=img)
			u1.save()
			return render(request,'login.html',{})
		else:
			return render(request,'hotelreg.html',{})
	else:
		return render(request,'hotelreg.html',{})	

def food(request):
	if request.method=='POST':
		img=request.FILES['foodimg']
		foodname=request.POST.get('foodname')
		foodid=request.POST.get('foodid')
		rate=request.POST.get('rate')
		chef=request.POST.get('chef')
		details=request.POST.get('details')
		ptime=request.POST.get('ptime')
		r=request.user
		r1=User.objects.get(username=r)
		r2=HotelReg.objects.get(user1=r1)

		r3=r2.hid

		r3=Foodlist(hotel=r2,hid=r3,foodid=foodid,foodname=foodname,prize=rate,details=details,time=ptime,img=img,chef=chef)
		r3.save()
		return render(request,'food.html',{})
	else:
		return render(request,'food.html',{})

def whotel(request):
	if request.method=='POST':
		get_value= request.body
		print(',jshdd qwugd lqwdhg lasdgcxlasuyhgxauyshcfgxlasyhf gcvsuzyxfhv')
		g=get_value.decode("utf-8")
		g1=ast.literal_eval(g)
		print(g,type(g),g1,type(g1))
		print('hgshgdcgsah jhgfwegb')
		# send_mail

		r=request.user
		r1=User.objects.get(username=r)
		r2=HotelReg.objects.get(user1=r1)
		r3=Cart.objects.get(hid=r2)
		r3.status=1
		r3.save()
		r4=Cart.objects.filter(status=1)
		r4.delete()

		data = {}
		data['result'] = 'you saved sccesssdkjfg'
		print(data)
		return HttpResponse(json.dumps(data), content_type="application/json")

	else:
		print('qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq')
		p=[]
		c=[]
		g=[]
		h=[]
		em=[]
		oxx=[]
		t=Cart.objects.filter(status=0)
		print('cjvjvjhjhvjhvjhvhhvhvvh')
		for x in t:
			ox=x.orderid
			print(ox)
			print('cjvjvjhjhvjhvjhvhhvhvvh')
			oxx.append(ox)
			y=x.order
			cid=x.customerid
			c1=CustomerR.objects.get(cid=cid)
			c2=c1.user1.email
			em.append(c2)
			r=request.user
			r1=User.objects.get(username=r)
			
			r2=HotelReg.objects.get(user1=r1)
			r3=r2.hid
			hid=x.hotelid
			print(r3,type(r3),hid,type(hid))
			if int(hid)	==r3:
				for z in y.keys():
					u=Foodlist.objects.get(fid=z)
					f=u.foodname
					p.append(f)
				for z in y.values():
					c.append(z)
				print(x.payment)
				g.append(x.payment)
				print(g,type(g))
				
				h.append(x.totamt)
		print(oxx)
		return render(request,'whotel.html',{'p':p,'c':c,'g':g,'h':h,'em':em,'oxx':oxx})
def logout1(request):
	logout(request)
	return render(request,'index.html',{})

def wcustomer(request):
	if request.method=='POST':
		get_value= request.body
		print(',jshdd qwugd lqwdhg lasdgcxlasuyhgxauyshcfgxlasyhf gcvsuzyxfhv')
		g=get_value.decode("utf-8")
		g1=int(g)
		print(g1)
		r=request.user

		r1=User.objects.get(username=r)
		r2=CustomerR.objects.get(user1=r1)
		r3=r2.cid
		r4=HotelReg.objects.get(hid=g1)
		print(g,g1,r,r1,r2,r3,r4)
		u=Cart(cid=r2,hid=r4,customerid=r3,hotelid=g1,)
		u.save()



		data = {}
		data['result'] = 'you saved sccesssdkjfg'
		print(data)
		return HttpResponse(json.dumps(data), content_type="application/json")
		print('jhvdjha hgdiug')
	else:
		u=HotelReg.objects.all()
		return render(request,'wcustomer.html',{'u':u})
def order(request):
	if request.method=='POST':
		get_value= request.body
		print(',jshdd qwugd lqwdhg lasdgcxlasuyhgxauyshcfgxlasyhf gcvsuzyxfhv')
		g=get_value.decode("utf-8")
		g1=ast.literal_eval(g)
		print(g,type(g),g1,type(g1))
		print('hgshgdcgsah jhgfwegb')

		r=request.user
		r1=User.objects.get(username=r)
		r2=CustomerR.objects.get(user1=r1)
		r3=Cart.objects.get(cid=r2)

		r3.order=g1
		r3.save()
		data = {}
		data['result'] = 'you saved sccesssdkjfg'
		print(data)
		return HttpResponse(json.dumps(data), content_type="application/json")



	else:
		r=request.user
		r1=User.objects.get(username=r)
		r2=CustomerR.objects.get(user1=r1)
		r3=Cart.objects.get(cid=r2)
		r4=r3.hotelid
		r5=HotelReg.objects.get(hid=r4)
		r6=Foodlist.objects.filter(hid=r4)
		return render(request,'order.html',{'f':r6})
def bill(request):
	if request.method=='POST':
		print('im gerer at oasdAFGH')
		get_value= request.body
		print(',jshdd qwugd lqwdhg lasdgcxlasuyhgxauyshcfgxlasyhf gcvsuzyxfhv')
		g=get_value.decode("utf-8")
		g1=ast.literal_eval(g)
		print(g,type(g),g1,type(g1))
		print('hgshgdcgsah jhgfwegb')
		if g1['mode']=='cash':
			location=g1['location']
			pho=g1['pho']
			r=request.user
			r1=User.objects.get(username=r)
			r2=CustomerR.objects.get(user1=r1)
			r3=Cart.objects.get(cid=r2)
			hh=r3.hotelid
			hhh=HotelReg.objects.get(hid=hh)
			l=[]
			l=[location,pho,'cash']
			ccc=r2.cid
			r3.payment=l
			r3.save()
			i=r3.orderid
			
			print('ughjcccccccccccccccccccccccccccccccccccccccc',i)
			z=Order(location=location,payment='cash',pho=pho,orderid=i)
			z.save()
			oo=Order.objects.get(orderid=i)
			m=Rate(orderid=oo,hid=hhh,hotelid=hh,cid=r2,customerid=ccc)
			m.save()
			data = {}
			data['result'] = 'you saved sccesssdkjfg'
			print(data)
			return HttpResponse(json.dumps(data), content_type="application/json")
		elif g1['mode']=='card':
			location=g1['location']
			pho=g1['pho']
			cardno=g1['cardno']
			cvv=g1['cvv']
			month=g1['month']
			year=g1['year']
			r=request.user
			r1=User.objects.get(username=r)
			r2=CustomerR.objects.get(user1=r1)
			ccc=r2.cid
			r3=Cart.objects.get(cid=r2)
			i=r3.orderid
			hh=r3.hotelid
			hhh=HotelReg.objects.get(hid=hh)
			l=[]
			l1=[]
			l=[location,pho,cardno,cvv,month,year,'card']
			l1=[cardno,cvv,month,year]
			r3.payment=l
			r3.save()
			z=Order(location=location,pho=pho,payment=l1,orderid=i)
			z.save()
			oo=Order.objects.get(orderid=i)
			m=Rate(orderid=oo,hid=hhh,hotelid=hh,cid=r2,customerid=ccc)
			m.save()
			data = {}
			data['result'] = 'you saved sccesssdkjfg'
			print(data)
			return HttpResponse(json.dumps(data), content_type="application/json")




		data = {}
		data['result'] = 'you saved sccesssdkjfg'
		print(data)
		return HttpResponse(json.dumps(data), content_type="application/json")

	else:
		print('inside billlllllllllllll')
		r=request.user
		r1=User.objects.get(username=r)
		r2=CustomerR.objects.get(user1=r1)
		r3=Cart.objects.get(cid=r2)
		r4=r3.order
		print(r1,r2,r3,r4)
		l=[]
		c=[]
		n=[]
		tot=[]
		s=0
		for x in r4.keys():
			y=Foodlist.objects.get(fid=x)
			y1=y.prize
			l.append(y1)
			p=y.foodname
			n.append(p)
		for x in r4.values():
			c.append(x)
			type(x)
		for x in range(len(l)):
			tot.append(int(l[x])*int(c[x]))
		for x in tot:
			s=s+int(x)
		w=Offer.objects.all()
		for x in w:
			tt=x.date.date()
			if tt==datetime.datetime.now().date():
				cc=x.cutoff
				pp=x.offerper
		if s>=int(cc):
			g=(int(pp)/100)*s
		else:
			g=0
		grand=s-g
		r3.totamt=grand
		r3.save()
		

		return render(request,'bill.html',{'l':n,'c':c,'tot':tot,'s':s,'grand':grand,'offer':pp})