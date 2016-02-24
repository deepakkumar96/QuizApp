angular.module('quizApp')
	.factory('AuthIntercepter', ['$cookies', function($cookies){
		return{
			request: function(config){
				if(config.method == 'POST'){
					config.headers['X-CSRFToken'] = $cookies.get('csrftoken');
				}
				return config;
			}
		};//$httpProvider.defaults.post['X-CSRFToken'] = $cookies.get('csrftoken');
	}])
    .factory('UserService', ['$http', function($http){
        var service =  {
            user: '',
            isLoggedIn: false,
            login: function(user){
                   return $http.post('/api/login/', user)/*.then(function(response){
                        service.isLoggedIn = true;
                        service.user = response.data;
                        console.log("Service login response : " + service.user);
                        return response;
                    })*/;
            },
            logout: function(){
                   return $http.get('/api/logout/');
            },
            session: function(){
                return $http.get('/api/session/');
            },
			getUserDetail: function(user_email){
				return $http.get('/api/user/' + user_email + '/');
			}
        };
        return service;
    }])
    .factory('QuestionService', ['$http', function($http){
        return {
            getQuestions: function(){
                return $http.get('/questions/');   
            },
            getQuestionByCriteria: function(language, level, totalQuestions){
                return $http.get('/questions/'+language+'/'+level+'/'+totalQuestions);
            }
        };
    }])
    .factory('LanguageService', ['$http', function($http){
        return{
            getLanguageDetail: function(id){
                return $http.get('/language/' + id + '/');
            }
        };
    }])
    .factory('ScoreService', ['$http', function($http){
        return {
            getUserScore: function(id){
                return $http.get('/score/'+id+'/');   
            },
            saveUserScore: function(userScore){
                return $http.post('/scores/create/', userScore);
            }
        };
    }]);