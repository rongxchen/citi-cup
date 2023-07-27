"""companies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = {
    # home page
    path("", views.home),
    path("index.html", views.home),
    path("news.html", views.news),
    path("about-us.html", views.about_us),
    path("report.html", views.report),
    path("industry.html", views.industry),
    path("knowledge_graph.html", views.knowledge_graph),


    # return by ticker (either code or name) + (exchange)
    path("companies/search/<str:ticker>/", views.get_company),
    path("companies/search/<str:ticker>/<str:exchange>", views.get_company_and_exchange),
    path("companies/details/<str:code>/<str:market>/", views.get_company_detail),


    # news data API
    path("companies/report/news/", views.report_enterprise_news),
    path("companies/topnews/", views.top_news_simple),
    path("companies/topnews/<str:cid>/<str:page>/<str:page_size>/", views.top_news),
    path("companies/topnews/eng/", views.top_news_eng),


    # esg rating
    path("companies/report/rating/", views.report_ratings),


    # specific scores by industry sector
    path("companies/report/score/sectorlist/", views.report_sector_subsector_list),
    path("companies/report/score/sector/<str:sector_id>/", views.report_sector_score),
    path("companies/report/score/subsector/<str:subsector_id>/", views.report_sub_sector_score),
    path("companies/report/score/sector/company/<str:stock_code>/<str:exchange>/", views.report_stock_sector),


    # get company notice by identifying its exchange
    path("companies/report/notice/<str:stock_code>/<str:exchange>/", views.report_notice),


    # get financial analysis
    path("companies/report/finratio/<str:stock_code>/<str:exchange>/", views.fin_ratio_analysis),
    path("companies/report/stockprice/<str:stock_code>/<str:exchange>/<str:interval>/<str:n>/", views.report_stock_price),
    path("companies/report/stockinfo/<str:stock_code>/<str:exchange>/", views.report_stock_info),


    # chatgpt
    path("chat/link/", views.news_analysis_with_link),


    # knowledge graph data
    path("knowledge/<str:entity>/", views.knowledge_data),


    # word cloud jpg path
    path("companies/wordcloud/<str:company>/", views.word_could_path),


    # ESG framework mysql database
    path("companies/esgframework/useofproceed/r/<str:code>/", views.select_use_of_proceed),
    path("companies/esgframework/useofproceed/c/<str:code>/", views.insert_use_of_proceed),
    path("companies/esgframework/useofproceed/u/<str:id>/", views.update_use_of_proceed),
    path("companies/esgframework/useofproceed/d/<str:id>/", views.delete_use_of_proceed),

}
