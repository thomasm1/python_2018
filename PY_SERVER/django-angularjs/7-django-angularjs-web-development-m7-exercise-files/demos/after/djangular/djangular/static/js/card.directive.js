(function () {
    'use strict';

    angular.module('scrumboard.demo')
        .directive('scrumboardCard', CardDirective);

    function CardDirective() {
        return {
            templateUrl: '/static/html/card.html',
            restrict: 'E',
            controller: ['$scope', '$http', function ($scope, $http) {

                $scope.update = function () {
                    return $http.put(
                        $scope.url,
                        $scope.card
                    );
                };

                function removeCardFromList(card, list) {
                    var cards = list.cards;
                    cards.splice(
                        cards.indexOf(card),
                        1
                    );
                }

                $scope.delete = function () {
                    $http.delete($scope.url).then(
                        function(){
                            removeCardFromList($scope.card, $scope.list);
                        }
                    );
                };

                $scope.modelOptions = {
                    debounce: 500
                };


                $scope.move = function () {
                    if ($scope.destList === undefined) {
                        return
                    }
                    $scope.card.list = $scope.destList.id;
                    $scope.update().then(function () {
                        {
                            removeCardFromList($scope.card, $scope.list);
                            $scope.destList.cards.push($scope.card);
                        }
                    });
                }

                $scope.changeOwner = function () {
                    $scope.card.owner = $scope.owner.id;
                    $scope.update();
                }


                activate();
                function activate() {
                    $scope.url = '/scrumboard/cards/' + $scope.card.id + '/';
                    $scope.list = $scope.project.lists.find(function (l) {
                        return l.id === $scope.card.list;
                    });
                    $scope.destList = $scope.list;
                    if (!!$scope.card.owner) {
                        $scope.owner = $scope.project.members.find(function (m) {
                            return m.id === $scope.card.owner;
                        })
                    }
                }

            }]
        };
    }
})();