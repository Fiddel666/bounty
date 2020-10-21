import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";

class Input extends Component {
	constructor(props) {
		super(props);
		this.state = {user : ''};
		this.handleInput = this.handleInput.bind(this);
		this.register = this.register.bind(this);
	}
	
	handleInput(event) {
		this.setState({
			[event.target.name]: event.target.value
		});
	}
	
	register(event) {
		// send data to server here
		return axios.post('http://127.0.0.1:8000/bounty/api/users/', this.state)
		.then(res => console.log(res))
		.catch(err => console.error(err));
	}
	
	render() {
		return(
			<label>
				user
				<input
					name="user"
					type="text"
					onChange={this.handleInput}
				/>
				<h5>
					{this.state.user}
				</h5>
				<button onClick={this.register}>
					register
				</button>
			</label>
		)
	}
}


export default Input;