var React = require('react');

class TodoForm extends React.Component {
  constructor(props) {
    super(props);
    this.inputRef = null;
    this.handleFormSubmit = this.handleFormSubmit.bind(this);
    this.handleRefInputEvt = this.handleRefInputEvt.bind(this);
  }
  handleFormSubmit(evt) {
    evt.preventDefault();
    var todo = this.inputRef.value;
    this.props.onNewTodoItem(todo);
    this.inputRef.value = '';
  }
  handleRefInputEvt(inputRef) {
    this.inputRef = inputRef;
  }
  render() {
    return (
      <form className="form-group" onSubmit={this.handleFormSubmit}>
        <input type="text" className="form-control" placeholder="Add to Tom's Priority List" ref={this.handleRefInputEvt}/>
      </form>
    );
  }
}

module.exports = TodoForm;
