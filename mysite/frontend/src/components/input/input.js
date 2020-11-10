import React, { Component } from "react";
import { render } from "react-dom";
import axios from "axios";

class Input extends Component {
	constructor(props) {
		super(props);
		this.state = {	username : '',
						password : ''
					};
		this.handleInput = this.handleInput.bind(this);
		this.register = this.register.bind(this);
		
		// set to automatically use django token
		axios.defaults.xsrfCookieName = 'csrftoken';
		axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
	}
	
	handleInput(event) {
		this.setState(
			{[event.target.name]: event.target.value},
			function (){ //callback function to use updated state
				console.log(this.state);
			}
		);
		console.log(this.state);
	}
	
	register(event) {
		// send data to server here
		return axios.post('http://127.0.0.1:8000/bounty/user/', this.state)
		.then(res => console.log(res))
		.catch(err => console.error(err));
	}
	
	render() {
		return(
			<label>
				username:
				<input
					name="username"
					type="text"
					onChange={this.handleInput}
				/>
				
				<br />
				
				password:
				<input
					name="password"
					type="text"
					onChange={this.handleInput}
				/>
				
				<h5>
					{this.state.username}
				</h5>
				
				<button onClick={this.register}>
					register
				</button>
			</label>
		)
	}
}

export default Input;

