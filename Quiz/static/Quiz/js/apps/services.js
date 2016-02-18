angular.module('quizApp')
    .factory('UserService', ['$http', function($http){
        var service =  {
            user: '',
            isLoggedIn: false,
            login: function(user){
                   return $http.post('/api/login/', user).then(function(response){
                        service.isLoggedIn = true;
                        service.user = response.data;
                        console.log("response : " + service.user);
                        return response;
                    });
            },
            logout: function(){
                   return $http.post('/api/logout/');
            },
            session: function(){
                return $http.get('/api/session/').then(function(response){
                    console.log("service session response : " + response.data);
                    service.isLoggedIn = true;
                    service.user = response.data;
                    return response;
                });   
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