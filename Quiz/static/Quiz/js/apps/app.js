angular.module('quizApp', ['ngRoute', 'ngCookies', 'ui.bootstrap'])
	.config(function($httpProvider, $routeProvider, $interpolateProvider) {
		$httpProvider.interceptors.push('AuthIntercepter');
		$interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');
    
        $routeProvider.when('/', {
            templateUrl: 'views/home_page.html',
            controller: 'MainController as controller'
        })
        .when('/login', {
            templateUrl: 'views/login.html',
            controller: 'LoginController as controller'
        })
        .when('/signup',{
            templateUrl: 'views/sign_up.html',
            controller: 'SignupController as controller'
        })
        .when('/language/:id', {
            templateUrl: 'views/language_detail.html',
            controller: 'LanguageController as controller'
        })
        .when('/user/:user_id', {
            templateUrl: 'views/user_detail.html',
			controller: 'UserController as controller'
        })
        .when('/play/:language_id/:level_id/:total_questions', {
            templateUrl: 'views/play.html',
            controller: 'PlayController as playCtrl',
			resolve : {
				auth : ['$q', '$location', 'UserService',
					function($q, $location, UserService){
						UserService.session().then(
							function(response){
								console.log('session is available.');
								console.log(response.status);
							},
							function(response){
								$location.path('/login');
								$location.replace();
								return $q.reject(response);
							}
						);
					}
				]
			}
        })
        .otherwise({
            redirectTo: '/'
        })
    
    });
    
    