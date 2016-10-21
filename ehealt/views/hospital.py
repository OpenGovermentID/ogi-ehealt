from django.shortcuts import render, redirect
from ehealt.models import Hospital

# Create your views here.
def index(request):
	list_hospital = Hospital.objects
	return render(request, 'hospital/index.html', {'list_hospital': list_hospital})

def detail(request, hospital_id):
	hospital = Hospital.objects.filter(id=hospital_id).first()
	return render(request, 'hospital/detail.html', {'hospital': hospital})

def add(request):
	if (request.method == 'POST'):
		hospital = Hospital(
				name=request.POST['name'],
				types=request.POST['types'],
				ownership=request.POST['ownership'],
				address=request.POST['address'],
				description=request.POST['description'],
				zip_code=request.POST['zip_code'],
				city=request.POST['city'],
				province='Jawa Barat',
				country='Indonesia',
				contact=[],
				facility=[],
				location={},
			)
		hospital.save()

		return redirect('/health/hospital')

	return render(request, 'hospital/add.html')

def edit(request, hospital_id):
	hospital = Hospital.objects.filter(id=hospital_id).first()
	if (request.method == 'POST'):

		hospital.name=request.POST['name']
		hospital.types=request.POST['types']
		hospital.ownership=request.POST['ownership']
		hospital.address=request.POST['address']
		hospital.description=request.POST['description']
		hospital.zip_code=request.POST['zip_code']
		hospital.city=request.POST['city']
		hospital.province='Jawa Barat'
		hospital.country='Indonesia'

		hospital.save()

		return redirect('/health/hospital/'+hospital_id)

	return render(request, 'hospital/edit.html', {'hospital': hospital})

def delete(request, hospital_id):
	hospital = Hospital.objects.filter(id=hospital_id).first()
	hospital.delete()

	return redirect('/health/hospital')

def contacts(request):
	pass

def add_contact(request):
	pass

def delete_contact(request):
	pass

def facilities(request):
	pass

def add_facility(request):
	pass

def delete_facility(request):
	pass

def edit_location(request):
	pass