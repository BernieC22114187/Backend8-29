"""TASBackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from apscheduler.schedulers.blocking import BlockingScheduler
# from crawler_api import crawler
from otherRest_api import crawler
from apscheduler.triggers.combining import OrTrigger
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.schedulers.background import BackgroundScheduler
sched = BlockingScheduler() 
from TASBackend.views import get_system_status


# def test():
#     print("testing...")

# @sched.scheduled_job('interval', seconds=60) 
# def mytask():  
#     print("Start crawlering......")
#     crawler.crawler()  

# def job():
#     print("Start Crawling.....")

    # crawler.crawler()


# scheduler = BackgroundScheduler()
# scheduler.add_job(job, 'interval', days = 0, hours = 0, minutes = 0, seconds = 10)
# scheduler.start()
# sched.start()
# crawler.crawler()
urlpatterns = [
    path('', get_system_status),
    path('member/', include('member_api.urls')),
    path('dish/', include('dish_api.urls')),
    path('nutritioninfo/', include('data_api.urls')),
    path('dailyMenu/', include('crawler_api.urls')),
    path('otherRest/', include('otherRest_api.urls')),
    path('exercise/', include('exercise_api.urls')),
    path('doexercise/', include('doExercise_api.urls'))
    
]

