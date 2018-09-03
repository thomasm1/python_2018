var React = require('react');
var Todo = require('./Todo');

function App() {
  return (
    <div className="container List-App text-center">
      <h3>Priority-List</h3>
      <Todo />
    </div>
  );
}

module.exports = App;
