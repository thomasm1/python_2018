import React, { Component } from 'react';

class TodoItem extends Component {
  // deleteProject(id){
	//	this.props.onDelete(id);
//	}
  render() {  
   return (      
    <li className="Todo">   
  <strong>{this.props.todo.title}</strong>: 

  
    </li>  
      );
  }
  
}
// Removed from below <strong>{this.props.todo ....}
//  {this.props.todo.category} <a href="#" onClick={this.deleteProject.bind(this, this.props.project.id)}>X</a>

export default TodoItem;
