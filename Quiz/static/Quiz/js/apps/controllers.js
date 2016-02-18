angular.module('quizApp')
	.controller('HomeController', [function(){
		var self = this;
		self.myInterval = 5000;
		self.noWrapSlides = false;
		self.currIndex = 0;
		self.slides = [
			{
				image: 'http://127.0.0.1:8000/static/Quiz/images/note.png',
				text: ['Nice image','Awesome photograph','That is so cool','I love that'],
				id: 1
			},
			{
				image: 'http://127.0.0.1:8000/static/Quiz/images/pic.png',
				text: ['Nice image','Awesome photograph','That is so cool','I love that'],
				id: 2
			}
		];
		for (var i = 0; i < 4; i++) {
			//addSlide();
		}
		
		self.languages = ['Java', 'C++', 'C', 'Scala'];
        
	}])
    .controller('LoginController', ['UserService', '$location', 
        function(UserService, $location){
        var self = this;
        self.user = {};
        self.userService = UserService;
        
        self.login = function(){
            UserService.login(self.user).then(function(success){
                console.log("controller response : " + success.data);
                UserService.isLoggedIn = true;
                UserService.user = success.data;
                $location.path('/');
            }, function(error){
                console.log('Error while login');
				alert(angular.isObject(error.data));
				alert(error.data);
            });
        };
    }])

    .controller('MainController', ['$window', '$location', 'UserService',
		function($window, $location, UserService){
			var self = this;
			$window.title = "Quiz";
			self.isActive = function(route){
				return route == $location.path();
			}
			self.userService = UserService;
        
			self.logout = function(){
				UserService.logout().then(function(response){
					console.log("Logout");
					UserService.user = '';
					UserService.isLoggedIn = false;
					$location.path('#/login');
				}, function(){
					console.log("Error while logout");   
				});   
			}
        
			self.userDetail = function(){
				alert(self.userService.user);
				alert(self.userService.isLoggedIn);
			}
			UserService.session();
			//console.log('user : '+ self.userService.user);
			//console.log("login : " + self.userService.isLoggedIn);
    }])
	
	.controller('UserController', ['UserService', 
		function(UserService){
			var self = this;
			self.userData = null;
			
			UserService.getUserDetail(UserService.user).then(function(response){
				self.userData = response.data;
				console.log(self.userData);
				window.title = self.userData.username;
			}, function(response){
				console.log(response.data);
			});
		}
	])
	
    .controller('SignupController', ['$http', function($http) {
        var self = this;
        self.user = null;
        self.repeatPassword = "1234";
        
        self.signUp = function(){
            if(self.user){
                console.log(self.user);
                $http.post('/signup/', self.user).then(function(response){
                    console.log("User account created.");
                    console.log(response.data);
                }, function(response){
                    console.log("Error while creating user account.");
                    console.log("Response : " + response.data);
                });
            }
            else{
                alert("Password doesn't match.")   
            }
        };
    }])

    .controller('PlayController', ['$routeParams', 'ScoreService', 'QuestionService', '$interval', 
        function(routeParams, ScoreService, QuestionService, $interval) {
        var self = this;
        self.questions = {};
        self.currentQuestion = 0;
        self.totalCorrect = 0;
		self.totalIncorrect = 0;
        self.score = 0;
        
        QuestionService.getQuestionByCriteria(routeParams.language_id, routeParams.level_id, 
        routeParams.total_questions).then(function(response){
            self.questions = response.data;
        });
        
        self.nextQuestion = function(result){
            if(self.currentQuestion < self.questions.length){
                self.currentQuestion++;
				self.isCorrect(result);
			}
			else{
				alert("Score : \n"+"Correct : "+self.totalCorrect+"\nIncorrect : "+self.totalIncorrect);
			}
        };
        
        self.isCorrect = function(result){
            if(result[0][0] == true){
                self.totalCorrect++;
			}
			else{
				self.totalIncorrect++;
			}
        };
            
        self.saveUserScore = function(){
            var userScore = {
                account: 'admin@gmail.com',
                language: 1, level: 1,
                score: 100, time_taken: 16, total_time: 10,
                total_question: 20, total_correct: 8
            };
            ScoreService.saveUserScore(userScore).then(function(response){
                console.log("Score Saved to Server : "+ response.data);
            }, function(response){
                console.log(response.data);
            });
        };
		self.time = new Time();
		self.manageTime = function(){
			self.time.increment();
			if(self.time.isComplete()){
				$interval.cancel(stop);
				alert(self.time.getTime());
			}
			console.log(self.time.getTime());
		}
		
		stop = $interval(self.manageTime, 10);
        
    }])
    .controller('LanguageController', ['$routeParams', 'LanguageService',        
        function(routeParams, LanguageService){
        var self = this;
        self.language = null;
        self.activeLevel = 0;
        LanguageService.getLanguageDetail(routeParams.id).then(function(response){
            self.language = response.data;  
            //self.currentLevel = self.language.levels[0].pk;
        });
    }]);