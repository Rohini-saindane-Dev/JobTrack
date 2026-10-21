



from django.shortcuts import render, redirect
from django.db.models import Q
from .models import JobApplication


def home(request):
    search_query = request.GET.get("search", "").strip()
    selected_status = request.GET.get("status", "").strip()

    # Get all applications
    all_jobs = JobApplication.objects.all()

    # Dashboard counts
    total_count = all_jobs.count()
    applied_count = all_jobs.filter(status="Applied").count()
    interview_count = all_jobs.filter(status="Interview").count()
    selected_count = all_jobs.filter(status="Selected").count()
    rejected_count = all_jobs.filter(status="Rejected").count()

    # Search applications
    jobs = all_jobs

    if search_query:
        jobs = jobs.filter(
            Q(company_name__icontains=search_query) |
            Q(job_role__icontains=search_query)
        )

    # Filter by status
    valid_statuses = ["Applied", "Interview", "Selected", "Rejected"]

    if selected_status in valid_statuses:
        jobs = jobs.filter(status=selected_status)

    jobs = jobs.order_by("-application_date")

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
        company_name = request.POST.get("company_name")
        job_role = request.POST.get("job_role")
        application_date = request.POST.get("application_date")
        status = request.POST.get("status")

        JobApplication.objects.create(
            company_name=company_name,
            job_role=job_role,
            application_date=application_date,
            status=status,
        )

        return redirect("home")

    return render(request, "jobs/add_application.html")


def delete_application(request, job_id):
    if request.method == "POST":
        job = JobApplication.objects.get(id=job_id)
        job.delete()

    return redirect("home")


def edit_application(request, job_id):
    job = JobApplication.objects.get(id=job_id)

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
