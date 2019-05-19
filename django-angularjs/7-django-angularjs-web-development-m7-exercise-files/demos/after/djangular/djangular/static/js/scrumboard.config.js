angular.module('scrumboard.demo').config(['$routeProvider',
    function config($routeProvider) {

        $routeProvider
            .when('/project/:projectId', {
                templateUrl: '/static/html/scrumboard.html',
                controller: 'ScrumboardController',
            })
            .when('/login', {
                templateUrl: '/static/html/login.html',
                controller: 'LoginController',
            })
            .when('/', {
                templateUrl: '/static/html/projects.html',
                controller: 'ProjectsController',
                controllerAs: 'vm'
            })
            .otherwise('/');
    }
]).run(run);

run.$inject = ['$http'];

/**
* @name run
* @desc Update xsrf $http headers to align with Django's defaults
*/
function run($http) {
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';
  $http.defaults.xsrfCookieName = 'csrftoken';
};