(function () {
    'use strict';

    angular.module('scrumboard.demo')
        .controller('ScrumboardController',
                    ['$scope', '$http', '$location', '$routeParams', 'Login', ScrumboardController]);

    function ScrumboardController($scope, $http, $location, $routeParams, Login) {
        $scope.add = function (list, title) {
            var card = {
                list: list.id,
                owner: Login.currentUser().id,
                title: title
            };

            $http.post('/scrumboard/cards/', card)
                .then(function (response) {
                    list.cards.push(response.data);
                },
                function(){
                    alert('Could not create card');
                }
            );

        };


        activate();

        function activate() {
            if (!Login.isLoggedIn()) {
                $location.url('/login');
            }

            $scope.project = {name: "Loading.."};
            $scope.logout = Login.logout;

            var url = '/scrumboard/projects/' + $routeParams.projectId + '/';
            $http.get(url).then(
                function (response) {
                    $scope.project = response.data;
                }, function(){
                    alert('Could not load project :(');
                }
            );
        }


    }

}());
