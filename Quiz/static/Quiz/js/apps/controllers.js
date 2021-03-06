angular.module('quizApp')
	.controller('HomeController', [function(){
        console.log("HomeController gets called!");
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
                console.log("controller login response : " + success.data);
                UserService.isLoggedIn = true;
                UserService.user = success.data;
                $location.path('/');
            }, function(error){
                console.log('Error while login');
				console.log(error.data)
				alert(angular.isObject(error.data));
				alert(error.data);
            });
        };
    }])

    .controller('MainController', ['$window', '$location', 'UserService', '$http', '$interval',
		function($window, $location, UserService, $http, $interval){
            console.log("MainController gets called!");
            var self = this;
            self.challenges = [];
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
					$location.path('/login');
				}, function(){
					console.log("Error while logout");   
				});   
			}
            
            self.getNewChallenges = function(){
                $http.get('/runtime/getChallengesIfAvailable/').then(
                    function(response){
                        self.challenges = response.data;
                        console.log(response.data);
                    },
                    function(response){
                        console.log("Error while fetching challenges!");
                    }
                );
            }
        
			self.userDetail = function(){
				alert(self.userService.user);
				alert(self.userService.isLoggedIn);
			}
			UserService.session().then(function(response){
                console.log("service session response : " + response.data);
                self.userService.isLoggedIn = true;
                self.userService.user = response.data;
                //self.getNewChallenges();
            }, function(response){
				console.log("You are not logged id!");
			});   
			//console.log('user : '+ self.userService.user);
			//console.log("login : " + self.userService.isLoggedIn);
            
            if(self.userService.isLoggedIn){
                self.getNewChallenges();
            }
            else
                console.log(self.userService.isLoggedIn);
            $interval(function(){
                if(self.userService.isLoggedIn)
                    self.getNewChallenges();
            }, 10000);
    }])
	
	.controller('UserController', ['UserService', '$window',
		function(UserService, $window){
            console.log('UserController gte called');
			var self = this;
			self.userData = null;
			
			UserService.getUserDetail(UserService.user).then(function(response){
				self.userData = response.data;
				console.log(self.userData);
                document.title = self.userData.first_name;
				document["background-color"] = 'green';
			}, function(response){
				console.log(response.data);
			});
            
		}
	])
	
    .controller('SignupController', ['$http', '$location', function($http, $location) {
        var self = this;
        self.user = null;
        self.repeatPassword = "1234";
        
        self.signUp = function(){
            if(self.user){
                $http.post('/signup/', self.user).then(function(response){
					console.log("User account created.");
                    console.log(response.data);
					$location.path('/');
                }, function(response){
                    console.log("Error while creating user account.");
                    console.log("Response : " + response.data);
					alert("Error while creating user account.");
                });
            }
            else{
                alert("Password doesn't match.")   
            }
        };
    }])

    .controller('PlayController', [
		'$routeParams', 'ScoreService', 'QuestionService', '$interval', 'UserService', '$location',
        function(routeParams, ScoreService, QuestionService, $interval, UserService, $location) {
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
            if((self.currentQuestion+1) <= self.questions.length){
                self.currentQuestion++;
				self.isCorrect(result);
			}
			else{
				alert("Score : \n"+"Correct : "+self.totalCorrect+"\nIncorrect :"+self.totalIncorrect);
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
                account: UserService.user,
                language: routeParams.language_id,
				level: routeParams.level_id,
                score: (self.totalCorrect / routeParams.total_questions)*100, 
				time_taken: 10, 
				total_time: 10,
                total_question: routeParams.total_questions, 
				total_correct: self.totalCorrect
            };
			console.log(userScore);
			ScoreService.saveUserScore(userScore).then(function(response){
                console.log("Score Saved to Server : "+ response.data);
				$location.path('/')
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
        
        if(stop)
            $interval.cancel(stop);
        stop = $interval(self.manageTime, 1000);
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