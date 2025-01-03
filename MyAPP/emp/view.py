from django.shortcuts import redirect, render, get_object_or_404
from .models import Emp, Testimonial
from .form import FeedbackForm

# Create your views here.
def emp_home(request):
    emps = Emp.objects.all()
    # Render the employee home page
    return render(request, 'emp/home.html', {
        'emps': emps
    })

def emp_add(request):
    if request.method == 'POST':
        # Fetch data from the form
        emp_name = request.POST.get('emp_name')
        emp_id = request.POST.get('emp_id')
        emp_phone = request.POST.get('emp_phone')
        emp_address = request.POST.get('emp_address')
        emp_working = request.POST.get('emp_working')  # Checkbox
        emp_department = request.POST.get('emp_department')

        # Create model object and set the data
        e = Emp()
        e.name = emp_name
        e.emp_id = emp_id
        e.phone = emp_phone
        e.address = emp_address
        e.department = emp_department
        e.working = emp_working == "on"  # Checkbox value

        # Save the data to the database
        e.save()

        print("Data saved successfully")
        return redirect("/emp/home/")

    return render(request, 'emp/add_emp.html')

def emp_delete(request, emp_id):
    # Fetch the employee record, or return a 404 if it doesn't exist
    emp = get_object_or_404(Emp, id=emp_id)

    # Delete the record
    emp.delete()

    # Redirect back to the home page (or wherever you want)
    return redirect('/emp/home/')

def update_emp(request, emp_id):
    # Fetch the employee record
    emp = get_object_or_404(Emp, id=emp_id)

    if request.method == 'POST':
        # Get updated data from the form
        emp.name = request.POST.get('emp_name')
        emp.emp_id = request.POST.get('emp_id')
        emp.phone = request.POST.get('emp_phone')
        emp.address = request.POST.get('emp_address')
        emp.working = True if request.POST.get('emp_working') == 'on' else False
        emp.department = request.POST.get('emp_department')

        # Save the updated record
        emp.save()

        # Redirect to the employee list or another page
        return redirect('/emp/home/')

    # Render the form with the existing data for GET request
    return render(request, 'emp/update_emp.html', {
        'emp': emp
    })

def about(request):
    return render(request, 'emp/about.html')

def testimonials(request):
    testi = Testimonial.objects.all()
    return render(request, 'emp/testimonials.html', {
        'testi': testi
    })

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            # Get data from the form
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            feedback = form.cleaned_data['feedback']

            # Print the data (debugging purposes)
            print("Email:", email)
            print("Name:", name)
            print("Feedback:", feedback)

            # Save the data
            t = Testimonial()
            t.email = email
            t.name = name
            t.feedback = feedback
            t.rating = 5  # Set a default rating or include it in your form
            t.save()

            print("Data saved successfully!")

            return redirect('/emp/feedback/')  # Redirect to the feedback page
    else:
        form = FeedbackForm()

    # Render the feedback form for GET requests
    return render(request, 'emp/feedback.html', {'form': form})