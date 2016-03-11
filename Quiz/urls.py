from django.conf.urls import include, url
from Quiz import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/login/$', views.login_template, name='login'),
    url(r'^logout$', views.user_logout),

    # Templates
    url(r'views/user_detail.html', views.get_user_template, name='get_user_template'),
    url(r'views/language_detail.html', views.get_language_template, name='get_language_template'),
    url(r'views/play.html', views.get_play_template, name='get_play_template'),
    url(r'views/sign_up.html', views.get_sign_up_template, name='get_sign_up_template'),
    url(r'views/login.html', views.get_login_template, name='get_login_template'),
    url(r'views/home_page.html', views.get_home_page_template, name='get_home_page_template'),
    # url(r'questions/', views.questions_list, name='questions_list'),

    # Rest_Framework

    url(r'^api/login/$', views.user_login),
    url(r'^api/session/$', views.user_session),
    url(r'^api/logout/$', views.user_logout),
    url(r'^signup/$', views.sign_up, name='signup'),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^api/user/(?P<email>[A-Za-z@._%0-9]+)/$', views.UserDetail.as_view()),
    url(r'questions/$', views.question_list),
    url(r'language/(?P<pk>[0-9]+)/$', views.LanguageDetail.as_view()),
    url(r'level/(?P<pk>[0-9]+)/$', views.LevelDetail.as_view()),
    url(r'^scores/$', views.UserScoreList.as_view()),
    url(r'^scores/create/$', views.save_user_score),
    url(r'^score/(?P<pk>[A-Za-z@._%0-9]+)/$', views.UserScoreDetail.as_view()),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^api/challenge/(?P<pk>[0-9]+)/$', views.ChallengeDetail.as_view()),

    url(r'questions/(?P<language_id>[0-9]+)/(?P<level_id>[0-9]+)/(?P<total_questions>[0-9]+)', views.play_data),

    # Challenge Related URLS
    url(r'runtime/getChallengesIfAvailable/', views.get_challenges_if_available, name='get_challenges_if_available')
]
