angular.module('quizApp', [])

    .controller('LoginController', ['UserService', function(UserService){
        var self = this;
        self.user = {};
        
        self.login = function(){
              UserService.login(user).then(function(response){
                  UserService.isLoggedIn = true;
                  UserService.user = user.username;
              }, function(response){
                  console.log("Error while logging user in.");
              });
        };
        
    }]);