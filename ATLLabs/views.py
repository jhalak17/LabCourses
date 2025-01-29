from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.views import View
from django.conf import settings
from django.http import HttpResponse

from .models import Equipment

def equipment_list(request):
    """
    Display a paginated list of equipment.

    - Fetches all equipment objects.
    - Implements pagination with 20 items per page.
    - Passes the paginated results to the template.

    Parameters:
    - request (HttpRequest): The request object.

    Returns:
    - HttpResponse: Rendered equipment list template with pagination.
    """
    equipments = Equipment.objects.all().order_by('id')
    
    # Create pagination
    paginator = Paginator(equipments, 9)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, 'equipmets.html', {'page_obj': page_obj})

def equipment_detail(request, pk):
    """
    View to retrieve detailed information about a specific equipment item.
    """
    equipment = get_object_or_404(Equipment, pk=pk)
    return render(request, 'equipment_detail.html', {'equipment': equipment})

class EquipmentEnquiry(View):
    """
    Handle the enquiry for equipments.
    """
    def post(self, request):
        """
        Handle POST request for form submission.
        """
        customer_name = request.POST.get('pname')
        customer_email = request.POST.get('pemail')
        customer_phone = request.POST.get('pnumber')
        additional_message = request.POST.get('add_message')
        equipment_id = request.POST.get('equipment_id')
        equipment_name = request.POST.get('equipment_name')

        self.send_email(customer_name, customer_email,customer_phone, equipment_name)

        return redirect('homepage')
    
    def send_email(self,customer_name, customer_email,customer_phone, equipment_name):
        subject = "Confirmation of Your Enquiry"
        message = f"""
        Hello {customer_name},

        Thank you for enquiring about {equipment_name} ! We have received your request and we will be reaching out to you at +91 {customer_phone} shortly.

        If you have any further questions, feel free to reach out.

        Best regards,
        The ATL Labs Team
        """
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [customer_email]
        try:
            send_mail(subject, message, from_email, recipient_list)
            return HttpResponse("Confirmation email sent successfully!")
        except Exception as e:
            return HttpResponse(f"Fail {e}")
