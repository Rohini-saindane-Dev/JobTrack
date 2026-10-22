





from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator
from .models import JobApplication


def home(request):
    search_query = request.GET.get("search", "").strip()
    selected_status = request.GET.get("status", "").strip()

    applications = JobApplication.objects.all().order_by(
        "-application_date", "-id"
    )

    if search_query:
        applications = applications.filter(
            Q(company_name__icontains=search_query)
            | Q(job_role__icontains=search_query)
        )

    if selected_status:
        applications = applications.filter(status=selected_status)

    paginator = Paginator(applications, 5)
    jobs = paginator.get_page(request.GET.get("page"))

    # Dashboard counts across all applications
    total_count = JobApplication.objects.count()
    applied_count = JobApplication.objects.filter(
        status="Applied"
    ).count()
    interview_count = JobApplication.objects.filter(
        status="Interview"
    ).count()
    selected_count = JobApplication.objects.filter(
        status="Selected"
    ).count()
    rejected_count = JobApplication.objects.filter(
        status="Rejected"
    ).count()

    context = {
        "jobs": jobs,
        "total_count": total_count,
        "applied_count": applied_count,
        "interview_count": interview_count,
        "selected_count": selected_count,
        "rejected_count": rejected_count,
        "search_query": search_query,
        "selected_status": selected_status,
    }

    return render(request, "jobs/home.html", context)


def add_application(request):
    if request.method == "POST":
        JobApplication.objects.create(
            company_name=request.POST.get("company_name"),
            job_role=request.POST.get("job_role"),
            application_date=request.POST.get("application_date"),
            status=request.POST.get("status"),
        )
        return redirect("home")

    return render(request, "jobs/add_application.html")


def delete_application(request, job_id):
    if request.method == "POST":
        job = get_object_or_404(JobApplication, id=job_id)
        job.delete()

    return redirect("home")


def edit_application(request, job_id):
    job = get_object_or_404(JobApplication, id=job_id)

    if request.method == "POST":
        job.company_name = request.POST.get("company_name")
        job.job_role = request.POST.get("job_role")
        job.application_date = request.POST.get("application_date")
        job.status = request.POST.get("status")
        job.save()

        return redirect("home")

    return render(
        request,
        "jobs/edit_application.html",
        {"job": job}
    )
